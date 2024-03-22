#include <stdio.h>
#include <lapacke.h>
#include "printHelper.h"
#include "generate.h"

#define N 4

int main()
{
    lapack_int n = N;
    lapack_int lda = N;

    int **laplacianMats = getLaplacianMatrices(n);
    int numLapMats = getNumLaplacianMatrices(n);

    for (int i = 0; i < numLapMats; i++)
    {
        printf("Matrix %d\n", i);

        int *lapMat = laplacianMats[i];

        double lapMatD[n * n];
        for (int i = 0; i < n * n; i++)
        {
            lapMatD[i] = (double)lapMat[i];
        }

        printMatrixD(n, lapMatD);

        double wr[n], wi[n];         // Arrays to store real and imaginary parts of eigenvalues
        double vl[n * n], vr[n * n]; // Left and right eigenvectors

        int info = LAPACKE_dgeev(LAPACK_COL_MAJOR, 'V', 'V', n, lapMatD, lda, wr, wi, vl, lda, vr, lda);

        // Check if LAPACKE_dgeev was successful
        if (info == 0)
        {
            printf("Eigenvalues:\n");
            for (int i = 0; i < n; i++)
            {
                if (wi[i] == 0)
                {
                    printf("  %f\n", wr[i]); // Real eigenvalue
                }
                else
                {
                    printf("  %f + %fi\n", wr[i], wi[i]); // Complex eigenvalue
                }
            }

            printf("Eigenvectors:\n");
            for (int i = 0; i < n; i++)
            {
                printf("  Eigenvector %d:\n", i);
                for (int j = 0; j < n; j++)
                {
                    printf("    %f\n", vl[i * n + j]);
                }
            }
        }
        else
        {
            printf("LAPACKE_dgeev failed with error code %d\n", info);
        }

        printf("Eigenvectors (columns):\n");
        printMatrixD(n, vr);
    }
    printf("Number of mats: %d\n", numLapMats);
    double x = pow(2, (3 - 1) * (3 / 2));
    printf("%f\n", x);
}