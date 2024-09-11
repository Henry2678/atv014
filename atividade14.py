# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
media = float(input("digite a nota 1"))
media2 = float(input("digite a nota 2"))
media3 = float(input("digite a nota 3"))
resultado = media+media2+media3/3
if resultado>=7:
    print("voce esta aprovado ")
elif resultado>5>7:
    print("recuperaçao")
else:
    print("aluno reprovado ")    
         