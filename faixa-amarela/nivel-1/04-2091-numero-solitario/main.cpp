#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

int main(int argc, char** argv) {
  ifstream input(argv[1]);  
  string inLine;
  char delimiter = ' ';  

  int n;
  stringstream ss_numbers;
  vector<string> s_numbers;
  vector<int> numbers = {};
  vector<int>::iterator it;
  int number;
  
  while(1) {
    getline(cin, inLine);    
    n = stoi(inLine);
    if (n == 0) break;

    numbers.clear();
    
    getline(cin, inLine);
    
    ss_numbers << inLine;
    istream_iterator<string> begin(ss_numbers);
    istream_iterator<string> end;
    vector<string> vstrings(begin, end);

    s_numbers = vstrings;
    
    for (int i=0; i<n; i++) {
      numbers.push_back(stoi(s_numbers[i]));
    }
    
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