#ifndef __ALGOHEAP__
#define __ALGOHEAP__

#include "SelectionAlgorithm.h"
#include "BinaryHeap.h"
#include <iostream>

using namespace std;

class AlgorithmSortHeap : public SelectionAlgorithm {
    public:
        int select();
        AlgorithmSortHeap(int);
};

#endif