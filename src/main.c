#include <stdio.h>
#include "printHelper.h"
#include "generate.h"

// #include "helper.h"
// #include "binaryVectors.h"

int main()
{

  int **laplacianMats = getLaplacianMatrices(4);
  int numLapMats = getNumLaplacianMatrices(4);
  for (int i = 0; i < numLapMats; i++) {
    int *lapMat = laplacianMats[i];
    printMatrix(4, lapMat);
  }
}