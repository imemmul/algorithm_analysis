#include "AlgorithmSortHeap.h"

AlgorithmSortHeap :: AlgorithmSortHeap(int k) : SelectionAlgorithm(k){
    this->k = k;
}

int AlgorithmSortHeap :: select(){
    BinaryHeap heap (k);
    int size;
    int N;
    cin >> size; // keeps size
    for (int i = 0; i < k; i ++){
        cin >> N;
        heap.insert(N); // inserting all items to heap
    }
    for (int i = 0; i < (size - k); i ++) {
        cin >> N;
        if (N >= heap.getMin()){
            heap.deleteMin();
            heap.insert(N);
        }
    }
    return heap.getMin();
}