/*Escreva um programa que receba do usuário um vetor com 20 valores
inteiros e apresente o maior e o menor e suas respectivas posições em
que os mesmos foram informados. Caso existam números iguais
mostre a posição da primeira ocorrência.*/
/*Com base no exercício 1 mostrar todos os valores digitados pares e
todos os valores digitados impares.*/
#include <iostream>
#include <vector>
using namespace std;
int main(){
int valor_maior = 1, valor_menor = 999999, posi_menor = 0, posi_maior = 0, pares = 0, impares = 0;
vector <int> valores;
vector <int> impar;
vector <int> par;
int add;
    for (int i = 1; i <= 20; i++){
        cout<<"Insira o "<<i<<" para o vetor: "<<endl;
        cin>>add;
        valores.push_back(add);
            if (add < valor_menor){
                 valor_menor = add;
                 posi_menor = i;
            }
            if (add > valor_maior){
                 valor_maior = add;
                 posi_maior = i;
            }
            if (add % 2 == 0){
                par.push_back(add);
                pares++;
            }
            if (add % 2 != 0){
                impar.push_back(add);
                impares++;
            }
            }
    cout<<"O valor maior eh: "<<valor_maior<<" Na posicao: "<<posi_maior<<endl;
    cout<<"O valor menor eh: "<<valor_menor<<" Na posicao: "<<posi_menor<<endl;
    cout<<"Voce inseriu "<<pares<<" Numeros pares, que sao: "<<endl;
    for (int i = 0; i < par.size(); i++){
        cout<<par.at(i)<<" ";
    }
    cout<<endl<<"Voce inseriu "<<impares<<" Numeros impar, que sao: "<<endl;
     for (int i = 0; i < impar.size(); i++){
        cout<<impar.at(i)<<" ";
    }


return 0;}
