#ifndef _AlgorithmSortK_
#define _AlgorithmSortK_
#include "SelectionAlgorithm.h"
#include <iostream>

using namespace std;

class AlgorithmSortK : public SelectionAlgorithm {
    public:
        int select();
        AlgorithmSortK(int);
};

#endif