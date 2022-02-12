#include <iostream>
#include <fstream>
#include <map>

using namespace std;

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
  string inputLine;
  string delimiter = " ";  
  size_t pos = 0;

  int n, m, fakeSigns;
  map<string, string> originalSign;
  string name, sign, actualSign;


  while(1) {
    getline(cin, inputLine);    
    n = stoi(inputLine);
    if (n == 0) break;

    originalSign = {};
    
    for (int i=0; i<n; i++) {
      getline(cin, inputLine);
      
      pos = inputLine.find(delimiter);
      name = inputLine.substr(0, pos);
      sign = inputLine.substr(pos);

      originalSign[name] = sign;
    }

    getline(cin, inputLine);    
    m = stoi(inputLine);
    fakeSigns = 0;

    for (int i=0; i<m; i++) {
      getline(cin, inputLine);
      
      pos = inputLine.find(delimiter);
      name = inputLine.substr(0, pos);
      actualSign = inputLine.substr(pos);

      if (hasMoreDiffsThan(2, originalSign[name], actualSign)) fakeSigns += 1;
    }

    cout << fakeSigns << endl;
  }
}