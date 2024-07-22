# 1.1. Length of a vector

import numpy as np

def compute_vector_len(vector):
    norm = np.sqrt(np.sum([v ** 2 for v in vector]))
    return norm

vector = np.array([3, 4, 5])
result = compute_vector_len(vector)
print(round(result,2))

def compute_vector_len(vector):
    norm = np.linalg.norm(vector)
    return norm

vector = np.array([3, 4, 5])
result = compute_vector_len(vector)
print(round(result,2))  # Output: 3.7416573867739413

v = np. array ([ -2 , 4 , 9 , 21])
result = compute_vector_len(v)
print(round(result,2))

# 1.2. Dot product

def compute_dot_product(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    return dot_product

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
result = compute_dot_product(vector1, vector2)
print(result)


v1 = np.array([0, 1, -1, 2])
v2 = np.array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(np.round(result, 2))

x = np.array([[1, 2],[3, 4]])
k = np.array([1, 2])
print('result \n', x.dot(k))

x = np.array ([[-1 , 2],[3, -4]])
k = np.array ([1, 2])
print('result \n', x @ k)

# 1.3. Multiplying a vector by a matrix
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result

v1 = np.array([[-1, 1, 1], [0, -4, 9]])
v2 = np.array([0, 2, 1])
print(v1.shape)
print(v2.shape)
result = matrix_multi_vector(v1, v2)
print(result)

m = np.array([[ -1, 1, 1], [0, -4, 9]])
v = np.array([0, 2, 1])
result = matrix_multi_vector(m, v)
print (result)

#  1.4 Multiply matrix with a matrix
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

m1 = np.array([[1, 2, 3], [1, 2, 3]])
print(m1.shape)
m2 = np.array([[1, 2], [3, 4], [5, 6]])
print(m2.shape)
result = matrix_multi_matrix(m1, m2)
print(result)

m1 = np.array([[0, 1, 2] , [2, -3, 1]])
m2 = np.array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print (result)

m1 = np.eye(3)
print(m1)
m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1 @ m2
print(result)

m1 = np.eye (2)
print(m1)
m1 = np.reshape(m1,(-1 ,4))[0]
print(m1)
m2 = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1 @ m2
print(result)

m1 = np. array([[1 , 2], [3, 4]])
m1 = np. reshape(m1 ,( -1 ,4) , "F")[0]
print(m1)
m2 = np. array ([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
print(m2)
result = m1 @ m2
print(result)

# 1.5 Matrix inverse
def inverse_matrix(matrix):
    return np.linalg.inv(matrix)

m = np.array([[-8, 4], [2, -4]])
result = inverse_matrix(m)
print(np.round(result,2))

i = m @ result
print(i)
print(np.round(i,2))

m1 = np.array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)

# 2.1 Eigenvector and eigenvalue
def eigen_values_eigen_vectors(matrix):
    eigen_values, eigen_vectors = np.linalg.eig(matrix)
    return eigen_values, eigen_vectors


m = np.array([[1, 2], [3, 4]])
eigen_values, eigen_vectors = eigen_values_eigen_vectors(m)
print(eigen_values)
print(eigen_vectors)

matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = eigen_values_eigen_vectors(matrix)
print(eigenvectors)

# 3.1. Cosine Similarity

def compute_cosine_similarity(v1, v2):
    cos_sim = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return cos_sim

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
result = compute_cosine_similarity(v1, v2)
print(result)

v1 = np.array([1, 2, 3, 4])
v2 = np.array([1, 0, 3, 0])
result = compute_cosine_similarity(v1, v2)
print(np.round(result,3))



