<div align="center">
  <h1><strong>Color Quantization using K-means Clustering</strong></h1>
  <p><strong>This project implements color quantization using the K-means clustering algorithm, a popular unsupervised machine learning technique.K-means clustering efficiently partitions all the pixels of an image into K clusters based on their color values, utilizing the centroid of each cluster as the representative color for all pixels within that cluster, thereby enabling users to reduce the number of colors in the image while maintaining visual quality. The application provides an intuitive GUI for users to browse an image, specify the number of colors for quantization, and save the quantized image.</strong></p> 

![Screenshot (354)](https://github.com/Roodaki/Kmeans-Color-Quantization/assets/89901590/3bce0467-f3c7-4321-8b01-55d1acd9240d)
![Screenshot (355)](https://github.com/Roodaki/Kmeans-Color-Quantization/assets/89901590/edfbd4ac-6049-478b-a788-e2676ee1211c)
![Screenshot (357)](https://github.com/Roodaki/Kmeans-Color-Quantization/assets/89901590/f51792fc-a43a-4d0d-aaf8-c132d6812682)
![Screenshot (363)](https://github.com/Roodaki/Kmeans-Color-Quantization/assets/89901590/393d2a48-a1b2-4858-b7e1-6b387be2d45e)
  
</div>

## Features
1. **Optimized Image Representation**: K-means clustering efficiently partitions the color space, resulting in an optimized representation of the image with the specified number of colors while preserving its visual quality.
2. **Fast and Scalable**: The K-means clustering algorithm is implemented with vectorization and optimization techniques, ensuring fast execution even for large images and high-dimensional color spaces.
3. **Convergence and Accuracy**: The algorithm converges when the centroids of the clusters stabilize, ensuring that the quantized image accurately represents the original image with the specified number of colors.
4. **Reproducibility**: The random initialization of centroids is seeded for reproducibility, allowing users to obtain consistent results across multiple runs.
5. **Modular and Extensible**: The K-means clustering functionality is encapsulated in a separate module, making it easy to integrate into other projects and extend with additional features or optimizations.
6. **Well-documented Code**: The implementation of the K-means clustering algorithm is accompanied by detailed comments and documentation, making it easy for developers to understand and modify as needed.

## Project Structure
The project follows a specific structure to organize its files and directories:
```
├── src/
│   ├── main.py
│   ├── gui.py
│   ├── image_processor.py
│   └── kmeans_clustering.py
├── assets/
│   └── image.jpg
├── .gitignore
└── README.md
```
- `src/`: This directory contains all the source code files of the project.
  - `main.py`: The main script to run the application. It orchestrates the initialization of the GUI and image processing modules, allowing users to interact with the application.
  - `gui.py`: Module for the graphical user interface. It handles user interactions, such as loading images, setting the number of colors for quantization, and displaying the original and quantized images.
  - `image_processor.py`: Module for loading, processing, and saving images. It provides functions to read image files, manipulate pixel data, and save processed images. Additionally, it handles the conversion between different image formats and ensures compatibility with the GUI module.
  - `kmeans_clustering.py`: Module for the implementation of the K-means clustering algorithm. It contains the logic for performing color quantization using K-means clustering, where pixels are grouped into clusters based on their color similarity. The module offers functions to initialize centroids, assign pixels to clusters, and update centroids iteratively until convergence, resulting in quantized image data.
- `assets/`: This directory contains input and output images used by the application.
  - `image.jpg`: Sample image for color quantization. Users can load this image into the application to test the color quantization algorithm.
- `.gitignore`: File to specify files and directories to be ignored by version control. It ensures that sensitive or unnecessary files, such as temporary files or compiled binaries, are not tracked by Git.
- `README.md`: Markdown file containing project information and instructions. It serves as the primary documentation for the project, providing an overview of its structure, functionality, and usage guidelines.

## Requirements
- Python (version 3.0 or higher)
- NumPy
- Pillow (Python Imaging Library)
- Tkinter (for GUI)
