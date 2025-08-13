def automata(palabra):
    estado_actual = 'e0'
    estados_aceptacion = {'e3'} 
    delta = {
        ('e0', 'a'): 'e1',
        ('e1', 'a'): 'e2',
        ('e2', 'b'): 'e3',
        ('e3', 'b'): 'e4',
        ('e3', 'c'): 'e3',
        ('e4', 'b'): 'e3',
        ('e4', 'c'): 'e4'
    }
    contador_b = 0 
    for simbolo in palabra:
        if simbolo == 'b':
            contador_b += 1
        elif simbolo == 'c':
            if contador_b % 2 == 0 and contador_b != 0:
                return False
            contador_b = 0 
        else:
            contador_b = 0  

        if (estado_actual, simbolo) in delta:
            estado_actual = delta[(estado_actual, simbolo)]
        else:
            return False
    
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
