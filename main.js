import { generateLaplacianMatrix } from "./randomMatrix.js";
import { getAllLaplacianMatrices } from "./systematicMatrix.js";  
import { getEigenState, pbhTest, printMatrix } from "./matrixMath.js";
// import {saveAs } from 'file-saver';
import {Blob} from 'node:buffer';

console.log(document.querySelector('body'));

const data = {
    'one': 271980,
    'two': 2980
};

import * as FileSaver from 'file-saver';
// const FileSaver = require('file-saver');
const blob = new Blob([JSON.stringify(data)], { type: 'application/json' });
FileSaver.saveAs(blob, 'new.txt');

// const lapMat = generateLaplacianMatrix(5);

// printMatrix(lapMat);
// const [ eigenValues, eigenVectors ] = getEigenState(lapMat);
// console.log(pbhTest(lapMat, eigenValues, eigenVectors));

// for (const matrix of getAllLaplacianMatrices(4)) {
//     const [ eigenValues, eigenVectors ] = getEigenState(matrix);
//     const controllability = pbhTest(matrix, eigenValues, eigenVectors);
//     console.log(controllability)
// };
