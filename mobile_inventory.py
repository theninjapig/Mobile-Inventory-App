from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import sqlite3
#import datetime
from datetime import datetime, date, time, timedelta
import os, sys
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
from kivy.uix.widget import Widget
import re


from kivy.uix.boxlayout import BoxLayout


## PLATA 10 KG COMPANY1  54 ELEMENTOS
## PLANTA 18/43 KG COMPANY2 28/28 ELEMENTOS  
## VEHICULOS 10 KG COMPANY3 84 ELEMENTOS
## VEHICULOS 18/43 COMPANY4 28/20 ELEMENTOS




today = date.today()

#today = datetime.datetime.now()

#today = date.today


one_day = timedelta(days=1)
#today = today + one_day

os.chdir(os.path.dirname(sys.argv[0]))

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        Button:
            #color: ( 1., 0, 0)
            #color: 1,0.65,0,1
            height: '48dp'
            size_hint: .5,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            #background_color: (0.55, .55, .0, .5)
            center_x: root.center_x-self.width*0
            center_y: root.center_y+self.height*0
            on_press: root.manager.current = 'dia'
            text: 'INVENTARIO \\n PLANTA AUTOMATIZADA \\n GENERALISIMO FRANCISCO DE MIRANDA'.format(\
            self.size_hint_x, self.size_hint_y)



<DIAScreen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    dia:_diae
    on_pre_enter: root.display_quote()
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'DIA'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1
            
        Button:
            id:quote_label
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.set_sea('hoy')
                root.manager.current = 'sel'


        Button:
            id:quote_label2
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.set_sea('otro')
                root.manager.current = 'in'
            text: '18/43 Kg'.format(\
            self.size_hint_x, self.size_hint_y)


##aca hay que incluir una ventana que separe entre inventario de planta
## y e inventario de GLP en tanques y camiones tanque
## se necesita una tabla/ventana donde se colocan los tanques disponibles
## y tablas/ventanas especificas para cada uno de los tanques.
## en las tablas especificas se detalla porcentaje , gravedad presion y
##temperatura






<INScreen>:
    quote_widget: quote_label
    dia:_diae
    ndia:_ndia
    on_pre_enter: root.display_quote()
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'OTRO DIA'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1
            

        Button:
            id:quote_label
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.5
            center_y: root.center_y+self.height*0
            on_press:
                root.set_date()
                

        TextInput:
            id: _ndia
            color: 1,0.65,0,1
            center_y: root.center_y+0.00*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .12,.05
            multiline: False

        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                #root.retu()
                root.manager.current = 'dia'


<SelScreen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    dia:_diae
    on_pre_enter:
        root.display_quote()
        root.get_date()
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'TIPO DE INVENTARIO'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1
            
        Button:
            id:quote_label
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                #root.set_seap('planta')
                root.manager.current = 'planta'


        Button:
            id:quote_label2
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                #root.set_seap('tanque')
               # root.manager.current = 'in'
            text: '18/43 Kg'.format(\
            self.size_hint_x, self.size_hint_y)

        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.retu()






<PLANTAScreen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    dia:_diae
    on_pre_enter:
        root.display_quote()
        root.get_date()
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'UBICACION GENERAL'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1
            
        Button:
            id:quote_label
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.set_ubc('plantau')
                root.manager.current = 'tipo'


        Button:
            id:quote_label2
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.set_ubc('vehiculos')
                root.manager.current = 'tipo'
            text: '18/43 Kg'.format(\
            self.size_hint_x, self.size_hint_y)

        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.retu()





<TIPOScreen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    dia:_diae
    direc:_direc
    on_pre_enter:
        root.get_date()
        root.set_direc()
        root.display_quote()
        
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            id:_direc
            color: 1,0.65,0,1
            #text: 'CAPACIDAD'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1
            
        Button:
            id:quote_label
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.sel_dir1()
                #root.manager.current = 'inventario'


        Button:
            id:quote_label2
            height: '48dp'
            size_hint: .2,.2
            halign: 'center'
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.sel_dir2()
                #root.manager.current = 'inventario2'
            

        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.retu()
                #root.manager.current = 'dia'




  
<INVENTARIOScreen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    quote_widget4: quote_label4
    quote_widget5: quote_label5
    quote_widget6: quote_label6
    #quote_widget7: quote_label7
    quote_widget8: quote_label8
    quote_widget9: quote_label9
    dia:_diae
    
    on_pre_enter:
        root.get_date()
        root.display_quote()
    
    
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            text: 'PLANTA - 10 Kg'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1
        Button:
            id: quote_label2
            #text: 'LINEA 1'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('l1')
                root.manager.current = 'operl2'
                      
        Button:
            id: quote_label
            #text: 'LINEA 2'
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('l2')
                root.manager.current = 'operl2'
        Button:
            id: quote_label5
            #text: 'PATIO 1'
            halign: 'center'
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pa1')
                root.manager.current = 'operl2'
            
        Button:
            id: quote_label6
            #text: 'PATIO 2'
            halign: 'center'
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pa2')
                root.manager.current = 'operl2'
##        Button:
##            id: quote_label7
##            #text: 'PLATAFORMA 1'
##            halign: 'center'
##            center_y: root.center_y-0.35*root.height+self.height*0.5
##            center_x: root.center_x-self.width*0.6
##            size_hint: .3,.13
##            on_press:
##                root.set_location('pla1')
##                root.manager.current = 'operl2'
        Button:
            id: quote_label3
            background_color: (0.416, .416, .416, 1)
            #text: 'PLATAFORMA 2'
            halign: 'center'
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            
            
            size_hint: .3,.13
            on_press:
                root.set_location('pla2')
                root.manager.current = 'operl2'
        Button:
            id: quote_label8
            background_color: (0.416, .416, .416, 1)
            #text: 'EPSDC'
            halign: 'center'
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            
            size_hint: .3,.13
            on_press:
                root.set_location('epsdc')
                root.manager.current = 'eps'

        Button:
            id: quote_label4
            background_color: (0.416, .416, .416, 1)
            #text: 'PATIO GANDOLA (CARGA)'
            halign: 'center'
            center_y: root.center_y-0.20*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pag')
                root.manager.current = 'operl2'

        Button:
            id: quote_label9
            background_color: (0.416, .416, .416, 1)
            #text: 'PLATAFORMA 43'
            halign: 'center'
            center_y: root.center_y-0.20*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pla43')
                root.manager.current = 'operl2'

        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                root.manager.current = 'tipo'


#aqui vamos 2
<INVENTARIO2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    #quote_widget4: quote_label4
    quote_widget5: quote_label5
    quote_widget6: quote_label6
    quote_widget7: quote_label7
   # quote_widget8: quote_label8
    quote_widget9: quote_label9
    dia:_diae
    
    on_pre_enter:
        root.get_date()
        root.display_quote()
    
    
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            text: 'PLANTA - 18/43 Kg'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1
        Button:
            id: quote_label2
            #text: 'LINEA 1'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('l1')
                root.manager.current = 'noperl2'
                      
        Button:
            id: quote_label
            #text: 'LINEA 2'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('l2')
                root.manager.current = 'noperl2'
        Button:
            id: quote_label5
            #text: 'PATIO 1'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pa1')
                root.manager.current = 'noperl2'
            
        Button:
            id: quote_label6
            #text: 'PATIO 2'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pa2')
                root.manager.current = 'noperl2'
        Button:
            id: quote_label7
            #text: 'PLATAFORMA 1'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pla1')
                root.manager.current = 'noperl2'
        Button:
            id: quote_label3
            #text: 'PLATAFORMA 2'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pla2')
                root.manager.current = 'noperl2'
##        Button:
##            id: quote_label8
##            #text: 'EPSDC'
##            halign: 'center'
##            center_y: root.center_y-0.20*root.height+self.height*0.5
##            center_x: root.center_x-self.width*0.6
##            
##            size_hint: .3,.13
##            on_press:
##                root.set_location('epsdc')
##                root.manager.current = 'noperl2'
##
##        Button:
##            id: quote_label4
##            #text: 'PATIO GANDOLA (CARGA)'
##            halign: 'center'
##            center_y: root.center_y-0.20*root.height+self.height*0.5
##            center_x: root.center_x+self.width*0.6
##            size_hint: .3,.13
##            on_press:
##                root.set_location('pag')
##                root.manager.current = 'noperl2'

        Button:
            id: quote_label9
            #text: 'PLATAFORMA 43'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.20*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('pla43')
                root.manager.current = 'noperl2'

        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                root.manager.current = 'tipo'  








<INVENTARIO3Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    quote_widget4: quote_label4
    quote_widget5: quote_label5
    quote_widget6: quote_label6
    quote_widget7: quote_label7
   
    dia:_diae
    
    on_pre_enter:
        root.get_date()
        root.display_quote()
    
    
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            text: 'VEHICULOS - 10 Kg'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Button:
            id: quote_label
            #text: 'GANDOLA 1'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('gan1')
                #root.manager.current = 'vhplinea2'
                      
        Button:
            id: quote_label2
            #text: 'GANDOLA 2'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('gan2')
                #root.manager.current = 'vhplinea2'
        Button:
            id: quote_label3
            #text: 'FLETERO 1'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('fle1')
                #root.manager.current = 'vhplinea2'
            
        Button:
            id: quote_label4
            #text: 'FLETERO 2'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('fle2')
                #root.manager.current = 'vhplinea2'
        Button:
            id: quote_label5
            #text: 'EPSDC 1'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('eps1')
                #root.manager.current = 'vhplinea2'
        Button:
            id: quote_label6
            #text: 'EPSDC 2'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('eps2')
                #root.manager.current = 'vhplinea2'
        Button:
            id: quote_label7
            #text: 'EPSDC 3'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.20*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            
            size_hint: .3,.13
            on_press:
                root.set_location('eps3')
                #root.manager.current = 'vhplinea2'

        
        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                root.manager.current = 'tipo'








<INVENTARIO4Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    quote_widget4: quote_label4
    quote_widget5: quote_label5
    quote_widget6: quote_label6
    quote_widget7: quote_label7
  
    dia:_diae
    
    on_pre_enter:
        root.get_date()
        root.display_quote()
    
    
    FloatLayout:
        
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            text: 'VEHICULOS - 18/43 Kg'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Button:
            id: quote_label
            #text: 'GANDOLA 1'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('gan1')
                root.manager.current = 'n1vhplinea2'
                      
        Button:
            id: quote_label2
            #text: 'GANDOLA 2'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            halign: 'center'
            on_press:
                root.set_location('gan2')
                root.manager.current = 'n1vhplinea2'
        Button:
            id: quote_label3
            #text: 'FLETERO 1'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('fle1')
                root.manager.current = 'n2vhplinea2'
            
        Button:
            id: quote_label4
            #text: 'FLETERO 2'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.1*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('fle2')
                root.manager.current = 'n2vhplinea2'
        Button:
            id: quote_label5
            #text: 'EPSDC 1'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('eps1')
                root.manager.current = 'n2vhplinea2'
        Button:
            id: quote_label6
            #text: 'EPSDC 2'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x+self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('eps2')
                root.manager.current = 'n2vhplinea2'


        Button:
            id: quote_label7
            #text: 'EPSDC 3'
            halign: 'center'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.20*root.height+self.height*0.5
            center_x: root.center_x-self.width*0.6
            size_hint: .3,.13
            on_press:
                root.set_location('eps3')
                root.manager.current = 'n2vhplinea2'

        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                root.manager.current = 'tipo'  



<EPSScreen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    direc:_direc

    dia: _diae
    
    
    #on_enter: root.display_quote()
    on_pre_enter:
        root.get_date()
        root.display_quote()
        root.set_direc()
    
    
    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_direc
            #text: '10kg - LINEA 2'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Button:
            id: quote_label
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.0
            center_y: root.center_y+self.height*0
            on_press:
                #root.manager.question = root
                root.set_locat2('patio')
                #root.manager.current = 'operl2'
           
        Button:
            id: quote_label2
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*1
            center_y: root.center_y+self.height*0
            on_press:
                root.set_locat2('pla1')
               # root.manager.current = 'operl2'

        Button:
            id: quote_label3
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*1
            center_y: root.center_y+self.height*0
            on_press:
                #root.manager.question = root
                root.set_locat2('pla2')
                #root.manager.current = 'operl2'
            
        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                root.manager.current = 'inventario'






<OPERL2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc:_direc

    dia: _diae
    
    
    #on_enter: root.display_quote()
    on_pre_enter:
        root.get_date()
        root.display_quote()
        root.set_direc()
    
    
    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_direc
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            #text: '10kg - LINEA 2'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1
        Button:
            id: quote_label
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.manager.question = root
                root.set_cond('op')
                root.manager.current = 'plinea2'
           
        Button:
            id: quote_label2
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.set_cond('nop')
                root.manager.current = 'plinea2'
            
        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.retu()
                
                #root.manager.current = 'inventario'


<NOPERL2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc:_direc

    dia: _diae
    
    
    #on_enter: root.display_quote()
    on_pre_enter:
        root.get_date()
        root.display_quote()
        root.set_direc()
    
    
    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_direc
            #text: '10kg - LINEA 2'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Button:
            id: quote_label
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x+self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.manager.question = root
                root.set_cond('op')
                root.manager.current = 'nplinea2'
           
        Button:
            id: quote_label2
            height: '48dp'
            halign: 'center'
            size_hint: .2,.2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_x: root.center_x-self.width*0.6
            center_y: root.center_y+self.height*0
            on_press:
                root.set_cond('nop')
                root.manager.current = 'nplinea2'
            
        
        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                root.manager.current = 'inventario2'




<CLIPON>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc2:_direc2
    #titp:_titp
    on_pre_enter:
        root.set_direc2()
        root.display_quote()
        
    
    agll: _agll
    agv: _agv
   
    dia: _diae
    

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            color: 1,0.65,0,1
            id: _result

        Label:
            id:_direc2
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTO GAS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1


        Button:
            text: 'VACIO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
           
        TextInput:
            id: _agv
            size_hint: .08,.05
            center_y: root.center_y+0.10*root.height+self.height
            center_x: root.center_x+root.width*0.0+self.width
            multiline: False

        Label:
            id: quote_label2
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5



        Button:
            text: 'LLENO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
           
        TextInput:
            id: _agll
            #size_hint_x: 50
            size_hint: .08,.05
            center_y: root.center_y+0.25*root.height+self.height
            center_x: root.center_x+root.width*0.0+self.width
            #size_hint: .1,.1
            
            multiline: False
            #size_hint: None, None
            #text: '%s, %s' % (self.get_center_x(), self.get_center_y())

        Label:
            id: quote_label
            #color: 1,0,0,1
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5     



        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.save()
                #root.manager.question.display_quote()
                #root.display_quote()  
                #root.manager.current = 'eps'


<PLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    #quote_widget4: quote_label4
    direc:direco
    on_pre_enter:
        root.get_date()
        root.set_direc()
        root.display_quote()
   
    
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id: direco
            color: 1,0.65,0,1
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1     



        Button:
            text: 'AUTO GAS'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('ag')
                root.moven()
                #root.manager.current = 'aglinea2'
       

        Label:
            id: quote_label
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


        Button:
            text: 'CLIP-ON'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('cln')
                root.moven()
                #root.manager.current = 'aglinea2'
           
        
        Label:
            id: quote_label2
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


        Button:
            text: 'PLASTICO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('p')
                root.moven()
                #root.manager.current = 'aglinea2'
     
        Label:
            id: quote_label3
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5




        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                #root.manager.question.display_quote()
                root.display_quote()
                root.moveback()
                #root.manager.current = 'operl2'


<VHPLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    quote_widget3: quote_label3
    #quote_widget4: quote_label4
    direc:direco
    on_pre_enter:
        root.get_date()
        root.set_direc()
        root.display_quote()
   
    
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1
            

        Label:
            id: direco
            color: 1,0.65,0,1
            #text: 'VEHICULOS - 10kg - LINEA 2 - OPERATIVOS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1     



        Button:
            text: 'AUTO GAS'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('ag')
                root.moven()
                #root.manager.current = 'vhaglinea2'
       

        Label:
            id: quote_label
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


        Button:
            text: 'CLIP-ON'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('cln')
                root.moven()
                #root.manager.current = 'vhaglinea2'
           
        
        Label:
            id: quote_label2
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


        Button:
            text: 'PLASTICO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('p')
                root.moven()
                #root.manager.current = 'vhaglinea2'
     
        Label:
            id: quote_label3
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y-0.05*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5




        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                #root.manager.question.display_quote()
                root.display_quote()  
                root.manager.current = 'inventario3'



<NPLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    #quote_widget3: quote_label3
    #quote_widget4: quote_label4
    direc:direco
    on_pre_enter:
        root.get_date()
        root.set_direc()
        root.display_quote()
   
    
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id: direco
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1     



        Button:
            text: '18 Kg'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('18')
                root.moven()
                #root.manager.current = 'naglinea2'
       

        Label:
            id: quote_label
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


        Button:
            text: '43 Kg'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('43')
                root.moven()
                #root.manager.current = 'naglinea2'
           
        
        Label:
            id: quote_label2
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5





        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                #root.manager.question.display_quote()
                root.display_quote()  
                root.manager.current = 'noperl2'




<N1VHPLINEA2Screen>:
    quote_widget: quote_label
    #quote_widget2: quote_label2
    #quote_widget3: quote_label3
    #quote_widget4: quote_label4
    direc:direco
    on_pre_enter:
        root.get_date()
        root.set_direc()
        root.display_quote()
   
    
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1
            

        Label:
            id: direco
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1     



        Button:
            text: '18 Kg'
            color: 1,0.65,0,1
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('18')
                root.moven()
                #root.manager.current = 'naglinea2'
       

        Label:
            id: quote_label
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.display_quote()  
                root.manager.current = 'inventario4'


<N2VHPLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    #quote_widget3: quote_label3
    #quote_widget4: quote_label4
    direc:direco
    on_pre_enter:
        root.get_date()
        root.set_direc()
        root.display_quote()
   
    
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id: direco
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS'
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1     



        Button:
            text: '18 Kg'
            color: 1,0.65,0,1
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('18')
                root.moven()
                #root.manager.current = 'naglinea2'
       

        Label:
            id: quote_label
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5

        Button:
            text: '43 Kg'
            color: 1,0.65,0,1
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                root.set_tipo('43')
                root.moven()
                #root.manager.current = 'naglinea2'
           
        
        Label:
            id: quote_label2
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5








        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                
                #root.manager.question.display_quote()
                root.display_quote()  
                root.manager.current = 'inventario4'


<AGLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc2:_direc2
    #titp:_titp
    on_pre_enter:
        root.set_direc2()
        root.display_quote()
        
    
##    agll: _agll
##    agv: _agv
   
    dia: _diae
    

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id:_direc2
            color: 1,0.65,0,1
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTO GAS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1


        Button:
            text: 'VACIO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('v')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agv
##            size_hint: .08,.05
##            center_y: root.center_y+0.10*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            multiline: False

        Label:
            id: quote_label2
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5



        Button:
            text: 'LLENO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('ll')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agll
##            #size_hint_x: 50
##            size_hint: .08,.05
##            center_y: root.center_y+0.25*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            #size_hint: .1,.1
##            
##            multiline: False
##            #size_hint: None, None
##            #text: '%s, %s' % (self.get_center_x(), self.get_center_y())

        Label:
            id: quote_label
            #color: 1,0,0,1
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5     



        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                #root.save()
                #root.manager.question.display_quote()
                #root.display_quote()  
                root.manager.current = 'plinea2'
                



<VHAGLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc2:_direc2
    #titp:_titp
    on_pre_enter:
        root.set_direc2()
        root.display_quote()
        
##    
##    agll: _agll
##    agv: _agv
   
    dia: _diae
    

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id:_direc2
            color: 1,0.65,0,1
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTO GAS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1


        Button:
            text: 'VACIO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('v')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agv
##            size_hint: .08,.05
##            center_y: root.center_y+0.10*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            multiline: False

        Label:
            id: quote_label2
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5



        Button:
            text: 'LLENO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('ll')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agll
##            #size_hint_x: 50
##            size_hint: .08,.05
##            center_y: root.center_y+0.25*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            #size_hint: .1,.1
##            
##            multiline: False
##            #size_hint: None, None
##            #text: '%s, %s' % (self.get_center_x(), self.get_center_y())

        Label:
            id: quote_label
            #color: 1,0,0,1
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5     



        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.save()
                #root.manager.question.display_quote()
                #root.display_quote()  
                #root.manager.current = 'operl2'


<NAGLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc2:_direc2
    #titp:_titp
    on_pre_enter:
        root.set_direc2()
        root.display_quote()
        
    
##    agll: _agll
##    agv: _agv
   
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id:_direc2
            color: 1,0.65,0,1
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTO GAS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1


        Button:
            text: 'VACIO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('v')
                root.manager.current = 'calculator'
##           
##        TextInput:
##            id: _agv
##            size_hint: .08,.05
##            center_y: root.center_y+0.10*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            
##            
##            multiline: False

        Label:
            id: quote_label2
            text_size: self.width-40, self.height-40
            italic: True
            color: 1,0.65,0,1
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5



        Button:
            text: 'LLENO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('ll')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agll
##            #size_hint_x: 50
##            size_hint: .08,.05
##            center_y: root.center_y+0.25*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            multiline: False
##            #size_hint: None, None
##            #text: '%s, %s' % (self.get_center_x(), self.get_center_y())

        Label:
            id: quote_label
            #color: 1,0,0,1
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


       



        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.save()
                



<N1VHAGLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc2:_direc2
    #titp:_titp
    on_pre_enter:
        root.set_direc2()
        root.display_quote()
        
    
##    agll: _agll
##    agv: _agv
##   
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id:_direc2
            color: 1,0.65,0,1
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTO GAS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1


        Button:
            text: 'VACIO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('v')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agv
##            size_hint: .08,.05
##            center_y: root.center_y+0.10*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            
##            
##            multiline: False

        Label:
            id: quote_label2
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5



        Button:
            text: 'LLENO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()
                root.set_esti('ll')
                root.manager.current = 'calculator'
           
