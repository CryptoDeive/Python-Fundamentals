name = "David"
last_name = "Gonzalez"
print(name)
print(last_name)

#concatenación
full_name = name + " " + last_name 
print(full_name)

#cambiar las comillas para que se vea el apostrofe
quote = "I'm David"

quote2 = ' She said "hello" '
print(quote2)

#format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('V1 ', template)

#En el orden que lo coloques es como remplaza las llaves
template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)

print('V2 ', template)

#f de format, la mas utilizada en python
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"

print('V3 ', template)

age = 38
template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y mi edad es {age}"

print('V4 ', template)

