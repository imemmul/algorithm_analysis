#include "BinaryHeap.h"

BinaryHeap::BinaryHeap(int capacity) {
    this->capacity = capacity;
	
	// The element at index 0 is not used!
	// The root element will be placed at index 1
	heap = new int[capacity+1];
	size = 0;
}

BinaryHeap::~BinaryHeap() {
	delete [] heap;
}

void BinaryHeap::insert(int element) {
	int position = size + 1;
	// TO BE COMPLETED
	// hole = position
	if(size < capacity){
		for (/* */; position > 1 && element < this->heap[position / 2]; position /= 2){
			this->heap[position] = this->heap[position / 2];
		}
		this->heap[position] = element;
		this->size += 1;
	}
	
	// this adds item to min heap array so after insertion we should rearrange the items in the array
	// The capacity of the heap is assumed to be fixed.
	// Insert the element if size < capacity
	// Do nothing otherwise.
	
	 // should increment this
	// After the new element is inserted, perform a percolate up operation here.
	// You can add a percolateUp method to the class,
	// or just implement the operations within this insert method.
}

void BinaryHeap::deleteMin() {

	// TO BE COMPLETED
	if (this->size < 1) {
		return;
	}else {
		//cout << "heap size" << this->heap[size];
		this->heap[1] = this->heap[size];
		size--;
		percolateDown(1);
	}
	// If the size is less than 1, do nothing and stop
	// Otherwise, replace the root of the heap with the last element on the last level
	// ...
	
	// Then, call the percolateDown function by providing the index of the root node, i.e., 1
}

int BinaryHeap::getMin() {
	
	// TO BE COMPLETED
	if(this->size < 1) {
		return -1;
	}else{
		return this->heap[1]; // returning root node
	}
	// If the size is less than 1, return -1
	// Otherwise, return the value of the root node
	
	return -1;
}

void BinaryHeap::display(){
	for(int i = 1; i < size + 1; i++){
		cout << "element is " << this->heap[i] << endl;
	}
}

void BinaryHeap::percolateDown(int hole) {

	// TO BE COMPLETED
	
	// Compare the node with its children; if they are in the correct order, stop
	// Otherwise, swap the element with the smallest child
	// Repeat the operation for the swapped child node
	
	int left_child = 2*hole;
	int right_child = 2*hole + 1;
	int min = hole;

	if(left_child <= size && this->heap[left_child] < this->heap[hole]){
		//cout << this->heap[left_child] << " min left" << endl;
		min = left_child;
	}
	if(right_child <= size && this->heap[right_child] < this->heap[min]){
		//cout << this->heap[right_child] << " min right" << endl;
		min = right_child;
	}
	if(min != hole){
		swap(hole, min);
		percolateDown(min); // min is swapped then recursed
	}
	// Make sure that you take care of all the possible cases:
	// 1. The node might not have a child at all
	// 2. The node might have only a left child
	// 2.1. The left child might be smaller
	// 3. The node might have both left and right children
	// 3.1 Only the left child might be smaller
	// 3.2 Only the right child might be smaller
	// 3.3 Both left and right children might be smaller, in which case the element should be swapped with the smallest of the two
}

void BinaryHeap::swap(int i, int j) {
	int t = heap[i];
	heap[i] = heap[j];
	heap[j] = t;
}