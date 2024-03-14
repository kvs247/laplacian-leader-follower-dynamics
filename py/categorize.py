'''
Calculates controllability class for all graphs of given dimension. 
The function categorize takes two arguments: the dimension, and the filepath if continuing a run 
    (optional: will create a new file if blank)
'''

import datetime
import glob
import numpy as np
import os
import sys

import matrixGeneration
import matrixMath

controllability_dict = {
    "essentially controllable": "EC",
    "conditionally controllable": "CC",
    "completely uncontrollable (disconnected)": "CU-dis",
    "completely uncontrollable (degenerate)": "CU-degen",
    "completely uncontrollable (nondegenerate)": "CU-nondegen"
}

def categorize(dim, directory = None):
    matrices_per_file = 1e6  # IMPORTANT
    num_matrices = int((2 ** int((dim / 2) * (dim - 1)))) # (dim / 2) * (dim - 1) elements in matrix triangle
    num_files = int(num_matrices / matrices_per_file)
    id_dim = str(dim).rjust(2, '0')
    
    # new run
    if not directory:
        start = 0
        file_number = 0
        continuing = False
        date = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        dir_path = f'data/laplacian{dim}-{date}'
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

    # continuing run - ASSUMES PROGRAM STOPPED MID FILE    
    else:
        print(" finding starting point...")
        files = glob.glob(f'{directory}/*.txt')
        files.sort(key = lambda x: int(os.path.basename(x).split('.')[0].split('-')[1]))
        last_file = files[-1]
        with open(last_file, 'r') as f:
            data = f.read()
            if not data.endswith(']'):
                data += ']'
            data = np.array(eval(data))
            matrix_generators = np.array([dataObj['id'][3:] for dataObj in data]).astype(int)

            file_number = int(os.path.basename(last_file)[:-4].split('-')[1])
            continuing = True
            dir_path = os.path.dirname(last_file)
    
    # begin calculation
    print(" running...")
    while file_number <= num_files:
        if continuing:
            continuing = False
            start = np.max(matrix_generators) + 1
            filepath = last_file
        else:
            start = 0
            filepath = f'{dir_path}/laplacian{dim}-{file_number}.txt'
            with open(filepath, 'a') as f:
                f.write('[')

        stop = int((file_number + 1) * matrices_per_file)
        # add rows
        for generator in range(start, stop):
            if generator == num_matrices:
                break

            id = f'{id_dim}{generator}'
            matrix = matrixGeneration.getLaplacianFromId(id)
            [eigen_values, eigen_vectors] = matrixMath.getEigenState(matrix)
            control_class = matrixMath.pbhTest(matrix, eigen_values, eigen_vectors)

            data_obj = { 'id': f'{id[0:2]}-{id[2:]}', 'class': controllability_dict[control_class] }
            with open(filepath, 'a') as f:
                f.write('\n')
                f.write(str(data_obj))
                f.write(',')

        with open(filepath, 'a') as f:
            f.write('\n')
            f.write(']')

        file_number += 1

if __name__ == '__main__':
    dim = int(input('dimension:'))
    path = input('path:')
    if path == '':
        path = None
    start_time = datetime.datetime.now()
    categorize(dim, path)
    print(f'Execution time: {datetime.datetime.now() - start_time}')


