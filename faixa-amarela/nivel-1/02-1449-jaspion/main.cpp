#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, char** argv) {
  ifstream input(argv[1]);

  string inputLine;
  string word;
  string translate;
  string phrase;
  string delimiter = " ";  
  string out;

  int t;  
  int m;
  int n;

  size_t pos = 0;

  map<string, string> table;

  getline (input, inputLine);
  t = stoi(inputLine);

  while (t--) {
    getline (input, inputLine);

    pos = inputLine.find(delimiter);
    m = stoi(inputLine.substr(0, pos));
    n = stoi(inputLine.substr(pos));

    for (int i=0; i<m;) {
      getline(input, word);
      getline(input, translate);
      table[word] = translate;
      i++;
    }

    for (int i=0; i<n; i++) {
      getline(input, phrase);
      out = "";

      while ((pos = phrase.find(delimiter)) != string::npos) {
          pos = phrase.find(delimiter);

          if (pos != string::npos) word = phrase.substr(0, pos);
          else word = phrase;
          
          translate = table[word];

          if (translate == "") out.append(word);
          else out.append(translate);

          if (pos != string::npos) {
            out.append(" ");
            phrase.erase(0, pos + delimiter.length());
          } 
      }
      out.append(table[phrase]);

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