//11)Elabore um algoritmo que lê um número que representa uma senha, verifica
//se a senha está correta ou não, comparando-a com a senha 34567, e informa
//"Acesso autorizado" ou "Acesso negado", conforme o caso.
#include <iostream>
using namespace std;
int main(){
    int senha;
    cout<<"Informe a senha"<<endl;
    cin>>senha;
        switch (senha){
        case 34567:
            cout<<"Acesso Autorizado"<<endl;
            break;
        default:
            cout<<"Acesso Negado"<<endl;
            break;
        }
    return 0;
}