import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV
ruta_archivo = r"C:\Users\gerso\OneDrive\Documentos\Graficos.csv\Marvel Vs DC NEW.csv"
df = pd.read_csv(ruta_archivo)

# Solicitar calificación al usuario
calificacion = float(input("Ingresa una calificación (por ejemplo, 8.0): "))

# Filtrar películas con calificaciones mayores a la ingresada
peliculas_mayores = df[df['IMDB_Score'] > calificacion].head(3)  # Tomar las primeras 3

# Filtrar películas con calificaciones menores a la ingresada
peliculas_menores = df[df['IMDB_Score'] < calificacion].head(2)  # Tomar las primeras 2

# Combinar ambas listas
peliculas_combined = pd.concat([peliculas_mayores, peliculas_menores])

# Verificar si hay suficientes películas para mostrar
if peliculas_combined.empty:
    print(f"No se encontraron películas con calificaciones cercanas a {calificacion}.")
else:
    # Crear el gráfico
    plt.figure(figsize=(12, 6))  # Aumentar el tamaño de la figura
    plt.plot(peliculas_combined['Movie'], peliculas_combined['IMDB_Score'], marker='o', linestyle='-', color='b')
    plt.axhline(y=calificacion, color='r', linestyle='--', label=f'Calificación ingresada: {calificacion}')
    plt.xlabel('Película')
    plt.ylabel('Calificación')
    plt.title(f'Películas con calificaciones superiores e inferiores a {calificacion}')
    plt.xticks(rotation=45, ha='right', fontsize=10)  # Rotar los nombres de las películas
    plt.tight_layout(pad=2)  # Ajustar el espacio entre los elementos
    plt.legend()
    plt.show()

#este es el link de la base de datos que utilice
#https://www.kaggle.com/datasets/willianoliveiragibin/marvel-vs-dc

#explicacion de grafico
#Este gráfico código muestra la relación entre las calificaciones de películas y su puntuación en IMDB.
#  Se seleccionaron películas con calificaciones específicas, tanto superiores como inferiores a un 
# valor de referencia ingresado por el usuario. Este gráfico permite visualizar cómo las calificaciones 
# varían entre diferentes películas, facilitando la comparación de sus puntuaciones. Los puntos 
# en el gráfico representan las calificaciones, mientras que las líneas conectan estos puntos,
#  destacando la tendencia de las calificaciones en función de la entrada del usuario.