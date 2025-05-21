print("Por favor, responda com sim ou não:")

pont_total = 0

resp1 = str(input("Você já concluiu o ensino médio? "))
resp1 = resp1.strip().upper()

if resp1 == "SIM":
    pont_total = pont_total + 10
elif resp1 == "NÃO":
    pont_total = 0
else:
    pont_total = 0
    print("digite uma resposta válida!")


resp2 = str(input("Estudou em escola pública? "))
resp2 = resp2.strip().upper()

if (resp2 == "SIM"):
    pont_total = pont_total + 10
elif (resp2 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")

resp3 = str(input("Fez algum curso técnico? "))
resp3 = resp3.strip().upper()

if (resp3 == "SIM"):
    pont_total = pont_total + 10
elif (resp3 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp4 = str(input("Já frequentou uma universidade? "))
resp4 = resp4.strip().upper()

if (resp4 == "SIM"):
    pont_total = pont_total + 10
elif (resp4 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp5 = str(input("Gosta de estudar matemática? "))
resp5 = resp5.strip().upper()

if (resp5 == "SIM"):
    pont_total = pont_total + 10
elif (resp5 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp6 = str(input("Tem interesse em fazer uma pós-graduação? "))
resp6 = resp6.strip().upper()

if (resp6 == "SIM"):
    pont_total = pont_total + 10
elif (resp6 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp7 = str(input("Já participou de algum intercâmbio estudantil? "))
resp7 = resp7.strip().upper()

if (resp7 == "SIM"):
    pont_total = pont_total + 10
elif (resp7 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp8 = str(input("Acredita que a escola preparou você bem para o mercado de trabalho? "))
resp8 = resp8.strip().upper()

if (resp8 == "SIM"):
    pont_total = pont_total + 10
elif (resp8 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp9 = str(input("Já fez um curso online? "))
resp9 = resp9.strip().upper()

if (resp9 == "SIM"):
    pont_total = pont_total + 10
elif (resp9 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")


resp10 = str(input("Gostaria de aprender um novo idioma? "))
resp10 = resp10.strip().upper()

if (resp10 == "SIM"):
    pont_total = pont_total + 10
elif (resp10 == "NÃO"):
    pont_total = pont_total
else:
    print("digite uma resposta válida!")
print("Esse foi o seu resultado:", pont_total)




