//Fazer um programa para saber se precisa levar casaco se for sair de casa, solicitando duas informações ao usuário Temperatura e Velocidade do Vento.
//Se o vento estiver mais de 40 km/h, preciso de um caso;
//Se a temperatura estiver abaixo de 15° C, preciso de um caso;
//Criar uma variável booleana vestir_casaco para validar as expressões e informar ao usuário.
#include <iostream>
using namespace std;
int main() {
const double velofixa = 40;
const double tempfixa = 15;
double velo, temp;
cout<<"Digite a velocidade do vento e a temperatura (Nesta ordem e separados por espaço): "<<endl;
cin>>velo>>temp;
cout<<boolalpha;
bool vestir_casaco;
vestir_casaco = (velo>velofixa)||(temp<tempfixa);
cout<<"Precisa vestir o casaco? "<<endl<<vestir_casaco;

    return 0;
}