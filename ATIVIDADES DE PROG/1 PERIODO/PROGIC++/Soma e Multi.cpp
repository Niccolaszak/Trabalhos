//7) Ler dois valores inteiros e apresentar a adição destes valores, quando o
//primeiro valor for maior que o segundo, caso contrário, efetuar a multiplicação
//dos valores.

#include <iostream>
using namespace std;
int main(){
    int n1, n2;
    cout<<"Digite dois valores separados por espaco: "<<endl;
    cin>>n1>>n2;
        if (n1>n2){
            cout<<"Ja que "<<n1<<" eh maior que "<<n2<<" O resultado da soma eh = "<<n1+n2<<endl;
        }else 
        cout<<"Ja que "<<n1<<" nao eh maior que "<<n2<<" Oresultado da multiplicacao eh = "<<n1*n2<<endl;
        
    return 0;
}