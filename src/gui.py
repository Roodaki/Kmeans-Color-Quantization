import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import image_processor as image_processor
from kmeans_clustering import KMeansClustering


class ImageQuantizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Quantization")
        self.root.resizable(False, False)  # Disable window resizing
        self.image_path = None
        self.height = None
        self.width = None
        self.quantized_pixels = None  # Initialize quantized pixels
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Browse an Image:").grid(
            row=0, column=0, padx=5, pady=5
        )
        self.browse_button = tk.Button(
            self.root, text="Browse Image", command=self.load_image
        )
        self.browse_button.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Number of Colors:").grid(
            row=1, column=0, padx=5, pady=5
        )
        self.num_colors_entry = tk.Entry(self.root)
        self.num_colors_entry.grid(row=1, column=1, padx=5, pady=5)

        self.quantize_button = tk.Button(
            self.root, text="Quantize Image", command=self.quantize_image
        )
        self.quantize_button.grid(row=1, column=2, padx=5, pady=5)

        self.save_button = tk.Button(
            self.root, text="Save Quantized Image", command=self.save_quantized_image
        )
        self.save_button.grid(row=1, column=3, padx=5, pady=5)

        self.original_label = tk.Label(self.root, text="Original Image")
        self.original_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.quantized_label = tk.Label(self.root, text="Quantized Image")
        self.quantized_label.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.pixels, self.height, self.width = (
                image_processor.load_image_and_get_dimensions(self.image_path)
            )
            self.display_image(self.pixels, self.original_label)

    def quantize_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        num_colors = self.num_colors_entry.get()
        if not num_colors:
            messagebox.showerror("Error", "Please enter the number of colors.")
            return

        if self.pixels is not None:
            num_colors = int(num_colors)
            kmeans = KMeansClustering(num_clusters=num_colors)
            self.quantized_pixels = kmeans.fit(
                self.pixels.reshape(-1, 3)
            )  # Set quantized pixels
            self.display_image(
                self.quantized_pixels, self.quantized_label
            )  # Display quantized image
        else:
            messagebox.showerror("Error", "Failed to load the image.")

    def save_quantized_image(self):
        if not self.image_path:
            messagebox.showerror("Error", "Please select an image first.")
            return

        if self.quantized_pixels is None:  # Check for quantized pixels availability
            messagebox.showerror("Error", "No quantized image available to save.")
            return

        save_path = filedialog.asksaveasfilename(defaultextension=".jpg")
        if save_path:
            image_processor.create_image_from_pixels(
                self.quantized_pixels, self.height, self.width, save_path
            )
            messagebox.showinfo("Success", "Image saved successfully.")

    def display_image(self, pixels, label):
        if pixels is not None:
            image = image_processor.create_image_from_pixels(
                pixels, self.height, self.width
            )
            image = image.resize((300, 300))
            image = ImageTk.PhotoImage(image)
            label.configure(image=image)
            label.image = image
        else:
            messagebox.showerror("Error", "Failed to load the image.")


def run_gui():
    root = tk.Tk()
    app = ImageQuantizationApp(root)
    root.mainloop()
