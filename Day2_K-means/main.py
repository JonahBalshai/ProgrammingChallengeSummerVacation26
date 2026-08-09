import numpy as np
import matplotlib.pyplot as plt

RANGE = 3
ITERATIONS = 10
TOL = 1e-3
GENERATOR = np.random.default_rng()

def k_means(n_clusters, data):
    clusters = GENERATOR.random(size=(n_clusters,2)) * RANGE

    # Suggested Improvements
    for _ in range(ITERATIONS):
        diff = data[:, None, :] - clusters[None, :, :]
        diff = (diff ** 2).sum(axis=-1)
        closest_clusters = np.argmin(diff, axis=1)

        converge_clusters = 0
        for i, _ in enumerate(clusters):
            cluster_data = data[closest_clusters == i]

            if cluster_data.size == 0:
                continue

            new_cluster = np.mean(cluster_data, axis=0)

            if ((new_cluster - clusters[i]) ** 2).sum(axis=-1) < TOL:
                converge_clusters += 1

            clusters[i] = new_cluster

        if converge_clusters == n_clusters:
            return clusters

    """ Previous Approach
        for _ in range(ITERATIONS):
            plt.scatter(data[:,0], data[:,1])
            plt.scatter(clusters[:,0], clusters[:,1], c='red')
            ax.set_aspect('equal')
            plt.show()

            closest_clusters = []
            for point in data:
                closest_clusters.append(np.argmin([np.linalg.norm(point - cluster) for cluster in clusters]))
            closest_clusters = np.asarray(closest_clusters)

            for i, _ in enumerate(clusters):
                cluster_data = np.asarray(data[np.where(closest_clusters == i)])
                clusters[i] = np.mean(cluster_data, axis=0)

        plt.scatter(data[:,0], data[:,1])
        plt.scatter(clusters[:,0], clusters[:,1], c='red')
        ax.set_aspect('equal')
        plt.show()
        """
    
    return clusters

def generate_data(n_clusters, n_points):
    # Suggested Improvements
    generator = np.random.default_rng()
    clusters = generator.random(size=(n_clusters, 2)) * RANGE
    data = generator.normal(size=(n_clusters, n_points, 2)) * np.sqrt(0.05) + clusters[:, None, :]

    """Previous Approach
    clusters = np.random.random_sample(size=(n_clusters,2)) * RANGE
    generator = np.random.default_rng()
    data = np.asarray([generator.multivariate_normal(mean=cluster, cov=[[0.05,0],[0,0.05]], size=(n_points, 2)) for cluster in clusters]).reshape(-1, 2)
    np.random.shuffle(data)
    """

    return data.reshape(-1, 2)

def main():
    data = generate_data(3, 100)
    clusters = k_means(3, data)

    plt.scatter(data[:,0], data[:,1])
    plt.scatter(clusters[:,0], clusters[:,1])
    plt.show()

if __name__ == "__main__":
    main()