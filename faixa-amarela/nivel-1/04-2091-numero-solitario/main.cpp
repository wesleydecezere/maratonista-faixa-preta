#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

string vtos(vector<char> v) {
  string s(v.begin(), v.end());
  return s;
}

int main(int argc, char** argv) {
  ifstream input(argv[1]);  
  string inLine;
  char delimiter = ' ';  

  int n;
  vector<char> numbers = {};
  vector<char>::iterator it;
  char number;

  
  while(1) {
    getline(input, inLine);    
    n = stoi(inLine);
    if (n == 0) break;

    getline(input, inLine);
    
    numbers.clear();
    copy(inLine.begin(), inLine.end(), std::back_inserter(numbers));
    numbers.erase(
      remove(numbers.begin(), numbers.end(), delimiter),
      numbers.end()
    );
      
    while(1) {
      cout << "Init: " << vtos(numbers) << endl;
      
      number = numbers[0];
      numbers.erase(numbers.begin());

      it = find(numbers.begin(), numbers.end(), number);
      
      if (it == numbers.end()) {
        cout << "Out: " << number << endl;
        break;
      }

      cout << "Final: " << vtos(numbers) << endl; 
      
      numbers.erase(it);
    }
  }

  input.close(); 
}