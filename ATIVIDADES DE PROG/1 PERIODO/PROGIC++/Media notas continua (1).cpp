//Faça um algoritmo que leia as 4 notas de um aluno e calcule a sua
//média anual ponderada, com o peso:
//1, 3, 4 e 5, respectivamente.
//Se a nota obtida for entre 7 a 10 está aprovado;
//Se a nota obtiva for entre 4 e 6.9 em recuperação;
//Se é menor que 4 reprovado.
//Ao final pergunte se o usuário quer calcular uma nova média.
#include <iostream>
using namespace std;
int main(){
    double nota1, nota2, nota3, nota4, media_anual;
    char res = 's';
   do{
    system("CLS");
    cout<<"Digite a primeira nota: "<<endl;
    cin>>nota1;
    system("CLS");
    cout<<"Digite a segunda nota: "<<endl;
    cin>>nota2;
    system("CLS");
    cout<<"Digite a terceira nota: "<<endl;
    cin>>nota3;
    system("CLS");
    cout<<"Digite a Quarta nota: "<<endl;
    cin>>nota4;
    media_anual = ((nota1*1)+(nota2*3)+(nota3*4)+(nota4*5))/13;
    system("CLS");
        if (media_anual >= 7 && media_anual <= 10){
            cout<<"Parabens esta aprovado."<<endl;
            cout<<"Sua media anual foi: "<<media_anual<<endl;
            system("pause");
            system("CLS");
        }if (media_anual >= 4 && media_anual <= 6.9999){
            cout<<"Esta de recuperacao"<<endl;
            cout<<"Sua media anual foi: "<<media_anual<<endl;
            system("pause");
            system("CLS");
        }if (media_anual < 4){
            cout<<"infelizmente voce reprovou"<<endl;
            cout<<"Sua media anual foi: "<<media_anual<<endl;
            system("pause");
            system("CLS");
        }
        cout<<"Deseja calcular outra media? (S/N)"<<endl;
        cin>>res;
        } while (res == 's' || res == 'S');
        system("CLS");
        cout<<"Obrigado por utilizar o sistema"<<endl;
    return 0;
}