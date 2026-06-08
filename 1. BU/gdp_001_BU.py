# Capa Bronce
##  Lectura de Datos
import pandas as pd
data = pd.read_csv('data/iris.csv')
data = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']]
data

## Integridad de datos

### Resumen General
import pandas as pd
import numpy as np

def resumen_variables(df, top_categorias=10):
    """
    Genera un resumen de las variables de un DataFrame.

    Parámetros:
    ----------
    df : pandas.DataFrame
        Dataset a analizar.
    top_categorias : int
        Número máximo de categorías a mostrar para variables categóricas.
    Retorna:
    -------
    resumen_df : pandas.DataFrame
        Resumen general de variables.
    categorias_dict : dict
        Conteos de categorías por variable categórica.
    """
    resumen = []
    categorias_dict = {}
    for col in df.columns:
        # Tipo de dato
        tipo = str(df[col].dtype)
        # Cantidad de missings
        n_missing = df[col].isnull().sum()
        pct_missing = round((n_missing / len(df)) * 100, 2)
        # Cantidad de valores únicos
        n_unicos = df[col].nunique(dropna=True)
        # Identificar si es numérica
        es_numerica = pd.api.types.is_numeric_dtype(df[col])
        # Estadísticas para numéricas
        if es_numerica:
            media = df[col].mean()
            minimo = df[col].min()
            maximo = df[col].max()
            resumen.append({
                "Variable": col,
                "Tipo": tipo,
                "Es_Numerica": True,
                "Missings": n_missing,
                "%_Missings": pct_missing,
                "Valores_Unicos": n_unicos,
                "Media": media,
                "Min": minimo,
                "Max": maximo
            })
        else:
            # Conteo de categorías
            conteo = (
                df[col]
                .value_counts(dropna=False)
                .head(top_categorias)
                .reset_index()
            )
            conteo.columns = ["Categoria", "Conteo"]
            categorias_dict[col] = conteo
            resumen.append({
                "Variable": col,
                "Tipo": tipo,
                "Es_Numerica": False,
                "Missings": n_missing,
                "%_Missings": pct_missing,
                "Valores_Unicos": n_unicos,
                "Media": np.nan,
                "Min": np.nan,
                "Max": np.nan
            })
    resumen_df = pd.DataFrame(resumen)
    return resumen_df, categorias_dict

resumen_variables(data)[0]

resumen_variables(data)[1]
## Missings
import matplotlib.pyplot as plt
plt.bar(resumen_variables(data)[0]['Variable'], resumen_variables(data)[0]['%_Missings'])
plt.xlabel('Variable')
plt.ylabel('% de Missings')
plt.title('Porcentaje de Missings por Variable')
plt.xticks(rotation=45)
plt.show()

## Duplicados

import pandas as pd

def contar_duplicados(df):
    """
    Cuenta la cantidad de registros duplicados en un DataFrame.
    Parámetros:
    -----------
    df : pandas.DataFrame
    Retorna:
    --------
    int
        Número de filas duplicadas.
    """
    return df.duplicated().sum()

contar_duplicados(data)
# Tratamiento de Datos Capa Plata

## Eliminación de Duplicados

data_silver = data.drop_duplicates(subset=None,
                               keep='first',
                               inplace=False
)
data_silver.head(10)
contar_duplicados(data_silver)

# Almacenamiento de Capa Plata

data_silver.to_csv('data/iris_silver.csv', index=False)
