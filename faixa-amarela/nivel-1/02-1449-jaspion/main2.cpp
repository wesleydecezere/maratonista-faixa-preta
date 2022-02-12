#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv) {
  ifstream input(argv[1]);

  string inputCase;

  input >> inputCase;
  cout << inputCase << endl;
  input >> inputCase;
  cout << inputCase << endl;
  input >> inputCase;
  cout << inputCase << endl;
  input >> inputCase;
  cout << inputCase << endl;

}