//1) Ler um valor inteiro e informar, através de uma mensagem, se este valor é um número par ou ímpar.

#include <iostream>
using namespace std;

int main() {
    int valor;
    cout<<"Digite um valor para teste: ";
    cin>>valor;
    double teste;
    teste = valor%2;
    if( teste == 0){
    cout<<"\nEste valor eh par.";
    }
    else
       cout<<"\nEste valor eh impar.";
 return 0;
}

