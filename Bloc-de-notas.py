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
#-------------------------------CÓDIGO DE VENTANA PRINCIPAL-------------------------------#
class Ventana_principal(QMainWindow):                 #Heredar desde la función QMainWindow
  
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
    #------------------------------------------------------------------------------------------#

    #---FUNCIÓN DE LOS widgets.SE AGREGA (self) indicando que pertenece a la ventana
    def componentes(self):

        #COMPONENTES: BOTONES------------------------------------------------------------------#
        self.boton_nuevo=QPushButton(" Nuevo")                          #CREAR BOTÓN DE NUEVO ARCHIVO
        self.boton_nuevo.setEnabled(False)                       #DESACTIVAR COMO ESTADO INICIAL
        #                                                                                      #
        self.boton_guardar=QPushButton(" Guardar")                    #CREAR BOTÓN DE GUARDAR ARCHIVO
        self.boton_guardar.setEnabled(False)                     #DESACTIVAR COMO ESTADO INICIAL
        #                                                                                      #
        boton_abrir=QPushButton(" Abrir")                          #CREAR BOTÓN DE ABRIR ARCHIVO
        #--------------------------------------------------------------------------------------#

        #COMPONENTES: CUADRO DE TEXTO PRINCIPAL------------------------------------------------#
        self.texto=QTextEdit()                                      #CREAR CUADRO DE TEXTO
        #--------------------------------------------------------------------------------------#

        #COMPONENTES: ETIQUETA PARA EL CONTADOR DE CARACTERES----------------#
        etiqueta_num_caracteres=QLabel("N° de caracteres: ")#CREAR ETIQUETA QUE AGREGA INFORMACIÓN DEL N° DE CARACTERES
        self.etiqueta_contador=QLabel("0")  #CREAR ETIQUETA QUE CUENTA EL N° DE CARACTERES INGRESADOS POR EL USUARIO. (El valor 0 cambiará por otro valor a medida que el usuario ingrese nuevos caracteres)
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
