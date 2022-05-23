#ifndef _TESTBED_
#define _TESTBED_
#include <iostream>
#include "SelectionAlgorithm.h"
#include "AlgorithmSortAll.h"
#include "AlgorithmSortK.h"
#include "AlgorithmSortHeap.h"
#include "AlgorithmSortQuick.h"
#include <ctime>

using namespace std;

class TestBed {
    public:
    TestBed();
    SelectionAlgorithm *algorithm;
    void execute();
    void setAlgorithm(int, int);
    ~TestBed();
};

#endif