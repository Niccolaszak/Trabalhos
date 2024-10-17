//Fazer um programa para descobrir a idade de uma pessoa, considerando apenas ano de nascimento e ano atual.
#include <iostream>
using namespace std;
int main() {
    double ano_atual, ano_nasc;
    cout<<"Digite o seu ano de nascimento e o ano atual(separados por espaco):"<<endl;
    cin>>ano_nasc>>ano_atual;
    cout<<"Considerando seu nascimento no ano de "<<ano_nasc<<", sua idade no ano de "<<ano_atual<<", e de: "<<ano_atual-ano_nasc<<" anos.";
    return 0;
}
