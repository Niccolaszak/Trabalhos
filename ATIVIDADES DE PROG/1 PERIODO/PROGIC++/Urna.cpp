//Faça um programa que simule a urna eletrônica.
//A tela a ser apresentada deverá ser da seguinte forma:
//As opções são:
//1. Candidato Antônio
//2. Candidato Simão
//3. Fim da votação
//O programa deverá ler os votos dos eleitores e, quando for digitado o
//número 3, apresentar as seguintes o número de votos de cada
//candidato.
//Fazer dois codigos, um utilizando if e outro switch.
#include <iostream>
using namespace std;
int main(){
    int antonio = 0, simao = 0, eleicao;
    do{
        system("CLS");
        cout<<"Escolha seu candidato: "<<endl;
        cout<<"1. Candidato Antonio "<<endl;
        cout<<"2. Candidato Simao "<<endl;
        cout<<"(Insira 3 para encerramento da eleicao)"<<endl;
        cout<<"Insira seu voto: "<<endl;
        cin>>eleicao;
        switch (eleicao){
        case 1:
            system("CLS");
            cout<<"Voce votou no candidato Antonio."<<endl;
            antonio++;
            cout<<"Obrigado por votar"<<endl;
            system("pause");
            break;
        case 2:
            system("CLS");
            cout<<"Voce votou no candidato Simao."<<endl;
            simao++;
            cout<<"Obrigado por votar"<<endl;
            system("pause");
        break;
    }
    } while (eleicao==1||eleicao==2);
        system("CLS");
        cout<<"O resultado da eleicao eh: "<<endl;
        cout<<"Antonio: "<<antonio<<endl;
        cout<<"Simao: "<<simao<<endl;
    return 0;
}



