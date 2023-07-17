#include <iostream>
using namespace std;

int main() {
    char operador;
    double num1, num2, resultado;

    cout << "Digite a operação (+, -, *, /): ";
    cin >> operador;

    cout << "Digite o primeiro número: ";
    cin >> num1;

    cout << "Digite o segundo número: ";
    cin >> num2;

    switch (operador) {
        case '+':
            resultado = num1 + num2;
            break;
        case '-':
            resultado = num1 - num2;
            break;
        case '*':
            resultado = num1 * num2;
            break;
        case '/':
            if (num2 != 0)
                resultado = num1 / num2;
            else {
                cout << "Erro: divisão por zero não é permitida." << endl;
                return 1;
            }
            break;
        default:
            cout << "Operação inválida." << endl;
            return 1;
    }

    cout << "Resultado: " << resultado << endl;
    return 0;
}
