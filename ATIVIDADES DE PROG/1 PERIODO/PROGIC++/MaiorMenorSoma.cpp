/*3 - Desenvolva um programa que solicite ao usuário o tamanho de uma matriz, no formato MxN (por exemplo, 3x4). 
Em seguida, leia todos os valores da matriz através do terminal. 
Após a leitura, informe o maior e o menor número digitado, bem como a soma de todos os valores da matriz. 
Por fim, pergunte ao usuário se ele deseja repetir a operação, 
permitindo que ele recomece o processo se desejar.*/
#include <iostream>
using namespace std;
char esc;
int linha, coluna, maior, menor;
int main (){
do{
cout<<"Informe o tamanho que deseja para a matriz separado por espaco: ex: (3x4)";
cin>>linha>>coluna;
int matriz[linha][coluna];
   for (int i = 0; i < linha; i++){
    for (int j = 0; j < coluna; j++){
        cout<<"Informe os numeros da matriz: ";
        cin>>matriz[i][j];
    }
}
menor = matriz[0][0];
maior = matriz[0][0];
int valortotal = 0;
    for (int i = 0; i < linha; i++){
        for (int j = 0; j < coluna ; j++){
            cout<<matriz[i][j]<<" ";
            if (matriz[i][j] < menor){
                menor = matriz[i][j];
}
            if (matriz [i][j] > maior){
                maior = matriz [i][j];
}
            valortotal += matriz [i][j];
}
cout<<endl;
}
cout<<"O maior valor eh: "<<maior<<endl;
cout<<"O menor valor eh: "<<menor<<endl;
cout<<"A soma de todos os valores da matriz eh: "<<valortotal<<endl;

cout<<"Deseja fazer uma nova matriz? (S/N)";
cin>>esc;
} while (esc == 'S' || esc == 's');
 return 0;
}