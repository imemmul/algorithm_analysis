#include "AlgorithmSortK.h"
using namespace std;

AlgorithmSortK :: AlgorithmSortK(int k) : SelectionAlgorithm(k) {
    // this constructor will use selection algorithm's constructor k so didnt initialized
    //subclasses of super class will call superclass default constructor
    this->k = k;
}

int AlgorithmSortK :: select() {
    //algorithm goes here
    int i,j,z; // loop variables
    int location; //this variable stores location of variable that will be inserted.
    int result;
    int *pNums;
    int key;
    int size;
    int temp;
    cin >> size;
    int N = 0;
    pNums = new int[k];
    for (i = 0; i < k; i++){
        cin >> N;
        pNums[i] = N;
    }
    for (i = 0; i < k; i++) { //insertion sort below
        key = pNums[i];
        j = i - 1;
        while(j >= 0 && pNums[j] < key) {
            pNums[j + 1] = pNums[j];
            --j;
        }
        pNums[j + 1] = key;
    }
    //hardest part below
    for (i = k; i < size; i++){
        cin >> N;
        if (N >= pNums[k - 1]){
            for (j = 0; j < k; j++){
                if (N >= pNums[j]){
                    location = j;
                    break; // when location is found break from loop
                }
            }
            for (z = location; z < k; z += 2){ // because of we storing two temp variables in our memory we should increment by two
                temp = pNums[z];
                pNums[z] = N;
                N = pNums[z + 1];
                pNums[z + 1] = temp;
            }
        }
    }
    result = pNums[k - 1];
    delete [] pNums;
    pNums = 0;
    return result;
}