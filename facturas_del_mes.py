#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import re
file = open(r'DETALLE.txt',mode='r')
data = file.read()
file.close()

def split_text(data):
  ##  Generamos una linea por cada salto de linea que equivale a una línea de factura.
    return data.splitlines()

linesText = split_text(data)

#busco la fecha con regex y hago una lista con todas las fechas
def fecha(linesText):
    fecha = []
  # RegExp to extract Time information
    timeRegex = re.compile("\d+\s(\d{8})\d+")
    for index, line in enumerate(linesText):
        matches = re.findall(timeRegex, line)
        if(len(matches) > 0):
            fecha.append(matches[0])
        else:
            fecha.append(None)
    return fecha


#busco el punto de venta
def ptoventa(linesText):
    ptoventa = []
  # RegExp to extract Time information
    puntoRegex = re.compile("\d+\s\d{8}(\d{4})\d+")
    for index, line in enumerate(linesText):
        matches = re.findall(puntoRegex, line)
        if(len(matches) > 0):
            ptoventa.append(matches[0])
        else:
            ptoventa.append(None)
    return ptoventa


#busco el nro de la factura con 00s sobrantes para que no deje de andar si se emiten muchas
def nrofc(linesText):
    nrofc = []
    fcRegex = re.compile("\d+\s\d{12}(\d{8})\d+")
    for index, line in enumerate(linesText):
        matches = re.findall(fcRegex, line)
        if(len(matches) > 0):
            nrofc.append(matches[0])
        else:
            nrofc.append(None)
    return nrofc


#busco la cantidad vendida
def cantfc(linesText):
    cantfc = []
    cantRegex = re.compile("\d+\s\d{30}(\d{5})\d+")
    for index, line in enumerate(linesText):
        matches = re.findall(cantRegex, line)
        if(len(matches) > 0):
            cantfc.append(matches[0])
        else:
            cantfc.append(None)
    return cantfc


#busco el precio unitario
def punit(linesText):
    punit = []

  # RegExp to extract Time information
    punitRegex = re.compile("\d+\s\d{47}(\d{8})\d+")
    centRegex = re.compile("\d+\s\d{55}(\d{2})\d+")
    for index, line in enumerate(linesText):
        matches = re.findall(punitRegex, line)
        matches2 = re.findall(centRegex, line)
        valor = matches+matches2
        if(len(matches) > 0):
            punit.append('.'.join(valor))
        else:
            punit.append(None)
    return punit


#busco el precio total
def precio_total(linesText):
    precio_total = []

  # RegExp to extract Time information
    ptotalRegex = re.compile("\d+\s\d{94}(\d{8})\d+")
    centRegex = re.compile("\d+\s\d{82}(\d{2})\d+")
    for index, line in enumerate(linesText):
        matches = re.findall(ptotalRegex, line)
        matches2 = re.findall(centRegex, line)
        valor = matches+matches2
        if(len(matches) > 0):
            precio_total.append('.'.join(valor))
        else:
            precio_total.append(None)
    return precio_total


#busco la descripción 
def producto(linesText):
    producto = []

  # RegExp to extract Time information
    productoRegex = re.compile("\d+\s\d+\s(\D*)")
    for index, line in enumerate(linesText):
        matches = re.findall(productoRegex, line)

        if(len(matches) > 0):
            producto.append(matches[0])
        else:
            producto.append(None)
    return producto


#guardo los valores obtenidos en cada función
fecha = fecha(linesText)
ptoventa = ptoventa(linesText)
nrofc = nrofc(linesText)
cantfc = cantfc(linesText)
punit = punit(linesText)
precio_total = precio_total(linesText)
producto = producto(linesText)


#chequeo por consola que todas tengan el mismo largo
print("total líneas: ",len(linesText))
print("total fechas: ",len(fecha))
print("total puntos venta: ",len(ptoventa))
print("total nros fc: ",len(nrofc))
print("total cant facturada: ",len(cantfc))
print("total precios unitarios: ",len(punit))
print("total precios totales: ",len(precio_total))
print("total descr producto: ",len(producto))


#armo una lista de listas con cada columna de datos extraidos
zipped = list(zip(fecha, ptoventa, nrofc, cantfc, punit, precio_total, producto))

#armo dataframe, y reseteo el index
df = pd.DataFrame(zipped, columns = ['Fecha' , 'Punto Venta','Nro Fc', 'Cantidad', "Precio unitario", "Precio total", "Producto"])

#configurando el tipo correcto de cada columna
df['Fecha'] = pd.to_datetime(df['Fecha'], format='%Y%m%d', errors='ignore')
df['Cantidad'] = df['Cantidad'].astype(int)
df['Precio unitario'] = df['Precio unitario'].astype(float)
df['Precio total'] = df['Precio total'].astype(float)

#descargo un excel para chequear y poder hacer la declaración
df.to_excel("detalle_facturas.xls", index=False, sheet_name="Listado")

#chequeo el total por consola
print("El total facturado en el período es ",df['Precio total'].sum())
