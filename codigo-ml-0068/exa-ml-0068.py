import sys
import os
import io
import pandas as pd

# -------------------------------------------------------------------
# IMPORTAR dicc_0068 DESDE LA CARPETA RAÍZ
# -------------------------------------------------------------------
# Subir un nivel desde 'codigo-ml-0068' hacia la carpeta raíz 'EXA-ML-0068'
script_dir = os.path.dirname(os.path.abspath(__file__))
carpeta_raiz = os.path.abspath(os.path.join(script_dir, '..'))

if carpeta_raiz not in sys.path:
    sys.path.append(carpeta_raiz)

# Importar el archivo dicc_0068.py ubicado en la raíz
import dicc_0068

# -------------------------------------------------------------------
# LÓGICA DEL REPORTE
# -------------------------------------------------------------------
print("Christian Garcia Machine Learning pandas, NC 0068")

# Variable para almacenar las salidas y guardarlas en el archivo .md
contenido_md = []
encabezado_pie = "Christian Garcia Machine Learning, NC 0068"
contenido_md.append(f"# Reporte de Análisis de Datos - Pandas\n\n`{encabezado_pie}`\n")

def registrar(titulo, contenido):
    """Muestra el resultado en terminal y lo formatea para el archivo Markdown."""
    print(f"\n--- {titulo} ---")
    print(contenido)
    contenido_md.append(f"## {titulo}\n```text\n{contenido}\n```\n")

# 1. Convertir diccionario a DataFrame
df = pd.DataFrame(dicc_0068.datos_teatros)
registrar("1. DataFrame Convertido", df)

# 2. Información Estructural
registrar("2.1 Primeras Filas (head)", df.head(2))
registrar("2.2 Últimas Filas (tail)", df.tail(2))
registrar("2.3 Dimensiones (Filas, Columnas)", df.shape)
registrar("2.4 Tipos de Datos por Columna", df.dtypes)

# Capturar salida de df.info()
buffer = io.StringIO()
df.info(buf=buffer)
registrar("2.5 Información General (info)", buffer.getvalue())

# 3. Estadísticas Generales de una Columna Numérica (Capacidad)
registrar("3. Estadísticas Generales de la Columna 'Capacidad'", df['Capacidad'].describe())

# 4. Ordenar Ascendente por Capacidad
df_asc_capacidad = df.sort_values(by="Capacidad", ascending=True)
registrar("4. Ordenar Ascendente por Capacidad", df_asc_capacidad)

# 5. Ordenar Descendente por Funciones_mes
df_desc_funciones = df.sort_values(by="Funciones_mes", ascending=False)
registrar("5. Ordenar Descendente por Funciones_mes", df_desc_funciones)

# 6. Guardar el archivo resultados-ml-0068.md dentro de resultados-0068
carpeta_resultados = os.path.join(carpeta_raiz, 'resultados-0068')
os.makedirs(carpeta_resultados, exist_ok=True)
ruta_archivo_md = os.path.join(carpeta_resultados, "resultados-ml-0068.md")

contenido_md.append(f"`{encabezado_pie}`")

with open(ruta_archivo_md, "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_md))

print(f"\n[ÉXITO] Archivo generado correctamente en: {ruta_archivo_md}")
print("Christian Garcia Machine Learning pandas, NC 0068")