#include <iostream>
#include <fstream>
#include <map>

using namespace std;

template<typename Map>
void PrintMap(Map& m) {
  cout << "[ ";
  for (auto &item : m) {
    cout << item.first << ":" << item.second << " ";
  }
  cout << "]\n";
}

bool hasMoreDiffsThan(int nDiff, string s1, string s2) {
  int n = 0;
  int diff = 0;

  while(s1[n] != '\0' or s2[n] != '\0') {
    if (s1[n] != s2[n]) diff += 1;
    n += 1;
    
    if (diff >= nDiff) return true;
  }

  return false;
} 


int main(int argc, char** argv) {
  ifstream input(argv[1]);

  string inputLine;
  string delimiter = " ";  
  size_t pos = 0;

  int n, m, fakeSigns;
  map<string, string> originalSign;
  string name, sign, actualSign;


  while(1) {
    getline(input, inputLine);    
    n = stoi(inputLine);
    if (n == 0) break;

    originalSign = {};
    
    for (int i=0; i<n; i++) {
      getline(input, inputLine);
      
      pos = inputLine.find(delimiter);
      name = inputLine.substr(0, pos);
      sign = inputLine.substr(pos);

      originalSign[name] = sign;
    }

    cout << "Original Signs - ";
    PrintMap(originalSign);
    cout << endl;

    getline(input, inputLine);    
    m = stoi(inputLine);
    fakeSigns = 0;

    for (int i=0; i<m; i++) {
      getline(input, inputLine);
      
      pos = inputLine.find(delimiter);
      name = inputLine.substr(0, pos);
      actualSign = inputLine.substr(pos);

      if (hasMoreDiffsThan(2, originalSign[name], actualSign)) fakeSigns += 1;

      cout << "Name: " << name << ", Actual sign: " << actualSign << endl;
    }

    cout << "Fake signs: " << fakeSigns << endl << endl;
  }

  input.close(); 
}