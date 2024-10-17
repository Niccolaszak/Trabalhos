#include <iostream>
using namespace std;
int main() {
    const double valorqp{100.00};
    const double valorqg{150.00};
    const double imposto{0.06};
    const double tempo{30};
        cout<<"Bem vindo ao servico de limpeza de carpetes do Frank"<<endl;
        int qp, qg;
        cout<<"Insira a quantidade de quartos pequenos e grandes que deseja limpar (nesta ordem e separados por espaco): "<<endl;
        cin>>qp>>qg;
        double tot_qp = (qp*valorqp);
        double tot_qg = (qg*valorqg);
        double valor_imp =(tot_qp+tot_qg)*imposto;
        double valor_tot =(tot_qp+tot_qg)+valor_imp;
        cout<<"=======================================";
        cout<<"\nOrcamento para servico de limpeza: ";
        cout<<"\nQuantidade de quartos pequenos: "<<qp;
        cout<<"\nQuantidade de quartos grandes: "<<qg;
        cout<<"\nPreco total dos quartos pequenos: "<<tot_qp;
        cout<<"\nPreco total dos quartos grandes: "<<tot_qg;
        cout<<"\nCusto: "<<tot_qp+tot_qg;
        cout<<"\nImposto: "<<valor_imp;
        cout<<"\n=======================================";
        cout<<"\nOrcamento total: "<<valor_tot;
        cout<<"\nEste orcamento e valido por "<<tempo<<" dias";
    return 0;
}

