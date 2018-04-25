from sklearn.cluster import MiniBatchKMeans, DBSCAN
from sklearn.mixture import GaussianMixture

# choice 5 because the data are from 5 resources
model = MiniBatchKMeans(n_clusters=5)
model.fit(matrix)
predict_label = model.predict(matrix)

