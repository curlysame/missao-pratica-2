saida = ''

def adicao(a,b):
    return a + b
def subracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    if b == 0:
        return "Não foi possivel realizar a divisao por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao in ['+']:
        resultado = adicao(num1, num2)
    elif operacao in ['-']:
        resultado = subracao(num1, num2)
    elif operacao in ['*']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/']:
        resultado = divisao(num1,num2)
    else:
        resultado= "Operação inválida"
    return resultado

while saida.lower() != 'n':
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        continue

    operacao = input("Digite a operação desejada(+, -, *, /): ").strip().lower()
    
    reultado = calculadora(num1, num2, operacao)
    print(f"Resultado da operação: {reultado}")

    saida = input("Deseja realizar outra operação? (S/N): ").strip().lower()
