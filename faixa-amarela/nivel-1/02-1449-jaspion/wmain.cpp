#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

int main(int argc, char** argv) {
  ifstream input(argv[1]);
  string inLine;

  string delimiter = " ";  
  size_t pos = 0;

  int t, m, n;  

  stringstream sPhrase;
  string word, translate, phrase;
  string out;
  map<string, string> table;

  getline(input, inLine);
  t = stoi(inLine);

  while (t--) {
    getline(input, inLine);

    pos = inLine.find(delimiter);
    m = stoi(inLine.substr(0, pos));
    n = stoi(inLine.substr(pos));

    for (int i=0; i<m;) {
      getline(input, word);
      getline(input, translate);
      table[word] = translate;
      i++;
    }

    for (int i=0; i<n; i++) {
      getline(input, phrase);
      stringstream sPhrase;
      sPhrase << phrase;
      out = "";

      while (sPhrase >> word) {
        if (out.length() != 0) out.append(" ");

        translate = table[word];

        if (translate == "") out.append(word);
        else out.append(translate);
      }

      cout << out << endl;
    }
    
    cout << endl;
  }

  input.close(); 
}

vector<string> split(string text, string delimiter) {
    vector<string> words{};
    size_t pos = 0;

    while ((pos = text.find(delimiter)) != string::npos) {
        words.push_back(text.substr(0, pos));
        text.erase(0, pos + delimiter.length());
    }

    return words;
}