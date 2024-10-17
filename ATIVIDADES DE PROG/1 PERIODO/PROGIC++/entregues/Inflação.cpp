//  Fazer um programa em "C" que lê o preço de um produto e inflacione o preço em 10% se ele for menor que 100 reais em 20% se for maior ou igual a 100 reais.
#include <iostream>
using namespace std;
int main() {
    double valor;
    cout<<"Digite o valor do produto: ";
    cin>>valor;
    if(valor<100){
        cout<<"o valor inflacionado e de: "<<(valor*0.10)+valor;
    }
else 
cout<<"o valor inflacionado e de: "<<(valor*0.20)+valor;
    return 0;
}
