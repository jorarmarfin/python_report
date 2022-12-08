from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4, letter,landscape
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
sexo = c.beginText(x+220, h - 130)
sexo.setFont(psfontname="Helvetica-Bold",size=10)
sexo.textLine("SEXO")
c.drawText(sexo)
#
especialidad = c.beginText(x+270, h - 130)
especialidad.setFont(psfontname="Helvetica-Bold",size=10)
especialidad.textLine("ESPECIALIDAD")
c.drawText(especialidad)
#
departamento = c.beginText(x+370, h - 130)
departamento.setFont(psfontname="Helvetica-Bold",size=10)
departamento.textLine("DEPARTAMENTO/PROVINCIA/DISTRITO")
c.drawText(departamento)
#
departamento = c.beginText(x+580, h - 130)
departamento.setFont(psfontname="Helvetica-Bold",size=10)
departamento.textLine("COLEGIO")
c.drawText(departamento)
#
departamento = c.beginText(x+650, h - 130)
departamento.setFont(psfontname="Helvetica-Bold",size=10)
departamento.textLine("GESTION")
c.drawText(departamento)
#
departamento = c.beginText(x+730, h - 130)
departamento.setFont(psfontname="Helvetica-Bold",size=10)
departamento.textLine("NOTA")
c.drawText(departamento)
#
c.line(x+40, y - 90, w - 30, y - 90)
incremento = 20
#
#
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
#
sexo = c.beginText(x+220, h - 130  - incremento)
sexo.setFont(psfontname="Helvetica",size=10)
sexo.textLine("Masculino")
c.drawText(sexo)
#
especialidad = c.beginText(x+270, h - 130  - incremento)
especialidad.setFont(psfontname="Helvetica",size=10)
especialidad.textLine("Ing. Sistemas")
c.drawText(especialidad)
#
departamento = c.beginText(x+370, h - 130  - incremento)
departamento.setFont(psfontname="Helvetica",size=10)
departamento.textLine("Lima/Lima/San Juan de Lurigancho")
c.drawText(departamento)
#
departamento = c.beginText(x+580, h - 130  - incremento)
departamento.setFont(psfontname="Helvetica",size=9)
departamento.textLine("Santo Domingo de Guzman")
c.drawText(departamento)
#
departamento = c.beginText(x+650, h - 130  - incremento)
departamento.setFont(psfontname="Helvetica",size=10)
departamento.textLine("Privada")
c.drawText(departamento)
#
departamento = c.beginText(x+730, h - 130  - incremento)
departamento.setFont(psfontname="Helvetica",size=10)
departamento.textLine("18.23")
c.drawText(departamento)
#





c.showPage()
c.save()


