#include "binary_search.h"

using namespace std;

Result binarySearch(float data[], float number, int size) {

	int left = 0;
	int right = size - 1;
	Result r;
	if (right < 0) {
		throw invalid_argument("The array cannot be empty.");
	}
	int middle;
	float guess;


	while (left <= right ) {
		middle = left + (right - left) / 2;
		guess = data[middle];
		if (guess == number) {
			r.number = guess;
			r.position = middle;
			return r;
		} else if (guess > number){
			right = middle - 1;


		} else {
			left = middle + 1;
		}
	}
	r.number = number;
	r.position = -1;
	return r;
}
/*
int main() {
  // float data[] = {1, 2, 5, 10, 11, 12, 20, 22, 23, 25};
  float data[] = {};
  float number = 1;
  int size = sizeof(data)/sizeof(data[0]);
  Result result = binarySearch(data, number, size);
  cout << "The number: " << result.number << ".\n";
  if (result.position >= 0){
    cout << "Was found at position: " << result.position << ".\n";
  } else {
    cout << "Was not found in the given array.\n";
  }

}
*/
