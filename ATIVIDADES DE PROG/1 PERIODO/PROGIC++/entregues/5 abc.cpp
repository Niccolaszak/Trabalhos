//Ler um valor inteiro e : a) exibir a mensagem 'número negativo' quando o
//valor informado for menor que zero; b) exibir a mensagem 'zero' quando este
//for igual a zero; e c) exibir a mensagem 'número positivo' quando o valor for
//maior que zero.
#include <iostream>
using namespace std;
int main(){
int valor;
cout<<"digite um valor: ";
cin>>valor;
if(valor < 0){
    cout<<"Este numero eh negativo.";
}else if (valor == 0){
    cout<<"Este valor eh o 0.";
}else if (valor > 0){
    cout<<"Este valor eh positivo.";
}




    return 0;
}