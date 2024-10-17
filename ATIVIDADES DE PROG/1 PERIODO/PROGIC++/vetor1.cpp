/*Projetar e implementar um programa que leia e armazene um total de
dez números e conte o número de suas entradas que são positivas,
negativas e zero.*/
#include <iostream>
#include <vector>
using namespace std;
int main(){
   vector <int> numeros;
   int posi = 0, neg = 0, igu = 0;
   double add;
   for (int i = 1; i <= 10; i++){
        cout<<"Insira o "<<i<<" de 10:";
        cin>>add;
        numeros.push_back(add);
        if (add < 0){
            neg++;
        }if (add > 0){
            posi++;
        }if (add == 0){
         igu++;
        }        
   }
cout<<"Voce inseriu "<<neg<<" Numeros negativos"<<endl;
cout<<"Voce inseriu "<<posi<<" Numeros positivos"<<endl;
cout<<"Voce inseriu "<<igu<<" Numeros 0"<<endl;
   return 0;
}