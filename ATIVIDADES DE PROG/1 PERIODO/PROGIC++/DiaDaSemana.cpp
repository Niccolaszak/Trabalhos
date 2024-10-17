//6) Ler um número inteiro que representa um dia da semana a apresentar o
//nome do dia correspondente (domingo, segunda-feira, ...).
#include <iostream>
using namespace std;
int main(){
    int numero;
    cout<<"Insira um numero de 1 a 7: ";
    cin>>numero;
        switch (numero){
        case 1 :
            cout<<"Domingo"<<endl;
            break;
        case 2 :
            cout<<"Segunda-Feira"<<endl;
            break;
        case 3 :
            cout<<"Terca-feira"<<endl;
            break;
        case 4 :
            cout<<"Quarta-feira"<<endl;
            break;
        case 5 :
            cout<<"Quinta-feira"<<endl;
            break;
        case 6 :
            cout<<"SEXTOUU"<<endl;
            break;
        case 7 :
            cout<<"Sabado"<<endl;
            break;
        default:
        cout<<"Informacao invalida"<<endl;
            break;
        }
return 0;}