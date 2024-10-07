import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV
ruta_archivo = r"C:\Users\gerso\OneDrive\Documentos\Graficos.csv\Ejercicio.csv"

try:
    # Leer el archivo CSV
    df = pd.read_csv(ruta_archivo)

    # Pedir al usuario que ingrese el género
    genero_input = input("Ingrese el género (Male/Female): ")

    # Filtrar el DataFrame por el género ingresado
    df_genero = df[df['Gender'].str.lower() == genero_input.lower()]

    # Comprobar si hay datos filtrados
    if df_genero.empty:
        print("No se encontraron datos para el género ingresado.")
    else:
        # Contar la cantidad de registros por cada nivel de experiencia
        conteo_experiencia = df_genero['Experience_Level'].value_counts()

        # Crear el gráfico de barras
        plt.figure(figsize=(10, 6))
        conteo_experiencia.plot(kind='bar', color='skyblue')

        # Etiquetas y título
        plt.title(f'Conteo de Niveles de Experiencia para {genero_input.capitalize()}', fontsize=14)
        plt.xlabel('Nivel de Experiencia', fontsize=12)
        plt.ylabel('Cantidad de Personas', fontsize=12)
        plt.xticks(rotation=0)  # Para que las etiquetas del eje X no se roten

        # Mostrar el gráfico
        plt.tight_layout()
        plt.show()

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

#este es el link de la base de datos que use para trabajar este codigo


#Exlplicacion
#La base de datos en si trata sobre ejercicios donde se muestra una cantidad de usuarios que hacen 
#los ejercicios que se divide por nombre,genero,edad,pesos y mas yo solo trabajare con el genero 
#Male y Female para que me muestre la cantidad de personas y el nivel de experiencia que se encuentran.
