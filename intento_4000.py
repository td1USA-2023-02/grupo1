import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
from tobler.util import h3fy
import contextily as ctx
from cenpy import products

# Cargar datos del producto ACS 2017
acs = products.ACS(2017)
acs.filter_tables('VALUE', by='description')
dc = acs.from_msa('Washington-Arlington', variables=['B25077_001E'])

# Visualización de los encabezados de la tabla
print("Encabezados de la tabla 'dc':")
print(dc.columns)

# Visualización de las primeras filas de la tabla
print("\nPrimeras filas de la tabla 'dc':")
print(dc.head())

# Convertir datos a hexágonos H3
dc_hex = h3fy(dc)

# Crear una figura y ejes para la visualización
fig, axs = plt.subplots(1, 2, figsize=(18, 10))
axs = axs.flatten()

# Graficar los datos originales en el primer eje
dc.plot(ax=axs[0], alpha=0.4, linewidth=1.6, edgecolor='white')
axs[0].set_title('Datos Originales')

# Graficar los datos en formato de hexágonos H3 en el segundo eje
dc_hex.plot(ax=axs[1], alpha=0.4, linewidth=1.6, edgecolor='white')
axs[1].set_title('Datos en Formato de Hexágonos H3')

# Agregar un mapa base a ambos ejes
for i in range(2):
    ctx.add_basemap(axs[i], source=ctx.providers.Stamen.TonerLite)
    axs[i].axis('off')

# Mostrar la visualización de gráficos
plt.show()
plt.savefig('mapa_final.jpg', dpi=300, bbox_inches='tight')