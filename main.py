import sys
from source.matrix_solver.jacobi_solver import JacobiSolver
from source.matrix_algebra.dense_matrix import DenseMatrix
from scipy.io import loadmat, savemat

def main(args):
    data_file = './data/system_100x100.mat'
    if "--add" in args:
        # read matrix a
        print('> Reading matrix A ...')
        mat_a = loadmat(data_file)['mat_a']
        # read matrix b
        print('> Reading matrix B ...')
        mat_b = loadmat(data_file)['mat_a']
        # add
        print('Adding system A + B...')
        densemat_operations = DenseMatrix()
        mat_c = densemat_operations.add(mat_a, 1., mat_b, 1.)
        # export solution to file
        export_filename = './data/result.mat'
        export_dict = {'result':mat_c}
        savemat(export_filename, export_dict)
        print('> Exported system to ' + export_filename)
    elif "--solve" in args:
        print('> Reading matrix A ...')
        # read matrix a
        mat_a = loadmat(data_file)['mat_a']
        print('> Reading vector b ...')
        # read vector b
        vec_b = loadmat(data_file)['vec_b'].flatten()
        # solving
        print('> Solving system A \\b...')
        my_solver = JacobiSolver()
        vec_x = my_solver.matrix_solve(mat_a, vec_b, 1e-6, 10000)
        # export solution to file
        export_filename = './data/result.mat'
        export_dict = {'result':vec_x}
        savemat(export_filename, export_dict)
        print('> Exported system to ' + export_filename)
    elif "--help" in args:
        print_help()
    else:
        print('Wrong usage!')
        print_help()
        sys.exit(-1)

def print_help():
    print('===========================================================')
    print('Matrix calculator')
    print('===========================================================')
    print('Usage  : --solve  Solves a linear system')
    print('                  from data in file ./data/system_100x100')
    print('                  with results = mat_a\\vec_b')
    print('                  Exports results to results.mat')
    print('         --add    Add two matrices')
    print('                  from data in file ./data/system_100x100')
    print('                  with results = mat_a + mat_b')
    print('                  Exports results to results.mat')
    print('         --help   Help')
    print('Example: python3 main.py --solve')
    print('         python3 main.py --add')
    print('===========================================================')

if __name__ == '__main__':
    main(sys.argv[1:])
    sys.exit(0)
