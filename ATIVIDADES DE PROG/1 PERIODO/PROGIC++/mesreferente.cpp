//1 - Criar um programa onde o usuário informa um numero inteiro entre 1 e 12 e imprime o mês correspondente.
#include <iostream>
using namespace std;
int main() {
    int num;
    cout<<"Digite um numero entre 1 e 12: ";
    cin>>num;
    switch(num){
        case 1:
        cout<<"Este numero se refere a janeiro"<<endl;
        break;
        case 2:
        cout<<"Este numero se refere a fevereiro"<<endl;
        break;
        case 3:
        cout<<"Este numero se refere a Marco"<<endl;
        break;
        case 4:
        cout<<"Este numero se refere a Abril"<<endl;
        break;
        case 5:
        cout<<"Este numero se refere a Maio"<<endl;
        break;
        case 6:
        cout<<"Este numero se refere a junho"<<endl;
        break;
        case 7:
        cout<<"Este numero se refere a julho"<<endl;
        break;
        case 8:
        cout<<"Este numero se refere a Agosto"<<endl;
        break;
        case 9:
        cout<<"Este numero se refere a setembro"<<endl;
        break;
        case 10:
        cout<<"Este numero se refere a Outubro"<<endl;
        break;
        case 11:
        cout<<"Este numero se refere a novembro"<<endl;
        break;
        case 12:
        cout<<"Este numero se refere a dezenbro"<<endl;
        break;
        default: 
        cout<<"Voce inseriu uma informaçao invalida"<<endl;
    }
    return 0;
}