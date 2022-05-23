#include "AlgorithmSortQuick.h"
using namespace std;

AlgorithmSortQuick :: AlgorithmSortQuick(int k) : SelectionAlgorithm(k) {
    this->k = k;
}

int AlgorithmSortQuick :: select() {
    int N = 0;
    int number = 0;
    int result = 0;
    cin >> N;
    // int numbers [15] = {10, 11, 3, 4, 19, 15, 31, 32, 69, 35, 12, 34, 90, 2};
    // int k = 15;
    int *numbers = new int[N];
    for(int i = 0; i < N; i++){
        cin >> number;
        numbers[i] = number;
    }
    result =  quickselect(numbers, 0, N - 1, k);
    //display(numbers, N);
    delete [] numbers;
    numbers = 0;
    return result;
}

int AlgorithmSortQuick :: quickselect(int *numbers, int left, int right, int k){
    if((right - left) < 10){
        for(int i = left + 1; i <= right; i++){
            int j, key = numbers[i];
            for(j = i - 1; j >= 0; j--){
                if(numbers[j] > key){
                    break;
                }
                numbers[j + 1] = numbers[j];
            }
            numbers[j + 1] = key;
        }
        return numbers[k - 1];
    }else {
        int pivot = pivotselect(numbers, left, right);
        int i = left + 1, j = right - 2;
        while(true){
            while(numbers[i] > pivot){
                i++;
            }
            while(numbers[j] < pivot){
                j--;
            }
            if(i < j){
                swap(&numbers[j], &numbers[i]);
                i++;
                j--;
            }else {
                break;
            }
        }
        swap(&numbers[i], &numbers[right - 1]);
        if(k <= (i - 1)){
            return quickselect(numbers, left, i-1, k);
        }else if (k == i){
            return pivot;
        }else {
            return quickselect(numbers, i + 1, right, k);
        }
    }
}

int AlgorithmSortQuick :: pivotselect(int *numbers, int left, int right){
    int center = (left + right) / 2;
    if(numbers[center] < numbers[left]){
        swap(&numbers[left], &numbers[center]);
    }
    if(numbers[right] < numbers[left]){
        swap(&numbers[left], &numbers[right]);
    }
    if(numbers[right] < numbers[center]){
        swap(&numbers[center], &numbers[right]);
    }
    swap(&numbers[center], &numbers[right - 1]);
    return numbers[right - 1];
}

void AlgorithmSortQuick :: swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void AlgorithmSortQuick :: display(int numbers [], int size) {
    for(int i = 0; i < size; i++){
        cout << "||"<< i << ": " <<numbers[i] << "|| ";
    }
    cout << "" << endl;
}