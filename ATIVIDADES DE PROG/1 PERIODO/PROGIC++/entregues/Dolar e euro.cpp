//Faça um programa para converter reais para Dólares e Euros
#include <iostream>
using namespace std;

int main() {
    double valor, dolar, euro;
    cout<<"Digite o valor em Reais para conversao: ";
    cin>> valor;
    cout<<"O valor de "<<valor<<" Reais em Dolares e: "<<valor/4.98<<"\nE em Euros e: "<<valor/5.39;
    return 0;
}