# def fai_somma(num1, num2):
#     sum=num1 + num2
#     return sum

# def fai_sottrazione(num1, num2):
#     diff= num1 - num2
#     return diff

# y=int(input())
# z=int(input())
# k=fai_somma(y , z)
# print(k)
# a=int(input())
# b=int(input())
# c=fai_sottrazione(a , b)
# print(k)
# print(c)


#Costruttore 
# class Persona:
#     def __init__(self , nome , cognome):
#         self.nome = nome
#         self.cognome = cognome
        
#     def saluta(self):
#         print("ciao sono " + self.nome + " " + self.cognome )      
    

# persona1 = Persona("Francesco" , "Davoli")
# persona2 = Persona("Rebecca", "Davoli")

# persona1.saluta()
# persona2.nome= "Giuseppe"
# persona2.saluta()
# del persona2.nome
# del persona2


for numero in range(101):
    if numero % 15 == 0:
        print("FizzBuzz")
    elif numero % 5 == 0:
        print("Buzz")
    elif numero % 3 == 0:
        print("Fizz")
    else:
        print(numero)            
        
   
     


