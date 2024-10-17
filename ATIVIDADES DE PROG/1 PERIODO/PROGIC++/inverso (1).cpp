/*5-Escrever o inverso de um número inteiro dado (1234, inverso 4321).*/
#include <iostream>
using namespace std;
int inverter(int num){
int num1 = 0;
while (num > 0){
    int num2 = num % 10;
    num1 = num1 * 10 + num2;
    num /= 10;
}
    return num1;
}
int main(){
int num;
cout<<"Insira um numero para saber seu inverso: ";
cin>>num;
int num1 = inverter(num);
cout<<"O inverso de "<<num<<" eh: "<<num1<<endl;


    return 0;
}