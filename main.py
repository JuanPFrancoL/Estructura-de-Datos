from prisionero import Prisionero
from lista_simple import ListaSimple

if __name__ == '__main__':
    prisioneros_data = {
        "Konstantinos": 47,
        "Theodoros": 23,
        "Nikephoros": 35,
        "Ioannis": 19,
        "Demetrios": 52,
        "Georgios": 28,
        "Alexios": 31,
        "Mikhail": 44,
        "Stavros": 38,
        "Basileios": 25,
        "Euphrosyne": 29,
        "Anastasios": 33,
        "Philippos": 21,
        "Zosimas": 41,
        "Kallistos": 26,
    }

    edad_gracia = 38
    k1 = 3
    k2 = 2

    # Contruir lista
    circulo = ListaSimple()
    for nombre, edad in prisioneros_data:
        circulo.agregar_prisionero(Prisionero(nombre, edad))

    # Primer dec
    circulo.ordenar()

    print("= Registro ordenado por edad =")
    circulo.imprimir()
    print(" ")

    # Segundo dec
    liberado = circulo.clemencia(edad_gracia)

    if liberado is not None:
        gracia = liberado.nombre
    else:
        gracia = None

    print("= Decreto de clemencia =")
    print(f"gracia -> ", gracia)
    print(" ")

    # Tercer y cuarto dec
    ejecutados = ListaSimple()
    sobreviviente = circulo.juego_circulo(k1, k2, ejecutados)



    print("= Resultado final =")
    print("Gracia ->", gracia)

    print("Ejecutados: ")
    puntero = ejecutados.cabeza
    while puntero is not None:
        print(puntero.nombre)
        puntero = puntero.siguiente

    print("Sobreviviente: ", sobreviviente.nombre)