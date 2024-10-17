/*3- Faça um programa para ler a nota da prova de 15 alunos e armazene em uma matriz, calcule e imprima a media geral.*/
#include <iostream>
using namespace std;
int main(){
int n, ins;
cout<<"Quantas notas deseja inserir?"<<endl;
cin>>n;
ins = n-1;
double nota [ins], menor_nota = 100, maior_nota = 0;
for ( int i = 0; i <= ins ; i++){  
    cout<<"insira a nota do "<<i+1<<" aluno: "<<endl;
    cin>>nota [i];
    if (nota[i]<menor_nota){
        menor_nota = nota[i];
    }if(nota[i]>maior_nota){
        maior_nota = nota[i];
    }
    system ("pause");
    system ("CLS");
}
cout<<"A media geral entre as "<<n<<" notas eh: "<<(maior_nota + menor_nota)/2<<endl;
return 0;
}
