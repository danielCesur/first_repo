import pandas as pd
import psycopg2
from psycopg2 import Error

pd.set_option('max_columns', None)
piezas = pd.read_excel("pieza.xlsx")


proveedores = pd.read_excel("Proveedor.xlsx")
dfproveedores = pd.DataFrame(piezas)
dfpiezas = pd.DataFrame(proveedores)
print(dfproveedores)
print(dfpiezas)

try:
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="fran")

    cursor = connection.cursor()
    record = 0
    for row in dfproveedores.index:
        codigo_proveedor = dfproveedores["codigo_proveedor"][row]
        codigo_pieza = dfproveedores["codigo_pieza"][row]
        cantidad = dfproveedores["cantidad"][row]
        fecha = dfproveedores["fecha"][row]
        insert_query = """INSERT INTO proveedores (codigo_proveedor, codigo_pieza, cantidad, fecha) VALUES (%s , %s, 
        %s, %s) """
        cursor.execute(insert_query, (codigo_proveedor, codigo_pieza, cantidad, fecha))
        record += 1

    connection.commit()
    print("Inserted successfully " + str(record) + " rows")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

try:
    connection = psycopg2.connect(user="postgres",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="fran")

    cursor = connection.cursor()
    record = 0
    for row in dfpiezas.index:
        codigo = dfpiezas["codigo"][row]
        nombre = dfpiezas["nombre"][row]
        color = dfpiezas["color"][row]
        precio = dfpiezas["precio"][row]
        codigo_categoria = dfpiezas["codigo_categoria"][row]
        insert_query = """INSERT INTO piezas (codigo, nombre, color, precio, codigo_categoria) VALUES (%s , %s, 
        %s, %s, %s) """
        cursor.execute(insert_query, (codigo, nombre, color, precio, codigo_categoria))
        record += 1

    connection.commit()
    print("Inserted successfully " + str(record) + " rows")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")