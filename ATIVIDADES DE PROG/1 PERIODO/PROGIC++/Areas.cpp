/*Escrever um programa que permita ao usuário escolher mediante
funções o cálculo da área de qualquer das figuras geométricas:
círculo, quadrado, retângulo ou triângulo*/
#include <iostream>
using namespace std;
void circulo(){
    double r;
    cout<<"insira o Raio do circulo: "<<endl;
    cin>>r;
    cout<<"A area total do circulo eh: "<<3.14*r*r<<" Metros quadrados"<<endl;
}
void quadrado(){
    double l;
    cout<<"Insira o tamanho do lado do quadrado: ";
    cin>>l;
    cout<<"A area total do quadrado eh: "<<l*l<<" Metros quadrados"<<endl;
}
void retangulo(){
    double b,h;
    cout<<"Insira o tamanho da base e da altura do retangulo (nesta ordem e separados por espaco): "<<endl;
    cin>>b>>h;
    cout<<"A area total do retangulo eh: "<<b*h<<" Metros quadrados"<<endl;
}
void triangulo(){
    double b,h;
    cout<<"Insira o tamanho da base e da altura do Triangulo (nesta ordem e separados por espaco): "<<endl;
    cin>>b>>h;
    cout<<"A area total do triangulo eh: "<<b*h/2<<" Metros quadrados"<<endl;
}
int esc;
int main(){
    cout<<"Insira qual figura geometrica quer calcular a area: "<<endl;
    cout<<"Circulo = 1 "<<endl;
    cout<<"Quadrado = 2 "<<endl;
    cout<<"Retangulo = 3 "<<endl;
    cout<<"Triangulo = 4 "<<endl;
    cin>>esc;
    if (esc == 1){
        circulo();
    }if (esc == 2){
        quadrado();
    }if (esc == 3){
        retangulo();
    }if (esc == 4){
        triangulo();
    }
    return 0;
}