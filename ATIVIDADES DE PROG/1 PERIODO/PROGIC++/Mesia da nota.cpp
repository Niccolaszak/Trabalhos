//14)Faça um algoritmo que leia as 3 notas de um aluno e calcule a sua média
//anual ponderada, com o peso: 2, 3 e 5, respectivamente. Se a nota obtida for
//entre 6 a 10 está aprovado; se é entre 4 e 5.9 em recuperação, se é menor
//que 4 reprovado. Se o aluno está em recuperação ler a nota de recuperação
//e calcular a média final (que é a média entre a média anual e a nota de
//recuperação). Se a média final é menor que 5 o aluno está reprovado após
//recuperação, se é igual ou maior que 5 está aprovado após recuperação.
#include <iostream>
using namespace std;
int main(){
    double nota1, nota2, nota3, media_anual;
    media_anual = ((nota1*2)+(nota2*3)+(nota3*5))/10;
    cout<<"digite da primeira nota: "<<endl;
    cin>>nota1;
    cout<<"digite da segunda nota: "<<endl;
    cin>>nota2;
    cout<<"digite da terceira nota: "<<endl;
    cin>>nota3;
        if (media_anual>=6 && media_anual<=10){
            cout<<"Parabens esta aprovado."<<endl;
        }if (media_anual>=4 && media_anual<=5.9999){
            cout<<"Esta de recuperacao"<<endl;
            double nota_rec, media_final;
            media_final = (nota_rec + media_anual)/2;
            cout<<"Digite a nota que tirou na recuperacao: "<<endl;
            cin>>nota_rec;
            if(media_final<5){
                cout<<"infelizmente voce reprovou"<<endl;
            }else{
                cout<<"Parabens voce foi aprovado"<<endl;
            } }
        if (media_anual<4){
             cout<<"infelizmente voce reprovou"<<endl;
        }
    return 0;
}