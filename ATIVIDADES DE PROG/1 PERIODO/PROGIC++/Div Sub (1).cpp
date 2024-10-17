/*Escrever uma função que tenha como parâmetros dois números
inteiros positivos num1 e num2 e calcule o resto da divisão inteira do
maior pelo menor mediante soma e subtração*/
#include <iostream>
using namespace std;
int restante (int num1,int num2){
if (num1<num2){
    int troca = 0;
    troca = num1;
    num1 = num2;
    num2 = troca;
}
int resto = num1, result = 0;
while (resto >= num2){
resto -= num2;
result++;
}
    cout<<"O resultado da divisao eh: "<<result<<endl;
    cout<<"E o resto da divisao eh: "<<resto<<endl;
    return 0;
}
int main(){
    int num1, num2;
    cout<<"Insira dois numeros pra divisao do maior pelo menor: "<<endl;
    cin>>num1>>num2;
    restante(num1,num2);
return 0;
}