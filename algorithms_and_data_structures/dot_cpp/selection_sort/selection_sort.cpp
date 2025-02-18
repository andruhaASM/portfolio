#include "selection_sort.h"

using namespace std;

int getSmallestElement(vector<float>& data){
  // Get the element.
  float smallest_element = data[0];
  int smallest_index = 0;
  int data_len = end(data) - begin(data);
  for (int i = 0; i < data_len; i++) {
    if (data[i] < smallest_element) {
      smallest_element = data[i];
      smallest_index = i;
    }
  }
  return smallest_index;
}

vector<float> selectionOrdering(vector<float> data) {
  int data_len = data.end() - data.begin();
  int smallest_item_index;
  if (data_len == 1) {
    return data;
  }

  if (data_len == 0) {
    throw invalid_argument("The array cannot be empty");
  }
  vector<float> ordered_array;
  while (!data.empty()) {
    smallest_item_index = getSmallestElement(data);
    ordered_array.push_back(data[smallest_item_index]);
    data.erase(data.begin() + smallest_item_index);
    data_len = data.end() - data.begin();
    
  }
  return ordered_array;
}

int main(){
  vector<float> data = {2, -1, 5, 5, 5, 0, 3};
  vector<float> result = selectionOrdering(data);
  cout << "The ordered array is: ";
  for (int i = 0; i < result.size(); i++) {
    cout << result[i] << " ";
  }
  cout << "\n";
  
}
