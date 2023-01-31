import matrixGeneration
import matrixMath

id = '07180207'
matrix = matrixGeneration.getLaplacianFromId(id)
matrixMath.printMatrix(matrix)