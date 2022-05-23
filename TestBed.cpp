#include "TestBed.h"

TestBed :: TestBed() {
    // constructor does nothing
}

void TestBed :: setAlgorithm(int type, int k) {
    if (type == 1) {
        algorithm = new AlgorithmSortK(k);
    }
    else if(type == 2){
        algorithm = new AlgorithmSortAll(k);
    }
    else if (type == 3){
        algorithm = new AlgorithmSortHeap(k);
    }
    else if (type == 4){
        algorithm = new AlgorithmSortQuick(k);
    }
}

void TestBed :: execute() {
    int result; 
    clock_t start = clock();
    result = algorithm->select(); //running selected algorithm
    clock_t end =clock();
    double cpu_time = static_cast<double>( end - start );
    cout << "Result is: " << result << endl;
    cout << "Time is: " << cpu_time << endl;
}

TestBed :: ~TestBed() {
    delete algorithm;
}