//10)Elaborar um algoritmo que leia uma letra que pode ser ‘F’ ou ‘J’ e mostra a
//mensagem “pessoa física”, “pessoa jurídica” ou "tipo de pessoa inválido",
//conforme o caso.

#include <iostream>
using namespace std;
int main(){
    char letra;
    cout<<"Digite J ou F para autenticacao: "<<endl;
    cin>>letra;
        switch (letra){
        case 'J':
        case 'j':
        cout<<"Pessoa Juridica";
            break;
        case 'F':
        case 'f':
        cout<<"Pessoa Fisica";
        break;
        default:
        cout<<"Tipo de pessoa invalido";
            break;
        }
    return 0;
}