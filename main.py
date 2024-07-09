# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Vector:
    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        formatted_components = ','.join(f'{x:.4f}' for x in self.components)
        return f"{formatted_components}"

    def __add__(self, other):
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def __mul__(self, scalar):
        return Vector(*(x * scalar for x in self.components))

    def dot(self, other):
        return sum(x * y for x, y in zip(self.components, other.components))

    def norm(self):
        return sum(x ** 2 for x in self.components) ** 0.5

    def distance(self, other):
        diff = self.__sub__(other)
        return diff.norm()

    def copy(self):
        return Vector(*self.components)


def read_vectors_from_file(file_path):
    vectors = []
    with open(file_path, 'r') as file:
        for line in file:
            components = list(map(float, line.strip().split(',')))
            vectors.append(Vector(*components))
        return vectors


def run(k, input_data, iter = 200):
    if iter <= 1 or iter >= 1000: #validation checks
        print("Invalid maximum iteration!")
        return
    vectors = read_vectors_from_file(input_data)
    if k <= 1 or k >= len(vectors):
        print("Invalid number of clusters!")
        return

    centroids = [] #initialize centroids
    for i in range(k):
        centroids.append((vectors[i].copy(), []))

    for j in range(iter):
        for i in range(len(vectors)): #Assign every xi to the closest cluster
            new_vector = vectors[i]
            d_min = float('inf')
            centroid_min = None
            cluster_min = None
            for centroid, cluster in centroids:
                d = new_vector.distance(centroid)
                if d < d_min:
                    d_min = d
                    centroid_min = centroid
                    cluster_min = cluster
            cluster_min.append(new_vector)

        counter = 0
        for centroid, cluster in centroids: #update the centroids
            if not cluster:
                continue
            sum_vector = Vector(*([0] * len(centroid.components)))
            for x in cluster:
                sum_vector = sum_vector.__add__(x)
            updated_centroid = sum_vector.__mul__(1/len(cluster))
            centroid_before = Vector(*centroid.components)
            centroid.components = updated_centroid.components
            if updated_centroid.distance(centroid_before) < 0.001:
                counter += 1
            cluster.clear()

        if counter == len(centroids): #check convergence for all centroids
            break

    for centroid, cluster in centroids:
        print(centroid)

if __name__ == "__main__":
    path = "C:/Users/inbar/PycharmProjects/Kmeans/tests/input_1.txt"
    run(3, path, 999)