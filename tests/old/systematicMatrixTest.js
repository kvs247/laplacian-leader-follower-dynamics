import * as systematicMatrix from '../systematicMatrix.js';

console.log('');

getAllBinaryVectorsTest();
getAllLaplacianMatricesTest();

console.log('all tests passed');
console.log('');

// getAllLaplacianMatrices
function getAllLaplacianMatricesTest() {
    const inputDim = 3;
    const expectedResult = [
        [ 
            [ -0, 0, 0 ], 
            [ 0, -1, 1 ], 
            [ 0, 1, -1 ] 
        ],
        [ 
            [ -1, 0, 1 ], 
            [ 0, -0, 0 ], 
            [ 1, 0, -1 ] 
        ],
        [ 
            [ -1, 0, 1 ], 
            [ 0, -1, 1 ], 
            [ 1, 1, -2 ] 
        ],
        [ 
            [ -1, 1, 0 ], 
            [ 1, -1, 0 ], 
            [ 0, 0, -0 ] 
        ],
        [ 
            [ -1, 1, 0 ], 
            [ 1, -2, 1 ], 
            [ 0, 1, -1 ] 
        ],
        [ 
            [ -2, 1, 1 ], 
            [ 1, -1, 0 ], 
            [ 1, 0, -1 ] 
        ]
      ];
      if (systematicMatrix.getAllLaplacianMatrices(inputDim).toString() !== expectedResult.toString()) {
        console.log(systematicMatrix.getAllLaplacianMatrices(inputDim));
        throw new Error('getAllLaplaciansMAtrices did not pass')
      };
      console.log('getAllLaplacianMatrices passed');
      console.log('');
}

// getAllBinaryVectors
function getAllBinaryVectorsTest() {
    const inputDim = 4;
    const expectedResult = [
        '0001', '0010', '0011',
        '0100', '0101', '0110',
        '0111', '1000', '1001',
        '1010', '1011', '1100',
        '1101', '1110'
      ];
    if (systematicMatrix.getAllBinaryVectors(inputDim).toString() !== expectedResult.toString()) {
        console.log(systematicMatrix.getAllBinaryVectors(inputDim));
        throw new Error('getAllBinaryVectors did not pass');
    };
    console.log('getAllBinaryVectors passed');
    console.log('');
}