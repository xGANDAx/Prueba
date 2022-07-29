from openpyxl import load_workbook
import mysql.connector

wb = load_workbook(filename = "datos.xlsx")
ws = wb['Hoja1']

col_length = len(ws['A'])
row_length = len(ws['1'])
numero_personas = col_length-1

dataNames = []
for names in ws['1']:
    dataNames.append(names.value)


tData = {}
for persona in range(numero_personas):
    dataValues = []
    for datos in ws[str(persona+2)]:
        dataValues.append(datos.value)

    tData["persona"+str(persona)] = dict(zip(dataNames,dataValues))
    data = eval(tData["persona"+str(persona)]['Data'])
    del tData["persona"+str(persona)]['Data']
    tData["persona"+str(persona)].update(data)
 
try: 
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port="23306",
        database="punto2"
        )
    mycursor = mydb.cursor()

    sql = "INSERT INTO datos_xlxs (Cedula, Nombres, Direccion, latitude, longitude, city, description) VALUES (%s,%s,%s,%s,%s,%s,%s)"

    for persona in tData:
        val = tuple(tData[persona].values())
        #print(val)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Datos insertados.")

    mycursor.close()
    mydb.close()

except mysql.connector.errors.InterfaceError:
    print('No se pudo conectar con la base de datos')
    