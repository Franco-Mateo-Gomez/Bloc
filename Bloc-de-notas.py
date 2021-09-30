#
#                             INTERFAZ GRÁFICA: BLOC DE NOTAS
#                          Desarrollado por: Franco Mateo Gomez
#                                                                                               
#--LIBRERÍAS--#
from PyQt5.QtGui import QFont, QFontMetrics
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import *#Importar desde la librería Pyqt5 -> Todos los componentes de la ventana
from PyQt5.QtGui import QIcon
import sys
import os
#------------#

#------------------------------------------FUNCIONES-------------------------------------------#
#-------FUNCIÓN: RUTA DE GUARDADO DE ARCHIVOS
def funcion_guardar_archivo(self):
    texto_a_guardar=self.texto.toPlainText()#GUARDAR EL CONTENIDO DEL CAMPO DE TEXTO EN UNA var.

    directorio_a_guardar=QFileDialog.getSaveFileName(self,"Guardar archivo","C:/","*.txt")
    # MOSTRAR AL USUARIO UNA VENTANA DONDE PODRÁ ELEGIR LA RUTA DE DESTINO (Por defecto se mostrará a partir de la raiz del SO y utilizará la extensión .txt)
    #Tomar en cuenta: la var.(directorio_a_guardar) es una tupla. La posición relevante es [0]
    
    if(os.path.exists(directorio_a_guardar[0])!=True):# SI LA RUTA DE DESTINO NO EXISTE
        guardar_archivo=open(directorio_a_guardar[0],"w")#CREAR UN ARCHIVO DE ESCRITURA CON LA RUTA
        guardar_archivo.write(texto_a_guardar)#AGREGAR EL CONTENIDO DEL CAMPO DE TEXTO AL ARCHIVO
        guardar_archivo.close()               #CERRAR EL ARCHIVO
    #---                                                                                    ---#
    else:                                             # SI LA RUTA DE DESTINO YA EXISTE
        guardar_archivo=open(directorio_a_guardar[0],"a")#CREAR UN ARCHIVO QUE AGREGUE NUEVA INFORMACIÓN EN LA RUTA ESPECIFICADA (esto quiere decir que no se eliminará el contenido guardado anteriormente)
        guardar_archivo.write(texto_a_guardar)#AGREGAR EL CONTENIDO DEL CAMPO DE TEXTO AL ARCHIVO
        guardar_archivo.close()               #CERRAR EL ARCHIVO
#--------------------------------------------

#-------FUNCIÓN: RUTA DE APERTURA DE ARCHIVOS
def funcion_abrir_archivo(self):
    seleccionar_archivo,_=QFileDialog.getOpenFileName(self,"Abrir archivo","C:/","*.txt")
    # MOSTRAR AL USUARIO UNA VENTANA DONDE PODRÁ ELEGIR LA RUTA DONDE SE ALOJA EL ARCHIVO DESEADO (Por defecto se mostrará a partir de la raiz del SO y utilizará la extensión .txt)
    #Tomar en cuenta: la var.(seleccionar_archivo) es una tupla. La posición relevante es [0]

    if (seleccionar_archivo):                           #SI SE SELECCIONA UNA RUTA
            abrir_archivo=open(seleccionar_archivo,"r")#CREAR UN ARCHIVO DE LECTURA CON LA RUTA
            contenido=abrir_archivo.read()              #LEER EL CONTENIDO DEL ARCHIVO
            self.texto.setText(contenido)               #AGREGARLO EN EL CAMPO DE TEXTO
            abrir_archivo.close()                       #CERRAR EL ARCHIVO
#--------------------------------------------

