import random

# Define las opciones del juego
options = ['piedra', 'papel', 'tijera']

def get_user_choice():
  # Solicita al usuario que elija una opción
  user_choice = input('Elige piedra, papel o tijera: ')
  user_choice = user_choice.lower()

  # Asegúrate de que la opción del usuario sea válida
  while user_choice not in options:
    print('Opción no válida. Inténtalo de nuevo.')
    user_choice = input('Elige piedra, papel o tijera: ')

  return user_choice

def determine_winner(user_choice, computer_choice):
  # Compara las elecciones y determina el ganador
  if user_choice == computer_choice:
    return 'Empate'
  elif user_choice == 'piedra' and computer_choice == 'tijera':
    return 'Ganas'
  elif user_choice == 'papel' and computer_choice == 'piedra':
    return 'Ganas'
  elif user_choice == 'tijera' and computer_choice == 'papel':
    return 'Ganas'
  else:
    return 'Pierdes'

# Ejecuta el juego en un bucle
while True:
  # Solicita al usuario que elija una opción
  user_choice = get_user_choice()

  # El ordenador elige una opción al azar
  computer_choice = random.choice(options)

  # Determina el ganador
  result = determine_winner(user_choice, computer_choice)

  # Muestra el resultado
  print(f'Tú elegiste {user_choice} y el ordenador eligió {computer_choice}.')
  print(f'{result}')
