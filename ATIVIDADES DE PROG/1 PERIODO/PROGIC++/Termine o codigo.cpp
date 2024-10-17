//Complete o codigo
#include <iostream>
using namespace std;

int main() {
    int numero{10};    
    //----ESCREVA SEU CÓDIGO ABAIXO DESTA LINHA----
    int original_number = numero;
   
    //-- Multiplica o número por 2 e atribui o resultado de volta ao número
    numero *= 2;
    cout<<original_number<<" x 2 = "<<numero<<endl;
    //-- Adiciona 9 ao número e atribui o resultado de volta ao número
    numero += 9;
    cout<<" + 9 = "<<numero<<endl;
    //-- Subtrair 3 do número e atribuir o resultado de volta ao número
    numero -= 3;
    cout<<" - 3 = "<<numero<<endl;
    //-- Divide o número por 2 e atribui o resultado de volta ao número
    numero /= 2;
    cout<<" / 2 = "<<numero<<endl;
    //-- Subtrair original_number de number e atribuir o resultado de volta a number
    numero -= original_number;
    cout<<" - "<<original_number<<" = "<<numero<<endl;
    //-- Pegue o módulo 3 (%) do número e atribua-o de volta ao número
    numero %= 3;
    cout<<" % 3 = "<<numero<<endl;
 
    cout<<"O resultado final eh: "<<numero<<endl;
    //----ESCREVA SEU CÓDIGO ACIMA DESTA LINHA----
   
    return 0;
}