def somar():
      numero1 = float(input("Digite o primeiro número: "))
      numero2 = float(input("Digite o segundo número: "))
      soma = numero1 + numero2
      print(f"O resultado da soma é: {soma}")

def subtrair():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    sub = numero1 - numero2
    print(f"O resultado da subtração é: {sub}")

def multiplicar():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    multi = numero1 * numero2
    print(f"O resultado da multiplicação é: {multi}")

def dividir():
     numero1 = float(input("Digite o primeiro número: "))
     numero2 = float(input("Digite o segundo número: "))
     div = numero1 / numero2
     print(f"O resultado da divisão é: {div}")

def pares():
    quantidade = int(input("Digite a quantidade que você deseja: "))
    cont = 1
    resultado = 0
    while cont <= quantidade:
        print(f"Os pares são: {resultado}")
        resultado += 2
        cont +=1

def impares():
    quantidade = int(input("Digite a quantidade que você deseja: "))
    cont = 1
    resultado = 1
    while cont <= quantidade:
        print(f"Os impares são: {resultado}")
        resultado += 2
        cont +=1

def somatorio():
    numero = float(input("Digite o número que deseja seu somatorio: "))
    
    cont = 1
    somatorio = 0

    while cont <= numero:
        somatorio = somatorio + cont
        cont +=1

    print(f"O somatorio vai ser igual a: {somatorio}")  

def fatorial():
    numero = float(input("Digite o número que deseja seu fatorial: "))
    
    cont = 1
    fatorial = 1

    while cont <= numero:
        fatorial = fatorial * cont
        cont +=1      
  
    print(f"O fatorial vai ser igual a: {fatorial}")  

while True: 
   print("CALCULADORA")
   print("1 - Adição")
   print("2 - subtração")
   print("3 - multiplicação")
   print("4 - divisão")
   print("5 - pares")
   print("6 - impares")
   print("7 - somatorio")
   print("8 - fatorial")
   print("0 - sair")

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
      somar()

   elif opcao == "2":
       subtrair()

   elif opcao == "3":
       multiplicar()

   elif opcao == "4":
       dividir()
   
   elif opcao == "5":
       pares()

   elif opcao == "6":
       impares()

   elif opcao == "7":
        somatorio()

   elif opcao == "8":
       fatorial()
   
   elif opcao == "0":
    print("Saindo do sistema...")
    break
  
   else:
       print("Opção inválida, tente novamente!!!")                   

