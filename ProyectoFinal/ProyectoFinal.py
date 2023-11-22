from colorama import Fore, Back, Style
from random import randint
from time import sleep,time

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class TextViewWindow(Gtk.Window):


    def __init__(self):
        Gtk.Window.__init__(self, title="Proyecto de Ordenar Listas")

        #Tamaño de la ventana
        self.set_default_size(800, 600)

        #Listas para almacenar los números del archivod e texto y para elegir los números aleatoreos
        self.lista = []
        self.listaAleatorea = []

        #Crear un contenedor para los Widgets
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)

        #crear la barra de herramientas
        toolbar = Gtk.Toolbar()

        #establecer el tamaño de los iconos del menu
        iconSize = Gtk.IconSize.DIALOG

        #Boton para accionar el abrir archivo
        openIcon = Gtk.Image.new_from_icon_name("document-open", iconSize)
        open_btn = Gtk.ToolButton.new(openIcon, "Open")
        open_btn.connect("clicked", self.OpenFile)
        toolbar.insert(open_btn, 0)

        #Boton de Ayuda y acerca del programa
        openIcon2 = Gtk.Image.new_from_icon_name("help-about",iconSize)
        help_btn = Gtk.ToolButton.new(openIcon2,"Help")
        help_btn.connect("clicked",self.OpenInfo)
        toolbar.insert(help_btn,1)


        #agregar la barra de herramientas
        self.box.pack_start(toolbar, False, True, 0)

        #Agregar los botones los cuales al presionarlos accionaran los distintos ordenamientos
        self.button1 = Gtk.Button(label="Ordenamiento Burbuja")
        self.button1.connect("clicked", self.OrdenamientoBurbuja)
        self.box.pack_start(self.button1, True, True, 0) 

        self.button2 = Gtk.Button(label="Ordenamiento Merge")
        self.button2.connect("clicked",self.OrdenamientoMerge)
        self.box.pack_start(self.button2,True,True,0)

        self.button3 = Gtk.Button(label="Ordentamiento Quick")
        self.button3.connect("clicked", self.OrdenamientoQuick)
        self.box.pack_start(self.button3,True,True,0)

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#

    def OpenInfo(self,widget):
        info = Gtk.AboutDialog()
        info.set_title("Informacion")
        info.set_comments("Proyecto Ordenador de Listas")
        info.set_version("Gtk 3.0\nPython 3.11")
        info.set_authors(["Lion"])
        info.set_website("https://github.com/LionLLL/PM1-2023-L")
        info.set_website_label("GitHub de Lion")
        info.connect('response', lambda dialog, data: dialog.destroy())
        info.show_all()

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#

    def OpenFile(self, widget):

        dialog = Gtk.FileChooserDialog(title="Elija el archivo de texto con los numeros", action=Gtk.FileChooserAction.OPEN,)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK)

        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)

        response = dialog.run()
        if(response == Gtk.ResponseType.OK):
            selected_file = dialog.get_filename()
            with open(selected_file, 'r') as f:
                for item in f:
                    self.lista+=item.split()
                print(self.lista[:])

        elif(response == Gtk.ResponseType.CANCEL):
            dialog.destroy()

        dialog.destroy()

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#

    def llenarListaAleatorea(self):
        NumeroAleatoreo = randint(5,15)
        for _ in range(NumeroAleatoreo):
            Na = self.lista[randint(0,len(self.lista)-1)]
            self.listaAleatorea.append(float(Na))
        print(Fore.RED,end="")
        print(self.listaAleatorea[:])
        print(Style.RESET_ALL,end="")

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
    def OrdenamientoBurbuja(self,widget):

        self.llenarListaAleatorea()

        inicio = time()
        for i in range(len(self.listaAleatorea)):
            for j in range(0, len(self.listaAleatorea) - i - 1):
                if(self.listaAleatorea[j] > self.listaAleatorea[j + 1]):

                    print(self.listaAleatorea[j],">",self.listaAleatorea[j + 1])
                    print(Fore.CYAN,self.listaAleatorea[:],Style.RESET_ALL)
                    
                    inicio+=1
                    sleep(1)
                    
                    
                    temp = self.listaAleatorea[j]
                    self.listaAleatorea[j] = self.listaAleatorea[j+1]
                    self.listaAleatorea[j+1] = temp
        fin = time()
        print("Tiempo:",fin-inicio,"segundos")
        print(self.listaAleatorea[:])
        print()

        self.listaAleatorea=[]
    
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # crear arrays izquierda y derechar temporales
        L = [0] * (n1)
        R = [0] * (n2)

        # llenar los arrays temporales
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        print(Fore.BLACK,end="")
        print(L[:],end="")
        print(Fore.GREEN,end="")
        print(R[:],end="")
        print(Style.RESET_ALL)
        sleep(1)
        # fusionarlos de nuevo
        i = 0     # indice inicial del primer sub Array
        j = 0     # indice inicial del segundo sub Array
        k = l     # indice inicial del sub Array fusionado

        while i < n1 and j < n2:
            if(L[i] <= R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            
            k += 1

        # Copiar lo que queda en la izquierda
        while i < n1:
            arr[k] = L[i]
            
            i += 1
            k += 1

        # copiar lo que queda en la derecha
        while j < n2:
            arr[k] = R[j]
            
            j += 1
            k += 1
        
        print(Fore.RED,end="")
        print(arr[:],end="")
        print(Style.RESET_ALL)
        sleep(1)

    def mergeSort(self,arr, l, r):
        if l < r:
            #(l+r)//2 buscar la mitada aproximada o exacta
            m = l+(r-l)//2
            print(Fore.YELLOW,end="")
            print(arr[0:m],end="")
            print(Fore.CYAN,end="")
            print(arr[m+1:])
            print(Style.RESET_ALL,end="")
            sleep(1)

            # ordenar las izquierda y luego derecha
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m+1, r)
            self.merge(arr, l, m, r)


    def merge2(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * (n1)
        R = [0] * (n2)
        for i in range(0, n1):
            L[i] = arr[l + i]
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if(L[i] <= R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1     
            k += 1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    def mergeSort2(self,arr, l, r):
        if l < r:
            m = l+(r-l)//2
            self.mergeSort2(arr, l, m)
            self.mergeSort2(arr, m+1, r)
            self.merge2(arr, l, m, r)

    def OrdenamientoMerge(self,widget):

        self.llenarListaAleatorea()
        listaCopia=[]
        for a in self.listaAleatorea:
            listaCopia.append(a)

        inicio = time()
        self.mergeSort2(listaCopia,0,len(listaCopia)-1)
        fin = time()

        n=len(self.listaAleatorea) 
        self.mergeSort(self.listaAleatorea,0,n-1)
        
        print("Tiempo:",fin-inicio,"segundos")
        print(self.listaAleatorea[:])
        print()

        self.listaAleatorea=[]

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
    def partition(self, array, low, high):
    
        # elemento mas a la derecha
        pivot = array[high]

        # el elemento mas grande
        i = low - 1
    
        # recorrer todos los elementos comparandolos con el pivot
        for j in range(low, high):
            if(array[j] <= pivot):
                # Si se encuentra un elemento menor que el pivot cambiarlo por el elemento mayor apuntado por i
                i = i + 1
                # intercambiar
                print(array[i],"<->",array[j])
                sleep(1)
                (array[i], array[j]) = (array[j], array[i])
        
        print(Fore.RED,end="")
        print(array[:],end="")
        print(Style.RESET_ALL)

        print(array[i+1]," <-> ",array[high])
        sleep(1)
        # Intercambia el elemento pivot con el elemento mayor especificado por i
        
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        
        print(Fore.RED,end="")
        print(array[:],end="")
        print(Style.RESET_ALL)
        sleep(1)
    
        # posición desde la que se realiza la partición
        return (i + 1)

    def quickSort(self,array, low, high):
        if(low < high):
    
            # Encontrar elemento pi tal que el elemento menor que pi está a la izquierda el elemento mayor que pi esté a la derecha
            pi = self.partition(array, low, high)
    
            print(Fore.YELLOW,end="")
            print(array[0:pi],end="")
            print(Fore.BLACK,end="")
            print(array[pi+1:],end="")
            print(Style.RESET_ALL)
            sleep(1)
            # recursividad hacia izquierda de pi
            self.quickSort(array, low, pi - 1)
    
            # recursividad hacia derecha de pi
            self.quickSort(array, pi + 1, high)


    def partition2(self, array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if (array[j] <= pivot):
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return (i + 1)
    def quickSort2(self,array, low, high):
        if(low < high):
            pi = self.partition2(array, low, high)
            self.quickSort2(array, low, pi - 1)
            self.quickSort2(array, pi + 1, high)


    def OrdenamientoQuick(self,widget):
        
        self.llenarListaAleatorea()
        listaCopia=[]
        for a in self.listaAleatorea:
            listaCopia.append(a)

        inicio=time()
        self.quickSort2(listaCopia,0,len(listaCopia)-1)
        fin=time()

        n = len(self.listaAleatorea)
        
        self.quickSort(self.listaAleatorea,0,n-1)

        print("Tiempo:",fin-inicio,"segundos")
        print(self.listaAleatorea[:])
        print()

        self.listaAleatorea=[]

#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------#

win = TextViewWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()