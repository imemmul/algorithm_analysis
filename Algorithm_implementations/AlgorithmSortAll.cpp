#include "AlgorithmSortAll.h"

AlgorithmSortAll :: AlgorithmSortAll(int k) : SelectionAlgorithm(k){
    this->k = k;
}

int AlgorithmSortAll :: select(){
    int i,j;
    int result;
    int key;
    int size;
    int temp;
    cin >> size;
    int N = 0;
    int *pNums = new int[size];
    for (i = 0; i < size; i++){ // adding all elements to array
        cin >> N;
        pNums[i] = N;
    }
    for (i = 0; i < size; i++) { // sorting decreasing order
        key = pNums[i];
        j = i - 1;
        while(j >= 0 && pNums[j] < key) {
            pNums[j + 1] = pNums[j];
            --j;
        }
        pNums[j + 1] = key;
    }
    result = pNums[k - 1];
    delete [] pNums;
    pNums = 0;
    return result;
}
