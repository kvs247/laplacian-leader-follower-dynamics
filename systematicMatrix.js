// systematic matrix generation

let x = getAllLaplacianMatrices(4);
// console.log(x)

// get array of all Laplacian matrices for dimension > 2
export function getAllLaplacianMatrices(dim) {
    const result = [];
    const allBinaryVectors = getAllBinaryVectors(dim);
    for (const elements of allBinaryVectors) {
        console.log(elements)
    };
}

// get dim 2 array containing all binary vectors for the given dimension
// NOTE: this does not include the zero vector or all 1s vector
export function getAllBinaryVectors(dim) {
    const result = [];
    for (let i = 1; i < 2 ** dim; i++) {
        result.push(i.toString(2).padStart(4, '0').split('').map(Number));
    };
    return result;
}