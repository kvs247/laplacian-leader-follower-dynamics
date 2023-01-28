import * as systematicMatrix from '../systematicMatrix.js';

console.log('');

getAllBinaryVectorsTest();

// getAllBinaryVectors
function getAllBinaryVectorsTest() {
    const inputDim = 4;
    const expectedResult = [
        '0001', '0010', '0011',
        '0100', '0101', '0110',
        '0111', '1000', '1001',
        '1010', '1011', '1100',
        '1101', '1110', '1111'
      ];
    if (systematicMatrix.getAllBinaryVectors(inputDim).toString() !== expectedResult.toString()) {
        console.log(systematicMatrix.getAllBinaryVectors(inputDim));
        throw new Error('getAllBinaryVectors did not pass');
    };
    console.log('getAllBinaryVectors passed');
    console.log('');
}