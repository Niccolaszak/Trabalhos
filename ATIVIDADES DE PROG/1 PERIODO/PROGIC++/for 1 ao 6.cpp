//Escreva um código que use um loop for para calcular a
//soma dos inteiros ímpares de 1 a 15, inclusive. O resultado
//final deve ser armazenado em uma variável inteira chamada sum.
#include <iostream>
using namespace std;
int main(){
    int sum = 0;
    for (int i = 1; i <= 15; ++i){
    if ( i % 2 != 0){// != representa diferente
    sum += i;
    }
    }
    cout<<"A soma dos numeros impares inteiros de 1 a 15 eh: "<<sum<<endl;
return 0;
}