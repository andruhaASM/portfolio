#ifndef BINARY_SEARCH_H
#define BINARY_SEARCH_H
#include <iostream>
#include <stdexcept>

struct Result {
  float number;
  int position;
};

Result binarySearch(float data[], float number, int size);
#endif // BINARY_SEARCH_H