#------FUNCIÓN: MENSAJE DE ADVERTENCIA POR CONTENIDO DE ARCHIVOS (botón NUEVO)
def funcion_nuevo_advertencia_hay_contenido(self):
    #____________________________MENSAJE DE ADVERTENCIA________________________________#
    mensaje_existente=QMessageBox()                 #CUADRO DE DIÁLOGO
    mensaje_existente.setIcon(QMessageBox.Warning)  #ESTABLECER UN ÍCONO DE ADVERTENCIA
    mensaje_existente.setWindowIcon(QIcon(str("Images/icon.png")))#AGREGAR ÍCONO
    
    mensaje_existente.setWindowTitle("Nuevo")       #PONER TÍTULO DE VENTANA AL CUADRO
    mensaje_existente.setText("Hay contenido en el campo")#INDICAR UN MENSAJE
    mensaje_existente.setInformativeText("¿Guardar archivo?")#INFORMAR AL USUARIO QUE ACCIÓN DESEA REALIZAR

    mensaje_existente.setStandardButtons(QMessageBox.Ok | QMessageBox.No)#ESTABLECER BOTONES AL CUADRO DE DIÁLOGO (OK,NO)
    mensaje_existente.setDefaultButton(QMessageBox.Ok)  #AGREGAR POR DEFECTO EL BOTÓN.ok

    salida_mensaje=mensaje_existente.exec_()            #EJECUTA LA VENTANA
    #__________________________________________________________________________________#
    #--CONDICIONALES EN CASO DE PULSACIÓN DE BOTONES--#
    if (salida_mensaje==QMessageBox.Ok):    #SI EL BOTÓN ES (si)
        funcion_guardar_archivo(self)       #LLAMAR A LA FUNCIÓN QUE GUARDA EL ARCHIVO
        self.texto.clear()                  #VACIAR EL CONTENIDO DEL CAMPO DE TEXTO

    elif (salida_mensaje==QMessageBox.No):  #SI EL BOTÓN ES (no)
        self.texto.clear()                  #VACIAR EL CONTENIDO DEL CAMPO DE TEXTO
#--------------------------------------------
        
#------FUNCIÓN: MENSAJE DE ADVERTENCIA POR CONTENIDO DE ARCHIVOS (botón ABRIR)
def funcion_abrir_advertencia_hay_contenido(self):
    #____________________________MENSAJE DE ADVERTENCIA________________________________#
    mensaje_existente=QMessageBox()                 #CUADRO DE DIÁLOGO
    mensaje_existente.setIcon(QMessageBox.Warning)  #ESTABLECER UN ÍCONO DE ADVERTENCIA
    mensaje_existente.setWindowIcon(QIcon(str("Images/icon.png")))#AGREGAR ÍCONO
    
    mensaje_existente.setWindowTitle("Abrir")       #PONER TÍTULO DE VENTANA AL CUADRO
    mensaje_existente.setText("Hay contenido en el campo")#INDICAR UN MENSAJE
    mensaje_existente.setInformativeText("¿Guardar archivo de todas formas?")#INFORMAR AL USUARIO QUE ACCIÓN DESEA REALIZAR

    mensaje_existente.setStandardButtons(QMessageBox.Ok | QMessageBox.No)#ESTABLECER BOTONES AL CUADRO DE DIÁLOGO (OK,NO)
    mensaje_existente.setDefaultButton(QMessageBox.Ok)  #AGREGAR POR DEFECTO EL BOTÓN.ok

    salida_mensaje=mensaje_existente.exec_()            #EJECUTA LA VENTANA
    #__________________________________________________________________________________#
    #--CONDICIONALES EN CASO DE PULSACIÓN DE BOTONES--#
    if (salida_mensaje==QMessageBox.Ok):    #SI EL BOTÓN ES (si)
        funcion_guardar_archivo(self)       #LLAMAR A LA FUNCIÓN QUE GUARDA EL ARCHIVO
        funcion_abrir_archivo(self)         #LUEGO LLAMAR A LA FUNCIÓN QUE ABRE EL ARCHIVO
    else:
        self.texto.clear()                  #SINO
        funcion_abrir_archivo(self)         #LLAMAR A LA FUNCIÓN QUE ABRE EL ARCHIVO
#--------------------------------------------
#----------------------------------------------------------------------------------------------#

#-------------------------------CÓDIGO DE VENTANA PRINCIPAL-------------------------------#
class Ventana_principal(QMainWindow):                 #Heredar desde la función QMainWindow
  
