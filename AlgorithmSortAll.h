#ifndef _AlgorithmSortAll_
#define _AlgorithmSortAll_
#include "SelectionAlgorithm.h"
#include <iostream>

using namespace std;

class AlgorithmSortAll : public SelectionAlgorithm  {
    public:
        int select();
        AlgorithmSortAll(int);
};

#endif
