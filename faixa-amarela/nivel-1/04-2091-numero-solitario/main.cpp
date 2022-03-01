#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>
#include <boost/algorithm/string/classification.hpp>
#include <boost/algorithm/string/split.hpp>

using namespace std;

int main(int argc, char** argv) {
  ifstream input(argv[1]);  
  string inLine;
  char delimiter = ' ';  

  int n;
  vector<string> s_numbers = {};
  vector<int> numbers = {};
  vector<int>::iterator it;
  int number;
  
  while(1) {
    getline(input, inLine);    
    n = stoi(inLine);
    if (n == 0) break;

    numbers.clear();
    
    // getline(input, inLine);
    // boost::split(
    //   s_numbers, 
    //   inLine, 
    //   boost::is_any_of(" "),
    //   boost::token_compress_on
    // );
    
    // for (int i=0; i<n; i++) {
    //   numbers.push_back(stoi(s_numbers[i]));
    // }

    for (int i=0; i<n; i++) {
      input >> inLine;
      numbers.push_back(stoi(inLine));
    }
    getline(input, inLine);
    
    while(1) {     
      number = numbers[0];
      numbers.erase(numbers.begin());

      it = find(numbers.begin(), numbers.end(), number);
      
      if (it == numbers.end()) {
        cout << number << endl;
        break;
      }

      numbers.erase(it);
    }
  }

  input.close(); 
}