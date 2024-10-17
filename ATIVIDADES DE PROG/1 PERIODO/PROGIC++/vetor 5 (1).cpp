/*Faça um programa que leia valores e adicione dentro de um vetor
valores até que o usuario não queira mais inserir dados e na
sequencia apresente na tela a quantidade de itens inseridos no
vetor.*/
#include <iostream>
#include <vector>
using namespace std;
int main(){
char esc;
double add, soma;
vector <double> valores;
    cout<<"Deseja atibuir um valor ao vetor? (S/N) "<<endl;
    cin>>esc;
    do{
     system("cls");
     cout<<"Insira o valor: "<<endl;
     cin>>add;
     valores.push_back(add);
     cout<<"Deseja incluir mais um valor? (S/N) "<<endl;
     cin>>esc;
    } while (esc == 's' || esc == 'S');
    system("cls");
    cout<<"Voce inseriu "<<valores.size()<<" valores ao vetor"<<endl;
    cout<<"Que Foram: "<<endl;
    for (int i = 0; i < valores.size() ; i++){
        cout<<valores.at(i)<<" ";
    }
    cout<<"\nA soma total desses valores eh: "<<endl;
    for (int i = 0; i < valores.size(); i++){
        soma += valores.at(i);
    }
    cout<<soma<<endl;
    cout<<"\nobrigado por utilizar o sistema"<<endl;
    
    return 0;
}
