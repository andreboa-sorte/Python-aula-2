'''
20 - Crie um classe Funcionário com os atributos nome, idade e salário.
 Deve ter  um método  aumenta_salario. Crie duas subclasses da classe funcionário, programador  e
 analista, implementando o método  nas duas subclasses. Para o programador some ao atributo salário mais 20 e
 ao analista some ao salário mais 30,  mostrando na tela o valor. Depois disso, crie uma classe de testes instanciando
  os objetos programador e analista e chame o método  aumenta_salario de cada um.
'''

class Funcionarios():

    nome=""
    idade=0
    salario=0.0
    def aumenta_salario(self,salario):
        situacao=True
        while situacao:
            salario_temp=float(input("digite a qunatidade de dinheiro a ser aumentado no salario"))
            op=int(input("o salario atual é de: {0:.2f} e a qunatidade a ser aumentada é: {0:.2f}\n"
                  "para confirmar aperte 1\n "
                  "opção: ".format(salario, salario_temp)))
            if op==1:
                salario=salario_temp
                print("operação feita com sucesso")
                situacao=False
            elif op!=0:
                print("digite o novo salario que se deseja aumentar\n\n")

class