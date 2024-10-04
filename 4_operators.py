
#operaciones con enteros
print("3+4 =", 3+4)
print("3-4 =", 3-4)
print("3*4=", 3*4)
print("3/4=", 3/4)

print("10%3=", 10/3)  #el resultado es el residuo del entero entre el dividendo
print("10//3=", 10/3) #el resultado, es el resultado entero del entero entre el dividendo
print("2**3=", 2*3)
print("2**3 + 3 -7 /1// 4=", 2**3+3-7/1 // 4)



#operaciones con cadena de texto
print("hola" + "python" + "¿que tal?")
print("hola" + str(5))

#operaciones mixtas
print("Hola" * 5)
print("Hola" * (2**3))

my_float = 2.5 *2
print("Hola" * int(my_float))

#Operadores comparativos

#operadores con enteros

print(3 > 4)
print(3 < 4)
print(3 >=4)
print(4 <=4)
print(3 == 4)
print(3 != 4)

#operaciones con cadena de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa") # ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #cuenta caracteres
print("Hola"<= "Python")
print("Hola" == "Hola")   #es falso "==""
print("Hola" != "Python") #es diferente "!""


print("a">"b")
print("b">"a")

#operadores logicos
#Basada en algebra de boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
print(3 > 4 and "Hola" > "Python") #y
print(3 > 4 or "Hola" > "Python") #o
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4)) #no
