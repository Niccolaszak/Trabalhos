//2 - Criar um programa que possui um menu com switch case onde o usuário escolhe qual operação matemática ele gostaria de fazer entre soma, subtração, multiplicação
// e divisão o usuário deverá informar dois números para realizar a operação.
#include <iostream>
using namespace std;
int main(){
    char operacao;
    double n1, n2;
    cout<<"Digite qual operação deseja realizar:"<<endl;
    cout<<"A - Adicao"<<endl;
    cout<<"B - Subtracao"<<endl;
    cout<<"C - Multiplicacao"<<endl;
    cout<<"D - Divisao"<<endl;
    cin>>operacao;
    cout<<"Digite 2 numeros para a operacao separados por espaco:"<<endl;
    cin>>n1>>n2;
        switch (operacao){
            case 'A':
            case 'a':
            cout<<"O resultado da soma eh = "<<n1+n2<<endl;
            break;
            case 'B':
            case 'b':
            cout<<"O resultado da subtracao eh = "<<n1-n2<<endl;
            break;
            case 'C':
            case 'c':
            cout<<"O resultado da multiplicacao eh = "<<n1*n2<<endl;
            break;
            case 'D':
            case 'd':
            cout<<"O resultado da divisao eh = "<<n1/n2<<endl;
            break;
        default:
        cout<<"Operacao invalida"<<endl;
            break;
        }
return 0;
}