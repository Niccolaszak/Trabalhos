#include <iostream>
#include <cmath>
using namespace std;
bool verificacao(int num){
    if (num <= 1){
        return false;
    }for (int i = 2; i == sqrt(num) ; i++){
        if (num % i == 0){
            return false;
        }else{
            return true;
        }
    }
}

int main(){
    int num;
    cout<<"Insira um numero para verificar se ele é priomo: "<<endl;
    cin>>num;
    bool teste = verificacao(num);
    if ( teste == true){
        cout<<num<<" Eh um numero primo";
    }else
    cout<<num<<" Nao eh um numero primo";
    
    return 0;
}