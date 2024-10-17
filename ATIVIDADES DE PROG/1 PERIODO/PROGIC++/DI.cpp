#include <iostream>
using namespace std;
int main(){
char esc;
int part;
double sal_grupo;
    cout<<"Bem vindo ao sistema de calculo de MVP para Startups"<<endl;
    cout<<"Deseja iniciar um calculo?(S/N)"<<endl;
    cin>>esc;
    do{
        cout<<"Considerando todo seu grupo, Quantas pessoa ele possui: "<<endl;
        cin>>part;
        string nome[part];
        double salario[part];
            for (int i = 0; i < part; i++){
                cout<<"insira o nome e o Salario do "<<i+1<<" participante:"<<endl;
                cout<<"(Separados por espaco EX.: Joao 1234,56)"<<endl;
                cin>>nome[i]>>salario[i];
                system("CLS");
                sal_grupo += salario[i];
            }

            for (int i = 0; i < part; i++){
                cout<<"Nome e salario do participante "<<i+1<<endl;
                cout<<nome[i]<<" "<<salario[i]<<endl;
            }
            cout<<"salario total do grupo: "<<sal_grupo<<endl;
            cout<<"salario medio do grupo: "<<sal_grupo/part<<endl;
            system("pause");
            cout<<"deseja iniciar outro calculo?(S/N)"<<endl;
            cin>>esc;

          } while (esc == 's' || esc == 'S');
    

    return 0;
}