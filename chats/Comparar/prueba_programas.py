import subprocess
import time

def ejecutar_programa(ruta_programa):
    inicio = time.time()
    resultado = subprocess.run(['python', ruta_programa], capture_output=True, text=True)
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return resultado.stdout.strip(), tiempo_ejecucion

def main():
    resultado1, tiempo1 = ejecutar_programa('programa1.py')
    resultado2, tiempo2 = ejecutar_programa('programa2.py')

    print("Resultado del Programa 1:", resultado1)
    print("Tiempo de Ejecución del Programa 1: {:.6f} segundos".format(tiempo1))
    
    print("Resultado del Programa 2:", resultado2)
    print("Tiempo de Ejecución del Programa 2: {:.6f} segundos".format(tiempo2))

    print("*" * 25)
    print("Comparando resultados...")
    if resultado1 == resultado2:
        print("Los resultados son iguales.")
    else:
        print("Los resultados son diferentes.")
    
    print("*" * 25)
    print("Comparando tiempos de ejecución...")
    if tiempo1 < tiempo2:
        print("El Programa 1 es más rápido por {:.6f} segundos.".format(tiempo2 - tiempo1))
    elif tiempo1 > tiempo2:
        print("El Programa 2 es más rápido por {:.6f} segundos.".format(tiempo1 - tiempo2))
    else:
        print("Ambos programas tienen el mismo tiempo de ejecución.")

if __name__ == "__main__":
    main()
