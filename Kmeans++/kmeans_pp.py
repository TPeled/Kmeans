import numpy as np

def initialize_centroids(data, k):
    # data is a 2D numpy array where each row is a data point
    # k is clusters

    n, dim = data.shape
    centroids = np.zeros((k, dim))

    # Step 1: Choose the first center randomly
    centroids[0] = data[np.random.randint(0, n)]

    # Step 2 to 4: Choose the remaining k-1 centers
    for i in range(1, k):
        # Compute D(x)
        distances = np.array([min([np.inner(x-c, x-c) for c in centroids[:i]]) for x in data])

        # Compute the probability distribution
        probabilities = distances / distances.sum()

        # Choose a new data point as a new center
        cumulative_probabilities = np.cumsum(probabilities)
        r = np.random.rand()

        for j, p in enumerate(cumulative_probabilities):
            if r < p:
                centroids[i] = data[j]
                break

    return centroids

