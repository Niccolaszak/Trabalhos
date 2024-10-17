/*Faça um programa que leia 10 números inteiros, armazene-
os em um vetor, solicite um valor de referência inteiro e:
a) Imprima os números do vetor que são maiores que o
valor referência.
b) Retorne quantos números armazenados no vetor são
menores que o valor de referência.
c) Retorne quantas vezes o valor de referência aparece no
vetor.*/
#include <iostream>
#include <vector>
using namespace std;
int main(){
vector <int> numeros, maiores, menores;
int add, ref, aparece = 0, maior_tam, menor_tam;
    for (int i = 1; i <= 10; i++){
        cout<<"insira o "<<i<<" valor: "<<endl;
        cin>>add;
        numeros.push_back(add);
    }
    cout<<"insira um valor inteiro de referencia para comparar com o vetor: "<<endl;
    cin>>ref;
    for (int i = 1; i < 10; i++){
        add = numeros.at(i);
        if (ref > add){
            menores.push_back(add);   
        }
        if (ref < add){
            maiores.push_back(add);   
        }
        if (ref == add){
            aparece++;
        }
    }
    menor_tam = menores.size();
    maior_tam = maiores.size();
    cout<<"Os numeros maiores que o valor de referencia sao: ";
    for (int i = 0; i < maior_tam; i++){
        cout<<maiores.at(i)<<" ";
    }
    cout<<endl<<"Os numeros menores que o valor de referencia sao: ";
    for (int i = 0; i < menor_tam; i++){
        cout<<menores.at(i)<<" ";
    }
    cout<<endl<<"O valor referencia aparece "<<aparece<<" vezes no vetor.";
    return 0;
}