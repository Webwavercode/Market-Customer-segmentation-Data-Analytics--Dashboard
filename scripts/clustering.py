from sklearn.cluster import KMeans

def run_kmeans(scaled_data, k):
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(scaled_data)
    return clusters
