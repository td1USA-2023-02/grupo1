import geopandas as gpd
import matplotlib.pyplot as plt
from cenpy import products
from tobler.util import h3fy
import contextily as ctx

acs = products.ACS(2018)
filtro = acs.filter_tables('VALUE', by='description')
print(filtro)

dc = acs.from_msa('Washington-Arlington', variables=['B25077_001E'])
print(dc.head())

dc_hex_large = h3fy(dc, resolution=5, clip=True)
dc_hex_small = h3fy(dc, resolution=7, clip=True)

fig, ax = plt.subplots(figsize=(10, 10))
fig, axs = plt.subplots(1, 2, figsize=(18, 10))

dc_hex_large.plot(ax=axs[0], alpha=0.4, linewidth=1.6, edgecolor='white')
dc_hex_small.plot(ax=axs[1], alpha=0.4, linewidth=1.6, edgecolor='white')

for ax in axs:
    ctx.add_basemap(ax=ax, source=ctx.providers.Stamen.TonerLite, zoom=2)  # Cambia el nivel de zoom aquí
    ax.axis('off')

plt.show()