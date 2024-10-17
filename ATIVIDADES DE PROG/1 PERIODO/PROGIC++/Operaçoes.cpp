//8) Fazer um programa em "C" que solicite 2 números e informe:
//a) A soma dos números;
//b) O produto do primeiro número pelo quadrado do segundo;
//c) O quadrado do primeiro número;
//d) A raiz quadrada da soma dos quadrados;
//e) O módulo do primeiro número.
#include <iostream>
#include <cmath>//biblioteca usada para ter operações matematicas como potencia e raiz quadrada
using namespace std;
int main(){
    double n1, n2;
    cout<<"Digite dois valores separados por espaco: "<<endl;
    cin>>n1>>n2;
    cout<<"A soma dos valores "<<n1<<" + "<<n2<<" = "<<n1+n2<<endl;
    cout<<"O produto do primeiro pelo quadrado do segundo eh = "<<n1*pow(n2, 2)<<endl;
    cout<<"O quadrado do primeiro numero eh = "<<pow(n1, 2)<<endl;
    cout<<"A raiz quadrada da soma dos quadrados eh = "<< sqrt(pow(n1, 2)+pow(n2, 2))<<endl;
    cout<<"O modulo do primeiro numero eh = "<< abs(n1)<<endl;
    return 0;
}