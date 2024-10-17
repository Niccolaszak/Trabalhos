//12) Elaborar um algoritmo que lê um valor que se refere a altura de uma pessoa
//e mostra uma mensagem conforme a faixa de altura:
//Altura           Informação mostrada
//menos que 1,50  “abaixo de um metro e meio”
//de 1,50 a 1,80 “entre um metro e meio e um metro e oitenta centímetros”
//mais que 1,80 “acima de um metro e oitenta centímetros”
#include <iostream>
using namespace std;
int main(){
    double altura;
    cout<<"Digite sua altura em CM: "<<endl;
    cin>>altura;
        if(altura<=150){
            cout<<"de 1,5m pra baixo(kkkk anao)"<<endl;
        }if(altura>150 && altura<180){
            cout<<"Esta entre 1,5m e 1,8m (Altinho em)"<<endl;
        }if(altura>=180){
            cout<<"de 1,8m pra mais (Comeu oque em kkkk)"<<endl;
        }

    return 0;
}