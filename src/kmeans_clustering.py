import numpy as np


class KMeansClustering:
    def __init__(self, num_clusters=8, max_iterations=100, tolerance=1e-4):
        """
        Initialize the KMeansClustering object.

        Parameters:
            num_clusters (int): The number of clusters to form.
            max_iterations (int): The maximum number of iterations to perform.
            tolerance (float): The tolerance to declare convergence.
        """
        self.num_clusters = num_clusters
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def fit(self, pixels):
        """
        Fit the KMeans clustering algorithm to the input data.

        Parameters:
            pixels (numpy.ndarray): The input data to cluster.

        Returns:
            numpy.ndarray: The quantized pixels after clustering.
        """
        # Initialize centroids randomly
        centroids = self._initialize_centroids(pixels)

        # Iterate until convergence or maximum iterations reached
        for _ in range(self.max_iterations):
            # Assign each pixel to the nearest centroid
            labels = self._assign_clusters(pixels, centroids)

            # Update centroids based on the assigned clusters
            new_centroids = self._update_centroids(pixels, labels, centroids)

            # Check for convergence
            if np.linalg.norm(new_centroids - centroids) < self.tolerance:
                break

            # Update centroids for the next iteration
            centroids = new_centroids

        # Quantize pixels based on the final centroids
        quantized_pixels = centroids[labels]
        return quantized_pixels

    def _initialize_centroids(self, pixels):
        """
        Initialize centroids randomly from the input pixels.

        Parameters:
            pixels (numpy.ndarray): The input data to cluster.

        Returns:
            numpy.ndarray: The initialized centroids.
        """
        np.random.seed(0)  # Ensure reproducibility
        indices = np.random.choice(len(pixels), self.num_clusters, replace=False)
        return pixels[indices]

    def _assign_clusters(self, pixels, centroids):
        """
        Assign each pixel to the nearest centroid.

        Parameters:
            pixels (numpy.ndarray): The input data to cluster.
            centroids (numpy.ndarray): The current centroids.

        Returns:
            numpy.ndarray: The cluster labels for each pixel.
        """
        # Calculate distances between pixels and centroids
        distances = np.linalg.norm(pixels[:, np.newaxis, :] - centroids, axis=2)

        # Assign each pixel to the nearest centroid
        return np.argmin(distances, axis=1)

    def _update_centroids(self, pixels, labels, centroids):
        """
        Update centroids based on the mean of the assigned pixels.

        Parameters:
            pixels (numpy.ndarray): The input data to cluster.
            labels (numpy.ndarray): The cluster labels for each pixel.
            centroids (numpy.ndarray): The current centroids.

        Returns:
            numpy.ndarray: The updated centroids.
        """
        # Compute new centroids as the mean of the assigned pixels for each cluster
        new_centroids = np.array(
            [pixels[labels == i].mean(axis=0) for i in range(self.num_clusters)]
        )
        return new_centroids
