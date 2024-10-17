//Escreva um programa em C++ que solicita 10 números ao usuário,
//através de um laço while, e ao final mostre qual destes números é o
//maior.
#include <iostream>
using namespace std;
int main(){
    int num, i = 1, nummaior = 0;
    do{
    system("CLS");
      cout<<"Digite um numero: ("<<i<<")"<<endl;
      cin>>num;
      if (num>nummaior){
        nummaior = num;
      }else{ }
      i++;
    }while (i<=10);
    cout<<"O maior numero inserido eh "<<nummaior<<endl;
    return 0;
}