from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4, letter,landscape
from MySQLdb import _mysql

#############DB################
db=_mysql.connect("localhost","root","r2d23poLui$","personal")
db.query("SELECT nombre FROM actividad where id <3 ")
r=db.store_result()

#################################

# from import psycopg2
#Instalar
#pip install psycopg2
#pip install pygresql
#

# conexion = psycopg2.connect("dbname=empleados user=neoguias password=pimientos44")


# c = canvas.Canvas("PrimerosPuestosPorEspecialidad.pdf",A4)
# w,h = A4
c = canvas.Canvas("PrimerosPuestosPorEspecialidad.pdf",landscape(A4))
w,h = landscape(A4)
x=0
y=h-45

c.drawImage("img/logo-uni.jpg", 10, h-80 ,width=35,height=50)

titulo_uni = c.beginText(50, h - 40)
titulo_uni.setFont(psfontname="Helvetica-Bold",size=10)
titulo_uni.textLine("UNIVERSIDAD NACIONAL DE INGENIERIA")
titulo_uni.textLine("OFICINA CENTRAL DE ADMISION")
c.drawText(titulo_uni)
titulo_uni.setFont(psfontname="Helvetica",size=10)
titulo_uni.textLine("INGRESO ESCOLAR NACIONAL")
titulo_uni.textLine("TALENTO BECA 18")
c.drawText(titulo_uni)
#
#PRIMEROS PUESTOS POR ESPECIALIDAD INGRESO ESCOLAR NACIONAL 2017-1
titulo_reporte = c.beginText(100, h - 100)
titulo_reporte.setFont(psfontname="Helvetica-Bold",size=10)
titulo_reporte.setFillColorRGB(255,0,0)
titulo_reporte.textLine("PRIMEROS PUESTOS POR ESPECIALIDAD INGRESO ESCOLAR NACIONAL")
c.drawText(titulo_reporte)
#
c.line(x+40, y - 70, w - 30, y - 70)
cabecera = [("N°","NOMBRES","SEXO",
"ESPECIALIDAD","DEPARTAMENTO",
"PROVINCIA","DISTRITO","COLEGIO",
"GESTION","NOTA")]

#
indice = c.beginText(x + 60, h - 130)
indice.setFillColorRGB(0,0,0)
indice.setFont(psfontname="Helvetica-Bold",size=10)
indice.textLine("N°")
c.drawText(indice)
#
nombre = c.beginText(x+80, h - 130)
nombre.setFont(psfontname="Helvetica-Bold",size=10)
nombre.textLine("NOMBRES")
c.drawText(nombre)
#
c.line(x+40, y - 90, w - 30, y - 90)
incremento = 20
#
print (type(r))
# registro = r.fetchone()
# while (registro != None):
#     print registro['nombre']
 
indice = c.beginText(x + 60, h - 130 - incremento)
indice.setFillColorRGB(0,0,0)
indice.setFont(psfontname="Helvetica",size=10)
indice.textLine("1")
c.drawText(indice)
#
nombre = c.beginText(x+80, h - 130  - incremento)
nombre.setFont(psfontname="Helvetica",size=10)
nombre.textLine("Luis Fernando Mayta Campos")
c.drawText(nombre)






c.showPage()
c.save()


