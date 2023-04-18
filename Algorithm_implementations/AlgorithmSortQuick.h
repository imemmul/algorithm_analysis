#ifndef _AlgorithmSortQuick_
#define _AlgorithmSortQuick_
#include "SelectionAlgorithm.h"
#include <iostream>

using namespace std;

class AlgorithmSortQuick : public SelectionAlgorithm  {
    public:
        int select();
        int quickselect(int *, int, int, int);
        int pivotselect(int *, int, int);
        void swap(int *, int *);
        void display(int *, int);
        AlgorithmSortQuick(int);
};

#endif