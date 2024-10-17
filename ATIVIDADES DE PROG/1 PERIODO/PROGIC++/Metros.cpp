//Fazer um programa que pergunte um valor em metros e imprima o correspondente em decímetros, centímetros e milímetros.
#include <iostream>
using namespace std;
int main() {
    double metros;
    cout<<"Digite um valor em Metros para efetuar a conversao: ";
    cin>>metros;
    cout<<"O valor de "<<metros<<" metros em: "<<endl;
    cout<<"Decimetros = "<<metros*10;
    cout<<"\nCentimetros = "<<metros*100;
    cout<<"\nMilimeetros = "<<metros*1000;
    return 0;
}
