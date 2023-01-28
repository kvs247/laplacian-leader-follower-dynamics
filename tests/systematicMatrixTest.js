import * as systematicMatrix from '../systematicMatrix.js';

console.log('');

getAllBinaryVectorsTest();

// getAllBinaryVectors
function getAllBinaryVectorsTest() {
    const inputDim = 4;
    const expectedResult = [
        [ 0, 0, 0, 1 ],
        [ 0, 0, 1, 0 ],
        [ 0, 0, 1, 1 ],
        [ 0, 1, 0, 0 ],
        [ 0, 1, 0, 1 ],
        [ 0, 1, 1, 0 ],
        [ 0, 1, 1, 1 ],
        [ 1, 0, 0, 0 ],
        [ 1, 0, 0, 1 ],
        [ 1, 0, 1, 0 ],
        [ 1, 0, 1, 1 ],
        [ 1, 1, 0, 0 ],
        [ 1, 1, 0, 1 ],
        [ 1, 1, 1, 0 ],
        [ 1, 1, 1, 1 ]
    ];
    if (systematicMatrix.getAllBinaryVectors(inputDim).toString() !== expectedResult.toString()) {
        console.log(systematicMatrix.getAllBinaryVectors(inputDim));
        throw new Error('getAllBinaryVectors did not pass');
    };
    console.log('getAllBinaryVectors passed');
    console.log('');
}