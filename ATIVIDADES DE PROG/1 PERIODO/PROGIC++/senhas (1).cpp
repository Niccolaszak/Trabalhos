//Faça um programa que receba uma senha formada de
//quatro números inteiros, verifique se a senha está correta e,
//caso não esteja, solicite novamente a senha. Se a senha
//entrada for a correta, deverá ser apresentada a mensagem
//“Senha Correta”, caso contrário, “Senha Incorreta”
#include <iostream>
using namespace std;
int main(){
    int senha, senhacerta = 2123;
    char res;
    do{
        cout<<"insira a senha de 4 algarismos: "<<endl;
        cin>>senha;
        if (senha==senhacerta){
            system("CLS");
            cout<<"Senha correta"<<endl;
            res='n';
        }else{
            system("CLS");
            cout<<"senha incorreta"<<endl;
            cout<<"Tente novamente"<<endl;
            res='s';
        }
    } while (res=='s'||res=='S');
    return 0;
}