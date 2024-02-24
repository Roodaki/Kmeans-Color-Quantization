from PIL import Image
import numpy as np


def load_image_and_get_dimensions(image_path):
    """
    Load an image and convert it to a numpy array of RGB pixel values.
    Also retrieves the dimensions of the image.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        numpy.ndarray: Array of RGB pixel values.
        int: Height of the image.
        int: Width of the image.
    """
    try:
        # Open the image file
        with Image.open(image_path).convert("RGB") as image:
            # Convert the image to a numpy array and get dimensions
            pixel_array = np.array(image)
            height, width, _ = pixel_array.shape

        return pixel_array, height, width

    except Exception as e:
        print(f"Error loading image: {e}")
        return None, None, None


def create_image_from_pixels(pixel_array, height, width, output_path=None):
    """
    Create an image from a numpy array of RGB pixel values and optionally save it to a file.

    Parameters:
        pixel_array (numpy.ndarray): Array of RGB pixel values.
        height (int): Height of the image.
        width (int): Width of the image.
        output_path (str, optional): Path to save the output image file. If None, the image will not be saved.

    Returns:
        Image: The created image.
    """
    try:
        # Reshape the pixel array to match the original shape
        pixel_array = pixel_array.reshape(height, width, -1).astype(np.uint8)

        # Create an image from the pixel array
        image = Image.fromarray(pixel_array, "RGB")

        # Save the image to the specified output path if provided
        if output_path:
            image.save(output_path)
            print(f"Image saved to '{output_path}'.")

        return image

    except Exception as e:
        print(f"Error creating image: {e}")
        return None
