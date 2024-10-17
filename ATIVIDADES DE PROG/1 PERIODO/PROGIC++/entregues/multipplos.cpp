//13) Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:
//‘São múltiplos’ ou ‘Não são múltiplos’.
#include <iostream>
using namespace std;
int main(){
    int a, b;
        cout<<"Digite dois valores separados por espaco para avaliacao se sao multiplos: "<<endl;
        cin>>a>>b;
        if (a%b==0 || b%a==0){
            cout<<"Os valores sao multiplos";
        }else
        cout<<"Os valores nao sao multiplos";
        


    return 0;
}