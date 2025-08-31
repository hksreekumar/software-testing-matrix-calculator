import numpy as np

class DenseMatrix:
    """Class implementation to perform dense matrix operations"""
    def add(self, mat_a: np.array, alpha: float, mat_b: np.array, beta: float):
        """function to perform mat_c = alpha*mat_a+beta*mat_b"""
        return np.add(alpha*mat_a, beta*mat_b)

    def matrix_vector_multiply(self, mat_a: np.array, vec_b: np.array, transpose_a: bool):
        """function to perform mat_c = op(mat_a)*vec_b"""
        if transpose_a:
            mat_a = np.transpose(mat_a)
        return mat_a.dot(vec_b)

    def matrix_inverse(self, mat_a: np.array):
        """function to return (mat_a)^{-1}"""
        return np.linalg.inv(mat_a)
        