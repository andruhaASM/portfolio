#include <gtest/gtest.h>
#include "binary_search.h"

TEST(BinarySearchTest, BasicAssertions){
  float data[] = {1, 2, 5, 8, 9};
  float number = 8;
  int size = sizeof(data)/sizeof(data[0]);
  Result r = binarySearch(data, number, size);
  EXPECT_EQ(r.number, number);
  EXPECT_EQ(r.position, 3);
}
