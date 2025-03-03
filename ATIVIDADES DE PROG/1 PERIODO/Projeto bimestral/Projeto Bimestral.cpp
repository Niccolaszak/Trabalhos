#include <iostream>
#include <iomanip> //Biblioteca utilizada Para conseguir limitar as casas decimais dos números em duas
#include <vector>
using namespace std;
int main() {
    double senha;
    cout<<"Por favor, Digite a senha de acesso ao sistema: "<<endl;
    cin>>senha;
        if(senha == 2023220106 || senha == 2023220065){//if para verificação de senha
            string cpf, local, tipagem;
            vector <string> nome;
            int dd, mm, aaaa;
            cout<<"Bem vindo ao Sistema de Registro de Empregados."<<endl;
            cout<<"Vamos iniciar um novo registro de funcionario."<<endl;
            cout<<"Digite o nome completo: "<<endl;
            cin.ignore();
            getline(cin, nome);
            cout<<"Digite o cpf do funcionario: "<<endl;
            cin>>cpf;
            cout<<"Digite o endereco completo:"<<endl;
            cin.ignore();
            getline(cin, local);
            cout<<"Digite a data de admissao no formato DD MM AAAA (nesta ordem e separados por espacos):"<<endl;
            cin>>dd>>mm>>aaaa;
            cout<<"Qual o tipo de funcionario (efetivo,temporario ou estagiario): "<<endl;
            cin>>tipagem;
            if (tipagem == "efetivo"){//condição caso o funcionário seja efetivo
                double salario_base, horas_extras, salario_hora, horas_trabalhadas, salario_total, salario_final, inss, ir, descontos;
                cout<<"Digite o salario base mensal da contratacao:"<<endl;
                cin>>salario_base;
                cout<<"informe a quantidade de horas extras do funcionario:"<<endl;
                cin>>horas_trabalhadas;
                salario_hora=(salario_base/30)/8;
                horas_extras=(salario_hora+(salario_hora*0.5))*horas_trabalhadas;
                salario_total=salario_base+horas_extras;
                inss=salario_total*0.08;
                ir=salario_total*0.12;
                descontos=ir+inss;
                salario_final=salario_total-descontos;
                cout<<fixed<<setprecision(2); //Comando utilizado para limitar as casas decimais em duas
                cout<<"=============================================================================="<<endl;
                cout<<"Nome: "<<nome <<"                           CPF: "<<cpf<<endl;
                cout<<"Endereco: "<<local<<"                       Data de admissao: "<<dd<<"/"<<mm<<"/"<<aaaa<<endl;
                cout<<"Tipo de emprego: "<<tipagem<<"                   Salario Mensal: "<<salario_base<<endl;
                cout<<"=============================================================================="<<endl;
                cout<<"       DESCRICAO       |   REFERENCIA   |    PROVENTOS    |    DESCONTOS    "<<endl;
                cout<<"       salario base                      "<<salario_base<<endl;
                cout<<"       horas extras      salario/hr+50%  "<<horas_extras<<endl;
                cout<<"       INSS                  8 %                           "<<inss<<endl;
                cout<<"       Imposto de renda     12 %                           "<<ir<<endl;
                cout<<"\n=============================================================================="<<endl;
                 cout<<"                             TOTAL       "<<salario_total<<"           "<<descontos<<endl;
                cout<<"    Salario final                        "<<salario_final<<endl;
                cout<<"=============================================================================="<<endl;
            }if (tipagem == "temporario"){//condição caso o funcionário seja Temporario
                double salario_base,tempo_empregado, horas_extras, salario_dia, salario_hora, horas_trabalhadas, salario_total, salario_final, inss, ir, descontos;
                cout<<"Digite o salario base diario da contratacao:"<<endl;
                cin>>salario_dia;
                cout<<"Digite a quantidade de dias trabalhados pelo funcionario:"<<endl;
                cin>>tempo_empregado;
                cout<<"informe a quantidade de horas extras do funcionario:"<<endl;
                cin>>horas_trabalhadas;
                salario_base=salario_dia*tempo_empregado;
                salario_hora=(salario_dia)/8;
                horas_extras=(salario_hora+(salario_hora*0.5))*horas_trabalhadas;
                salario_total=salario_base+horas_extras;
                inss=salario_total*0.08;
                ir=salario_total*0.12;
                descontos=ir+inss;
                salario_final=salario_total-descontos;
                cout<<fixed<<setprecision(2); //Comando utilizado para limitar as casas decimais em duas
                cout<<"=============================================================================="<<endl;
                cout<<"Nome: "<<nome <<"                           CPF: "<<cpf<<endl;
                cout<<"Endereco: "<<local<<"                       Data de admissao: "<<dd<<"/"<<mm<<"/"<<aaaa<<endl;
                cout<<"Tipo de emprego: "<<tipagem<<"                   Salario Diario: "<<salario_dia<<endl;
                cout<<"Observacao: Salario referente ao trabalho de "<<tempo_empregado<<"dias para a empresa."<<endl;
                cout<<"=============================================================================="<<endl;
                cout<<"       DESCRICAO       |   REFERENCIA   |    PROVENTOS    |    DESCONTOS    "<<endl;
                cout<<"       salario           diaria*tempo    "<<salario_base<<endl;
                cout<<"       horas extras      salario/hr+50%  "<<horas_extras<<endl;
                cout<<"       INSS                  8 %                           "<<inss<<endl;
                cout<<"       Imposto de renda     12 %                           "<<ir<<endl;
                cout<<"\n=============================================================================="<<endl;
                cout<<"                             TOTAL       "<<salario_total<<"           "<<descontos<<endl;
                cout<<"    Salario final                        "<<salario_final<<endl;
                cout<<"=============================================================================="<<endl;
            }if (tipagem == "estagiario"){//condição caso o funcionário seja estagiario
                double salario, inss, ir, descontos;
                salario = 800;
                inss = 0;
                ir = 0;
                descontos = ir+inss;
                 cout<<fixed<<setprecision(2); //Comando utilizado para limitar as casas decimais em duas
                cout<<"=============================================================================="<<endl;
                cout<<"Nome: "<<nome <<"                           CPF: "<<cpf<<endl;
                cout<<"Endereco: "<<local<<"                       Data de admissao: "<<dd<<"/"<<mm<<"/"<<aaaa<<endl;
                cout<<"Tipo de emprego: "<<tipagem<<"                   Salario Mensal: "<<salario<<endl;
                cout<<"=============================================================================="<<endl;
                cout<<"       DESCRICAO       |   REFERENCIA   |    PROVENTOS    |    DESCONTOS    "<<endl;
                cout<<"       salario base                      "<<salario<<endl;
                cout<<"       INSS                  8 %                           "<<inss<<endl;
                cout<<"       Imposto de renda     12 %                           "<<ir<<endl;
                cout<<"\n=============================================================================="<<endl;
                 cout<<"                             TOTAL       "<<salario<<"           "<<descontos<<endl;
                cout<<"    Salario final                        "<<salario<<endl;
                cout<<"=============================================================================="<<endl;
            }else{
                cout<<"Tipo de Funcionario Invalido."<<endl;
            }
            } else
        cout<<"<A SENHA ESTA INCORRETA>";
    return 0;
}


