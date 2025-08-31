import numpy as np
from source.matrix_algebra.dense_matrix import DenseMatrix

class JacobiSolver:
    """class implementation for jacobi solver"""
    
    def matrix_solve(self, mat_a, vec_b, error_tol: float, max_iter: int):
        """function to perform matrix solve"""
        # decide matrix algebra for matrix type
        if isinstance(mat_a,np.ndarray):
            matrix_ops = DenseMatrix()
            print('Jacobi solver: dense matrix type')
            # setup matrix C and inverse
            mat_c = np.diag(mat_a)
            inv_mat_c = np.diag(1/mat_c)
        else:
            raise RuntimeError('Jacobi solver: unknown matrix type')

        # setup initial guess
        sol_x =  np.ones(vec_b.shape)
        
        # loop metrics
        current_error = 1e36
        current_iter = 1

        # iterative solving
        while current_error > error_tol and current_iter <= max_iter:
            pdt = matrix_ops.matrix_vector_multiply(mat_a, sol_x, False)
            pdt = matrix_ops.add(vec_b, 1., pdt, -1.)
            pdt = matrix_ops.matrix_vector_multiply(inv_mat_c, pdt, False)
            sol_x_iter = matrix_ops.add(sol_x, 1., pdt, 1.)

            error = matrix_ops.add(sol_x_iter, 1., sol_x, -1.)
            sol_x = sol_x_iter
            current_error = np.linalg.norm(error)
            current_iter+=1

        # unconvergence checks
        if current_iter > max_iter:
            raise RuntimeError('Jacobi solver did not converge because of max_iter')

        # essential infos
        print(f'Jacobi solver converged with {current_iter-1} iterations with absolute error norm {current_error}')
        return sol_x
