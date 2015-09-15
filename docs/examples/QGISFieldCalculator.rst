QGIS Field Calculator
=====================

Using the QGIS Field Calculator this will output WKT format.

Output Field
------------

- **Name:** wkt

- **Type:** Text, unlimited length (text)

Function Editor
---------------

.. code-block:: python

    import geocoder

    @qgsfunction(group='Geocoder')
    def geocode(location, feature, parent):
        g = geocoder.google(location)
        return g.wkt

Expression
----------

Find the **geocode** expression in the **Geocoder** function list, the final result will look something like this:

.. code-block:: bash

    geocode("address")  

Once the wkt field is added, you can then save your document as a CSV format and in the **Layer Options** define the **GEOMETRY** = **AS_WKT**.