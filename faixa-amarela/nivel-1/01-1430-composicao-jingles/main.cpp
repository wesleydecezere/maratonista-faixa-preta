#include <iostream>
#include <fstream> 
using namespace std;

int main(int argc, char** argv) {
  string inputLine;
  ifstream input(argv[1]);

  string delimiter = "/";
  size_t pos = 0;
  string compass;

  int len = 7;
  string id = "WHQESTX";
  double time[] = {1, 0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625};
  float duration;
  int correct;

  while (getline (input, inputLine)) {
    if (inputLine == "*") break;

    correct = 0;

    while ((pos = inputLine.find(delimiter)) != string::npos) {
      compass = inputLine.substr(0, pos);
      duration = 0;

      for (int i=0; i<compass.length(); i++) {
        int idx = id.find(compass[i]);
        duration += time[idx];
      }

      if (duration == 1) correct++;

      inputLine.erase(0, pos + delimiter.length());
    }

    cout << correct << endl;
  }

  input.close();
} 

