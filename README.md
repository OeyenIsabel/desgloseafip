# desgloseafip
Pasaje a Excel del txt con el detalle de las Facturas emitidas por Afip online

1- En sitio web de AFIP
a) Necesitamos loguearnos con clave fiscal, ingresar a "Comprobantes en línea" - "Consultas". 
b) Le cargaremos un filtro de fechas y el punto de venta. Con esto llegamos al famoso listado en que podríamos ir descargando y chequeando cada PDF.
c) En vez de eso, debajo de todo, haremos clic en el botón "Exportar duplicados electrónicos (todos).". Nos descarga un .rar que contiene dos archivos, extraeremos y guardaremos el que se llama "Detalle.txt" en la misma carpeta donde esta el notebook.

Este archivo está formado por tantas líneas como facturas, y cada línea es como esta:
11 2020080100010000095300000953000000100000070000000003400000000000000000000000000000000000000000000034000000000 Freno Trasero Sh 315

2- En Jupyter:
Simplemente corremos el código.
Nos informa en las líneas el importe total del período, y nos exporta un excel con las ventas desglosadas por línea.
