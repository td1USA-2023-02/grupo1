#Importar todas las librerias necesarias
import geopandas  as gpd
import matplotlib.pyplot as plt
import pandas
import libpysal
from tobler.util import h3fy
from tobler.area_weighted import area_interpolate
import contextily as ctx
from cenpy import products

acs = products.ACS(2017)


#Filtrar valores
filtro= acs.filter_tables('VALUE', by='description')
print(filtro.head())

#Variable buscada
dc = acs.from_msa('Washington-Arlington', variables=['B25077_001E'])
print("Empezaré el proceso")
print(dc.head())
print("terminé el proceso")

#Graficar


#Varios tamaños
dc_hex_large = h3fy(dc, resolution=5, clip=True)
dc_hex_small = h3fy(dc, resolution=7, clip=True)

fig, axs = plt.subplots(1,2, figsize=(18,10))

dc_hex_large.plot(ax=axs[0], alpha=0.4, linewidth=1.6, edgecolor='white')
dc_hex_small.plot(ax=axs[1], alpha=0.4, linewidth=1.6, edgecolor='white')

for ax in axs:
    ctx.add_basemap(ax=ax, source=ctx.providers.Stamen.TonerLite)
    ax.axis('off')
print("Voy a imprimir el grafico")
plt.show()
print("Grafico realizado")