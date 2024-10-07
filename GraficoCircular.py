import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
ruta_archivo = r"C:\Users\gerso\OneDrive\Documentos\Graficos.csv\laptop.csv"

# Cargar el DataFrame
df = pd.read_csv(ruta_archivo)

# Lista de precios disponibles
precios_disponibles = [22990, 36289, 78500, 55490, 21990, 34990, 
                       49599, 39990, 33111, 48990, 92990, 
                       31490, 104990, 44999, 112980, 52800, 
                       36990, 47999]

# Ordenar la lista de precios
precios_disponibles.sort()

# Imprimir los precios disponibles en grupos de 4
print("Precios disponibles:")
for i in range(0, len(precios_disponibles), 4):
    print(" | ".join(f"{precio: >7}" for precio in precios_disponibles[i:i + 4]))

# Solicitar un precio al usuario
while True:
    precio_usuario = input("Ingresa un precio: ")

    try:
        precio_usuario = float(precio_usuario)  # Intentar convertir a float
        if precio_usuario in precios_disponibles:  # Verificar si el precio está en la lista
            break  # Salir del bucle si la entrada es válida
        else:
            print("Por favor, ingresa un precio válido de la lista.")
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar un número.")

# Filtrar las laptops que tienen el precio ingresado
laptops_seleccionadas = df[df['Price'] == precio_usuario]

# Verificar si se encontraron laptops con el precio ingresado
if laptops_seleccionadas.empty:
    print(f"No se encontraron laptops con el precio de {precio_usuario}.")
else:
    # Obtener las marcas de las laptops seleccionadas
    marcas = laptops_seleccionadas['Brand'].value_counts()
    
    # Crear el gráfico circular
    plt.figure(figsize=(8, 8))
    plt.pie(marcas, labels=marcas.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'Porcentaje de Marcas para Laptops con Precio {precio_usuario}')
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.show()

    #Este es el link de la base d datos que se trabajo 
    #https://www.kaggle.com/datasets/pradeepjangirml007/laptop-data-set
    

    #la ecxplicacion de esta grafica es simple mas que las anteriores solo es de ingresar el precio de la 
    #lista que se muestra como precios disponibles dado que que la base de datos ya tiene unos precios extraños
    #y son varios solo coloque algunos al momento de seleccionar un porecio de la lista mostrara una grafica circular
    #donde saldran las marcas que tengas mas laptop del precio que nosotros  ingresamos