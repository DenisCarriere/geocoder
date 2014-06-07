from osgeo import ogr

path = 'shapefiles/US State - Tiger/states.shp'
driver = ogr.GetDriverByName("ESRI Shapefile")
dataSource = driver.Open(path, 0)
layer = dataSource.GetLayer()

for item in layer:
    geom = item.geometry()
    name = item.GetField("NAME")
    print name, geom
    break