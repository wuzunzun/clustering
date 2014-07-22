from numpy import *
import unittest
import distance
from kmeans import *


def create_clusters(centroids, size, distance):
    X = []
    for centroid in centroids:
        X.extend(create_cluster(array(centroid), size, distance))
    return mat(X)


class DistanceTest(unittest.TestCase):

    def test_euclid_array(self):
        a = array((1, 2))
        b = array((3, 4))
        dist = distance.euclid(a, b)
        self.assertEqual(sqrt(8), dist)

    def test_euclid_matrix(self):
        a = mat([1, 2])
        b = mat([3, 4])
        dist = distance.euclid(a, b)
        self.assertEqual(sqrt(8), dist)

    def test_euclid_3dms(self):
        a = mat([1, 2, 3])
        b = mat([4, 5, 6])
        dist = distance.euclid(a, b)
        self.assertEqual(sqrt(27), dist)

    def test_euclid_1dms(self):
        a = mat([1])
        b = mat([4])
        dist = distance.euclid(a, b)
        self.assertEqual(3, dist)


def create_cluster(centroid, size, distance):
    cluster = []
    for x in xrange(size):
        cluster.append(
            centroid + array([randrange(-distance, distance, 1) for x in xrange(len(centroid))]))
    return cluster


class KMeansTest(unittest.TestCase):

    def test_k_means(self):
        X = create_clusters([(20, 30), (20, 60), (30, 45), (40, 60)], 30, 8)
        labels = k_means(X, 4)
        icons = ['b_', 'b.', 'bo', 'b+', 'b*']

        for idx, l in enumerate(labels):
            plt.plot(X[idx, 0], X[idx, 1], icons[int(l)])

        plt.show()


if __name__ == '__main__':
    unittest.main()
