def automata(palabra):
  estado_actual = 'e0'
  estados_aceptacion = {'e4'}
  delta = {
      ('e0', 'a'): 'e1',
      ('e1', 'a'): 'e2',
      ('e2', 'b'): 'e3',
      ('e3', 'b'): 'e3',
      ('e3', 'c'): 'e4',
      ('e4', 'b'): 'e3',
      ('e4', 'c'): 'e4'
  }
  for simbolo in palabra:
      if (estado_actual, simbolo) in delta:
          estado_actual = delta[(estado_actual, simbolo)]
      else:
          return False
  return estado_actual in estados_aceptacion


while True:
  palabra = input("Introduce la palabra (a, b, c) o escribe 'x': ").strip()
  if palabra.lower() == "x":
      print("fin del programa")
      break

  if automata(palabra):
      print("bien")
  else:
      print("mal")