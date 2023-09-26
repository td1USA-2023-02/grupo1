#1.Muestre de forma gráfica como se pueden diferenciar cada una de las especies de flores del dataset Iris.
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])

# Mostrar las primeras filas del dataframe
print(df.head())

# Obtener información general sobre el dataframe
print(df.info())
#Informacion de la variable target
print(df["target"].describe())

print(df["target"].unique())
# Resumen estadístico de las variables numéricas
print(df.describe())



# Verificar si hay valores nulos en el conjunto de datos
print(df.isnull().sum())

'''
sns.set_theme(style="ticks")

sns.scatterplot(data=df, x="sepal length (cm)", y="sepal width (cm)", hue="target")
plt.title("Diagrama de Dispersión Sépalo")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Ancho del Sépalo (cm)")
plt.show()

sns.countplot(data=df,x="target")
plt.xticks([0, 1, 2], iris.target_names)
plt.show()
'''

'''
sns.pairplot(data=df, hue="target")
plt.xticks([0, 1, 2], iris.target_names)
plt.show()

sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=df)
plt.xlabel('Longitud del Sépalo (cm)')
plt.ylabel('Ancho del Sépalo (cm)')
plt.title('Distribución de Sépalos por Especie')
plt.legend(title='Especie')
plt.show()
'''
	
#2.Utilizando la biblioteca NumPy, encuentra el valor de la mediana de la longitud del pétalo 
# de las flores de la especie 'setosa' en el conjunto de datos Iris. 
# Proporciona el valor numérico resultante. Asuma que el target es 3 para esa especie.


setosa_petal_length = iris.data[iris.target == 0, 2]

# Calcular la mediana de la longitud del pétalo
mediana_setosa_petal_length = np.median(setosa_petal_length)

# Imprimir el valor numérico resultante
print("Mediana de la longitud del pétalo para la especie 'setosa':", mediana_setosa_petal_length)










	
#3.Dentro del conjunto de datos Iris, ¿cuál es la diferencia promedio en la longitud del 
# sépalo entre las flores de las especies 'setosa' y 'versicolor'? Asuma que 
# Setosa es target=3 y Versicolor es target = 0.

#setosa=target 0

setosa_sepal_length = iris.data[iris.target == 0, 0]

# Obtener las longitudes del sépalo para la especie 'versicolor' (target = 1)
versicolor_sepal_length = iris.data[iris.target == 1, 0]

# Calcular la diferencia promedio en la longitud del sépalo entre estas dos especies
diferencia_promedio = np.mean(setosa_sepal_length) - np.mean(versicolor_sepal_length)

# Imprimir el valor numérico resultante
print("Diferencia promedio en la longitud del sépalo entre 'setosa' y 'versicolor':", diferencia_promedio)
	
	
	
#4.Realice 3 gráficas diferentes haciendo uso de seaborn y que no se hayan visto en clase.
#  Concluya sobre cada una de éstas.

##Diagramas ya realizados

# Histograma de las longitudes del sépalo para cada especie
sns.histplot(data=df, x="sepal length (cm)", hue="target", bins=20)
plt.title("Histograma de Longitud del Sépalo")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Frecuencia")
plt.show()

# Diagrama de dispersión de longitud del sépalo vs. ancho del sépalo
sns.scatterplot(data=df, x="sepal length (cm)", y="sepal width (cm)", hue="target")
plt.title("Diagrama de Dispersión Sépalo")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Ancho del Sépalo (cm)")
plt.show()

# Diagrama de caja de longitud del pétalo por especie
sns.boxplot(data=df, x="target", y="petal length (cm)")
plt.xticks([0, 1, 2], iris.target_names)
plt.title("Diagrama de Caja de Longitud del Pétalo por Especie")
plt.xlabel("Especie")
plt.ylabel("Longitud del Pétalo (cm)")
plt.show()

# Matriz de correlación
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()

#Countplot
sns.countplot(iris, x="target").set(title="Cantidad de flores por target")
plt.show()

