# Reporte de Análisis de Datos - Pandas

`Christian Garcia Machine Learning, NC 0068`

## 1. DataFrame Convertido
```text
                      Teatro  ...  Funciones_mes
0               Metropolitan  ...             25
1                    Lunario  ...             20
2  Teatro de los Insurgentes  ...             18
3                    Hidalgo  ...             22
4             Esperanza Iris  ...             15
5               De la Ciudad  ...             12

[6 rows x 3 columns]
```

## 2.1 Primeras Filas (head)
```text
         Teatro  Capacidad  Funciones_mes
0  Metropolitan       3000             25
1       Lunario        900             20
```

## 2.2 Últimas Filas (tail)
```text
           Teatro  Capacidad  Funciones_mes
4  Esperanza Iris       1200             15
5    De la Ciudad        800             12
```

## 2.3 Dimensiones (Filas, Columnas)
```text
(6, 3)
```

## 2.4 Tipos de Datos por Columna
```text
Teatro             str
Capacidad        int64
Funciones_mes    int64
dtype: object
```

## 2.5 Información General (info)
```text
<class 'pandas.DataFrame'>
RangeIndex: 6 entries, 0 to 5
Data columns (total 3 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   Teatro         6 non-null      str  
 1   Capacidad      6 non-null      int64
 2   Funciones_mes  6 non-null      int64
dtypes: int64(2), str(1)
memory usage: 276.0 bytes

```

## 3. Estadísticas Generales de la Columna 'Capacidad'
```text
count       6.000000
mean     1650.000000
std       900.555384
min       800.000000
25%       975.000000
50%      1350.000000
75%      2250.000000
max      3000.000000
Name: Capacidad, dtype: float64
```

## 4. Ordenar Ascendente por Capacidad
```text
                      Teatro  ...  Funciones_mes
5               De la Ciudad  ...             12
1                    Lunario  ...             20
4             Esperanza Iris  ...             15
3                    Hidalgo  ...             22
2  Teatro de los Insurgentes  ...             18
0               Metropolitan  ...             25

[6 rows x 3 columns]
```

## 5. Ordenar Descendente por Funciones_mes
```text
                      Teatro  ...  Funciones_mes
0               Metropolitan  ...             25
3                    Hidalgo  ...             22
1                    Lunario  ...             20
2  Teatro de los Insurgentes  ...             18
4             Esperanza Iris  ...             15
5               De la Ciudad  ...             12

[6 rows x 3 columns]
```

`Christian Garcia Machine Learning, NC 0068`