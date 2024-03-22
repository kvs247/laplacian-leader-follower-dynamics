#include <stdio.h>

void printVector(int dim, int *vector)
{
    printf("[");
    for (int i = 0; i < dim; i++)
    {
        printf("%d", vector[i]);
        if (i != (dim - 1))
        {
            printf(", ");
        }
    }
    printf("]\n");
}

void printMatrix(int dim, int matrix[])
{
    printf("\n");
    for (int i = 0; i < dim; i++)
    {
        printf("|");
        for (int j = 0; j < dim; j++)
        {
            int idx = (dim * i) + j;
            int value = matrix[idx];
            if (value < 0)
            {
                printf(" %d", value);
            }
            else
            {
                printf("  %d", value);
            }
        }
        printf(" |\n");
    }
    printf("\n");
}

void printMatrixD(int dim, double matrix[])
{
    printf("\n");
    for (int i = 0; i < dim; i++)
    {
        printf("|");
        for (int j = 0; j < dim; j++)
        {
            int idx = (dim * i) + j;
            double value = matrix[idx];
            if (value < 0)
            {
                printf(" %f", value);
            }
            else
            {
                printf("  %f", value);
            }
        }
        printf(" |\n");
    }
    printf("\n");
}

void printBinaryVectors(int **binaryVectors)
{
    int dim = sizeof(binaryVectors) / (sizeof(binaryVectors[0]) / sizeof(binaryVectors[0][0]));
    printf("%d", dim);
    printf("\n");
    int numVectors = (1 << dim) - 2;
    for (int i = 0; i < numVectors; ++i)
    {
        for (int j = 0; j < dim; ++j)
        {
            printf("%d ", binaryVectors[i][j]);
        }
        printf("\n");
    }
}
