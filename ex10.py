#10 - receba três notas de um aluno e informe se ele passou ou reprovou.
nota_minima=int(input("digite a nota minima para passar: "))
nota1=float(input("digite a primeira nota do aluno: "))
nota2=float(input("digite a segunda nota do aluno: "))
nota3=float(input("digite a terceira nota do aluno: "))
nota_final=(nota1+nota2+nota3)/3
if nota_final>=nota_minima:
    print("aluno aprovado com: ",nota_final)
elif nota_final<nota_minima:
    print("aluno foi reprovado com: ",nota_final)