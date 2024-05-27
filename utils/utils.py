import cartopy.feature as cfeature

def add_basemap(ax, extent=[-180, 180, -90, 90]):
    ax.set_extent(extent)
    ax.add_feature(cfeature.LAND, facecolor='WhiteSmoke')
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE, edgecolor='Black', linewidth=0.3)
    gridl = ax.gridlines(draw_labels=True, linewidth=0.)