##        TextInput:
##            id: _agll
##            #size_hint_x: 50
##            size_hint: .08,.05
##            center_y: root.center_y+0.25*root.height+self.height
##            center_x: root.center_x+root.width*0.0+self.width
##            multiline: False
##            #size_hint: None, None
##            #text: '%s, %s' % (self.get_center_x(), self.get_center_y())

        Label:
            id: quote_label
            #color: 1,0,0,1
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


       



        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.save()
                


<N2VHAGLINEA2Screen>:
    quote_widget: quote_label
    quote_widget2: quote_label2
    direc2:_direc2
    #titp:_titp
    on_pre_enter:
        root.set_direc2()
        root.display_quote()
        
    
##    agll: _agll
##    agv: _agv
##   
    dia: _diae

    
    FloatLayout:
        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
            
        Label:
            id: _result
            color: 1,0.65,0,1

        Label:
            id:_direc2
            color: 1,0.65,0,1
            #text: 'PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTO GAS'
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.0+self.width*0.0
            size_hint: .3,.1

        Label:
            id:_diae
            color: 1,0.65,0,1
            center_y: root.center_y+0.40*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.4+self.width*0.0
            size_hint: .3,.1


        Button:
            text: 'VACIO'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
            on_press:
                #root.display_quote()  
                root.manager.current = 'calculator'

            #MODIFYING HERE
           
        TextInput:
            id: _agv
            size_hint: .08,.05
            center_y: root.center_y+0.10*root.height+self.height
            center_x: root.center_x+root.width*0.0+self.width
            
            
            multiline: False

        Label:
            id: quote_label2
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.10*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5



        Button:
            text: 'LLENO'
            color: 1,0.65,0,1
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x-root.width*0.5+self.width
            size_hint: .3,.1
           
        TextInput:
            id: _agll
            #size_hint_x: 50
            size_hint: .08,.05
            center_y: root.center_y+0.25*root.height+self.height
            center_x: root.center_x+root.width*0.0+self.width
            multiline: False
            #size_hint: None, None
            #text: '%s, %s' % (self.get_center_x(), self.get_center_y())

        Label:
            id: quote_label
            #color: 1,0,0,1
            color: 1,0.65,0,1
            text_size: self.width-40, self.height-40
            italic: True
            center_y: root.center_y+0.25*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.0+self.width
            size_hint: .5,.5


       



        Button:
            text: 'Retorno'
            color: 1,0.65,0,1
            background_color: (0.416, .416, .416, 1)
            center_y: root.center_y-0.4*root.height+self.height*0.5
            center_x: root.center_x+root.width*0.45-self.width*0.5
            size_hint: .2,.1
            on_press:
                root.save()
        



<Calculator>:
    id: calculator
    display: input
    #dia: _diae
    on_pre_enter:
        #root.entrada()
        input.text=''

    BoxLayout:
        orientation: 'vertical'
##        padding: 20
##        spacing: 10

        canvas:
            Color:
                rgb: (0., .25, .25)
            Rectangle:
                pos: self.pos
                size: self.size
        
        TextInput:
            id: input
            size_hint: 1, None
            readonly: True
            multiline: False
            font_size: 50

        GridLayout:
            rows: 4
            cols: 5

            Button:
                text: '1'
                on_press: input.text += self.text 

            Button:
                text: '2'
                on_press: input.text += self.text

            Button:
                text: '3'
                on_press: input.text += self.text                
        
            BubbleButton:
                text: '+'
                on_press: input.text += self.text

            BubbleButton:
                text: '-'
                on_press: input.text += self.text

            Button:
                text: '4'
                on_press: input.text += self.text

            Button:
                text: '5'
                on_press: input.text += self.text

            Button:
                text: '6'
                on_press: input.text += self.text

            BubbleButton:
                text: '*'
                on_press: input.text += self.text

            BubbleButton:
                text: ''
                #on_press: input.text += self.text

            Button: 
                text: '7'
                on_press: input.text += self.text

            Button:
                text: '8'
                on_press: input.text += self.text

            Button:
                text: '9'
                on_press: input.text += self.text

            BubbleButton:
                text: '='
                on_press: calculator.calculate(input.text)

            BubbleButton:
                text: 'LIMP MEM'
                on_press:
                    #input.text -= root.entrada()
                    root.save('-'+ root.entrada())
                    input.text = '0'

                    
                
                #on_press: calculator.calculate(input.text)

            BubbleButton:
                text: 'C'
                on_press: calculator.backward(input.text)

            Button:
                text: '0'
                on_press: input.text += self.text

            BubbleButton:
                text: 'Cesta'
                #on_press: input.text += self.text
                on_press: input.text += '*'+'35'

            BubbleButton:
                text: 'PREV'
                on_press: input.text += root.entrada()
                #on_press: root.entrada()

            BubbleButton:
                text: 'Retorno'
                on_press:
                    calculator.calculate(input.text)
                    root.save(input.text)
                    root.reto()
                    # _agll=
                     
   
            
        

