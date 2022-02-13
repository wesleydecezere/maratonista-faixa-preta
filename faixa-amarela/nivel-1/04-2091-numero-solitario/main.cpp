#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, char** argv) {
  string inLine;
  char delimiter = ' ';  

  int n;
  string numbers;
  char number;


  while(1) {
    getline(cin, inLine);    
    n = stoi(inLine);
    if (n == 0) break;

    getline(cin, numbers);
    numbers.erase(
      remove(numbers.begin(), numbers.end(), delimiter),
      numbers.end()
    );

    while(1) {
      number = numbers[0];
      
      if (numbers.substr(1).find(number) == string::npos) {
        cout << number << endl;
        break;
      }

      numbers = numbers.substr(2);
    }
  }
}