#____________________EVENTOS DE BOTONES____________________#
    #--EN CASO DE ELEGIR: NUEVO
    def click_nuevo(self,e):
        texto_ingresado=self.texto.toPlainText()         #TOMAR EL CONTENIDO DEL CAMPO DE TEXTO

        if (texto_ingresado !=""):                      #SI EL CONTENIDO NO ESTÁ VACÍO
            funcion_nuevo_advertencia_hay_contenido(self)   #LLAMAR A LA FUNCIÓN DE ADVERTENCIA PORQUE HAY CONTENIDO EN EL CAMPO DE TEXTO        
    #--------------------------        

    #--EN CASO DE ELEGIR: GUARDAR
    def click_guardar(self,e):
        funcion_guardar_archivo(self)               #LLAMAR A LA FUNCIÓN QUE GUARDA EL ARCHIVO
    #-------------------------- 
    
    #--EN CASO DE ELEGIR: ABRIR
    def click_abrir(self,e):
        campo_de_texto=self.texto.toPlainText()     #TOMAR EL CONTENIDO DEL CAMPO DE TEXTO

        if (campo_de_texto==""):                    #SI EL CONTENIDO ESTÁ VACÍO
            funcion_abrir_archivo(self)             #LLAMAR A LA FUNCIÓN QUE ABRE EL ARCHIVO

        else:                                       #SI EL CONTENIDO NO ESTÁ VACÍO
            funcion_abrir_advertencia_hay_contenido(self)   #LLAMAR A LA FUNCIÓN DE ADVERTENCIA PORQUE HAY CONTENIDO EN EL CAMPO DE TEXTO        
    #--------------------------
    #___________________________________________________________#

    #__________EVENTO QUE DETECTA CONTENIDO VACÍO EN EL CAMPO DE TEXTO__________#
    #Nos aseguramos de que el usuario no pueda guardar ni crear nuevos archivos vacíos porque sino no tendría sentido#
    def texto_vacio(self):
        contenido=self.texto.toPlainText()  #GUARDAR EL CONTENIDO DEL CAMPO DE TEXTO EN UNA var.

        if (contenido==""):            #CONDICIONAL: EN CASO DE QUE NO EXISTAN CARACTERES DENTRO
            self.boton_nuevo.setEnabled(False)      #DESHABILITAR BOTÓN(nuevo)
            self.boton_guardar.setEnabled(False)    #DESHABILITAR BOTÓN(guardar)

        else:                           #CONDICIONAL: CUANDO SE DETECTA CONTENIDO
            self.boton_nuevo.setEnabled(True)       #HABILITAR BOTÓN(nuevo)
            self.boton_guardar.setEnabled(True)     #HABILITAR BOTÓN(guardar)
    #___________________________________________________________________________#

    #_______EVENTO QUE CUENTA EL N° DE CARACTERES QUE INGRESA EL USUARIO________#
    def cuenta_caracteres(self):
        contenido=self.texto.toPlainText()  #GUARDAR EL CONTENIDO DEL CAMPO DE TEXTO EN UNA var.
        contenido_sin_espacios=contenido.split()#CONVERTIR EL TEXTO INGRESADO EN UNA LISTA QUE CONTIENE PALABRAS SIN CONTAR LOS ESPACIOS " "

        contador_caracteres=0               #var. ENCARGADA DE CONTAR EL N° DE CARACTERES
        palabras_recolectadas=""                          #var. ACUMULADOR DE PALABRAS RECORRIDAS

        for indice in contenido_sin_espacios:       #BUCLE: RECORRE CADA PALABRA DE LA LISTA
            palabras_recolectadas = palabras_recolectadas+indice  #POR CADA VUELTA, CONCATENAR TODAS LAS PALABRAS RECORRIDAS   
            contador_caracteres=len(palabras_recolectadas)      #GUARDAR LA LONGITUD DE LAS PALABRAS CONCATENADAS EN EL contador_caracteres.

        #EL BUCLE SE REPETIRÁ HASTA QUE EL USUARIO DEJE DE INGRESAR NUEVOS DATOS AL CAMPO DE TEXTO

        num_char=contador_caracteres                   #var. GUARDA EL TOTAL DE N° DE CARACTERES
        self.etiqueta_contador.setText(str(num_char))  #AGREGAR EL TOTAL EN LA ETIQUETA contador
    #___________________________________________________________________________#        

    #__________EVENTO: EN CASO DE CIERRE DE LA VENTANA PRINCIPAL__________#
    def closeEvent(self, e):
            campo_de_texto=self.texto.toPlainText()     #TOMAR EL CONTENIDO DEL CAMPO DE TEXTO

            if (campo_de_texto!=""):                 #CONDICIONAL: SI EL CONTENIDO NO ESTÁ VACÍO
                #_________________________MENSAJE DE ADVERTENCIA_______________________________#
                salida_programa=QMessageBox.question(self, "Ventana de cierre", "Hay contenido \n ¿Estás seguro de abandonar?",QMessageBox.Ok | QMessageBox.No | QMessageBox.Save)
                #______________________________________________________________________________#
                #--CONDICIONALES EN CASO DE PULSACIÓN DE BOTONES--#
                if salida_programa == QMessageBox.Ok:       #SI EL BOTÓN ES (si)           
                    e.accept()                              #CERRAR EL PROGRAMA

                elif salida_programa == QMessageBox.Save:   #SI EL BOTÓN ES (guardar/save)
                    funcion_guardar_archivo(self)     #LLAMAR A LA FUNCIÓN QUE GUARDA EL ARCHIVO
                    e.accept()                              #CERRAR EL PROGRAMA

                else:                                       #SI EL BOTÓN ES (no)
                    e.ignore()                              #CERRAR ADVERTENCIA

            else:                                    # SI EL CONTENIDO ESTÁ VACÍO
                e.accept()                           # CERRAR EL PROGRAMA
    #_____________________________________________________________________#

    #------------------------------FUNCIÓN: VENTANA PRINCIPAL----------------------------------#
    def __init__(self):
        super().__init__()
        #---CONTENIDO DE LA VENTANA QUE TAMBIÉN APLICA A LOS DEMÁS ELEMENTOS QUE LA COMPONEN---#
        self.titulo="Bloc de notas"                                 #var.TÍTULO
        self.setGeometry(0,0,600,500)                               #POSICIÓN Y TAMAÑO
        #---------CENTRADO DE VENTANA PRINCIPAL------------#
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #--------------------------------------------------#
        self.setWindowTitle(self.titulo)                       #INSERTAR EL TÍTULO (var:titulo)
        self.componentes()                     #LLAMAR A LA FUNCIÓN DE LOS COMPONENTES (widgets)
        self.setStyleSheet("background-color:rgb(200,176,130)")        #COLOR DE FONDO
        self.setWindowIcon(QIcon(str("icono.png")))                  #INSERTAR ÍCONO
    #------------------------------------------------------------------------------------------#

    #---FUNCIÓN DE LOS widgets.SE AGREGA (self) indicando que pertenece a la ventana
    def componentes(self):

        #COMPONENTES: BOTONES------------------------------------------------------------------#
        self.boton_nuevo=QPushButton(" Nuevo")                     #CREAR BOTÓN DE NUEVO ARCHIVO
        self.boton_nuevo.setEnabled(False)                       #DESACTIVAR COMO ESTADO INICIAL
        self.boton_nuevo.clicked.connect(self.click_nuevo)      #AGREGAR A LA FUNCIÓN DE EVENTOS
        #                             *-_ESTILOS_-*                                                 #
        self.boton_nuevo.setToolTip("Nuevo archivo")           #DESCRIPCIÓN CUANDO SE ACERCA AL BOTÓN
        self.boton_nuevo.setIcon(QIcon("nuevo.png"))                       #AGREGAR ÍCONO
        self.boton_nuevo.setStyleSheet("background-color:rgb(188,70,34)")#COLOR DE FONDO
        self.boton_nuevo.setFont(QFont("Linux Biolinum G",12))   #AGREGAR FUENTE Y TAMAÑO
        #                                                                                      #
        self.boton_guardar=QPushButton(" Guardar")               #CREAR BOTÓN DE GUARDAR ARCHIVO
        self.boton_guardar.setEnabled(False)                     #DESACTIVAR COMO ESTADO INICIAL
        self.boton_guardar.clicked.connect(self.click_guardar)   #AGREGAR A LA FUNCIÓN DE EVENTOS
        #                             *-_ESTILOS_-*                                                 #
        self.boton_guardar.setToolTip("Guardar archivo")       #DESCRIPCIÓN CUANDO SE ACERCA AL BOTÓN
        self.boton_guardar.setIcon(QIcon("guardar.png"))                    #AGREGAR ÍCONO
        self.boton_guardar.setStyleSheet("background-color:rgb(188,70,34)")#COLOR DE FONDO
        self.boton_guardar.setFont(QFont("Linux Biolinum G",12)) #AGREGAR FUENTE Y TAMAÑO 
        #                                                                                      #
        boton_abrir=QPushButton(" Abrir")                          #CREAR BOTÓN DE ABRIR ARCHIVO
        boton_abrir.clicked.connect(self.click_abrir)           #AGREGAR A LA FUNCIÓN DE EVENTOS
        #                             *-_ESTILOS_-*                                                 #
        boton_abrir.setIcon(QIcon("abrir.png"))           #DESCRIPCIÓN CUANDO SE ACERCA AL BOTÓN
        boton_abrir.setToolTip("Abrir archivo existente")            #AGREGAR ÍCONO
        boton_abrir.setStyleSheet("background-color:rgb(188,70,34)")#COLOR DE FONDO
        boton_abrir.setFont(QFont("Linux Biolinum G",12))       #AGREGAR FUENTE Y TAMAÑO
        #--------------------------------------------------------------------------------------#

        #COMPONENTES: CUADRO DE TEXTO PRINCIPAL------------------------------------------------#
        self.texto=QTextEdit()                                      #CREAR CUADRO DE TEXTO
        self.texto.textChanged.connect(self.texto_vacio)   #CONECTAR CON EL EVENTO DE TEXTO VACÍO
        self.texto.textChanged.connect(self.cuenta_caracteres)#CONECTAR CON EL EVENTO ENCARGADO DE CONTAR EL N° DE CARACTERES
        #                             *-_ESTILOS_-*                                                 #
        self.texto.setStyleSheet("background-image:url(fondo.jpg)")         #COLOR DE FONDO
        self.texto.setFont(QFont("Book Antiqua",12))                #AGREGAR FUENTE Y TAMAÑO
        #--------------------------------------------------------------------------------------#

        #COMPONENTES: ETIQUETA PARA EL CONTADOR DE CARACTERES----------------#
        etiqueta_num_caracteres=QLabel("N° de caracteres: ")#CREAR ETIQUETA QUE AGREGA INFORMACIÓN DEL N° DE CARACTERES
        self.etiqueta_contador=QLabel("0")  #CREAR ETIQUETA QUE CUENTA EL N° DE CARACTERES INGRESADOS POR EL USUARIO. (El valor 0 cambiará por otro valor a medida que el usuario ingrese nuevos caracteres)
        #                             *-_ESTILOS_-*                                                 #
        etiqueta_num_caracteres.setFont(QFont("Linux Biolinum G",12))   #AGREGAR FUENTE Y TAMAÑO
        self.etiqueta_contador.setFont(QFont("Linux Biolinum G",12))    #AGREGAR FUENTE Y TAMAÑO
        #--------------------------------------------------------------------------------------#
    
        #---------------------------------CONTENEDORES-----------------------------------------#
        contenedor_principal=QVBoxLayout()  #CREACIÓN DE CONTENEDOR PRINCIPAL. Se agregarán los demás contenedores dentro
        
        #--------------------------------------------CONTENEDOR VERTICAL PARA EL CUADRO DE TEXTO
        contenedor_panel_txt=QVBoxLayout()
        contenedor_panel_txt.addWidget(self.texto)    #_AGREGAR EL CUADRO DE TEXTO AL CONTENEDOR

        #-------------------------------------------------CONTENEDOR HORIZONTAL PARA LOS BOTONES
        contenedor_botones_H=QHBoxLayout()         
        contenedor_botones_H.addWidget(self.boton_nuevo)   #_AGREGAR EL BOTÓN NUEVO AL CONTENEDOR
        contenedor_botones_H.addWidget(self.boton_guardar) #_AGREGAR EL BOTÓN GUARDAR AL CONTENEDOR
        contenedor_botones_H.addWidget(boton_abrir)   #_AGREGAR EL BOTÓN ABRIR AL CONTENEDOR

        #----------------------CONTENEDOR HORIZONTAL PARA LOS WIDGETS QUE CUENTAN LOS CARACTERES
        contenedor_contadorChar=QHBoxLayout()
        contenedor_contadorChar.addWidget(etiqueta_num_caracteres)  #_AGREGAR LA ETIQUETA DE INFORMACIÓN DEL N° DE CARACTERES
        contenedor_contadorChar.addWidget(self.etiqueta_contador)   #_AGREGAR LA ETIQUETA QUE CUENTA EL N° DE CARACTERES
                                                                                           
        #------AÑADIR LOS CONTENEDORES AL PRINCIPAL------------#
        contenedor_principal.addLayout(contenedor_botones_H)    #PRIMERO AGREGAR EL CONTENEDOR DE LOS BOTONES
        contenedor_principal.addLayout(contenedor_panel_txt)    #SEGUNDO AGREGAR EL CONTENEDOR DEL PANEL DE TEXTO
        contenedor_principal.addLayout(contenedor_contadorChar) #POR ÚLTIMO SE AGREGA EL CONTENEDOR DEL CONTADOR DE CARACTERES
        #------------------------------------------------------#

        #----------WIDGET PRINCIPAL----------#
        widget_principal=QWidget()                           #CREACIÓN DEL WIDGET PRINCIPAL
        widget_principal.setLayout(contenedor_principal)     #AGREGAR EL CONTENEDOR PRINCIPAL
        self.setCentralWidget(widget_principal)
        #------------------------------------#

    #------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------#

#--FUNCIÓN PRINCIPAL--#
programa=QApplication(sys.argv)
ventana=Ventana_principal()
ventana.show()
programa.exec()
#---------------------#
