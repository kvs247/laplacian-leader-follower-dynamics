#include <stdio.h>
#include <stdlib.h>

int** getBinaryVectors(int dim) {
    int numVectors = (1 << dim) - 2;
    int** result = (int**)malloc(numVectors * sizeof(int*));

    for (int i = 0; i < numVectors; ++i) {
        result[i] = (int*)malloc(dim * sizeof(int));

        int val = i + 1;
        for (int j = dim - 1; j >= 0; --j) {
            result[i][j] = val % 2;
            val /= 2;
        }
    }

    return result;
}

int binaryVectorsTest() {
    int dim = 5;
    int** result = getBinaryVectors(dim);

    printBinaryVectors(result);

    // Free the allocated memory
    for (int i = 0; i < (1 << dim) - 1; ++i) {
        free(result[i]);
    }
    free(result);

    return 0;
}