""")

# Declare both screens

#global ch_ubc

ch_ubc='plant'
ch_loc='gan1'
locat2='patio'
toda=today

global condp, locatp, tipoop, direc2p


class Calculator(Screen):
    agll= ObjectProperty()
    tipoo=StringProperty('ag')
    cond=StringProperty('op')
    locat = StringProperty('l2')
    dia = ObjectProperty()
    #global condp, locatp, tipoop, direc2p


           
##        def __init__(self, **kwargs):
##                super(Calculator, self).__init__(**kwargs)
##                #self.display_quote()
##                self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
##                #self.get_date()
                
                
    def reto(self):
        if table == "COMPANY":
            self.manager.current = 'aglinea2'
        elif table == "COMPANY3":
            self.manager.current = 'vhaglinea2'
                    
    def backward(self, express):
        if express:
            self.display.text = express[:-1]

    def calculate(self, express):
        #if not express: return

        try: 
            self.display.text = str( eval(express) )
            
        except Exception:
            self.display.text = 'error'

    def entrada(self):
        self.cond=condp
        self.locat=locatp
        self.tipoo=tipoop
        self.direc2=direc2p
        conn = sqlite3.connect('planta47.db')



        ban=0
        bao1=0


        if self.display.text:
            bao1=1


        ##            try:

        #print 'DATOS'
        #print   self.display.text
        ##print   self.agv.text

        

        if ban==0:
                #print "ESTI", esti
                qe='''SELECT  cantidad, consultas from '''+ table +''' WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
                   AND CAPACIDAD='10' AND ESTADO=?) '''

                cursor = conn.execute(qe, (self.tipoo, today, self.locat,self.cond, esti))



##                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY3 WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op'
##          AND CAPACIDAD='10') ''', (self.tipoo, today, ch_loc))

                my_data  = cursor.fetchall()
                #print "DATAPP", my_data



                #print  "TIPO", self.tipoo
                #print "LOCAT", self.locat
                #print "COND", self.cond
                #print "ESTI", esti
                
                #print "DATA", my_data[0][0]

                ##                if not self.display.text:
                #

                #self.display.text=str(my_data[0][0])


                return str(my_data[0][0])
##                try:
##                        agllop=int(self.display.text)+ my_data[0][0]
##                        
##                except ValueError:
##                        agllop= my_data[0][0]
        
            
    def save(self, express):
        #global condp, locatp, tipoop, direc2p
        self.cond=condp
        self.locat=locatp
        self.tipoo=tipoop
        self.direc2=direc2p
        if not express: return

        try: 
            self.display.text = str( eval(express) )
            
        except Exception:
            self.display.text = 'No actualizado'
                
            
                
                    
            
                   

##            #UPDATE
    #ba2=1
        conn = sqlite3.connect('planta47.db')



        ban=0
        bao1=0


        if self.display.text:
            bao1=1


        ##            try:

        #print 'DATOS'
        #print   self.display.text
        ##print   self.agv.text



        if ban==0:
                qe='''SELECT  cantidad, consultas from '''+ table +''' WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
                   AND CAPACIDAD='10' AND ESTADO=?) '''

                cursor = conn.execute(qe, (self.tipoo, today, self.locat,self.cond, esti))



##                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY3 WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op'
##          AND CAPACIDAD='10') ''', (self.tipoo, today, ch_loc))

                my_data  = cursor.fetchall()
                #print "DATAPP", my_data



                #print  "TIPO", self.tipoo
                #print "LOCAT", self.locat
                #print "COND", self.cond
                #print "ESTI", esti
                
                #print "DATA", my_data[0][0]

                ##                if not self.display.text:
                #
                try:
                        agllop=int(self.display.text)+ my_data[0][0]
                        
                except ValueError:
                        agllop= my_data[0][0]
                            
                            
                    


                    
                    


                opo=my_data[0][1]
                #opo2=my_data[1][1]

                if bao1==1:
                    opo =+ 1


                #self.agll.text, self.agv.text



                #print "EPA!!" "\n"
                #print "agllop", agllop


                    

                my_data2 = ({'locate':self.locat, 'tip':self.tipoo, 'est':esti, 'value':agllop ,'condi':self.cond ,'con':opo, 'fe': today})
                            
                qq="UPDATE "+ table + " SET CANTIDAD =:value WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) "
                conn.execute(qq, my_data2)



                conn.commit()

                qqq="UPDATE "+ table + " SET   CONSULTAS=:con WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) "
                conn.execute(qqq, my_data2)



                conn.commit()


                #print "Total number of rows updated :", conn.total_changes


                ##                #print "Operation done successfully";
                conn.close()
##                if table == "COMPANY":
##                    self.manager.current = 'aglinea2'
##                elif table == "COMPANY3":
##                    self.manager.current = 'vhaglinea2'
                
   
            

class MenuScreen(Screen):
    pass




class DIAScreen(Screen):
    quote_widget=ObjectProperty()
    quote_widget2=ObjectProperty()
    dia = ObjectProperty()
    sea=StringProperty()


    def __init__(self, **kwargs):
        super(DIAScreen, self).__init__(**kwargs)
        self.get_date()



    def display_quote(self):
         self.quote_widget.text = 'HOY'
         self.quote_widget2.text = 'OTRO DIA'       

    def set_sea(self,val):
        global seato
        seato=val
        self.sea=val
    
    def get_date(self):
            self.dia.text= str(today)


class INScreen(Screen):
    quote_widget=ObjectProperty()
    ndia= ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty('dia')
    sea=StringProperty()
    sta=0


    def __init__(self, **kwargs):
        super(INScreen, self).__init__(**kwargs)
        self.get_date()

    def display_quote(self):
         if self.sta==0:
             self.ndia.text= str(today)
         self.quote_widget.text = 'INTRODUZCA \n FECHA'

    @staticmethod
    def valid_date(datestring):
        try:
            datetime.strptime(datestring, '%Y-%m-%d').date()
            return True
        except ValueError:
            return False

    def set_date(self):
            global toda
            conn = sqlite3.connect('planta47.db')
            #today=self.ndia.text
            self.sta=1
            #print "DIA", self.ndia.text
            #print "TODA", toda
            toda=self.ndia.text
            #print "TODA actualizado", toda
            at=toda
            #print at
            if self.valid_date(at)==True:
                todau= datetime.strptime(toda, "%Y-%m-%d").date()
                #today= datetime.strptime(self.ndia.text, "%Y-%m-%d").date()
                #print "TODAU", todau
                cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
            
                my_data  = cursor.fetchall()

                bio=0
                if not my_data:
                    #self.manager.current = 'in'
                    bio=1
                    #self.ndia.text= str(today)
                    self.quote_widget.text = 'FECHA \n NO DISPONIBLE \n (INTRODUZCA OTRA)'
                    #self.ndia.text=str("ND")
                    #toda=self.ndia.text
                if bio==0:
                    #toda=self.ndia.text
                    self.quote_widget.text = ' INTRODUZCA \n FECHA'
                    self.manager.current = 'sel'
            else:
                self.quote_widget.text = ' INTRODUZCA \n FECHA VALIDA'
                self.ndia.text= str(today)
                #self.ndia.text=str("")
            
                
                     

    def get_date(self):
            self.dia.text= str(today)


class SelScreen(Screen):
    quote_widget=ObjectProperty()
    quote_widget2=ObjectProperty()
    dia = ObjectProperty()
    sea=StringProperty()
    global seato
    seato='hoy'


    def __init__(self, **kwargs):
        super(SelScreen, self).__init__(**kwargs)
        self.get_date()


   
    def display_quote(self):
         self.quote_widget.text = 'CILINDROS'
         self.quote_widget2.text = 'TANQUES'


    def get_date(self):
       
        #print "SEATO", seato
        if seato=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)
        
    def set_sea(self,val):
        self.sea=val
    
##    def get_date(self):
##            self.dia.text= str(today)
    def retu(self):
        if self.sea=='otro':
            self.manager.current = 'in'
        else:
            self.manager.current = 'dia'





class PLANTAScreen(Screen):
    global ch_ubc
    quote_widget=ObjectProperty()
    quote_widget2=ObjectProperty()
    dia = ObjectProperty()
    sea=StringProperty()
    #toda = StringProperty()
    #ubc=StringProperty(ch_ubc)


    def __init__(self, **kwargs):
        super(PLANTAScreen, self).__init__(**kwargs)
        self.get_date()



    def display_quote(self):
         self.quote_widget.text = 'PLANTA'
         self.quote_widget2.text = 'VEHICULOS'       

    def set_ubc(self,val):
        global ch_ubc
        ch_ubc=val
        #print "FIJA UBC", ch_ubc

    def retu(self):
        self.manager.current = 'sel'
##        if self.sea=='otro':
##            self.manager.current = 'in'
##        else:
##            self.manager.current = 'dia'
    
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)




class TIPOScreen(Screen):
    quote_widget=ObjectProperty()
    quote_widget2=ObjectProperty()
    dia = ObjectProperty()
    direc=ObjectProperty()
    ##toda = StringProperty()
    sea=StringProperty()
    


    def __init__(self, **kwargs):
        super(TIPOScreen, self).__init__(**kwargs)
        #self.get_date()

    def sel_dir1(self):
        #global ch_ubc
        #print "UBC", ch_ubc
        if ch_ubc=='plantau':
            self.manager.current = 'inventario'
        else:
            self.manager.current = 'inventario3'

    def sel_dir2(self):
        #global ch_ubc
        #print "UBC", ch_ubc
        if ch_ubc=='plantau':    
            self.manager.current = 'inventario2'
        else:
            self.manager.current = 'inventario4'
            
        
    def retu(self):
        self.manager.current = 'planta'


    @staticmethod
    def valid_date(datestring):
        try:
            datetime.strptime(datestring, '%Y-%m-%d').date()
            return True
        except ValueError:
            return False


    def set_direc(self):
        if ch_ubc=='plantau': 
            self.direc.text=str('PLANTA ')
            ##print "condicion", self.locat
        else:
            self.direc.text=str('VEHICULOS')
            ##print "condicion", self.locat



    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
                
        #print "TODAY2",todau
        conn = sqlite3.connect('planta47.db')
        if ch_ubc=='plantau':
            
        
            cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE
               ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='ll') ''', (todau,))
            
            my_data  = cursor.fetchall()


            cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE
               ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='v') ''', (todau,))
            
            my_datava  = cursor.fetchall()

            


            cursor = conn.execute('''SELECT  consultas from COMPANY WHERE
              ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='ll' ) ''', (todau,))

            my_datac  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY WHERE
              ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='v' ) ''', (todau,))

            my_datacva  = cursor.fetchall()


            
            cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE
               ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='ll'  ) ''', (todau-one_day,))
            
            my_datav  = cursor.fetchall()



            cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE
              ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='v'  ) ''', (todau-one_day,))
            
            my_datavva = cursor.fetchall()
            


            cursor = conn.execute('''SELECT  consultas from COMPANY WHERE
              ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='ll' ) ''', (todau-one_day,))

            my_datacv  = cursor.fetchall()

            cursor = conn.execute('''SELECT  consultas from COMPANY WHERE
               ( FECHA = ?   AND CAPACIDAD='10' AND ESTADO='v' ) ''', (todau-one_day,))

            my_datacvva  = cursor.fetchall()


            

            
            bb=0
            if not my_datav:
                        #self.manager.current = 'in'
                        bb=1
                        dif=str("ND")
                        difva=str("ND")
                        #toda=self.ndia.text
            



            #print "MY DATA LENGTH", len(my_data)    

    ##        bio=0
    ##        if not my_data:
    ##            self.manager.current = 'in'
    ##            bio=1
    ##            
    ##        #print "DATA", my_data
    ##        if bio==0:
            self.quote_widget.color=[1,1,1,1] 
            if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
                and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0 \
                and my_datac[12][0]==0 and my_datac[13][0]==0 and my_datac[14][0]==0 and my_datac[15][0]==0 and my_datac[16][0]==0 and my_datac[17][0]==0 \
                and my_datac[18][0]==0 and my_datac[19][0]==0 and my_datac[20][0]==0 and my_datac[21][0]==0 and my_datac[22][0]==0 and my_datac[23][0]==0 \
                and my_datac[24][0]==0 and my_datac[25][0]==0 and my_datac[26][0]==0 and my_datac[27][0]==0 and my_datac[28][0]==0 and my_datac[29][0]==0 \
                and my_datac[30][0]==0 and my_datac[31][0]==0 and my_datac[32][0]==0 and my_datac[33][0]==0 and my_datac[34][0]==0 and my_datac[35][0]==0 \
                and my_datac[36][0]==0 and my_datac[37][0]==0 and my_datac[38][0]==0 and my_datac[39][0]==0 and my_datac[40][0]==0 and my_datac[41][0]==0 \
                and my_datac[42][0]==0 and my_datac[43][0]==0 and my_datac[44][0]==0 and my_datac[45][0]==0 and my_datac[46][0]==0 and my_datac[47][0]==0  \
                and my_datac[48][0]==0 and my_datac[49][0]==0 and my_datac[50][0]==0  and



                my_datacva[0][0]==0 and my_datacva[1][0]==0 and my_datacva[2][0]==0 and my_datacva[3][0]==0 and my_datacva[4][0]==0 and my_datacva[5][0]==0 \
                and my_datacva[6][0]==0 and my_datacva[7][0]==0 and my_datacva[8][0]==0 and my_datacva[9][0]==0 and my_datacva[10][0]==0 and my_datacva[11][0]==0 \
                and my_datacva[12][0]==0 and my_datacva[13][0]==0 and my_datacva[14][0]==0 and my_datacva[15][0]==0 and my_datacva[16][0]==0 and my_datacva[17][0]==0 \
                and my_datacva[18][0]==0 and my_datacva[19][0]==0 and my_datacva[20][0]==0 and my_datacva[21][0]==0 and my_datacva[22][0]==0 and my_datacva[23][0]==0 \
                and my_datacva[24][0]==0 and my_datacva[25][0]==0 and my_datacva[26][0]==0 and my_datacva[27][0]==0 and my_datacva[28][0]==0 and my_datacva[29][0]==0 \
                and my_datacva[30][0]==0 and my_datacva[31][0]==0 and my_datacva[32][0]==0 and my_datacva[33][0]==0 and my_datacva[34][0]==0 and my_datacva[35][0]==0 \
                and my_datacva[36][0]==0 and my_datacva[37][0]==0 and my_datacva[38][0]==0 and my_datacva[39][0]==0 and my_datacva[40][0]==0 and my_datacva[41][0]==0 \
                and my_datacva[42][0]==0 and my_datacva[43][0]==0 and my_datacva[44][0]==0 and my_datacva[45][0]==0 and my_datacva[46][0]==0 and my_datacva[47][0]==0  \
                and my_datacva[48][0]==0 and my_datacva[49][0]==0 and my_datacva[50][0]==0 ):
                self.quote_widget.color=[1,0,0,1]
                #self.quote_widget.text = '10Kgs \n NA '

                
                    
                #self.quote_widget.text = '10Kg \n LL %s (%s)' % (d ,  dif)


                
            elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
                or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0 \
                 or my_datac[12][0]==0 or my_datac[13][0]==0 or my_datac[14][0]==0 or my_datac[15][0]==0 or my_datac[16][0]==0 or my_datac[17][0]==0 \
                or my_datac[18][0]==0 or my_datac[19][0]==0 or my_datac[20][0]==0 or my_datac[21][0]==0 or my_datac[22][0]==0 or my_datac[23][0]==0 \
                  or my_datac[24][0]==0 or my_datac[25][0]==0 or my_datac[26][0]==0 or my_datac[27][0]==0 or my_datac[28][0]==0 or my_datac[29][0]==0 \
                or my_datac[30][0]==0 or my_datac[31][0]==0 or my_datac[32][0]==0 or my_datac[33][0]==0 or my_datac[34][0]==0 or my_datac[35][0]==0 \
                or my_datac[36][0]==0 or my_datac[37][0]==0 or my_datac[38][0]==0 or my_datac[39][0]==0 or my_datac[40][0]==0 or my_datac[41][0]==0 \
                or my_datac[42][0]==0 or my_datac[43][0]==0 or my_datac[44][0]==0 or my_datac[45][0]==0 or my_datac[46][0]==0 or my_datac[47][0]==0  \
                or my_datac[48][0]==0 or my_datac[49][0]==0 or my_datac[50][0]==0  ):
                self.quote_widget.color=[1,1,0,1]
                
                
                     
            
                    
                



            dp=0
            n=0
            while n <= 50:
                dp=dp+my_data[n][0]
                n=n+1
            d=str(dp)

            

            if bb==0:
                dpv=0
                n=0
                while n <= 50:
                    dpv=dpv+my_datav[n][0]
                    n=n+1
                
                dif=str(dp-dpv)

            dp=0
            n=0
            while n <= 50:
                dp=dp+my_datava[n][0]
                n=n+1
            dva=str(dp)

            

            if bb==0:
                dpv=0
                n=0
                while n <= 50:
                    dpv=dpv+my_datavva[n][0]
                    n=n+1
                
                difva=str(dp-dpv)


            self.quote_widget.text = '10Kg \n LL %s (%s)  \n V %s (%s)' % (d ,  dif, dva, difva)
            
            cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
            
            my_data  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE
                ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))

            my_datac  = cursor.fetchall()


            cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
               ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau-one_day,))
            
            my_datav  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE
             ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau-one_day,))

            my_datacv  = cursor.fetchall()
            ##print "DATA", my_data

            bb2=0
            if not my_datav:
                        #self.manager.current = 'in'
                        bb2=1
                        dif=str("ND")
                        #toda=self.ndia.text


            cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
                 ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
            
            my_data4  = cursor.fetchall()

            #print "DATA4", my_data4


            cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE
                  ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))

            my_datac4  = cursor.fetchall()


            cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau-one_day,))
            
            my_datav4  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE
                 ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau-one_day,))

            my_datacv4  = cursor.fetchall()
            ##print "DATA", my_data

            bb24=0
            if not my_datav4:
                        #self.manager.current = 'in'
                        bb24=1
                        dif4=str("ND")
                        #toda=self.ndia.text



                        
            
            self.quote_widget2.color=[1,1,1,1] 
            if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
                and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0 \
                and my_datac[12][0]==0 and my_datac[13][0]==0 and my_datac[14][0]==0 and my_datac[15][0]==0 and my_datac[16][0]==0 and my_datac[17][0]==0 \
                and my_datac[18][0]==0 and my_datac[19][0]==0 and my_datac[20][0]==0 and my_datac[21][0]==0 and my_datac[22][0]==0 and my_datac[23][0]==0 \
                and my_datac[24][0]==0 and my_datac[25][0]==0 and my_datac[26][0]==0 and my_datac[27][0]==0 \
                and my_datac4[0][0]==0 and my_datac4[1][0]==0 and my_datac4[2][0]==0 and my_datac4[3][0]==0 and my_datac4[4][0]==0 and my_datac4[5][0]==0 \
                and my_datac4[6][0]==0 and my_datac[7][0]==0 and my_datac4[8][0]==0 and my_datac4[9][0]==0 and my_datac4[10][0]==0 and my_datac4[11][0]==0)\
                and my_datac4[12][0]==0 and my_datac4[13][0]==0 and my_datac4[14][0]==0 and my_datac4[15][0]==0 and my_datac4[16][0]==0 and my_datac4[17][0]==0 \
                and my_datac4[18][0]==0 and my_datac4[19][0]==0 and my_datac4[20][0]==0 and my_datac4[21][0]==0 and my_datac4[22][0]==0 and my_datac4[23][0]==0 \
                and my_datac4[24][0]==0 and my_datac4[25][0]==0 and my_datac4[26][0]==0 and my_datac4[27][0]==0 :
                self.quote_widget2.color=[1,0,0,1]
                #self.quote_widget2.text = '18/43 Kg \n NA '
                dp=0
                n=0
                while n <= 27:
                    dp=dp+my_data[n][0]
                    n=n+1
                d=str(dp)

                if bb2==0:
                    dpv=0
                    n=0
                    while n <= 27:
                        dpv=dpv+my_datav[n][0]
                        n=n+1
                    
                    dif=str(dp-dpv)

                dp4=0
                n=0
                while n <= 27:
                    dp4=dp4+my_data4[n][0]
                    n=n+1
                d4=str(dp4)

                if bb24==0:
                    dpv4=0
                    n=0
                    while n <= 27:
                        dpv4=dpv4+my_datav4[n][0]
                        n=n+1
                    
                    dif4=str(dp4-dpv4)
                self.quote_widget2.text = '18/43 Kg  \n %s/%s  \n (%s/%s)' % (d,d4 ,  dif,dif4)
                


                
            elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
                or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0 \
                or my_datac[12][0]==0 or my_datac[13][0]==0 or my_datac[14][0]==0 or my_datac[15][0]==0 or my_datac[16][0]==0 or my_datac[17][0]==0 \
                or my_datac[18][0]==0 or my_datac[19][0]==0 or my_datac[20][0]==0 or my_datac[21][0]==0 or my_datac[22][0]==0 or my_datac[23][0]==0 \
                or my_datac[24][0]==0 or my_datac[25][0]==0 or my_datac[26][0]==0 or my_datac[27][0]==0 \
                or my_datac4[0][0]==0 or my_datac4[1][0]==0 or my_datac4[2][0]==0 or my_datac4[3][0]==0 or my_datac4[4][0]==0 or my_datac4[5][0]==0 \
                or my_datac4[6][0]==0 or my_datac4[7][0]==0 or my_datac4[8][0]==0 or my_datac4[9][0]==0 or my_datac4[10][0]==0 or my_datac4[11][0]==0)\
                or my_datac4[12][0]==0 or my_datac4[13][0]==0 or my_datac4[14][0]==0 or my_datac4[15][0]==0 or my_datac4[16][0]==0 or my_datac4[17][0]==0 \
                or my_datac4[18][0]==0 or my_datac4[19][0]==0 or my_datac4[20][0]==0 or my_datac4[21][0]==0 or my_datac4[22][0]==0 or my_datac4[23][0]==0 \
                  or my_datac4[24][0]==0 or my_datac4[25][0]==0 or my_datac4[26][0]==0 or my_datac4[27][0]==0:
                self.quote_widget2.color=[1,1,0,1]
                dp=0
                n=0
                while n <= 27:
                    dp=dp+my_data[n][0]
                    n=n+1
                d=str(dp)

                if bb2==0:
                    dpv=0
                    n=0
                    while n <= 27:
                        dpv=dpv+my_datav[n][0]
                        n=n+1
                    
                    dif=str(dp-dpv)

                dp4=0
                n=0
                while n <= 27:
                    dp4=dp4+my_data4[n][0]
                    n=n+1
                d4=str(dp4)

                if bb24==0:
                    dpv4=0
                    n=0
                    while n <= 27:
                        dpv4=dpv4+my_datav4[n][0]
                        n=n+1
                    
                    dif4=str(dp4-dpv4)
                self.quote_widget2.text = '18/43 Kg  \n %s/%s  \n (%s/%s)' % (d,d4 ,  dif,dif4)
                     
            else:
                dp=0
                n=0
                while n <= 27:
                    dp=dp+my_data[n][0]
                    n=n+1
                d=str(dp)

                if bb2==0:
                    dpv=0
                    n=0
                    while n <= 27:
                        dpv=dpv+my_datav[n][0]
                        n=n+1
                    
                    dif=str(dp-dpv)

                dp4=0
                n=0
                while n <= 27:
                    dp4=dp4+my_data4[n][0]
                    n=n+1
                d4=str(dp4)

                if bb24==0:
                    dpv4=0
                    n=0
                    while n <= 27:
                        dpv4=dpv4+my_datav4[n][0]
                        n=n+1
                    
                    dif4=str(dp4-dpv4)
                self.quote_widget2.text = '18/43 Kg  \n %s/%s  \n (%s/%s)' % (d,d4 ,  dif,dif4)




        else:
            
        
            cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
               ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='ll') ''', (todau,))
            
            my_data  = cursor.fetchall()


            cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
               ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='v') ''', (todau,))
            
            my_datava  = cursor.fetchall()

            


            cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='ll' ) ''', (todau,))

            my_datac  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='v' ) ''', (todau,))

            my_datacva  = cursor.fetchall()


            
            cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
               ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='ll'  ) ''', (todau-one_day,))
            
            my_datav  = cursor.fetchall()



            cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='v'  ) ''', (todau-one_day,))
            
            my_datavva = cursor.fetchall()
            


            cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='ll' ) ''', (todau-one_day,))

            my_datacv  = cursor.fetchall()

            cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
               ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='10' AND ESTADO='v' ) ''', (todau-one_day,))

            my_datacvva  = cursor.fetchall()


            

            
            bb=0
            if not my_datav:
                        #self.manager.current = 'in'
                        bb=1
                        dif=str("ND")
                        difva=str("ND")
                        #toda=self.ndia.text
            



            

    ##        bio=0
    ##        if not my_data:
    ##            self.manager.current = 'in'
    ##            bio=1
    ##            
    ##        #print "DATA", my_data
    ##        if bio==0:
            self.quote_widget.color=[1,1,1,1] 
            if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
                and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0 \
                and my_datac[12][0]==0 and my_datac[13][0]==0 and my_datac[14][0]==0 and my_datac[15][0]==0 and my_datac[16][0]==0 and my_datac[17][0]==0 \
                and my_datac[18][0]==0 and my_datac[19][0]==0 and my_datac[20][0]==0 and my_datac[21][0]==0 and my_datac[22][0]==0 and my_datac[23][0]==0 \
                and my_datac[24][0]==0 and my_datac[25][0]==0 and my_datac[26][0]==0 and my_datac[27][0]==0 and my_datac[28][0]==0 and my_datac[29][0]==0 \
                and my_datac[30][0]==0 and my_datac[31][0]==0 and my_datac[32][0]==0 and my_datac[33][0]==0 and my_datac[34][0]==0 and my_datac[35][0]==0 \
                and my_datac[36][0]==0 and my_datac[37][0]==0 and my_datac[38][0]==0 and my_datac[39][0]==0 and my_datac[40][0]==0 and my_datac[41][0]==0 \
                



                and my_datacva[0][0]==0 and my_datacva[1][0]==0 and my_datacva[2][0]==0 and my_datacva[3][0]==0 and my_datacva[4][0]==0 and my_datacva[5][0]==0 \
                and my_datacva[6][0]==0 and my_datacva[7][0]==0 and my_datacva[8][0]==0 and my_datacva[9][0]==0 and my_datacva[10][0]==0 and my_datacva[11][0]==0 \
                and my_datacva[12][0]==0 and my_datacva[13][0]==0 and my_datacva[14][0]==0 and my_datacva[15][0]==0 and my_datacva[16][0]==0 and my_datacva[17][0]==0 \
                and my_datacva[18][0]==0 and my_datacva[19][0]==0 and my_datacva[20][0]==0 and my_datacva[21][0]==0 and my_datacva[22][0]==0 and my_datacva[23][0]==0 \
                and my_datacva[24][0]==0 and my_datacva[25][0]==0 and my_datacva[26][0]==0 and my_datacva[27][0]==0 and my_datacva[28][0]==0 and my_datacva[29][0]==0 \
                and my_datacva[30][0]==0 and my_datacva[31][0]==0 and my_datacva[32][0]==0 and my_datacva[33][0]==0 and my_datacva[34][0]==0 and my_datacva[35][0]==0 \
                and my_datacva[36][0]==0 and my_datacva[37][0]==0 and my_datacva[38][0]==0 and my_datacva[39][0]==0 and my_datacva[40][0]==0 and my_datacva[41][0]==0 \
               ):
                self.quote_widget.color=[1,0,0,1]
                #self.quote_widget.text = '10Kgs \n NA '

                
                    
                #self.quote_widget.text = '10Kg \n LL %s (%s)' % (d ,  dif)


                
            elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
                or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0 \
                 or my_datac[12][0]==0 or my_datac[13][0]==0 or my_datac[14][0]==0 or my_datac[15][0]==0 or my_datac[16][0]==0 or my_datac[17][0]==0 \
                or my_datac[18][0]==0 or my_datac[19][0]==0 or my_datac[20][0]==0 or my_datac[21][0]==0 or my_datac[22][0]==0 or my_datac[23][0]==0 \
                  or my_datac[24][0]==0 or my_datac[25][0]==0 or my_datac[26][0]==0 or my_datac[27][0]==0 or my_datac[28][0]==0 or my_datac[29][0]==0 \
                or my_datac[30][0]==0 or my_datac[31][0]==0 or my_datac[32][0]==0 or my_datac[33][0]==0 or my_datac[34][0]==0 or my_datac[35][0]==0 \
                or my_datac[36][0]==0 or my_datac[37][0]==0 or my_datac[38][0]==0 or my_datac[39][0]==0 or my_datac[40][0]==0 or my_datac[41][0]==0 \
                 ):
                self.quote_widget.color=[1,1,0,1]
                
                
                     
            
                    
                



            dp=0
            n=0
            while n <= 41:
                dp=dp+my_data[n][0]
                n=n+1
            d=str(dp)

            

            if bb==0:
                dpv=0
                n=0
                while n <= 41:
                    dpv=dpv+my_datav[n][0]
                    n=n+1
                
                dif=str(dp-dpv)

            dp=0
            n=0
            while n <= 41:
                dp=dp+my_datava[n][0]
                n=n+1
            dva=str(dp)

            

            if bb==0:
                dpv=0
                n=0
                while n <= 41:
                    dpv=dpv+my_datavva[n][0]
                    n=n+1
                
                difva=str(dp-dpv)


            self.quote_widget.text = '10Kg \n LL %s (%s)  \n V %s (%s)' % (d ,  dif, dva, difva)
            
            cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
            
            my_data  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
                ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))

            my_datac  = cursor.fetchall()


            cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
               ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau-one_day,))
            
            my_datav  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
             ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau-one_day,))

            my_datacv  = cursor.fetchall()
            ##print "DATA", my_data

            bb2=0
            if not my_datav:
                        #self.manager.current = 'in'
                        bb2=1
                        dif=str("ND")
                        #toda=self.ndia.text


            cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
                 ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
            
            my_data4  = cursor.fetchall()

            #print "DATA4", my_data4


            cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
                  ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))

            my_datac4  = cursor.fetchall()


            cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
              ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau-one_day,))
            
            my_datav4  = cursor.fetchall()


            cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
                 ( FECHA = ?  AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau-one_day,))

            my_datacv4  = cursor.fetchall()
            ##print "DATA", my_data

            bb24=0
            if not my_datav4:
                        #self.manager.current = 'in'
                        bb24=1
                        dif4=str("ND")
                        #toda=self.ndia.text



                        
            
            self.quote_widget2.color=[1,1,1,1] 
            if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and
                my_datac[4][0]==0 and my_datac[5][0]==0 \
                and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0
                and my_datac[10][0]==0 and my_datac[11][0]==0 \
                and my_datac[12][0]==0 and my_datac[13][0]==0 and my_datac[14][0]==0 and my_datac[15][0]==0
                and my_datac[16][0]==0 and my_datac[17][0]==0 \
                and my_datac[18][0]==0 and my_datac[19][0]==0 and my_datac[20][0]==0 and my_datac[21][0]==0
                and my_datac[22][0]==0 and my_datac[23][0]==0 \
                and my_datac[24][0]==0 and my_datac[25][0]==0 and my_datac[26][0]==0 and my_datac[27][0]==0 \
                and my_datac4[0][0]==0 and my_datac4[1][0]==0 and my_datac4[2][0]==0 and my_datac4[3][0]==0
                and my_datac4[4][0]==0 and my_datac4[5][0]==0 \
                and my_datac4[6][0]==0 and my_datac[7][0]==0 and my_datac4[8][0]==0 and my_datac4[9][0]==0
                and my_datac4[10][0]==0 and my_datac4[11][0]==0\
                and my_datac4[12][0]==0 and my_datac4[13][0]==0 and my_datac4[14][0]==0 and my_datac4[15][0]==0
                  and my_datac4[16][0]==0 and my_datac4[17][0]==0 \
                and my_datac4[18][0]==0 and my_datac4[19][0]==0 ):
                self.quote_widget2.color=[1,0,0,1]
                #self.quote_widget2.text = '18/43 Kg \n NA '
                dp=0
                n=0
                while n <= 27:
                    dp=dp+my_data[n][0]
                    n=n+1
                d=str(dp)

                if bb2==0:
                    dpv=0
                    n=0
                    while n <= 27:
                        dpv=dpv+my_datav[n][0]
                        n=n+1
                    
                    dif=str(dp-dpv)

                dp4=0
                n=0
                while n <= 19:
                    dp4=dp4+my_data4[n][0]
                    n=n+1
                d4=str(dp4)

                if bb24==0:
                    dpv4=0
                    n=0
                    while n <= 19:
                        dpv4=dpv4+my_datav4[n][0]
                        n=n+1
                    
                    dif4=str(dp4-dpv4)
                self.quote_widget2.text = '18/43 Kg  \n %s/%s  \n (%s/%s)' % (d,d4 ,  dif,dif4)
                


                
            elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
                or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0 \
                or my_datac[12][0]==0 or my_datac[13][0]==0 or my_datac[14][0]==0 or my_datac[15][0]==0 or my_datac[16][0]==0 or my_datac[17][0]==0 \
                or my_datac[18][0]==0 or my_datac[19][0]==0 or my_datac[20][0]==0 or my_datac[21][0]==0 or my_datac[22][0]==0 or my_datac[23][0]==0 \
                or my_datac[24][0]==0 or my_datac[25][0]==0 or my_datac[26][0]==0 or my_datac[27][0]==0 \
                or my_datac4[0][0]==0 or my_datac4[1][0]==0 or my_datac4[2][0]==0 or my_datac4[3][0]==0 or my_datac4[4][0]==0 or my_datac4[5][0]==0 \
                or my_datac4[6][0]==0 or my_datac4[7][0]==0 or my_datac4[8][0]==0 or my_datac4[9][0]==0 or my_datac4[10][0]==0 or my_datac4[11][0]==0\
                or my_datac4[12][0]==0 or my_datac4[13][0]==0 or my_datac4[14][0]==0 or my_datac4[15][0]==0 or my_datac4[16][0]==0 or my_datac4[17][0]==0 \
                or my_datac4[18][0]==0 or my_datac4[19][0]==0):
                self.quote_widget2.color=[1,1,0,1]
                dp=0
                n=0
                while n <= 27:
                    dp=dp+my_data[n][0]
                    n=n+1
                d=str(dp)

                if bb2==0:
                    dpv=0
                    n=0
                    while n <= 27:
                        dpv=dpv+my_datav[n][0]
                        n=n+1
                    
                    dif=str(dp-dpv)

                dp4=0
                n=0
                while n <= 19:
                    dp4=dp4+my_data4[n][0]
                    n=n+1
                d4=str(dp4)

                if bb24==0:
                    dpv4=0
                    n=0
                    while n <= 19:
                        dpv4=dpv4+my_datav4[n][0]
                        n=n+1
                    
                    dif4=str(dp4-dpv4)
                self.quote_widget2.text = '18/43 Kg  \n %s/%s  \n (%s/%s)' % (d,d4 ,  dif,dif4)
                     
            else:
                dp=0
                n=0
                while n <= 27:
                    dp=dp+my_data[n][0]
                    n=n+1
                d=str(dp)

                if bb2==0:
                    dpv=0
                    n=0
                    while n <= 27:
                        dpv=dpv+my_datav[n][0]
                        n=n+1
                    
                    dif=str(dp-dpv)

                dp4=0
                n=0
                while n <= 27:
                    dp4=dp4+my_data4[n][0]
                    n=n+1
                d4=str(dp4)

                if bb24==0:
                    dpv4=0
                    n=0
                    while n <= 27:
                        dpv4=dpv4+my_datav4[n][0]
                        n=n+1
                    
                    dif4=str(dp4-dpv4)
                self.quote_widget2.text = '18/43 Kg  \n %s/%s  \n (%s/%s)' % (d,d4 ,  dif,dif4)


   

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)

        











class INVENTARIOScreen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    quote_widget4 = ObjectProperty()
    quote_widget5 = ObjectProperty()
    quote_widget6 = ObjectProperty()
    quote_widget7 = ObjectProperty()
    quote_widget8 = ObjectProperty()
    quote_widget9 = ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()

    
    locat = StringProperty()

    

    def __init__(self, **kwargs):
        super(INVENTARIOScreen, self).__init__(**kwargs)
        self.create()
        #self.get_date()
        #self.display_quote()



##    def set_llocation(self):
##        if self.locat=='l1':
##            self.quote_widget2.text='LINEA 1'
##        elif self.locat=='l2':
##            self.quote_widget2.text='LINEA 2'

            
    def set_location(self,loc):
        self.locat=loc
        #print "LOCATION_INV", self.locat
        


    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
    
        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'l2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'l2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget.text = 'LINEA 2  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget.text = 'LINEA 2  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget.text = 'LINEA 2  \n %s ' % d




        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'l1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'l1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget2.text = 'LINEA 1 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'LINEA 1  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'LINEA 1  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'LINEA 1  \n %s ' % d


        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA PLATAFORMA 2", my_data
        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget3.text = 'PLATAFORMA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget3.text = 'PLATAFORMA 2 \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget3.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget3.text = 'PLATAFORMA 2 \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget3.text = 'PLATAFORMA 2 (NO EPSDC) \n %s ' % d



        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pag' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pag' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget4.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget4.color=[1,0,0,1]
            #self.quote_widget4.text = 'PATIO GANDOLA (CARGA) \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget4.text = 'PATIO GANDOLA (CARGA)  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget4.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget4.text = 'PATIO GANDOLA (CARGA)  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget4.text = 'PATIO GANDOLA (CARGA)  \n %s ' % d

        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pa1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pa1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget5.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget5.color=[1,0,0,1]
            #self.quote_widget5.text = 'PATIO 1 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget5.text = 'PATIO 1  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget5.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget5.text = 'PATIO 1  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget5.text = 'PATIO 1  \n %s ' % d


        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pa2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pa2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget6.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget6.color=[1,0,0,1]
            #self.quote_widget6.text = 'PATIO 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget6.text = 'PATIO 2  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget6.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget6.text = 'PATIO 2  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget6.text = 'PATIO 2  \n %s ' % d



##
##        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
##        
##        my_data  = cursor.fetchall()
##
##
##        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
##
##        my_datac  = cursor.fetchall()
##        #print "DATA", my_data
##        
##        self.quote_widget7.color=[1,1,1,1] 
##        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
##            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
##            self.quote_widget7.color=[1,0,0,1]
##            #self.quote_widget7.text = 'PLATAFORMA 1 \n NA '
##            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
##                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
##            self.quote_widget7.text = 'PLATAFORMA 1 (NO EPSDC) \n %s ' % d
##        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
##            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
##            self.quote_widget7.color=[1,1,0,1]
##            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
##                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
##            self.quote_widget7.text = 'PLATAFORMA 1 (NO EPSDC) \n %s ' % d
##                 
##        else:
##            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
##                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
##            self.quote_widget7.text = 'PLATAFORMA 1 (NO EPSDC) \n %s ' % d



        ############################

        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data1  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac1  = cursor.fetchall()
        #print "DATA", my_data
##        
##        self.quote_widget7.color=[1,1,1,1] 
##        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
##            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
##            self.quote_widget7.color=[1,0,0,1]
##            #self.quote_widget7.text = 'PLATAFORMA 1 \n NA '
##            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
##                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
##            self.quote_widget7.text = 'PLATAFORMA 1 (NO EPSDC) \n %s ' % d
##        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
##            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
##            self.quote_widget7.color=[1,1,0,1]
##            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
##                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
##            self.quote_widget7.text = 'PLATAFORMA 1 (NO EPSDC) \n %s ' % d
##                 
##        else:
##            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
##                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
##            self.quote_widget7.text = 'PLATAFORMA 1 (NO EPSDC) \n %s ' % d



        

        ############################




        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'epsdc'  AND CAPACIDAD='10' AND (ORIGEN='0' OR ORIGEN='2') ) ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'epsdc'  AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget8.color=[1,1,1,1] 
        if (my_datac1[0][0]==0 and my_datac1[1][0]==0 and my_datac[2][0]==0 and my_datac1[3][0]==0 and my_datac1[4][0]==0 and my_datac1[5][0]==0 and my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0):
            self.quote_widget8.color=[1,0,0,1]
            #self.quote_widget8.text = 'EPSDC \n NA '
            d= str(my_data1[0][0]+my_data1[1][0]+my_data1[2][0]+my_data1[3][0]+my_data1[4][0]+my_data1[5][0]+my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            self.quote_widget8.text = 'EPSDC   \n %s ' % d
        elif (my_datac1[0][0]==0 or my_datac1[1][0]==0 or my_datac[2][0]==0 or my_datac1[3][0]==0 or my_datac1[4][0]==0 and my_datac1[5][0]==0 or my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0):
            self.quote_widget8.color=[1,1,0,1]
            d= str(my_data1[0][0]+my_data1[1][0]+my_data1[2][0]+my_data1[3][0]+my_data1[4][0]+my_data1[5][0]+my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            self.quote_widget8.text = 'EPSDC   \n %s ' % d
                 
        else:
            d= str(my_data1[0][0]+my_data1[1][0]+my_data1[2][0]+my_data1[3][0]+my_data1[4][0]+my_data1[5][0]+my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            self.quote_widget8.text = 'EPSDC   \n %s ' % d



        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla43' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla43' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget9.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget9.color=[1,0,0,1]
            #self.quote_widget9.text = 'EPSDC \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget9.text = 'PLATAFORMA 43   \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget9.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget9.text = 'PLATAFORMA 43   \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget9.text = 'PLATAFORMA 43   \n %s ' % d




            


     
    

    def create(self):
        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)
        #print "Opened database successfully";
        #INT     NOT NULL
        conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
               (ID INT PRIMARY KEY   NOT NULL,
                UBICACION           CHAR(50),
                TIPO                CHAR(50),
                ORIGEN                CHAR(50),
                CONDICION                CHAR(50),
                CAPACIDAD                CHAR(50),
                ESTADO                CHAR(50),
                CANTIDAD            INT     NOT NULL,
                CONSULTAS           INT     NOT NULL,
                FECHA  date );''')

        #print "Table created successfully";
        conn.close()




       # ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA 

        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)

        iterator = conn.execute('SELECT max(ID), UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA  FROM COMPANY')
        #max_id = iterator.fetchone()[0]
        user1 = iterator.fetchone() #retrieve the first row
        max_id= user1[0]
        last_day = user1[9]

        #last_day = last_day - one_day

        
        
        #user1 = cursor

        #UBICACION - plat43,pa43,l1,l2,pa,pal1,pla1pa,pla2,2,gandola,fle17 (fleteros),fle18,eps1662,eps1661,eps5696,fp (fuera de planta)
        #TIPO - p (plastico),ag (autogas),cln (cli-pon),tp (troquel privado)
        #ORIGEN eps
        #CONDICION op,nop, ph
        #CAPACIDAD 10,18,43
        #ESTADO ll,v
        
        
       
        
        #print "FECHA today = ", today
        #print "FECHA last day = ", last_day
        
        
        
        if max_id == None :
                 max_id=1
                 my_data = [
                   (max_id,'l2', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+1,'l2', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+2,'l2', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+3,'l2', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+4,'l2', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+5,'l2', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+6,'l2', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+7,'l2', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+8,'l2', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+9,'l2', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+10,'l2', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+11,'l2', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),


                   (max_id+12,'l1', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+13,'l1', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+14,'l1', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+15,'l1', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+16,'l1', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+17,'l1', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+18,'l1', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+19,'l1', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+20,'l1', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+21,'l1', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+22,'l1', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+23,'l1', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+24,'pla2', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+25,'pla2', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+26,'pla2', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+27,'pla2', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+28,'pla2', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+29,'pla2', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+30,'pla2', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+31,'pla2', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   

                   (max_id+32,'pla2', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+33,'pla2', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+34,'pla2', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+35,'pla2', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+36,'pag', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+37,'pag', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+38,'pag', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+39,'pag', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+40,'pag', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+41,'pag', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+42,'pag', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+43,'pag', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+44,'pag', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+45,'pag', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+46,'pag', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+47,'pag', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+48,'pa1', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+49,'pa1', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+50,'pa1', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+51,'pa1', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+52,'pa1', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+53,'pa1', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+54,'pa1', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+55,'pa1', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+56,'pa1', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+57,'pa1', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+58,'pa1', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+59,'pa1', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+60,'pa2', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+61,'pa2', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+62,'pa2', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+63,'pa2', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+64,'pa2', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+65,'pa2', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+66,'pa2', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+67,'pa2', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+68,'pa2', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+69,'pa2', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+70,'pa2', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+71,'pa2', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+72,'pla1', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+73,'pla1', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+74,'pla1', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+75,'pla1', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+76,'pla1', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+77,'pla1', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+78,'pla1', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+79,'pla1', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+80,'pla1', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+81,'pla1', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+82,'pla1', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+83,'pla1', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+84,'epsdc', 'cln','0','op', '10', 'll',  0, 0, today),
                   (max_id+85,'epsdc', 'cln','0', 'op', '10', 'v',  0,  0, today),
                   (max_id+86,'epsdc', 'cln','1', 'op', '10', 'll',  0,  0, today),
                   (max_id+87,'epsdc', 'cln','1', 'op', '10', 'v',  0,  0, today),
                   
                   (max_id+88,'epsdc', 'cln', '2', 'op', '10', 'll',  0,  0, today),
                   (max_id+89,'epsdc', 'cln', '2', 'op', '10', 'v',  0,  0, today),
##                   (max_id+90,'epsdcn', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
##                   (max_id+91,'epsdcn', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
##                   
##                   (max_id+92,'epsdcn', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
##                   (max_id+93,'epsdcn', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
##                   (max_id+94,'epsdcn', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
##                   (max_id+95,'epsdcn', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+90,'pla43', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+91,'pla43', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+92,'pla43', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+93,'pla43', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+94,'pla43', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+95,'pla43', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+96,'pla43', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+97,'pla43', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+98,'pla43', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+99,'pla43', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+100,'pla43', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+101,'pla43', 'p', 'eps', 'nop', '10', 'v',  0,  0, today)

                                  ]
                            
                            
                   
                 conn.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?)",my_data) 
                

                            
        else:
            if last_day < today:
##                #print "FECHA = ", user1[1]
##                #print "FECHA today = ", today
                #print "FECHA ANTERIOR", last_day

                #last_day=today
                

                conn = sqlite3.connect('planta47.db')
    
                cursor = conn.execute('''SELECT  ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA from COMPANY  WHERE  \
                FECHA = ?  ''', (last_day,))
        
                my_data  = cursor.fetchall()

                #print "tuple", my_data
                

                #data=list(my_data)
                data=[]

##                for i in my_data:
##                    data.append(list(i))

                data=[list(i) for i in my_data]

                #print "ESTE ES !!", data
                    
                

                max_id = max_id +1
##
                for i in data:
                    i[0]= max_id
                    i[8]= 0
                    i[9]= today
                    max_id = max_id +1
                    #print i , "\n"
                    

##                for i in range(len(data)):
##                    data[i][0]= max_id
##                    data[i][8]= 0
##                    max_id = max_id +1
                m_data=[]
                for i in data:
                    #m_data.append(tuple(i))
                    conn.execute("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?)",i) 
                    
                #my_data=(tuple(i) for i in data)

                #print m_data
                                

                #conn.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?)",m_data) 
                ##print "ESTE ES !!", my_data
                

                          
        conn.commit()
        cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##        for row in cursor:
##           #print "ID = ", row[0]
##           #print "FECHA = ", row[1]
##           #print "UBICACION = ", row[2]
##           #print "TIPO = ", row[3]
##           #print "Numero de cilindros = ", row[4], "\n"
##
##        #print "Records created successfully";
        conn.close()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
            #print "otro"
        else:
            #print "hoy"
            todau= today
        self.dia.text= str(todau)

            
            #self.dia.text= str(today)

    


class INVENTARIO2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    quote_widget4 = ObjectProperty()
    quote_widget5 = ObjectProperty()
    quote_widget6 = ObjectProperty()
    quote_widget7 = ObjectProperty()
    quote_widget8 = ObjectProperty()
    quote_widget9 = ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()

    
    locat = StringProperty()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
            #print "otro"
        else:
            #print "hoy"
            todau= today
        self.dia.text= str(todau)

    

    def __init__(self, **kwargs):
        super(INVENTARIO2Screen, self).__init__(**kwargs)
        self.create()
        #self.display_quote()



##    def set_llocation(self):
##        if self.locat=='l1':
##            self.quote_widget2.text='LINEA 1'
##        elif self.locat=='l2':
##            self.quote_widget2.text='LINEA 2'


    
            
    def set_location(self,loc):
        self.locat=loc
        #print "LOCATION_INV", self.locat
        


    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
    
        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget.text = 'LINEA 2  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget.text = 'LINEA 2  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget.text = 'LINEA 2  \n %s/%s ' % (d,  d2)



        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget2.text = 'LINEA 1  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget2.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget2.text = 'LINEA 1  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget2.text = 'LINEA 1  \n %s/%s ' % (d,  d2)



        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
          ( FECHA = ? AND UBICACION= 'pla2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE
           ( FECHA = ? AND UBICACION= 'pla2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
             ( FECHA = ? AND UBICACION= 'pla2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE
           ( FECHA = ? AND UBICACION= 'pla2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget3.text = 'PLATAFORMA 2  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget3.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget3.text = 'PLATAFORMA 2  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget3.text = 'PLATAFORMA 2  \n %s/%s ' % (d,  d2)



        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
         ( FECHA = ? AND UBICACION= 'pa1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE
        ( FECHA = ? AND UBICACION= 'pa1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE
        ( FECHA = ? AND UBICACION= 'pa1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE
        ( FECHA = ? AND UBICACION= 'pa1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget5.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget5.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget5.text = 'PATIO 1  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget5.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget5.text = 'PATIO 1  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget5.text = 'PATIO 1  \n %s/%s ' % (d,  d2)



        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pa2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pa2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pa2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pa2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget6.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget6.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget6.text = 'PATIO 2  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget6.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget6.text = 'PATIO 2  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget6.text = 'PATIO 2  \n %s/%s ' % (d,  d2)




        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget7.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget7.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget7.text = 'PLATAFORMA 1  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget7.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget7.text = 'PLATAFORMA 1  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget7.text = 'PLATAFORMA 1  \n %s/%s ' % (d,  d2)




        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla43' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla43' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla43' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'pla43' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget9.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget9.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget9.text = 'PLATAFORMA 43  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget9.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget9.text = 'PLATAFORMA 43  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget9.text = 'PLATAFORMA 43  \n %s/%s ' % (d,  d2)

       
    



            


     
    

    def create(self):
        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)
        #print "Opened database successfully";
        #INT     NOT NULL
        conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY2
               (ID INT PRIMARY KEY   NOT NULL,
                UBICACION           CHAR(50),
                TIPO                CHAR(50),
                ORIGEN                CHAR(50),
                CONDICION                CHAR(50),
                CAPACIDAD                CHAR(50),
                ESTADO                CHAR(50),
                CANTIDAD            INT     NOT NULL,
                CONSULTAS           INT     NOT NULL,
                FECHA  date );''')

        #print "Table created successfully";
        conn.close()




       # ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA 

        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)

        iterator = conn.execute('SELECT max(ID), UBICACION, TIPO,  ORIGEN, CONDICION,\
                                CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA  FROM COMPANY2')
        #max_id = iterator.fetchone()[0]
        user1 = iterator.fetchone() #retrieve the first row
        max_id= user1[0]
        last_day = user1[9]
##        #print "max_id=", max_id
##        #print "FECHA anterior= ", user1[9]
##        #print "FECHA today = ", today
        #user1 = cursor

        #UBICACION - plat43,pa43,l1,l2,pa,pal1,pla1pa,pla2,2,gandola,fle17 (fleteros),fle18,eps1662,eps1661,eps5696,fp (fuera de planta)
        #TIPO - p (plastico),ag (autogas),cln (cli-pon),tp (troquel privado), r (rosca noruega)
        #ORIGEN eps
        #CONDICION op,nop, ph
        #CAPACIDAD 18,43
        #ESTADO ll,v
        
        
       
       
        
        
        if max_id == None :
                 #print "max_id=", max_id
                 #print "FECHA anterior= ", user1[9]
                 #print "FECHA today = ", today
                 max_id=1
                 my_data = [
                   (max_id,'l2', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+1,'l2', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+2,'l2', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+3,'l2', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+4,'l1', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+5,'l1', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+6,'l1', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+7,'l1', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+8,'pa1', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+9,'pa1', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+10,'pa1', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+11,'pa1', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+12,'pa2', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+13,'pa2', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+14,'pa2', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+15,'pa2', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+16,'pla1', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+17,'pla1', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+18,'pla1', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+19,'pla1', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+20,'pla2', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+21,'pla2', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+22,'pla2', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+23,'pla2', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+24,'l2', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+25,'l2', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+26,'l2', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+27,'l2', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+28,'l1', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+29,'l1', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+30,'l1', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+31,'l1', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+32,'pa1', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+33,'pa1', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+34,'pa1', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+35,'pa1', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+36,'pa2', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+37,'pa2', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+38,'pa2', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+39,'pa2', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+40,'pla1', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+41,'pla1', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+42,'pla1', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+43,'pla1', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+44,'pla2', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+45,'pla2', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+46,'pla2', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+47,'pla2', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+48,'pla43', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+49,'pla43', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+50,'pla43', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+51,'pla43', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+52,'pla43', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+53,'pla43', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+54,'pla43', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+55,'pla43', 'r','eps', 'nop', '43', 'v',  0,  0, today)
                                  ]
                            
                            
                   
                 conn.executemany("INSERT INTO COMPANY2 VALUES (?,?,?,?,?,?,?,?,?,?)",my_data) 
                

                            
        else:
            if last_day < today:
                #print "FECHA ANTERIOR", last_day

                #last_day=today
                

                conn = sqlite3.connect('planta47.db')
    
                cursor = conn.execute('''SELECT  ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA from COMPANY2 WHERE  \
                FECHA = ?  ''', (last_day,))
        
                my_data  = cursor.fetchall()

                #print "tuple", my_data
                

                #data=list(my_data)
                data=[]

##                for i in my_data:
##                    data.append(list(i))

                data=[list(i) for i in my_data]

                #print "ESTE ES !!", data
                    
                

                max_id = max_id +1
##
                for i in data:
                    i[0]= max_id
                    i[8]= 0
                    i[9]= today
                    max_id = max_id +1
                    #print i , "\n"
                    

##                for i in range(len(data)):
##                    data[i][0]= max_id
##                    data[i][8]= 0
##                    max_id = max_id +1
                m_data=[]
                for i in data:
                    #m_data.append(tuple(i))
                    conn.execute("INSERT INTO COMPANY2 VALUES (?,?,?,?,?,?,?,?,?,?)",i) 
                    
                #my_data=(tuple(i) for i in data)

                #print m_data
                                

                #conn.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?)",m_data) 
                ##print "ESTE ES !!", my_data
                

                          
        conn.commit()
        cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad, consultas, capacidad  from COMPANY2 where (fecha=? and ubicacion=?) ",(today,'l2'))
##        for row in cursor:
##           #print "COMPANY2"
##           #print "ID = ", row[0]
##           #print "FECHA = ", row[1]
##           #print "UBICACION = ", row[2]
##           #print "TIPO = ", row[3]
##           #print "Numero de cilindros = ", row[4]
##           #print "Numero de consultas = ", row[5],
##           #print "capacidad = ", row[6],"\n"
##
##        #print "Records created successfully COMPANY2";
        conn.close()




class INVENTARIO3Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    quote_widget4 = ObjectProperty()
    quote_widget5 = ObjectProperty()
    quote_widget6 = ObjectProperty()
    quote_widget7 = ObjectProperty()
    #quote_widget8 = ObjectProperty()
    #quote_widget9 = ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()

    
    locat = StringProperty()

    

    def __init__(self, **kwargs):
        super(INVENTARIO3Screen, self).__init__(**kwargs)
        self.create()
        #self.get_date()
        #self.display_quote()



##    def set_llocation(self):
##        if self.locat=='l1':
##            self.quote_widget2.text='LINEA 1'
##        elif self.locat=='l2':
##            self.quote_widget2.text='LINEA 2'

            
    def set_location(self,loc):
        global ch_loc
        #self.locat=loc
        ch_loc=loc
        self.manager.current = 'vhplinea2'
       # #print "LOCATION_INV", self.locat
        #print "LOCATION_INV", ch_loc
        


    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
    
        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION= 'gan1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
       ( FECHA = ? AND UBICACION= 'gan1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget.text = 'GANDOLA 1  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget.text = 'GANDOLA 1  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget.text = 'GANDOLA 1  \n %s ' % d




        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'gan2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'gan2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget2.text = 'LINEA 1 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'GANDOLA 2  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'GANDOLA 2  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'GANDOLA 1  \n %s ' % d


        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'fle1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'fle1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA PLATAFORMA 2", my_data
        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget3.text = 'PLATAFORMA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget3.text = 'FLETERO 1  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget3.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget3.text = 'FLETERO 1  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget3.text = 'FLETERO 1  \n %s ' % d



        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'fle2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'fle2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget4.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget4.color=[1,0,0,1]
            #self.quote_widget4.text = 'PATIO GANDOLA (CARGA) \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget4.text = 'FLETERO 2  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget4.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget4.text = 'FLETERO 2  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget4.text = 'FLETERO 2  \n %s ' % d

        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'eps1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'eps1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget5.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget5.color=[1,0,0,1]
            #self.quote_widget5.text = 'PATIO 1 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget5.text = 'EPSDC 1  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget5.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget5.text = 'EPSDC 1  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget5.text = 'EPSDC 1  \n %s ' % d


        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget6.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget6.color=[1,0,0,1]
            #self.quote_widget6.text = 'PATIO 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget6.text = 'EPSDC 2  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget6.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget6.text = 'EPSDC 2  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget6.text = 'EPSDC 2  \n %s ' % d




        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'eps3' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE ( FECHA = ? AND UBICACION= 'eps3' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget7.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget7.color=[1,0,0,1]
            #self.quote_widget7.text = 'PLATAFORMA 1 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget7.text = 'EPSDC 3  \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget7.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget7.text = 'EPSDC 3  \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget7.text = 'EPSDC 3  \n %s ' % d




        
            


     
    

    def create(self):
        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)
        #print "Opened database successfully";
        #INT     NOT NULL
        conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY3
               (ID INT PRIMARY KEY   NOT NULL,
                UBICACION           CHAR(50),
                TIPO                CHAR(50),
                ORIGEN                CHAR(50),
                CONDICION                CHAR(50),
                CAPACIDAD                CHAR(50),
                ESTADO                CHAR(50),
                CANTIDAD            INT     NOT NULL,
                CONSULTAS           INT     NOT NULL,
                FECHA  date );''')

        #print "Table created successfully";
        conn.close()




       # ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA 

        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)

        iterator = conn.execute('SELECT max(ID), UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA  FROM COMPANY3')
        #max_id = iterator.fetchone()[0]
        user1 = iterator.fetchone() #retrieve the first row
        max_id= user1[0]
        last_day = user1[9]

        #last_day = last_day - one_day

        
        
        #user1 = cursor

        #UBICACION - plat43,pa43,l1,l2,pa,pal1,pla1pa,pla2,2,gandola,fle17 (fleteros),fle18,eps1662,eps1661,eps5696,fp (fuera de planta)
        #TIPO - p (plastico),ag (autogas),cln (cli-pon),tp (troquel privado)
        #ORIGEN eps
        #CONDICION op,nop, ph
        #CAPACIDAD 10,18,43
        #ESTADO ll,v
        
        
       
        
        #print "FECHA today = ", today
        #print "FECHA last day = ", last_day
        
        
        
        if max_id == None :
                 max_id=1
                 my_data = [
                   (max_id,'gan1', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+1,'gan1', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+2,'gan1', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+3,'gan1', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+4,'gan1', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+5,'gan1', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+6,'gan1', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+7,'gan1', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+8,'gan1', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+9,'gan1', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+10,'gan1', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+11,'gan1', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),


                   (max_id+12,'gan2', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+13,'gan2', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+14,'gan2', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+15,'gan2', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+16,'gan2', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+17,'gan2', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+18,'gan2', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+19,'gan2', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+20,'gan2', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+21,'gan2', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+22,'gan2', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+23,'gan2', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+24,'fle1', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+25,'fle1', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+26,'fle1', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+27,'fle1', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+28,'fle1', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+29,'fle1', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+30,'fle1', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+31,'fle1', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   

                   (max_id+32,'fle1', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+33,'fle1', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+34,'fle1', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+35,'fle1', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+36,'fle2', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+37,'fle2', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+38,'fle2', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+39,'fle2', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+40,'fle2', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+41,'fle2', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+42,'fle2', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+43,'fle2', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+44,'fle2', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+45,'fle2', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+46,'fle2', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+47,'fle2', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+48,'eps1', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+49,'eps1', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+50,'eps1', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+51,'eps1', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+52,'eps1', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+53,'eps1', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+54,'eps1', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+55,'eps1', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+56,'eps1', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+57,'eps1', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+58,'eps1', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+59,'eps1', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+60,'eps2', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+61,'eps2', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+62,'eps2', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+63,'eps2', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+64,'eps2', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+65,'eps2', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+66,'eps2', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+67,'eps2', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+68,'eps2', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+69,'eps2', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+70,'eps2', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+71,'eps2', 'p', 'eps', 'nop', '10', 'v',  0,  0, today),

                   (max_id+72,'eps3', 'ag','eps','op', '10', 'll',  0, 0, today),
                   (max_id+73,'eps3', 'ag','eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+74,'eps3', 'ag','eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+75,'eps3', 'ag','eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+76,'eps3', 'cln', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+77,'eps3', 'cln', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+78,'eps3', 'cln', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+79,'eps3', 'cln', 'eps', 'nop', '10', 'v',  0,  0, today),
                   
                   (max_id+80,'eps3', 'p', 'eps', 'op', '10', 'll',  0,  0, today),
                   (max_id+81,'eps3', 'p', 'eps', 'op', '10', 'v',  0,  0, today),
                   (max_id+82,'eps3', 'p', 'eps', 'nop', '10', 'll',  0,  0, today),
                   (max_id+83,'eps3', 'p', 'eps', 'nop', '10', 'v',  0,  0, today)

                                  ]
                            
                            
                   
                 conn.executemany("INSERT INTO COMPANY3 VALUES (?,?,?,?,?,?,?,?,?,?)",my_data) 
                

                            
        else:
            if last_day < today:
##                #print "FECHA = ", user1[1]
##                #print "FECHA today = ", today
                #print "FECHA ANTERIOR", last_day

                #last_day=today
                

                conn = sqlite3.connect('planta47.db')
    
                cursor = conn.execute('''SELECT  ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA from COMPANY3  WHERE  \
                FECHA = ?  ''', (last_day,))
        
                my_data  = cursor.fetchall()

                #print "tuple", my_data
                

                #data=list(my_data)
                data=[]

##                for i in my_data:
##                    data.append(list(i))

                data=[list(i) for i in my_data]

                #print "ESTE ES !!", data
                    
                

                max_id = max_id +1
##
                for i in data:
                    i[0]= max_id
                    i[8]= 0
                    i[9]= today
                    max_id = max_id +1
                    #print i , "\n"
                    

##                for i in range(len(data)):
##                    data[i][0]= max_id
##                    data[i][8]= 0
##                    max_id = max_id +1
                m_data=[]
                for i in data:
                    #m_data.append(tuple(i))
                    conn.execute("INSERT INTO COMPANY3 VALUES (?,?,?,?,?,?,?,?,?,?)",i) 
                    
                #my_data=(tuple(i) for i in data)

                #print m_data
                                

                #conn.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?)",m_data) 
                ##print "ESTE ES !!", my_data
                

                          
        conn.commit()
        cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY3")
##        for row in cursor:
##           #print "ID = ", row[0]
##           #print "FECHA = ", row[1]
##           #print "UBICACION = ", row[2]
##           #print "TIPO = ", row[3]
##           #print "Numero de cilindros = ", row[4], "\n"
##
##        #print "Records created successfully";
        conn.close()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
            #print "otro"
        else:
            #print "hoy"
            todau= today
        self.dia.text= str(todau)

            
            #self.dia.text= str(today)

    



class INVENTARIO4Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    quote_widget4 = ObjectProperty()
    quote_widget5 = ObjectProperty()
    quote_widget6 = ObjectProperty()
    quote_widget7 = ObjectProperty()
    
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()

    
    locat = StringProperty()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
            #print "otro"
        else:
            #print "hoy"
            todau= today
        self.dia.text= str(todau)

    

    def __init__(self, **kwargs):
        super(INVENTARIO4Screen, self).__init__(**kwargs)
        self.create()
        #self.display_quote()

            
##    def set_location(self,loc):
##        self.locat=loc
##        #print "LOCATION_INV", self.locat

    def set_location(self,loc):
        global ch_loc
        #self.locat=loc
        ch_loc=loc
        #self.manager.current = 'vhplinea2'
       # #print "LOCATION_INV", self.locat
        #print "LOCATION_INV", ch_loc
        
        


    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
    
        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'gan1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
            ( FECHA = ? AND UBICACION= 'gan1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()



        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 ):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            #print "MYDATA18", my_data
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            self.quote_widget.text = 'GANDOLA 1  \n %s ' % (d)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0):
            self.quote_widget.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            self.quote_widget.text = 'GANDOLA 1  \n %s ' % (d)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
           
            
            self.quote_widget.text = '  \n %sGANDOLA 1 ' % (d)



        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'gan2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'gan2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


       
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            
            self.quote_widget2.text = 'GANDOLA 2  \n %s ' % (d)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            self.quote_widget2.text = 'GANDOLA 2  \n %s ' % (d)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            
            self.quote_widget2.text = 'GANDOLA 2  \n %s' % (d)



        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'fle1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION= 'fle1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'fle1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'fle1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget3.text = 'FLETERO 1  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget3.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget3.text = 'FLETERO 1  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget3.text = 'FLETERO 1  \n %s/%s ' % (d,  d2)



        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
            ( FECHA = ? AND UBICACION= 'fle2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'fle2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
            ( FECHA = ? AND UBICACION= 'fle2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
           ( FECHA = ? AND UBICACION= 'fle2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget4.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget4.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget4.text = 'FLETERO 2  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget4.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget4.text = 'FLETERO 2  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget4.text = 'FLETERO 2  \n %s/%s ' % (d,  d2)



        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'eps1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION= 'eps1' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
            ( FECHA = ? AND UBICACION= 'eps1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
            ( FECHA = ? AND UBICACION= 'eps1' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget5.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget5.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget5.text = 'EPSDC 1  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget5.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget5.text = 'EPSDC 1  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget5.text = 'EPSDC 1  \n %s/%s ' % (d,  d2)




        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
       ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget6.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget6.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget6.text = 'EPSDC 2  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget6.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget6.text = 'EPSDC 2  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget6.text = 'EPSDC 2  \n %s/%s ' % (d,  d2)




        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'eps3' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'eps3' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac  = cursor.fetchall()


        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
          ( FECHA = ? AND UBICACION= 'eps3' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2') ''', (today,))
        
        my_data2  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY4 WHERE
         ( FECHA = ? AND UBICACION= 'eps3' AND ORIGEN='eps' AND CAPACIDAD='43') ''', (todau,))
        #cursor = conn.execute('''SELECT  consultas,cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= 'l2' AND CAPACIDAD='18') ''', (today,))

        my_datac2  = cursor.fetchall()
        

        
        self.quote_widget7.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac2[0][0]==0 \
            and my_datac2[1][0]==0 and my_datac2[2][0]==0 and my_datac2[3][0]==0 ):
            self.quote_widget7.color=[1,0,0,1]
            #self.quote_widget.text = 'LINEA 2 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget7.text = 'EPSDC 3  \n %s/%s ' % (d,  d2)
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac2[0][0]==0 \
              or my_datac2[1][0]==0 or my_datac2[2][0]==0 or my_datac2[3][0]==0 ):
            self.quote_widget7.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            self.quote_widget7.text = 'EPSDC 3  \n %s/%s ' % (d,  d2)
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0])
            d2= str(my_data2[0][0]+my_data2[1][0]+my_data2[2][0]+my_data2[3][0])
            
            self.quote_widget7.text = 'EPSDC 3  \n %s/%s ' % (d,  d2)

       
    



            


     
    

    def create(self):
        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)
        #print "Opened database successfully";
        #INT     NOT NULL
        conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY4
               (ID INT PRIMARY KEY   NOT NULL,
                UBICACION           CHAR(50),
                TIPO                CHAR(50),
                ORIGEN                CHAR(50),
                CONDICION                CHAR(50),
                CAPACIDAD                CHAR(50),
                ESTADO                CHAR(50),
                CANTIDAD            INT     NOT NULL,
                CONSULTAS           INT     NOT NULL,
                FECHA  date );''')

        #print "Table created successfully";
        conn.close()




       # ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA 

        conn = sqlite3.connect('planta47.db',detect_types=sqlite3.PARSE_DECLTYPES)

        iterator = conn.execute('SELECT max(ID), UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA  FROM COMPANY4')
        #max_id = iterator.fetchone()[0]
        user1 = iterator.fetchone() #retrieve the first row
        max_id= user1[0]
        last_day = user1[9]
##        #print "max_id=", max_id
##        #print "FECHA anterior= ", user1[9]
##        #print "FECHA today = ", today
        #user1 = cursor

        #UBICACION - plat43,pa43,l1,l2,pa,pal1,pla1pa,pla2,2,gandola,fle17 (fleteros),fle18,eps1662,eps1661,eps5696,fp (fuera de planta)
        #TIPO - p (plastico),ag (autogas),cln (cli-pon),tp (troquel privado), r (rosca noruega)
        #ORIGEN eps
        #CONDICION op,nop, ph
        #CAPACIDAD 18,43
        #ESTADO ll,v
        
        
       
       
        
        
        if max_id == None :
                 #print "max_id=", max_id
                 #print "FECHA anterior= ", user1[9]
                 #print "FECHA today = ", today
                 max_id=1
                 my_data = [
                   (max_id,'gan1', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+1,'gan1', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+2,'gan1', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+3,'gan1', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+4,'gan2', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+5,'gan2', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+6,'gan2', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+7,'gan2', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+8,'fle1', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+9,'fle1', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+10,'fle1', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+11,'fle1', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+12,'fle2', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+13,'fle2', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+14,'fle2', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+15,'fle2', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+16,'eps1', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+17,'eps1', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+18,'eps1', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+19,'eps1', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+20,'eps2', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+21,'eps2', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+22,'eps2', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+23,'eps2', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+24,'eps3', 'r','eps','op', '18', 'll',  0, 0, today),
                   (max_id+25,'eps3', 'r','eps', 'op', '18', 'v',  0,  0, today),
                   (max_id+26,'eps3', 'r','eps', 'nop', '18', 'll',  0,  0, today),
                   (max_id+27,'eps3', 'r','eps', 'nop', '18', 'v',  0,  0, today),

                   (max_id+28,'fle1', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+29,'fle1', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+30,'fle1', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+31,'fle1', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+32,'fle2', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+33,'fle2', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+34,'fle2', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+35,'fle2', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+36,'eps1', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+37,'eps1', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+38,'eps1', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+39,'eps1', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+40,'eps2', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+41,'eps2', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+42,'eps2', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+43,'eps2', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                   (max_id+44,'eps3', 'r','eps','op', '43', 'll',  0, 0, today),
                   (max_id+45,'eps3', 'r','eps', 'op', '43', 'v',  0,  0, today),
                   (max_id+46,'eps3', 'r','eps', 'nop', '43', 'll',  0,  0, today),
                   (max_id+47,'eps3', 'r','eps', 'nop', '43', 'v',  0,  0, today),

                                  ]
                            
                            
                   
                 conn.executemany("INSERT INTO COMPANY4 VALUES (?,?,?,?,?,?,?,?,?,?)",my_data) 
                

                            
        else:
            if last_day < today:
                #print "FECHA ANTERIOR", last_day

                #last_day=today
                

                conn = sqlite3.connect('planta47.db')
    
                cursor = conn.execute('''SELECT  ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, CONSULTAS, FECHA from COMPANY4 WHERE  \
                FECHA = ?  ''', (last_day,))
        
                my_data  = cursor.fetchall()

                #print "tuple", my_data
                

                #data=list(my_data)
                data=[]

##                for i in my_data:
##                    data.append(list(i))

                data=[list(i) for i in my_data]

                #print "ESTE ES !!", data
                    
                

                max_id = max_id +1
##
                for i in data:
                    i[0]= max_id
                    i[8]= 0
                    i[9]= today
                    max_id = max_id +1
                    #print i , "\n"
                    

##                for i in range(len(data)):
##                    data[i][0]= max_id
##                    data[i][8]= 0
##                    max_id = max_id +1
                m_data=[]
                for i in data:
                    #m_data.append(tuple(i))
                    conn.execute("INSERT INTO COMPANY4 VALUES (?,?,?,?,?,?,?,?,?,?)",i) 
                    
                #my_data=(tuple(i) for i in data)

                #print m_data
                                

                #conn.executemany("INSERT INTO COMPANY VALUES (?,?,?,?,?,?,?,?,?,?)",m_data) 
                ##print "ESTE ES !!", my_data
                

                          
        conn.commit()
        cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad, consultas, capacidad  from COMPANY4 where (fecha=? and ubicacion=?) ",(today,'l2'))
##        for row in cursor:
##           #print "COMPANY2"
##           #print "ID = ", row[0]
##           #print "FECHA = ", row[1]
##           #print "UBICACION = ", row[2]
##           #print "TIPO = ", row[3]
##           #print "Numero de cilindros = ", row[4]
##           #print "Numero de consultas = ", row[5],
##           #print "capacidad = ", row[6],"\n"
##
##        #print "Records created successfully COMPANY2";
        conn.close()








class EPSScreen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    locat = StringProperty()
    
    cond=StringProperty()
    direc=ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()
    
    
    def __init__(self, **kwargs):
        super(EPSScreen, self).__init__(**kwargs)
        #self.display_quote()
        self.get_date()

    def set_locat2(self,locc):
        global locat2
        locat2=locc
        #print "LOCAT2", locat2
        if locat2 == 'pla1':
            self.manager.current = 'plinea2'
        else:
            self.manager.current = 'clipon'

            
            
        
    def set_direc(self):
        self.direc.text=str('PLANTA - 10kg - EPSDC')
        
        
        
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today

        #print "LOCATION", self.locat
        conn = sqlite3.connect('planta47.db')
        
    
        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
                 AND ORIGEN='0' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau,self.locat))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION=?
              AND ORIGEN='0' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau,self.locat))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 ):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'OPERATIVOS \n NA '
            d= str(my_data[0][0]+my_data[1][0])
            self.quote_widget.text = 'PATIO \n %s ' % d
            
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 ):
            self.quote_widget.color=[1,1,0,1]
            
            d= str(my_data[0][0]+my_data[1][0])
            self.quote_widget.text = 'PATIO \n %s ' % d
            
        else:
            d= str(my_data[0][0]+my_data[1][0])
            self.quote_widget.text = 'PATIO \n %s ' % d

        #######################
        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= 'pla1' AND ORIGEN='eps' AND CAPACIDAD='10') ''', (todau,))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0 \
            and my_datac[6][0]==0 and my_datac[7][0]==0 and my_datac[8][0]==0 and my_datac[9][0]==0 and my_datac[10][0]==0 and my_datac[11][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget7.text = 'PLATAFORMA 1 \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'PLATAFORMA 1 \n %s ' % d
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0 \
            or my_datac[6][0]==0 or my_datac[7][0]==0 or my_datac[8][0]==0 or my_datac[9][0]==0 or my_datac[10][0]==0 or my_datac[11][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'PLATAFORMA 1 \n %s ' % d
                 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0]+my_data[6][0]+my_data[7][0]+my_data[8][0] \
                   +my_data[9][0]+my_data[10][0]+my_data[11][0])
            self.quote_widget2.text = 'PLATAFORMA 1 \n %s ' % d


        #################

##        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
##         AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau, self.locat))
##        
##        my_data  = cursor.fetchall()
##
##
##        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
##          AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau, self.locat))
##
##        my_datac  = cursor.fetchall()
##        #print "DATA", my_data
##        
##        self.quote_widget2.color=[1,1,1,1] 
##        if (my_datac[0][0]==0 and my_datac[1][0]==0 ):
##            self.quote_widget2.color=[1,0,0,1]
##            #self.quote_widget2.text = 'NO OPERATIVOS \n NA '
##            d= str(my_data[0][0]+my_data[1][0])
##            self.quote_widget2.text = 'PLATAFORMA 1 \n %s ' % d 
##        elif (my_datac[0][0]==0 or my_datac[1][0]==0 ):
##            self.quote_widget2.color=[1,1,0,1]
##            
##            d= str(my_data[0][0]+my_data[1][0])
##            self.quote_widget2.text = 'PLATAFORMA 1 \n %s ' % d 
##        else:
##            d= str(my_data[0][0]+my_data[1][0])
##            self.quote_widget2.text = 'PLATAFORMA 1 \n %s ' % d
##
##
##            
        
        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
         AND ORIGEN='2' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau, self.locat))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
          AND ORIGEN='2' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau, self.locat))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 ):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget2.text = 'NO OPERATIVOS \n NA '
            d= str(my_data[0][0]+my_data[1][0])
            self.quote_widget3.text = 'PLATAFORMA 2 \n %s ' % d 
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 ):
            self.quote_widget3.color=[1,1,0,1]
            
            d= str(my_data[0][0]+my_data[1][0])
            self.quote_widget3.text = 'PLATAFORMA 2 \n %s ' % d 
        else:
            d= str(my_data[0][0]+my_data[1][0])
            self.quote_widget3.text = 'PLATAFORMA 2 \n %s ' % d

            
        conn.close()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)
    














class OPERL2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    locat = StringProperty('l2')
    cond=StringProperty()
    direc=ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()
    
    
    def __init__(self, **kwargs):
        super(OPERL2Screen, self).__init__(**kwargs)
        #self.display_quote()
        self.get_date()


    def retu(self):
        #print self.locat
        if self.locat=='epsdc':
            self.manager.current = 'eps'
            #print "EPSDC"
        else:
            self.manager.current = 'inventario'
            #print "INVENTARIO"
            

    def set_cond(self,condd):
        self.cond=condd
        #print "CONDICION", self.cond

    def set_direc(self):
        #global locat2
        if self.locat=='l1':
            self.direc.text=str('PLANTA - 10kg - LINEA 1')
            #print "condicion", self.locat
        elif self.locat=='l2':
            self.direc.text=str('PLANTA - 10kg - LINEA 2')
            #print "condicion", self.locat
        elif self.locat=='pag':
            self.direc.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA)')
            #print "condicion", self.locat
        if self.locat=='pa1':
            self.direc.text=str('PLANTA - 10kg - PATIO 1')
            #print "condicion", self.locat
        if self.locat=='pa2':
            self.direc.text=str('PLANTA - 10kg - PATIO 2')
            #print "condicion", self.locat
        if self.locat=='pla1':
            self.direc.text=str('PLANTA - 10kg - PLATAFORMA 1')
            #print "condicion", self.locat
        if self.locat=='pla2':
            self.direc.text=str('PLANTA - 10kg - PLATAFORMA 2')
            #print "condicion", self.locat
        if self.locat=='epsdc':
            if locat2=='patio':
                self.direc.text=str('PLANTA - 10kg - EPSDC - PATIO ')
                #print "condicion", locat2
            elif locat2=='pla1':
                self.direc.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 1 ')
                #print "condicion", locat2
            elif locat2=='pla2':
                self.direc.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 2 ')
                #print "condicion", locat2
        if self.locat=='pla43':
            self.direc.text=str('PLANTA - 10kg - PLATAFORMA 43 ')
            #print "condicion", self.locat
        
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today

        #print "LOCATION", self.locat
        conn = sqlite3.connect('planta47.db')
        
    
        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
                 AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau,self.locat))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION=?
              AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='10') ''', (todau,self.locat))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'OPERATIVOS \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0])
            self.quote_widget.text = 'OPERATIVOS \n %s ' % d 
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0):
            self.quote_widget.color=[1,1,0,1]
            
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0])
            self.quote_widget.text = 'OPERATIVOS \n %s ' % d 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0])
            self.quote_widget.text = 'OPERATIVOS \n %s ' % d



        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
         AND ORIGEN='eps' AND CONDICION='nop' AND CAPACIDAD='10') ''', (todau, self.locat))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE ( FECHA = ? AND UBICACION= ?
          AND ORIGEN='eps' AND CONDICION='nop' AND CAPACIDAD='10') ''', (todau, self.locat))

        my_datac  = cursor.fetchall()
        #print "DATA", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0 and my_datac[2][0]==0 and my_datac[3][0]==0 and my_datac[4][0]==0 and my_datac[5][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget2.text = 'NO OPERATIVOS \n NA '
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0])
            self.quote_widget2.text = 'NO OPERATIVOS \n %s ' % d 
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 or my_datac[2][0]==0 or my_datac[3][0]==0 or my_datac[4][0]==0 or my_datac[5][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0])
            self.quote_widget2.text = 'NO OPERATIVOS \n %s ' % d 
        else:
            d= str(my_data[0][0]+my_data[1][0]+my_data[2][0]+my_data[3][0]+my_data[4][0]+my_data[5][0])
            self.quote_widget2.text = 'NO OPERATIVOS \n %s ' % d
        

        conn.close()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)
    

class NOPERL2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    locat = StringProperty('l2')
    cond=StringProperty()
    direc=ObjectProperty()
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()
    
    
    
    def __init__(self, **kwargs):
        super(NOPERL2Screen, self).__init__(**kwargs)
        #self.display_quote()

    def set_cond(self,condd):
        self.cond=condd
        #print "CONDICION", self.cond

    def set_direc(self):
        if self.locat=='l1':
            self.direc.text=str('18/43 kg  - LINEA 1')
            #print "condicion", self.locat
        elif self.locat=='l2':
            self.direc.text=str('18/43 kg  - LINEA 2')
            #print "condicion", self.locat
##        elif self.locat=='pag':
##            self.direc.text=str('18/43 kg  - PATIO GANDOLA (CARGA)')
##            #print "condicion", self.locat
        if self.locat=='pa1':
            self.direc.text=str('18/43 kg  - PATIO 1')
            #print "condicion", self.locat
        if self.locat=='pa2':
            self.direc.text=str('18/43 kg  - PATIO 2')
            #print "condicion", self.locat
        if self.locat=='pla1':
            self.direc.text=str('18/43 kg  - PLATAFORMA 1')
            #print "condicion", self.locat
        if self.locat=='pla2':
            self.direc.text=str('18/43 kg  - PLATAFORMA 2')
            #print "condicion", self.locat
        if self.locat=='pla43':
            self.direc.text=str('18/43 kg  - PLATAFORMA 43 ')
            #print "condicion", self.locat
        
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today

        #print "LOCATION", self.locat
        conn = sqlite3.connect('planta47.db')
        
        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= ?
                 AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='18') ''', (todau,self.locat))        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION=?
              AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='18') ''', (todau,self.locat))
        my_datac  = cursor.fetchall()

        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= ?
                 AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='43') ''', (todau,self.locat))
        my_data4  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION=?
              AND ORIGEN='eps' AND CONDICION='op' AND CAPACIDAD='43') ''', (todau,self.locat))

        my_datac4  = cursor.fetchall()
        
        #print "DATA4", my_data4
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0   \
            and my_datac4[0][0]==0 and my_datac4[1][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = 'OPERATIVOS \n NA '
            d= str(my_data[0][0]+my_data[1][0])
            d4= str(my_data4[0][0]+my_data4[1][0])
            self.quote_widget.text = 'OPERATIVOS \n %s/%s ' % (d,d4) 
        elif (my_datac[0][0]==0 or my_datac[1][0]==0 \
              or my_datac4[0][0]==0 or my_datac4[1][0]==0 ):
            self.quote_widget.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0])
            d4= str(my_data4[0][0]+my_data4[1][0])
            self.quote_widget.text = 'OPERATIVOS \n %s/%s ' % (d,d4) 
        else:
            d= str(my_data[0][0]+my_data[1][0])
            d4= str(my_data4[0][0]+my_data4[1][0])
            self.quote_widget.text = 'OPERATIVOS \n %s/%s ' % (d,d4) 



        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= ?
                 AND ORIGEN='eps' AND CONDICION='nop' AND CAPACIDAD='18') ''', (todau,self.locat))        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION=?
              AND ORIGEN='eps' AND CONDICION='nop' AND CAPACIDAD='18') ''', (todau,self.locat))
        my_datac  = cursor.fetchall()

        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE ( FECHA = ? AND UBICACION= ?
                 AND ORIGEN='eps' AND CONDICION='nop' AND CAPACIDAD='43') ''', (todau,self.locat))
        my_data4  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE ( FECHA = ? AND UBICACION=?
              AND ORIGEN='eps' AND CONDICION='nop' AND CAPACIDAD='43') ''', (todau,self.locat))

        my_datac4  = cursor.fetchall()
        ##print "DATA", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0  \
            and my_datac4[0][0]==0 and my_datac4[1][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget.text = 'OPERATIVOS \n NA '
            d= str(my_data[0][0]+my_data[1][0])
            d4= str(my_data4[0][0]+my_data4[1][0])
            self.quote_widget2.text = 'NO OPERATIVOS \n %s/%s ' % (d,d4) 
        elif (my_datac[0][0]==0 or my_datac[1][0]==0\
              or my_datac4[0][0]==0 or my_datac4[1][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            d= str(my_data[0][0]+my_data[1][0])
            d4= str(my_data4[0][0]+my_data4[1][0])
            self.quote_widget2.text = 'NO OPERATIVOS \n %s/%s ' % (d,d4) 
        else:
            d= str(my_data[0][0]+my_data[1][0])
            d4= str(my_data4[0][0]+my_data4[1][0])
            self.quote_widget2.text = 'NO OPERATIVOS \n %s/%s ' % (d,d4) 
        

        conn.close()

    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)


class CLIPON(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    direc2=ObjectProperty()
    agll= ObjectProperty()
    agv= ObjectProperty()
    tipoo=StringProperty('cln')
    cond=StringProperty('op')
    locat = StringProperty('epsdc')
    sea=StringProperty()
    
    dia = ObjectProperty()
    oro=StringProperty('0')


   
    def __init__(self, **kwargs):
        super(CLIPON, self).__init__(**kwargs)
        self.display_quote()
        #self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
        self.get_date()
        self.oro='0'
        
        #ba2=0

    
    def set_direc2(self):
            #print "localt2", locat2
            if locat2 == 'patio':
                self.direc2.text=str('PLANTA - 10kg - EPSDC - PATIO - CLIP ON')
                #print "localt2", locat2
                self.oro='0'
            elif locat2 == 'pla1':
                self.direc2.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 1 - CLIP ON')
                #print "localt2", locat2
                self.oro='1'
            elif locat2 == 'pla2':
                self.direc2.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 2 - CLIP ON')
                #print "localt2", locat2
                self.oro='2'
               
            
           

    def set_ttipo(self,tio):
        self.tipoo=tio

   

    def display_quote(self):
        #print "condicion", self.cond
        conn = sqlite3.connect('planta47.db')
        
        #print "LOCAT", self.locat
        #print "LOCAT2", self.oro
        cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY WHERE (TIPO= 'cln' AND FECHA = ? AND UBICACION= ? AND ORIGEN=? AND CONDICION= 'op'
          AND CAPACIDAD='10') ''', ( today, self.locat , self.oro))
        
        my_data  = cursor.fetchall()
        #print "MY DATA", my_data
        self.quote_widget.color= [1,1,1,1]
        self.quote_widget2.color= [1,1,1,1]

        self.quote_widget.text = str( my_data[0][0])
        if my_data[0][1] == 0:
            self.quote_widget.color= [1,0,0,1]
            #self.quote_widget.text=str('NA')
            #self.agll.text=str('')
            #self.agll.text=self.quote_widget.text
            
        #else:
            #self.agll.text=str('')

        self.quote_widget2.text = str( my_data[1][0])
        if my_data[1][1] == 0:
            self.quote_widget2.color= [1,0,0,1]
            #self.quote_widget2.text=str('NA')
            #self.agv.text=str('')
            #self.agv.text=self.quote_widget2.text
            
            
        #else:
            #self.agv.text=str('')
            

        
        #print "tipo", self.tipoo
        ##print "VAC", self.agll.text

        #print "MY DATA", my_data
        

        conn.close()

        #random_quote = self.get_random_quote()
        #self.quote_widget.text = r'"%s"%s-- %s' % \
        #    (random_quote['quote'], '\n' * 2, random_quote['author'])
    
        
    def save(self):

##            #UPDATE
            #ba2=1
            conn = sqlite3.connect('planta47.db')



            ban=0
            bao1=0
            bao2=0

            if self.agll.text:
                bao1=1

            if self.agv.text:
                bao2=1


            if self.agll.text:
                try:
                    int(self.agll.text)        
                except ValueError:
                    ban=1
                    #print "ERROR"
                    #print "ban", ban


            if self.agv.text:
                try:
                    int(self.agv.text)        
                except ValueError:
                    ban=1
                    #print "ERROR"
                    #print "ban", ban
                

          
            #self.p.text=str(0)
            #print 'DATOS'
            #print   self.agll.text
            #print   self.agv.text
            
#ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA
##            if ban==2:
##                self.quote_widget.color= [1,0,0,1]
##                self.agll.text=self.quote_widget.text
##                self.agv.text=self.quote_widget2.text
##                self.manager.current = 'plinea2'
                
            if ban==0:

                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY WHERE (TIPO= 'cln' AND FECHA = ? AND UBICACION= ? AND ORIGEN= ? AND CONDICION= 'op'
                   AND CAPACIDAD='10') ''', (today, self.locat , self.oro))
        
                my_data  = cursor.fetchall()

                #self.quote_widget.color= [1,1,1,1]
                #self.quote_widget2.color= [1,1,1,1]


##                agllop=int(self.agll.text)+ my_data[0][0]
##                agvop=int(self.agv.text)+ my_data[1][0]

                if not self.agll.text:
                    #self.quote_widget.color= [1,0,0,1]
                    agllop=0+ my_data[0][0]
                    self.quote_widget.text=str(agllop)
                else:
                    self.quote_widget.color= [1,1,1,1]
                    agllop=int(self.agll.text)+ my_data[0][0]
                    self.quote_widget.text=str(agllop)

                
                    
                    
                if not self.agv.text:
                    #self.quote_widget2.color= [1,0,0,1]
                    agvop=0+ my_data[1][0]
                    self.quote_widget2.text=str(agvop)
                else:
                    self.quote_widget2.color= [1,1,1,1]
                    agvop=int(self.agv.text)+ my_data[1][0]
                    self.quote_widget2.text=str(agvop)
                    
                
                opo=my_data[0][1]
                opo2=my_data[1][1]

                if bao1==1:
                    opo =+ 1

                if bao2==1:
                    opo2 =+ 1

                #self.agll.text, self.agv.text



                #print "EPA!!" "\n"
                #print "agllop", agllop
                #print "agvop", agvop
                
                    
                
                my_data2 = ({'locate':self.locat, 'tip':'cln', 'est':'ll', 'value':agllop ,'condi':'op' ,'con':opo, 'fe': today, 'orol':self.oro}, \
                            {'locate':self.locat,'tip':'cln', 'est':'v', 'value':agvop , 'condi':'op' ,'con':opo2, 'fe': today, 'orol':self.oro})
                            

                conn.executemany("UPDATE COMPANY SET CANTIDAD =:value WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN=:orol \
                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()


                conn.executemany("UPDATE COMPANY SET  CONSULTAS=:con WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN=:orol \
                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()

                
                #print "Total number of rows updated :", conn.total_changes

##                cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##                for row in cursor:
##                   #print "ID = ", row[0]
##                   #print "FECHA = ", row[1]
##                   #print "UBICACION = ", row[2]
##                   #print "TIPO = ", row[3]
##                   #print "Numero de cilindros = ", row[4], "\n"
##
##                #print "Operation done successfully";
                conn.close()
                self.manager.current = 'eps'

                
            
    def get_date(self):
            self.dia.text= str(today)



  
            
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)

    

    


class PLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    cond=StringProperty('op')
    direc=ObjectProperty()
    direc2=ObjectProperty()
    tipoo=StringProperty('ag')
    locat = StringProperty('l2')
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()
       
    
   
    #dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(PLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.get_date()
        self.set_direc()

    def set_tipo(self,tipp):
        self.tipoo=tipp

    def moven(self):
        if self.sea!='otro':
            self.manager.current = 'aglinea2'
        
        
    def moveback(self):
        if self.locat=='pla1':
            self.manager.current = 'eps'
        else:
            self.manager.current = 'operl2'


    
    def set_direc(self):
        if self.locat=='l2':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - LINEA 2 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='l1':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - LINEA 1 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - LINEA 1 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pag':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pa1':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - PATIO 1 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - PATIO 1 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pa2':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - PATIO 2 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - PATIO 2 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pla1':
            self.cond='op'
            self.direc.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 1')
            #print "condicion", self.cond
        elif self.locat=='pla2':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - PLATAFORMA 2 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - PLATAFORMA 2 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='epsdc':
            if self.cond=='op':
                if locat2=='patio':
                    self.direc.text=str('PLANTA - 10kg - EPSDC- PATIO - OPERATIVOS')
                    #print "condicion", self.cond
                elif locat2=='pla1':
                    self.direc.text=str('PLANTA - 10kg - EPSDC- PLATAFORMA 1')
                    #print "condicion", self.cond
                elif locat2=='pla2':
                    self.direc.text=str('PLANTA - 10kg - EPSDC- PLATAFORMA 2- OPERATIVOS')
                    #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - EPSDC - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pla43':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 10kg - PLATAFORMA 43 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 10kg - PLATAFORMA 43 - NO OPERATIVOS')
                #print "condicion", self.cond
            
        
            
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')

        if self.locat=='epsdc':
            self.locat='pla1'

        
 
        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE (TIPO='ag' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
          AND CAPACIDAD='10') ''', (todau,self.locat,self.cond))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE (TIPO='ag' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION=?
          AND CAPACIDAD='10') ''', (todau,self.locat,self.cond))

        my_datac  = cursor.fetchall()

        #print "LOCAT", self.locat
        
        #print "LOCAT", self.locat
        #print "AQUI", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = str('NA')
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget.color=[1,1,0,1]
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])   
        else:
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])


        




        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE (TIPO='cln' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
          AND CAPACIDAD='10') ''', (todau,self.locat,self.cond))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE (TIPO='cln' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION=?
          AND CAPACIDAD='10') ''', (todau,self.locat,self.cond))

        my_datac  = cursor.fetchall()
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget2.text = str('NA')
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])     
        else:
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])




        

        cursor = conn.execute('''SELECT  cantidad from COMPANY WHERE (TIPO='p' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION=?
          AND CAPACIDAD='10') ''', (todau,self.locat,self.cond))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY WHERE (TIPO='p' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION=?
          AND CAPACIDAD='10') ''', (todau,self.locat,self.cond))

        my_datac  = cursor.fetchall()
        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget3.text = str('NA')
            self.quote_widget3.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget3.color=[1,1,0,1]
            self.quote_widget3.text = str(my_data[0][0]+my_data[1][0])   
        else:
            self.quote_widget3.text = str(my_data[0][0]+my_data[1][0])



      

        #print "MY DATA", my_data
        

        conn.close()

  
            
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)



class VHPLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    quote_widget3 = ObjectProperty()
    cond=StringProperty('op')
    direc=ObjectProperty()
    direc2=ObjectProperty()
    tipoo=StringProperty('ag')
    locat = StringProperty('ga1')
    dia = ObjectProperty()
    #toda = StringProperty()
    sea=StringProperty()
       
    
   
    #dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(VHPLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.get_date()
        self.set_direc()

    def set_tipo(self,tipp):
        self.tipoo=tipp

    def moven(self):
        if self.sea!='otro':
            self.manager.current = 'vhaglinea2'
        
        

    def set_direc(self):
        if ch_loc=='gan1':
            self.direc.text=str('VEHICULOS - 10kg - GANDOLA 1')
        elif ch_loc=='gan2':
           self.direc.text=str('VEHICULOS - 10kg - GANDOLA 2')
           #print "ubicacion", ch_loc
        elif ch_loc=='fle1':
           self.direc.text=str('VEHICULOS - 10kg - FLETERO 1')
        elif ch_loc=='fle2':
           self.direc.text=str('VEHICULOS - 10kg - FLETERO 2')
        elif ch_loc=='eps1':
           self.direc.text=str('VEHICULOS - 10kg - EPSDC 1')
        elif ch_loc=='eps2':
           self.direc.text=str('VEHICULOS - 10kg - EPSDC 1')
        elif ch_loc=='eps3':
           self.direc.text=str('VEHICULOS - 10kg - EPSDC 1')
               
            
        
            
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
        #print "LOCC", ch_loc


        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='10'
        AND CONDICION='op' AND TIPO='ag') ''', (todau,ch_loc))
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='10'
        AND CONDICION='op' AND TIPO='ag') ''', (todau,ch_loc))
        my_datac  = cursor.fetchall()

        
        
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget.text = str('NA')
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget.color=[1,1,0,1]
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])   
        else:
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])


        




        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='10'
        AND CONDICION='op' AND TIPO='cln') ''', (todau,ch_loc))
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='10'
        AND CONDICION='op' AND TIPO='cln') ''', (todau,ch_loc))
        my_datac  = cursor.fetchall()

        #print "AQUI AQUI", todau
        #print "AQUI AQUI", ch_loc
        #print "AQUI AQUI", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget2.text = str('NA')
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])     
        else:
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])




        

        cursor = conn.execute('''SELECT  cantidad from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='10'
        AND CONDICION='op' AND TIPO='p') ''', (todau,ch_loc))
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY3 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='10'
        AND CONDICION='op' AND TIPO='p') ''', (todau,ch_loc))
        my_datac  = cursor.fetchall()

        
        self.quote_widget3.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget3.color=[1,0,0,1]
            #self.quote_widget3.text = str('NA')
            self.quote_widget3.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget3.color=[1,1,0,1]
            self.quote_widget3.text = str(my_data[0][0]+my_data[1][0])   
        else:
            self.quote_widget3.text = str(my_data[0][0]+my_data[1][0])



      

        #print "MY DATA", my_data
        

        conn.close()

  
            
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)


class N1VHPLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    #quote_widget2 = ObjectProperty()
    #quote_widget3 = ObjectProperty()
    cond=StringProperty('op')
    direc=ObjectProperty()
    direc2=ObjectProperty()
    tipoo=StringProperty('ag')
    locat = StringProperty('l2')
    #toda = StringProperty()
    sea=StringProperty()
       
    
   
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(N1VHPLINEA2Screen, self).__init__(**kwargs)
       # self.display_quote()
        self.get_date()
        self.set_direc()


    def moven(self):
        if self.sea!='otro':
            self.manager.current = 'n1vhaglinea2'

    def set_tipo(self,tipp):
        self.tipoo=tipp
        

    def set_direc(self):
        if ch_loc=='gan1':
            self.direc.text=str('VEHICULOS - 18 kg  - GANDOLA 1 ')
        elif ch_loc=='gan2':
            self.direc.text=str('VEHICULOS - 18 kg  - GANDOLA 2 ')
    
            
            
        
            
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
        
##        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
##         ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
##        
 
        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='18'
        AND CONDICION='op' ) ''', (todau,ch_loc))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='18'
        AND CONDICION='op' ) ''', (todau,ch_loc))
        my_datac  = cursor.fetchall()

        #print "AQUI AQUI", todau
        #print "AQUI AQUI", ch_loc
        #print "AQUI AQUI", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget2.text = str('NA')
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget.color=[1,1,0,1]
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])     
        else:
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])

        




        


      

        #print "MY DATA", my_data
        

        conn.close()

  
            
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)



class N2VHPLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    #quote_widget3 = ObjectProperty()
    cond=StringProperty('op')
    direc=ObjectProperty()
    direc2=ObjectProperty()
    tipoo=StringProperty('ag')
    locat = StringProperty('l2')
    #toda = StringProperty()
    sea=StringProperty()
       
    
   
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(N2VHPLINEA2Screen, self).__init__(**kwargs)
       # self.display_quote()
        self.get_date()
        self.set_direc()


    def moven(self):
        if self.sea!='otro':
            self.manager.current = 'n2vhaglinea2'

    def set_tipo(self,tipp):
        self.tipoo=tipp
        

    def set_direc(self):
        if ch_loc=='fle1':
            self.direc.text=str('VEHICULOS - 18/43 kg  - FLETERO 1 ')
        elif ch_loc=='fle2':
            self.direc.text=str('VEHICULOS - 18/43 kg  - FLETERO 2 ')
        elif ch_loc=='eps1':
            self.direc.text=str('VEHICULOS - 18/43 kg  - EPSD 1 ')
        elif ch_loc=='eps2':
            self.direc.text=str('VEHICULOS - 18/43 kg  - EPSD 2  ')
        elif ch_loc=='eps3':
            self.direc.text=str('VEHICULOS - 18/43 kg  - EPSD 3  ')
    
    
            
            
        
            
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
        
##        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
##         ( FECHA = ? AND UBICACION= 'eps2' AND ORIGEN='eps' AND CAPACIDAD='18') ''', (todau,))
##        
 
        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='18'
        AND CONDICION='op' ) ''', (todau,ch_loc))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='18'
        AND CONDICION='op' ) ''', (todau,ch_loc))
        my_datac  = cursor.fetchall()

        #print "AQUI AQUI", todau
        #print "AQUI AQUI", ch_loc
        #print "AQUI AQUI", my_data
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget.color=[1,0,0,1]
            #self.quote_widget2.text = str('NA')
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget.color=[1,1,0,1]
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])     
        else:
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])



        cursor = conn.execute('''SELECT  cantidad from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='43'
        AND CONDICION='op' ) ''', (todau,ch_loc))
        
        my_data  = cursor.fetchall()

        cursor = conn.execute('''SELECT  consultas from COMPANY4 WHERE
        ( FECHA = ? AND UBICACION=? AND ORIGEN='eps' AND CAPACIDAD='43'
        AND CONDICION='op' ) ''', (todau,ch_loc))
        my_datac  = cursor.fetchall()

        #print "AQUI AQUI", todau
        #print "AQUI AQUI", ch_loc
        #print "AQUI AQUI", my_data
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            #self.quote_widget2.text = str('NA')
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])     
        else:
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])

        




        #print "MY DATA", my_data
        
        conn.close()

  
            
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)



#por aqui vamos
class NPLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    #quote_widget3 = ObjectProperty()
    cond=StringProperty('op')
    direc=ObjectProperty()
    direc2=ObjectProperty()
    tipoo=StringProperty('ag')
    locat = StringProperty('l2')
    #toda = StringProperty()
    sea=StringProperty()
       
    
   
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(NPLINEA2Screen, self).__init__(**kwargs)
       # self.display_quote()
        self.get_date()
        self.set_direc()


    def moven(self):
        if self.sea!='otro':
            self.manager.current = 'naglinea2'

    def set_tipo(self,tipp):
        self.tipoo=tipp
        

    def set_direc(self):
        if self.locat=='l2':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - LINEA 2 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - LINEA 2 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='l1':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - LINEA 1 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - LINEA 1 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pag':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pa1':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - PATIO 1 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - PATIO 1 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pa2':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - PATIO 2 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - PATIO 2 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pla1':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pla2':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='epsdc':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - EPSDC - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - EPSDC - NO OPERATIVOS')
                #print "condicion", self.cond
        elif self.locat=='pla43':
            if self.cond=='op':
                self.direc.text=str('PLANTA - 18/43 kg  - PLATAFORMA 43 - OPERATIVOS')
                #print "condicion", self.cond
            elif self.cond=='nop':
                self.direc.text=str('PLANTA - 18/43 kg  - PLATAFORMA 43 - NO OPERATIVOS')
                #print "condicion", self.cond
            
        
            
        

    def display_quote(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        conn = sqlite3.connect('planta47.db')
        
 
        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE (CAPACIDAD='18' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?)''',
                              (todau,self.locat,self.cond))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE (CAPACIDAD='18' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION=?) ''',
                              (todau,self.locat,self.cond))

        my_datac  = cursor.fetchall()
        
        self.quote_widget.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget.color=[1,0,0,1]
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])
            #self.quote_widget.text = str('NA')
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget.color=[1,1,0,1]
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])   
        else:
            self.quote_widget.text = str(my_data[0][0]+my_data[1][0])


        




        cursor = conn.execute('''SELECT  cantidad from COMPANY2 WHERE (CAPACIDAD='43' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?) ''',
                              (todau,self.locat,self.cond))
        
        my_data  = cursor.fetchall()


        cursor = conn.execute('''SELECT  consultas from COMPANY2 WHERE (CAPACIDAD='43' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION=?) ''',
                              (todau,self.locat,self.cond))

        my_datac  = cursor.fetchall()
        
        self.quote_widget2.color=[1,1,1,1] 
        if (my_datac[0][0]==0 and my_datac[1][0]==0):
            self.quote_widget2.color=[1,0,0,1]
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])
            #self.quote_widget2.text = str('NA')
        elif (my_datac[0][0]==0 or my_datac[1][0]==0):
            self.quote_widget2.color=[1,1,0,1]
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])     
        else:
            self.quote_widget2.text = str(my_data[0][0]+my_data[1][0])




      

      

        #print "MY DATA", my_data
        

        conn.close()

  
            
    def get_date(self):
        if self.sea=='otro':
            todau= datetime.strptime(toda, "%Y-%m-%d").date()
        else:
            todau= today
        self.dia.text= str(todau)





class AGLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    direc2=ObjectProperty()
    agll= ObjectProperty()
    agv= ObjectProperty()
    tipoo=StringProperty('ag')
    cond=StringProperty('op')
    locat = StringProperty('l2')
    
    dia = ObjectProperty()

    #global condp, locatp, tipoop, direc2p


   
    def __init__(self, **kwargs):
        super(AGLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
        self.get_date()
        
        #ba2=0

    def set_esti(self,estt):
        global esti
        esti=estt
        

    
    def set_direc2(self):
        global condp, locatp, tipoop, direc2p
        global table
        table= "COMPANY"
        condp=self.cond
        locatp=self.locat
        tipoop=self.tipoo
        direc2p=self.direc2
        #print "ACA LO HIZO !!"
        #cond,locat,tipoo,direc2
        if self.locat=='l2':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 2 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 2 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 2 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='l1':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 1 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 1 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 1 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 1 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 1 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - LINEA 1 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pag':    
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PATIO GANDOLA (CARGA) - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pa1':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 1 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 1 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 1 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 1 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 1 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 1 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pa2':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 2 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 2 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 2 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 2 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 2 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PATIO 2 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pla1':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 1 - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 1  - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - PLATAFORMA 1  - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 1 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 1 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 1 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pla2':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 2 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 2 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 2 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 2 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 2 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 2 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='epsdc':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - EPSDC - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pla43':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 43 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 4 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 4 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 4 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 4 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 10kg - PLATAFORMA 4 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            
        
        
        

    def set_ttipo(self,tio):
        self.tipoo=tio

   

    def display_quote(self):
        #print "condicion", self.cond
        conn = sqlite3.connect('planta47.db')
        
 
        cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
          AND CAPACIDAD='10') ''', (self.tipoo, today, self.locat,self.cond))
        
        my_data  = cursor.fetchall()
        self.quote_widget.color= [1,1,1,1]
        self.quote_widget2.color= [1,1,1,1]

        self.quote_widget.text = str( my_data[0][0])
        if my_data[0][1] == 0:
            self.quote_widget.color= [1,0,0,1]
            #self.quote_widget.text=str('NA')
            ##self.agll.text=str('')
            #self.agll.text=self.quote_widget.text
##            
##        else:
##            #self.agll.text=str('')

        self.quote_widget2.text = str( my_data[1][0])
        if my_data[1][1] == 0:
            self.quote_widget2.color= [1,0,0,1]
            #self.quote_widget2.text=str('NA')
            ##self.agv.text=str('')
            #self.agv.text=self.quote_widget2.text
            
            
##        else:
##            #self.agv.text=str('')
            

        #print "condicion", self.cond
        #print "tipo", self.tipoo
       # #print "VAC", self.agll.text

        #print "MY DATA", my_data
        

        conn.close()

        #random_quote = self.get_random_quote()
        #self.quote_widget.text = r'"%s"%s-- %s' % \
        #    (random_quote['quote'], '\n' * 2, random_quote['author'])
    
        
    def save(self):

##            #UPDATE
            #ba2=1
            conn = sqlite3.connect('planta47.db')



            ban=0
            bao1=0
            bao2=0

            if self.agll.text:
                bao1=1

            if self.agv.text:
                bao2=1
            
            try:
                int(self.agll.text)
            except ValueError:
                if not self.agll.text:
                    # self.quote_widget.color= [1,0,0,1]
                     self.quote_widget.text=str('NA')
                     
                    #self.quote_widget3.text = 'X'
                else:
                    ban=1

            try:
                int(self.agv.text)
            except ValueError:
                if not self.agv.text:
                   # self.quote_widget2.color= [1,0,0,1]
                    self.quote_widget2.text=str('NA')
                   
                    #self.quote_widget.text = 'X'
                else:
                    ban=1


##            try:
##                int(self.agv.text)
##            except ValueError:
##                ban=1
          
            #self.p.text=str(0)
            #print 'DATOS'
            #print   self.agll.text
            #print   self.agv.text
            
#ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA
##            if ban==2:
##                self.quote_widget.color= [1,0,0,1]
##                self.agll.text=self.quote_widget.text
##                self.agv.text=self.quote_widget2.text
##                self.manager.current = 'plinea2'
                
            if ban==0:

                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
                   AND CAPACIDAD='10') ''', (self.tipoo, today, self.locat,self.cond))
        
                my_data  = cursor.fetchall()

                self.quote_widget.color= [1,1,1,1]
                self.quote_widget2.color= [1,1,1,1]


##                agllop=int(self.agll.text)+ my_data[0][0]
##                agvop=int(self.agv.text)+ my_data[1][0]

                if not self.agll.text:
                    self.quote_widget.color= [1,0,0,1]
                    agllop=0+ my_data[0][0]
                    self.quote_widget.text=str(agllop)
                else:
                    agllop=int(self.agll.text)+ my_data[0][0]
                    self.quote_widget.text=str(agllop)

                
                    
                    
                if not self.agv.text:
                    self.quote_widget2.color= [1,0,0,1]
                    agvop=0+ my_data[1][0]
                    self.quote_widget2.text=str(agvop)
                else:
                    agvop=int(self.agv.text)+ my_data[1][0]
                    self.quote_widget2.text=str(agvop)
                    
                
                opo=my_data[0][1]
                opo2=my_data[1][1]

                if bao1==1:
                    opo =+ 1

                if bao2==1:
                    opo2 =+ 1

                #self.agll.text, self.agv.text



                #print "EPA!!" "\n"
                #print "agllop", agllop
                #print "agvop", agvop
                
                    
                
                my_data2 = ({'locate':self.locat, 'tip':self.tipoo, 'est':'ll', 'value':agllop ,'condi':self.cond ,'con':opo, 'fe': today}, \
                            {'locate':self.locat,'tip':self.tipoo, 'est':'v', 'value':agvop , 'condi':self.cond ,'con':opo2, 'fe': today})
                            

                conn.executemany("UPDATE COMPANY SET CANTIDAD =:value WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()


                conn.executemany("UPDATE COMPANY SET  CONSULTAS=:con WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()

                
                #print "Total number of rows updated :", conn.total_changes

##                cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##                for row in cursor:
##                   #print "ID = ", row[0]
##                   #print "FECHA = ", row[1]
##                   #print "UBICACION = ", row[2]
##                   #print "TIPO = ", row[3]
##                   #print "Numero de cilindros = ", row[4], "\n"
##
##                #print "Operation done successfully";
                conn.close()
                self.manager.current = 'plinea2'

                
            
    def get_date(self):
            self.dia.text= str(today)





class VHAGLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    direc2=ObjectProperty()
    agll= ObjectProperty()
    agv= ObjectProperty()
    tipoo=StringProperty('ag')
    cond=StringProperty('op')
    locat = StringProperty('gan1')
    
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(VHAGLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 1 - AUTOGAS')
        self.get_date()
        
        #ba2=0

    def set_esti(self,estt):
        global esti
        esti=estt
        
    def set_direc2(self):
        global table
        table= "COMPANY3"
        global condp, locatp, tipoop, direc2p
        condp=self.cond
        locatp=ch_loc
        tipoop=self.tipoo
        direc2p=self.direc2
        
        if ch_loc=='gan1':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 1 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 1 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 1 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
        if ch_loc=='gan2':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 2 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 2 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - GANDOLA 2 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
        if ch_loc=='fle1':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - FLETERO 1 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - FLETERO 1 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - FLETERO 1 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
        if ch_loc=='fle2':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - FLETERO 2 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - FLETERO 2 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - FLETERO 2 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
        if ch_loc=='eps1':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 1 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 1 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 1 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
        if ch_loc=='eps2':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 2 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 2 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 2 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
        if ch_loc=='eps3':
            if self.tipoo=='ag':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 3 - AUTOGAS')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='cln':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 3 - CLIP ON')
                #print "condicion", self.cond
                #print "tipo", self.tipoo
            elif self.tipoo=='p':
                self.direc2.text=str('VEHICULOS - 10kg - EPSDC 3 - PLASTICO')
                #print "condicion", self.cond
                #print "tipo", self.tipoo



                


        
        
        
        

    def set_ttipo(self,tio):
        global tipoop
        self.tipoo=tio
        tipoop=self.tipoo

   

    def display_quote(self):
        #print "condicion", self.cond
        conn = sqlite3.connect('planta47.db')
        
 
        cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY3 WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op'
          AND CAPACIDAD='10') ''', (self.tipoo, today, ch_loc))
        
        my_data  = cursor.fetchall()
        #print "TIPO", self.tipoo
        #print "UBICACION", self.locat
        #print "MIS DATOS", my_data
        self.quote_widget.color= [1,1,1,1]
        self.quote_widget2.color= [1,1,1,1]

        self.quote_widget.text = str( my_data[0][0])
        if my_data[0][1] == 0:
            self.quote_widget.color= [1,0,0,1]
            #self.quote_widget.text=str('NA')
            ##self.agll.text=str('')
            #self.agll.text=self.quote_widget.text
            
        #else:
            #self.agll.text=str('')

        self.quote_widget2.text = str( my_data[1][0])
        if my_data[1][1] == 0:
            self.quote_widget2.color= [1,0,0,1]
            #self.quote_widget2.text=str('NA')
           # #self.agv.text=str('')
            #self.agv.text=self.quote_widget2.text
            
            
        #else:
            #self.agv.text=str('')
            

        #print "condicion", self.cond
        #print "tipo", self.tipoo
        ##print "VAC", self.agll.text

        #print "MY DATA", my_data
        

        conn.close()

        #random_quote = self.get_random_quote()
        #self.quote_widget.text = r'"%s"%s-- %s' % \
        #    (random_quote['quote'], '\n' * 2, random_quote['author'])
    
        
    def save(self):

##            #UPDATE
            #ba2=1
            conn = sqlite3.connect('planta47.db')



            ban=0
            bao1=0
            bao2=0

##            if self.agll.text:
##                bao1=1
##
##            if self.agv.text:
##                bao2=1
##            
##            try:
##                int(self.agll.text)
##            except ValueError:
##                if not self.agll.text:
##                    # self.quote_widget.color= [1,0,0,1]
##                     self.quote_widget.text=str('NA')
##                     
##                    #self.quote_widget3.text = 'X'
##                else:
##                    ban=1
##
##            try:
##                int(self.agv.text)
##            except ValueError:
##                if not self.agv.text:
##                   # self.quote_widget2.color= [1,0,0,1]
##                    self.quote_widget2.text=str('NA')
##                   
##                    #self.quote_widget.text = 'X'
##                else:
##                    ban=1


##            try:
##                int(self.agv.text)
##            except ValueError:
##                ban=1
          
            #self.p.text=str(0)
##            #print 'DATOS'
##            #print   self.agll.text
##            #print   self.agv.text
            
#ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA
##            if ban==2:
##                self.quote_widget.color= [1,0,0,1]
##                self.agll.text=self.quote_widget.text
##                self.agv.text=self.quote_widget2.text
##                self.manager.current = 'plinea2'
                
            if ban==0:

                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY3 WHERE (TIPO= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?
                   AND CAPACIDAD='10') ''', (self.tipoo, today, ch_loc,self.cond))
        
                my_data  = cursor.fetchall()

                self.quote_widget.color= [1,1,1,1]
                self.quote_widget2.color= [1,1,1,1]


##                agllop=int(self.agll.text)+ my_data[0][0]
##                agvop=int(self.agv.text)+ my_data[1][0]
##
##                if not self.agll.text:
##                    self.quote_widget.color= [1,0,0,1]
##                    agllop=0+ my_data[0][0]
##                else:
##                    agllop=int(self.agll.text)+ my_data[0][0]
##
##                
##                    
##                    
##                if not self.agv.text:
##                    self.quote_widget2.color= [1,0,0,1]
##                    agvop=0+ my_data[1][0]
##                else:
##                    agvop=int(self.agv.text)+ my_data[1][0]
                    
                
                opo=my_data[0][1]
                opo2=my_data[1][1]

                if bao1==1:
                    opo =+ 1

                if bao2==1:
                    opo2 =+ 1

                #self.agll.text, self.agv.text


##
##                #print "EPA!!" "\n"
##                #print "agllop", agllop
##                #print "agvop", agvop
                
                    
                
##                my_data2 = ({'locate':ch_loc, 'tip':self.tipoo, 'est':'ll', 'value':agllop ,'condi':self.cond ,'con':opo, 'fe': today}, \
##                            {'locate':ch_loc,'tip':self.tipoo, 'est':'v', 'value':agvop , 'condi':self.cond ,'con':opo2, 'fe': today})
##                            
##
##                conn.executemany("UPDATE COMPANY3 SET CANTIDAD =:value WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
##                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) ", my_data2)
##                
##                
##            
##                conn.commit()
##
##
##                conn.executemany("UPDATE COMPANY3 SET  CONSULTAS=:con WHERE (UBICACION=:locate AND TIPO=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
##                 AND CONDICION=:condi AND CAPACIDAD='10' AND ESTADO=:est) ", my_data2)
##                
##                
##            
##                conn.commit()

                
                #print "Total number of rows updated :", conn.total_changes

##                cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##                for row in cursor:
##                   #print "ID = ", row[0]
##                   #print "FECHA = ", row[1]
##                   #print "UBICACION = ", row[2]
##                   #print "TIPO = ", row[3]
##                   #print "Numero de cilindros = ", row[4], "\n"
##
##                #print "Operation done successfully";
                conn.close()
                self.manager.current = 'vhplinea2'

                
            
    def get_date(self):
            self.dia.text= str(today)




class NAGLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    direc2=ObjectProperty()
    agll= ObjectProperty()
    agv= ObjectProperty()
    tipoo=StringProperty('18')
    cond=StringProperty('op')
    locat = StringProperty('l2')
    
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(NAGLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
        self.get_date()
        
        #ba2=0

   

    def set_esti(self,estt):
        global esti
        esti=estt
        
    def set_direc2(self):
        if self.locat=='l2':
            if self.cond=='op':
                if self.tipoo=='18':
                    self.direc2.text=str('PLANTA - 18 kg  - LINEA 2 - OPERATIVOS ')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='43':
                    self.direc2.text=str('PLANTA - 43 kg  - LINEA 2 - OPERATIVOS ')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 2 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 2 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 2 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 2 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='l1':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 1 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 1 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 1 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 1 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 1 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - LINEA 1 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pag':    
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO GANDOLA (CARGA) - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pa1':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 1 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 1 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 1 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 1 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 1 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 1 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pa2':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 2 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 2 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 2 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 2 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 2 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PATIO 2 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pla1':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 1 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='pla2':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - PLATAFORMA 2 - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        if self.locat=='epsdc':
            if self.cond=='op':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - EPSDC - OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - EPSDC - OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - EPSDC - OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            if self.cond=='nop':
                if self.tipoo=='ag':
                    self.direc2.text=str('PLANTA - 18/43 kg  - EPSDC - NO OPERATIVOS - AUTOGAS')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='cln':
                    self.direc2.text=str('PLANTA - 18/43 kg  - EPSDC - NO OPERATIVOS - CLIP ON')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                elif self.tipoo=='p':
                    self.direc2.text=str('PLANTA - 18/43 kg  - EPSDC - NO OPERATIVOS - PLASTICO')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        
        
        

    def set_ttipo(self,tio):
        self.tipoo=tio

   

    def display_quote(self):
        #print "condicion", self.cond
        conn = sqlite3.connect('planta47.db')
        
 
        cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE (CAPACIDAD= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?) ''',
                              (self.tipoo, today, self.locat,self.cond))
        
        my_data  = cursor.fetchall()
        self.quote_widget.color= [1,1,1,1]
        self.quote_widget2.color= [1,1,1,1]

        self.quote_widget.text = str( my_data[0][0])
        if my_data[0][1] == 0:
            self.quote_widget.color= [1,0,0,1]
            #self.quote_widget.text=str('NA')
            #self.agll.text=str('')
            
        #else:
            #self.agll.text=str('')
            #self.agll.text=self.quote_widget.text

        self.quote_widget2.text = str( my_data[1][0])
        if my_data[1][1] == 0:
            self.quote_widget2.color= [1,0,0,1]
            #self.quote_widget2.text=str('NA')
            #self.agv.text=str('')
        #else:
            #self.agv.text=str('')
            #self.agv.text=self.quote_widget2.text
            

        #print "condicion", self.cond
        #print "tipo", self.tipoo
        ##print "VAC", self.agll.text

        #print "MY DATA", my_data
        

        conn.close()

        #random_quote = self.get_random_quote()
        #self.quote_widget.text = r'"%s"%s-- %s' % \
        #    (random_quote['quote'], '\n' * 2, random_quote['author'])
    
        
    def save(self):

##            #UPDATE
            #ba2=1
            conn = sqlite3.connect('planta47.db')



            ban=0
            bao1=0
            bao2=0

            if self.agll.text:
                bao1=1

            if self.agv.text:
                bao2=1
            
            try:
                int(self.agll.text)
            except ValueError:
                if not self.agll.text:
                    # self.quote_widget.color= [1,0,0,1]
                     self.quote_widget.text=str('NA')
                     
                    #self.quote_widget3.text = 'X'
                else:
                    ban=1

            try:
                int(self.agv.text)
            except ValueError:
                if not self.agv.text:
                   # self.quote_widget2.color= [1,0,0,1]
                    self.quote_widget2.text=str('NA')
                   
                    #self.quote_widget.text = 'X'
                else:
                    ban=1


##            try:
##                int(self.agv.text)
##            except ValueError:
##                ban=1
          
            #self.p.text=str(0)
            #print 'DATOS'
            #print   self.agll.text
            #print   self.agv.text
            
#ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA
##            if ban==2:
##                self.quote_widget.color= [1,0,0,1]
##                self.agll.text=self.quote_widget.text
##                self.agv.text=self.quote_widget2.text
##                self.manager.current = 'plinea2'
                
            if ban==0:

                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY2 WHERE (CAPACIDAD= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= ?) ''',
                                      (self.tipoo, today, self.locat,self.cond))
        
                my_data  = cursor.fetchall()

                self.quote_widget.color= [1,1,1,1]
                self.quote_widget2.color= [1,1,1,1]

                if not self.agll.text:
                    self.quote_widget.color= [1,0,0,1]
                    agllop=0+ my_data[0][0]
                else:
                    agllop=int(self.agll.text)+ my_data[0][0]

                
                    
                    
                if not self.agv.text:
                    self.quote_widget2.color= [1,0,0,1]
                    agvop=0+ my_data[1][0]
                else:
                    agvop=int(self.agv.text)+ my_data[1][0]
                    
                
                opo=my_data[0][1]
                opo2=my_data[1][1]


                if bao1==1:
                    opo =+ 1

                if bao2==1:
                    opo2 =+ 1

                #self.agll.text, self.agv.text
                #print "LLENO", agllop
                #print "VACIO", agvop
                
                    
                
                my_data2 = ({'locate':self.locat, 'tip':self.tipoo, 'est':'ll', 'value':agllop ,'condi':self.cond ,'con':opo, 'fe': today},
                            {'locate':self.locat,'tip':self.tipoo, 'est':'v', 'value':agvop , 'condi':self.cond ,'con':opo2, 'fe': today})
                            

                conn.executemany("UPDATE COMPANY2 SET CANTIDAD =:value WHERE (UBICACION=:locate AND CAPACIDAD=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi  AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()


                conn.executemany("UPDATE COMPANY2 SET  CONSULTAS=:con WHERE (UBICACION=:locate AND CAPACIDAD=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi  AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()

                
                #print "Total number of rows updated :", conn.total_changes

##                cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##                for row in cursor:##                   #print "ID = ", row[0]
##                   #print "FECHA = ", row[1]
##                   #print "UBICACION = ", row[2]
##                   #print "TIPO = ", row[3]
##                   #print "Numero de cilindros = ", row[4], "\n"
##
##                #print "Operation done successfully";
                conn.close()

                self.manager.current = 'nplinea2'
            
    def get_date(self):
            self.dia.text= str(today)




class N1VHAGLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    direc2=ObjectProperty()
    agll= ObjectProperty()
    agv= ObjectProperty()
    tipoo=StringProperty('18')
    cond=StringProperty('op')
    locat = StringProperty('gan1')
    
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(N1VHAGLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
        self.get_date()
        
        #ba2=0

   

    def set_esti(self,estt):
        global esti
        esti=estt
        
    def set_direc2(self):
        if ch_loc=='gan1':
            self.direc2.text=str('VEHICULOS - 18 kg  - GANDOLA 1')
            #print "condicion", self.cond
            #print "tipo", self.tipoo
        elif ch_loc=='gan2':
            self.direc2.text=str('VEHICULOS - 18 kg  - GANDOLA 2')
            #print "condicion", self.cond
            #print "tipo", self.tipoo
                
           

    def set_ttipo(self,tio):
        self.tipoo=tio

   

    def display_quote(self):
        #print "condicion", self.cond
        conn = sqlite3.connect('planta47.db')
        
 
        cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY4 WHERE (CAPACIDAD= '18' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op') ''',
                              (today, ch_loc))
        
        my_data  = cursor.fetchall()

        #print "UBICACION", ch_loc
        #print "DATA", my_data
        self.quote_widget.color= [1,1,1,1]
        self.quote_widget2.color= [1,1,1,1]

        self.quote_widget.text = str( my_data[0][0])
        if my_data[0][1] == 0:
            self.quote_widget.color= [1,0,0,1]
            #self.quote_widget.text=str('NA')
            #self.agll.text=str('')
            
        #else:
            #self.agll.text=str('')
            #self.agll.text=self.quote_widget.text

        self.quote_widget2.text = str( my_data[1][0])
        if my_data[1][1] == 0:
            self.quote_widget2.color= [1,0,0,1]
            #self.quote_widget2.text=str('NA')
            #self.agv.text=str('')
        #else:
            #self.agv.text=str('')
            #self.agv.text=self.quote_widget2.text
            

        conn.close()

        #random_quote = self.get_random_quote()
        #self.quote_widget.text = r'"%s"%s-- %s' % \
        #    (random_quote['quote'], '\n' * 2, random_quote['author'])
    
        
    def save(self):

##            #UPDATE
            #ba2=1
            conn = sqlite3.connect('planta47.db')



            ban=0
            bao1=0
            bao2=0

            if self.agll.text:
                bao1=1

            if self.agv.text:
                bao2=1
            
            try:
                int(self.agll.text)
            except ValueError:
                if not self.agll.text:
                    # self.quote_widget.color= [1,0,0,1]
                     self.quote_widget.text=str('NA')
                     
                    #self.quote_widget3.text = 'X'
                else:
                    ban=1

            try:
                int(self.agv.text)
            except ValueError:
                if not self.agv.text:
                   # self.quote_widget2.color= [1,0,0,1]
                    self.quote_widget2.text=str('NA')
                   
                    #self.quote_widget.text = 'X'
                else:
                    ban=1


##            try:
##                int(self.agv.text)
##            except ValueError:
##                ban=1
          
            #self.p.text=str(0)
            #print 'DATOS'
            #print   self.agll.text
            #print   self.agv.text
            
#ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA
##            if ban==2:
##                self.quote_widget.color= [1,0,0,1]
##                self.agll.text=self.quote_widget.text
##                self.agv.text=self.quote_widget2.text
##                self.manager.current = 'plinea2'
                
            if ban==0:

                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY4 WHERE
               (CAPACIDAD= '18' AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op') ''',
                                      (today, ch_loc))
        
                my_data  = cursor.fetchall()

                self.quote_widget.color= [1,1,1,1]
                self.quote_widget2.color= [1,1,1,1]

                if not self.agll.text:
                    self.quote_widget.color= [1,0,0,1]
                    agllop=0+ my_data[0][0]
                else:
                    agllop=int(self.agll.text)+ my_data[0][0]

                
                    
                    
                if not self.agv.text:
                    self.quote_widget2.color= [1,0,0,1]
                    agvop=0+ my_data[1][0]
                else:
                    agvop=int(self.agv.text)+ my_data[1][0]
                    
                
                opo=my_data[0][1]
                opo2=my_data[1][1]


                if bao1==1:
                    opo =+ 1

                if bao2==1:
                    opo2 =+ 1

                
                
                my_data2 = ({'locate':ch_loc, 'tip':'18', 'est':'ll', 'value':agllop ,'condi':'op' ,'con':opo, 'fe': today},
                            {'locate':ch_loc,'tip':'18', 'est':'v', 'value':agvop , 'condi':'op' ,'con':opo2, 'fe': today})
                            

                conn.executemany("UPDATE COMPANY4 SET CANTIDAD =:value WHERE (UBICACION=:locate AND CAPACIDAD=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi  AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()


                conn.executemany("UPDATE COMPANY4 SET  CONSULTAS=:con WHERE (UBICACION=:locate AND CAPACIDAD=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi  AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()

                
                #print "Total number of rows updated :", conn.total_changes

##                cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##                for row in cursor:##                   #print "ID = ", row[0]
##                   #print "FECHA = ", row[1]
##                   #print "UBICACION = ", row[2]
##                   #print "TIPO = ", row[3]
##                   #print "Numero de cilindros = ", row[4], "\n"
##
##                #print "Operation done successfully";
                conn.close()

                self.manager.current = 'n1vhplinea2'
            
    def get_date(self):
            self.dia.text= str(today)





class N2VHAGLINEA2Screen(Screen):
    quote_widget = ObjectProperty()
    quote_widget2 = ObjectProperty()
    direc2=ObjectProperty()
    agll= ObjectProperty()
    agv= ObjectProperty()
    tipoo=StringProperty('18')
    cond=StringProperty('op')
    locat = StringProperty('gan1')
    
    dia = ObjectProperty()


   
    def __init__(self, **kwargs):
        super(N2VHAGLINEA2Screen, self).__init__(**kwargs)
        self.display_quote()
        self.direc2.text=str('PLANTA - 10kg - LINEA 2 - OPERATIVOS - AUTOGAS')
        self.get_date()
        
        #ba2=0

   

    def set_esti(self,estt):
        global esti
        esti=estt
        
    def set_direc2(self):
        if ch_loc=='fle1':
            if self.tipoo=='18':
                    self.direc2.text=str('VEHICULOS - 18 kg  - FLETERO 1')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            elif self.tipoo=='43':
                    self.direc2.text=str('VEHICULOS - 43 kg  - FLETERO 1')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        elif ch_loc=='fle2':
            if self.tipoo=='18':
                    self.direc2.text=str('VEHICULOS - 18 kg  - FLETERO 2')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            elif self.tipoo=='43':
                    self.direc2.text=str('VEHICULOS - 43 kg  - FLETERO 2')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        elif ch_loc=='eps1':
            if self.tipoo=='18':
                    self.direc2.text=str('VEHICULOS - 18 kg  - EPSDC 1')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            elif self.tipoo=='43':
                    self.direc2.text=str('VEHICULOS - 43 kg  - EPSDC 1')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        elif ch_loc=='eps2':
            if self.tipoo=='18':
                    self.direc2.text=str('VEHICULOS - 18 kg  - EPSDC 2')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            elif self.tipoo=='43':
                    self.direc2.text=str('VEHICULOS - 43 kg  - EPSDC 2')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
        elif ch_loc=='eps3':
            if self.tipoo=='18':
                    self.direc2.text=str('VEHICULOS - 18 kg  - EPSDC 3')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
            elif self.tipoo=='43':
                    self.direc2.text=str('VEHICULOS - 43 kg  - EPSDC 3')
                    #print "condicion", self.cond
                    #print "tipo", self.tipoo
                
           

    def set_ttipo(self,tio):
        self.tipoo=tio


    def display_quote(self):
        #print "condicion", self.cond
        conn = sqlite3.connect('planta47.db')
        
 
        cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY4 WHERE
        (CAPACIDAD= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op') ''',
                              (self.tipoo, today, ch_loc))
        
        my_data  = cursor.fetchall()
        self.quote_widget.color= [1,1,1,1]
        self.quote_widget2.color= [1,1,1,1]

        self.quote_widget.text = str( my_data[0][0])
        if my_data[0][1] == 0:
            self.quote_widget.color= [1,0,0,1]
            #self.quote_widget.text=str('NA')
            ##self.agll.text=str('')
            
        #else:
            #self.agll.text=str('')
            #self.agll.text=self.quote_widget.text

        self.quote_widget2.text = str( my_data[1][0])
        if my_data[1][1] == 0:
            self.quote_widget2.color= [1,0,0,1]
            #self.quote_widget2.text=str('NA')
            #self.agv.text=str('')
        #else:
            #self.agv.text=str('')
            #self.agv.text=self.quote_widget2.text
            

        #print "condicion", self.cond
        #print "tipo", self.tipoo
        ##print "VAC", self.agll.text

        #print "MY DATA", my_data
        

        conn.close()

        #random_quote = self.get_random_quote()
        #self.quote_widget.text = r'"%s"%s-- %s' % \
        #    (random_quote['quote'], '\n' * 2, random_quote['author'])
    
        
    def save(self):

##            #UPDATE
            #ba2=1
            conn = sqlite3.connect('planta47.db')



            ban=0
            bao1=0
            bao2=0

            if self.agll.text:
                bao1=1

            if self.agv.text:
                bao2=1
            
            try:
                int(self.agll.text)
            except ValueError:
                if not self.agll.text:
                    # self.quote_widget.color= [1,0,0,1]
                     self.quote_widget.text=str('NA')
                     
                    #self.quote_widget3.text = 'X'
                else:
                    ban=1

            try:
                int(self.agv.text)
            except ValueError:
                if not self.agv.text:
                   # self.quote_widget2.color= [1,0,0,1]
                    self.quote_widget2.text=str('NA')
                   
                    #self.quote_widget.text = 'X'
                else:
                    ban=1


##            try:
##                int(self.agv.text)
##            except ValueError:
##                ban=1
          
            #self.p.text=str(0)
            #print 'DATOS'
            #print   self.agll.text
            #print   self.agv.text
            
#ID, UBICACION, TIPO,  ORIGEN, CONDICION, CAPACIDAD, ESTADO, CANTIDAD, FECHA
##            if ban==2:
##                self.quote_widget.color= [1,0,0,1]
##                self.agll.text=self.quote_widget.text
##                self.agv.text=self.quote_widget2.text
##                self.manager.current = 'plinea2'
                
            if ban==0:

                cursor = conn.execute('''SELECT  cantidad, consultas from COMPANY4 WHERE
                 (CAPACIDAD= ? AND FECHA = ? AND UBICACION= ? AND ORIGEN='eps' AND CONDICION= 'op') ''',
                                      (self.tipoo, today, ch_loc))
        
                my_data  = cursor.fetchall()

                self.quote_widget.color= [1,1,1,1]
                self.quote_widget2.color= [1,1,1,1]

                if not self.agll.text:
                    self.quote_widget.color= [1,0,0,1]
                    agllop=0+ my_data[0][0]
                else:
                    agllop=int(self.agll.text)+ my_data[0][0]

                
                    
                    
                if not self.agv.text:
                    self.quote_widget2.color= [1,0,0,1]
                    agvop=0+ my_data[1][0]
                else:
                    agvop=int(self.agv.text)+ my_data[1][0]
                    
                
                opo=my_data[0][1]
                opo2=my_data[1][1]


                if bao1==1:
                    opo =+ 1

                if bao2==1:
                    opo2 =+ 1

                #self.agll.text, self.agv.text
                #print "LLENO", agllop
                #print "VACIO", agvop
                
                    
                
                my_data2 = ({'locate':ch_loc, 'tip':self.tipoo, 'est':'ll', 'value':agllop ,'condi':'op' ,'con':opo, 'fe': today},
                            {'locate':ch_loc,'tip':self.tipoo, 'est':'v', 'value':agvop , 'condi':'op' ,'con':opo2, 'fe': today})
                            

                conn.executemany("UPDATE COMPANY4 SET CANTIDAD =:value WHERE (UBICACION=:locate AND CAPACIDAD=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi  AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()


                conn.executemany("UPDATE COMPANY4 SET  CONSULTAS=:con WHERE (UBICACION=:locate AND CAPACIDAD=:tip  AND  FECHA =:fe AND ORIGEN='eps' \
                 AND CONDICION=:condi  AND ESTADO=:est) ", my_data2)
                
                
            
                conn.commit()

                
                #print "Total number of rows updated :", conn.total_changes

##                cursor = conn.execute("SELECT id, fecha, ubicacion, tipo,cantidad  from COMPANY")
##                for row in cursor:##                   #print "ID = ", row[0]
##                   #print "FECHA = ", row[1]
##                   #print "UBICACION = ", row[2]
##                   #print "TIPO = ", row[3]
##                   #print "Numero de cilindros = ", row[4], "\n"
##
##                #print "Operation done successfully";
                conn.close()

                self.manager.current = 'n2vhplinea2'

   

    

                
            
    def get_date(self):
            self.dia.text= str(today)






           
# Create the screen manager
sm = ScreenManager()
sm = ScreenManager(transition= FadeTransition())


sm.add_widget(MenuScreen(name='menu'))

sm.add_widget(DIAScreen(name='dia'))


sm.add_widget(SelScreen(name='sel'))


sm.add_widget(INScreen(name='in'))

sm.add_widget(PLANTAScreen(name='planta'))


sm.add_widget(TIPOScreen(name='tipo'))





sm.add_widget(INVENTARIOScreen(name='inventario'))

sm.add_widget(INVENTARIO2Screen(name='inventario2'))

sm.add_widget(INVENTARIO3Screen(name='inventario3'))

sm.add_widget(INVENTARIO4Screen(name='inventario4'))

sm.add_widget(EPSScreen(name='eps'))


sm.add_widget(OPERL2Screen(name='operl2'))

sm.add_widget(PLINEA2Screen(name='plinea2'))

sm.add_widget(CLIPON(name='clipon'))


sm.add_widget(VHPLINEA2Screen(name='vhplinea2'))

sm.add_widget(N1VHPLINEA2Screen(name='n1vhplinea2'))



sm.add_widget(N2VHPLINEA2Screen(name='n2vhplinea2'))

sm.add_widget(AGLINEA2Screen(name='aglinea2'))

sm.add_widget(VHAGLINEA2Screen(name='vhaglinea2'))

sm.add_widget(NOPERL2Screen(name='noperl2'))
sm.add_widget(NPLINEA2Screen(name='nplinea2'))
sm.add_widget(NAGLINEA2Screen(name='naglinea2'))

sm.add_widget(N1VHAGLINEA2Screen(name='n1vhaglinea2'))




sm.add_widget(N2VHAGLINEA2Screen(name='n2vhaglinea2'))

sm.add_widget(Calculator(name='calculator'))

sm.get_screen('dia').bind(sea=sm.get_screen('in').setter('sea'))

sm.get_screen('in').bind(sea=sm.get_screen('sel').setter('sea'))



sm.get_screen('in').bind(sea=sm.get_screen('planta').setter('sea'))
#sm.get_screen('in').bind(toda=sm.get_screen('planta').setter('toda'))

sm.get_screen('planta').bind(sea=sm.get_screen('tipo').setter('sea'))
#sm.get_screen('planta').bind(toda=sm.get_screen('tipo').setter('toda'))
#sm.get_screen('planta').bind(toda=sm.get_screen('tipo').setter('ubc'))




sm.get_screen('tipo').bind(sea=sm.get_screen('inventario').setter('sea'))
#sm.get_screen('tipo').bind(toda=sm.get_screen('inventario').setter('toda'))


sm.get_screen('tipo').bind(sea=sm.get_screen('inventario2').setter('sea'))
#sm.get_screen('tipo').bind(toda=sm.get_screen('inventario2').setter('toda'))


sm.get_screen('tipo').bind(sea=sm.get_screen('inventario3').setter('sea'))
#sm.get_screen('tipo').bind(toda=sm.get_screen('inventario3').setter('toda'))


sm.get_screen('tipo').bind(sea=sm.get_screen('inventario4').setter('sea'))
#sm.get_screen('tipo').bind(toda=sm.get_screen('inventario4').setter('toda'))


sm.get_screen('inventario').bind(locat=sm.get_screen('operl2').setter('locat'))

sm.get_screen('inventario').bind(sea=sm.get_screen('operl2').setter('sea'))
#sm.get_screen('inventario').bind(toda=sm.get_screen('operl2').setter('toda'))

sm.get_screen('inventario').bind(locat=sm.get_screen('eps').setter('locat'))


sm.get_screen('inventario').bind(sea=sm.get_screen('eps').setter('sea'))
#sm.get_screen('inventario').bind(toda=sm.get_screen('eps').setter('toda'))

sm.get_screen('eps').bind(sea=sm.get_screen('clipon').setter('sea'))
#sm.get_screen('eps').bind(toda=sm.get_screen('clipon').setter('toda'))


sm.get_screen('eps').bind(locat=sm.get_screen('clipon').setter('locat'))
#sm.get_screen('eps').bind(locat=sm.get_screen('clipon').setter('locat2'))




sm.get_screen('inventario2').bind(locat=sm.get_screen('noperl2').setter('locat'))

sm.get_screen('inventario2').bind(sea=sm.get_screen('noperl2').setter('sea'))
#sm.get_screen('inventario2').bind(toda=sm.get_screen('noperl2').setter('toda'))

sm.get_screen('inventario3').bind(sea=sm.get_screen('vhplinea2').setter('sea'))
#sm.get_screen('inventario3').bind(toda=sm.get_screen('vhplinea2').setter('toda'))
sm.get_screen('inventario3').bind(locat=sm.get_screen('vhplinea2').setter('locat'))



sm.get_screen('inventario4').bind(sea=sm.get_screen('n1vhplinea2').setter('sea'))
#sm.get_screen('inventario4').bind(toda=sm.get_screen('n1vhplinea2').setter('toda'))
sm.get_screen('inventario4').bind(locat=sm.get_screen('n1vhplinea2').setter('locat'))


sm.get_screen('inventario4').bind(sea=sm.get_screen('n2vhplinea2').setter('sea'))
#sm.get_screen('inventario4').bind(toda=sm.get_screen('n2vhplinea2').setter('toda'))
sm.get_screen('inventario4').bind(locat=sm.get_screen('n2vhplinea2').setter('locat'))


sm.get_screen('operl2').bind(cond=sm.get_screen('plinea2').setter('cond'))
sm.get_screen('operl2').bind(locat=sm.get_screen('plinea2').setter('locat'))

sm.get_screen('operl2').bind(sea=sm.get_screen('plinea2').setter('sea'))
#sm.get_screen('operl2').bind(toda=sm.get_screen('plinea2').setter('toda'))


sm.get_screen('noperl2').bind(cond=sm.get_screen('nplinea2').setter('cond'))
sm.get_screen('noperl2').bind(locat=sm.get_screen('nplinea2').setter('locat'))

sm.get_screen('noperl2').bind(sea=sm.get_screen('nplinea2').setter('sea'))
#sm.get_screen('noperl2').bind(toda=sm.get_screen('nplinea2').setter('toda'))


sm.get_screen('plinea2').bind(cond=sm.get_screen('aglinea2').setter('cond'))
sm.get_screen('plinea2').bind(locat=sm.get_screen('aglinea2').setter('locat'))
sm.get_screen('plinea2').bind(tipoo=sm.get_screen('aglinea2').setter('tipoo'))
sm.get_screen('plinea2').bind(direc2=sm.get_screen('aglinea2').setter('direc2'))

##sm.get_screen('aglinea2').bind(cond=sm.get_screen('calculator').setter('cond'))
##sm.get_screen('aglinea2').bind(locat=sm.get_screen('calculator').setter('locat'))
##sm.get_screen('aglinea2').bind(tipoo=sm.get_screen('calculator').setter('tipoo'))
##sm.get_screen('aglinea2').bind(direc2=sm.get_screen('calculator').setter('direc2'))



sm.get_screen('vhplinea2').bind(cond=sm.get_screen('vhaglinea2').setter('cond'))
sm.get_screen('vhplinea2').bind(locat=sm.get_screen('vhaglinea2').setter('locat'))
sm.get_screen('vhplinea2').bind(tipoo=sm.get_screen('vhaglinea2').setter('tipoo'))
sm.get_screen('vhplinea2').bind(direc2=sm.get_screen('vhaglinea2').setter('direc2'))



sm.get_screen('nplinea2').bind(cond=sm.get_screen('naglinea2').setter('cond'))
sm.get_screen('nplinea2').bind(locat=sm.get_screen('naglinea2').setter('locat'))
sm.get_screen('nplinea2').bind(tipoo=sm.get_screen('naglinea2').setter('tipoo'))
sm.get_screen('nplinea2').bind(direc2=sm.get_screen('naglinea2').setter('direc2'))

sm.get_screen('n1vhplinea2').bind(cond=sm.get_screen('n1vhaglinea2').setter('cond'))
sm.get_screen('n1vhplinea2').bind(locat=sm.get_screen('n1vhaglinea2').setter('locat'))
sm.get_screen('n1vhplinea2').bind(tipoo=sm.get_screen('n1vhaglinea2').setter('tipoo'))
sm.get_screen('n1vhplinea2').bind(direc2=sm.get_screen('n1vhaglinea2').setter('direc2'))


sm.get_screen('n2vhplinea2').bind(cond=sm.get_screen('n2vhaglinea2').setter('cond'))
sm.get_screen('n2vhplinea2').bind(locat=sm.get_screen('n2vhaglinea2').setter('locat'))
sm.get_screen('n2vhplinea2').bind(tipoo=sm.get_screen('n2vhaglinea2').setter('tipoo'))
sm.get_screen('n2vhplinea2').bind(direc2=sm.get_screen('n2vhaglinea2').setter('direc2'))


class Planta_AutomatizadaApp(App):
    title = 'Planta Automatizada GFM'
    #icon = 'icono3.jpg'

    def build(self):
        self.icon = 'icono3.png'
        
        return sm

if __name__ == '__main__':
    Planta_AutomatizadaApp().run()
