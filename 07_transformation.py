name ="David"
print(type(name))

#cambiamos tipo.
name = 12
print(type(name))

name = True
print(type(name))

numero = 123
texto = "El número es: "
resultado = texto + str(numero)
print(resultado)

print("David " + " Gonzalez")
print(10 + 20)
print("David" + str(12))

age = 12
print(f"Mi edad es {age}")

age = input ('Escribe tu edad=> ')
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años será {age}')