#include <iostream>
#include <string>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;
void mvp(){
    bool mvpBool = true, boolEscolha = true;
    int part = 0, escolha;
    double salario_unit = 0;
    double salario_tot = 0, tempo_desenvolvimento = 0, ass_mensal = 0;
    while(mvpBool == true){
    cout<<"Insira quantos participantes a Startup possui: "<<endl;
    cin>>part;
    for (int i = 0; i < part; i++){
        cout<<"insira o salario do "<<i+1<<" Participante: "<<endl;
        cin>>salario_unit;
        salario_tot += salario_unit;
    }
    cout<<"Insira quanto tempo levou para ser desenvolvido o software: (em meses)"<<endl;
    cin>>tempo_desenvolvimento;
    cout<<"Insira qual o valor mensal da assinatura do software: "<<endl;
    cin>>ass_mensal;
    cout<<fixed<<setprecision(2);
    cout<<"=== QUANTIDADE DE ASS. === RECEBIDO/MES === CUSTOS === TEMPO PARA GERAR LUCRO ==="<<endl;
    cout<<"    1                       "<<ass_mensal<<"         "<<salario_tot<<"     "<<salario_tot/ass_mensal<<endl;
    cout<<"    10                      "<<ass_mensal*10<<"        "<<salario_tot<<"     "<<salario_tot/(ass_mensal*10)<<endl;
    cout<<"    50                      "<<ass_mensal*50<<"        "<<salario_tot<<"     "<<salario_tot/(ass_mensal*50)<<endl;
    cout<<"    100                     "<<ass_mensal*100<<"       "<<salario_tot<<"     "<<salario_tot/(ass_mensal*100)<<endl;
    cout<<"    500                     "<<ass_mensal*500<<"       "<<salario_tot<<"     "<<salario_tot/(ass_mensal*500)<<endl;
    cout<<"    1000                    "<<ass_mensal*1000<<"      "<<salario_tot<<"     "<<salario_tot/(ass_mensal*1000)<<endl;
    while (boolEscolha == true){  
    cout<<"1- Simular outro mvp"<<endl<<"2- Voltar para pagina de escolha"<<endl<<"insira a escolha:"<<endl;
    cin>>escolha;
    if (escolha<1 && escolha>2){
        cout<<"Opcao invalida, tente novamente!!!"<<endl;
    }
    if (escolha == 1){
        system("cls");
        boolEscolha = false;
    }
    if (escolha == 2){
        system("cls");
        boolEscolha = false;
        mvpBool = false;
    }
    }
}
    boolEscolha=true;
    mvpBool=true;
    cout<<"voltando para a pagina de escolha..."<<endl;
    system("pause");
}
void tabela(){
    int esc, id_exc, ids;
    string nome, data;
    double valor;
    vector <int> id;
    vector <string> nomes;
    vector <double> valor_ass;
    vector <string> datas;
    bool systemesc = true;
    while(systemesc == true){
    cout<<"==GESTAO DE ASSINATURAS=="<<endl;
    if (nomes.size() > 0){   
    for (int i = 0; i < id.size(); i++){
        cout<<id.at(i)<<" - "<<nomes.at(i)<<" | "<<valor_ass.at(i)<<" | "<<datas.at(i)<<endl;
    }
    }
    cout<<"(1) registrar nova assinatura."<<endl;
    cout<<"(2) excluir registro. "<<endl;
    cout<<"(0) Voltar ao menu de escolhas."<<endl;
    cin>>esc;
    if (esc == 1){
        bool testeid = true;
        cout<<"Insira o id para a assinatura: (SOMENTE NUMEROS)"<<endl;      
        id.push_back(ids); 
        cout<<"Insira o nome do assinante: (Usando _ no lugar dos espacos)"<<endl;
        cin>>nome;
        nomes.push_back(nome);
        cout<<"insira o valor da assinatura: (SOMENTE NUMEROS)"<<endl;
        cin>>valor;
        valor_ass.push_back(valor);
        cout<<"Que dia foi realizada a assinatura: (Insira como dd/mm/aaaa com barras)"<<endl;
        cin>>data;
        datas.push_back(data);
        cout<<"Assinatura salva com sucesso"<<endl;
        system("pause");
        }   
    if (esc == 2){
        cout<<"insira o id da assinatura que deseja excluir: "<<endl;
        cin>>id_exc;
        for (int i = 0; i < id.size(); i++){
            if (id_exc == id.at(i)){
                id.erase(id.begin()+i);
                nomes.erase(nomes.begin()+i);
                valor_ass.erase(valor_ass.begin()+i);  //.erase é usado para apagar valores de um vector
                datas.erase(datas.begin()+i);
                system("CLS");
            }
        }
        cout<<"registro excluido com sucesso"<<endl;
        cout<<"Voltando a tabela de gestao..."<<endl;
        system("pause");
    }
    if (esc == 0){
        systemesc = false;
    }
       
} 
}
void escempresa(){
    int esc;
    bool systemBool = true;
    system("CLS");
    while (systemBool == true){
    cout<<"===ESCOLHA DE FUNCIONALIDADES==="<<endl;
    cout<<"1- SIMULAR MVP."<<endl;
    cout<<"2- TABELA DE GESTAO."<<endl;
    cout<<"0- Voltar Ao Menu Inicial"<<endl;
    cout<<"Insira a escolha desejada: "<<endl;
    cin>>esc;

    if (esc == 0){
       systemBool = false;
       cout<<"voltando para menu..."<<endl;
       system("pause");

    }
    if (esc == 1 ){
        mvp();
    }
    if (esc == 2){
        tabela();
    }
    if (esc < 0 && esc > 2){
    cout<<"==ESCOLHA INVALIDA=="<<endl;
    cout<<"Tente novamente"<<endl;
    system("pause");
    }  
    }
    systemBool = true;
}
void login(){
    string usuario;
    int senha;
    system("CLS");
    cout<<"Insira seu usuario: (Inteiramente em letras maiusculas e sem acentos)"<<endl;
    cin>>usuario;

    if (usuario == "MAPIO"){
        cout<<"Digite sua senha: "<<endl;
        cin>>senha;

    if (senha == 2023220106 || senha == 2023220065){
        escempresa();
    }else{
        cout<<"==USUARIO ou SENHA INVALIDOS=="<<endl;
        cout<<"Tente Novamente"<<endl;
        system("pause");
        login();
    }
}else{
        cout<<"==USUARIO ou SENHA INVALIDOS=="<<endl;
        cout<<"Tente Novamente"<<endl;
        system("pause");
        login();
    }
    }
int main(){
    int esc;
    bool systembool = true;
    while (systembool == true){
    cout<<"==Bem vindo ao sistema de calculo de MVP=="<<endl;
    cout<<"0 - Finalizar o sistema."<<endl;
    cout<<"1 - Efetuar o Login. "<<endl;
    cout<<"Digite sua escolha: "<<endl;
    cin>>esc;
        if(esc == 1){
            systembool = false;
            login();
        }
        else if (esc == 0){
            cout<<" Obrigado por utilizar o sistema :) ";
            systembool = false;
            } if (esc < 0 && esc > 1){
               cout<<"Escolha invalida";
            }
            
    }
    return 0;
    
}