from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 
from sklearn.datasets import load_iris


dataset = load_iris()


X = dataset.data
y = dataset.target


X_train, x_test, y_train, y_test train_test_split(x, y, shuffle=True, test_size=0.2)


knn = KNeighborsClassifier(n_neighbors=7)


knn.fit(x_train, y_train)


print(knn.predict(x_test))
