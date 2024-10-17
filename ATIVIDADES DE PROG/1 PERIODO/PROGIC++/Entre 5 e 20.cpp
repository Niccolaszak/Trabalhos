//4) Escreva um algoritmo que leia um valor verifique se ele se encontra no intervalo entre 5 e 20.
#include <iostream>
using namespace std;
int main(){
    double valor;
    cout<<"Digite um valor: ";
    cin>>valor;
    if (valor>=5 && valor<20){
        cout<<"O valor "<<valor<<" esta entre 5 e 20.";
    }else
    cout<<"O valor "<<valor<<" Nao esta entre 5 e 20.";
    


    return 0;
    }