#include <iostream>
#include <iomanip>
using namespace std;
int main(){
  int i = 0;
  char operation;
  cin>>operation;
  double result = 0;
  double num;
  while(i<144){
    cin>>num;
    result += num;
    i++;
  }
  if (operation=='S')
    cout<<result<<endl;
  else cout<<setprecision(2)<<result/144.0<<endl;
  return 0;
}