
from Plugins.Plugin import PluginDescriptor
from Components.ActionMap import ActionMap
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Components.Label import Label
from Components.MenuList import MenuList

#screen taille H-V
#title taille 
#menu taille(380:ligne bleu) - elargir verticalement la hauteur du Screen(size=400*400)
#position screen: position="center,center"

class Enigma2_STORE(Screen):
    skin = """
        <screen name="Enigma2_STORE" title="Enigma2 Tools" position="center,center" size="600,700">             
            <widget name="title" position="70,30" size="500,60" font="Regular;24" halign="center" />    
            <widget name="menu" position="100,120" size="400,400" itemHeight="50" />                        
        </screen>
    """

    def __init__(self, session):
        Screen.__init__(self, session)
        self.list = []
        self.list.append(('1- IMAGES', 'ejecutar1'))
        self.list.append(('2- CHANNELS', 'ejecutar2'))
        self.list.append(('3- PICONS', 'ejecutar3'))
        self.list.append(('4- PLUGINS', 'ejecutar4'))
        self.list.append(('5- CAM', 'ejecutar5'))
        self.list.append(('6- IPTV', 'ejecutar6'))      
        self.list.append(('7- TOOLS', 'ejecutar7'))
        self.list.append(('8- NEW OPTION', 'ejecutar8')) 
        self.menu = MenuList(self.list)
        self['menu'] = self.menu
        self['title'] = Label('PANEL Enigma2')

        self['actions'] = ActionMap(['OkCancelActions'], {
            'ok': self.seleccionarfuncion,
            'cancel': self.close,
        }, -2)
           
    def seleccionarfuncion(self):
        ejecutarfuncion = self.menu.getCurrent()[1]
        if ejecutarfuncion == "ejecutar1":
            self.funcion1()
        elif ejecutarfuncion == "ejecutar2":
            self.funcion2()
        elif ejecutarfuncion == "ejecutar3":
            self.funcion3()
        elif ejecutarfuncion == "ejecutar4":
            self.funcion4()
        elif ejecutarfuncion == "ejecutar5":
            self.funcion5()
        elif ejecutarfuncion == "ejecutar6":
            self.funcion6()  
        elif ejecutarfuncion == "ejecutar7":
            self.funcion7()
        elif ejecutarfuncion == "ejecutar8":
            self.funcion8()
    
    def funcion1(self):
        self.session.open(MessageBox, "Liste des IMAGES ...", MessageBox.TYPE_INFO)
     
    def funcion2(self):
        self.session.open(MessageBox, "Liste des CHANNELS ...", MessageBox.TYPE_INFO)
        
    def funcion3(self):
        self.session.open(MessageBox, "Liste des PICONS ...", MessageBox.TYPE_INFO)
     
    def funcion4(self):
        self.session.open(MessageBox, "Liste des PLUGINS ...", MessageBox.TYPE_INFO)
    
    def funcion5(self):
        self.session.open(MessageBox, "Liste des CAM ...", MessageBox.TYPE_INFO)
     
    def funcion6(self):
        self.session.open(MessageBox, "Liste des IPTV ...", MessageBox.TYPE_INFO) 
    
    def funcion7(self):
        self.session.open(MessageBox, "Liste des TOOLS ...", MessageBox.TYPE_INFO)

    def funcion8(self):
        self.session.open(MessageBox, "NEW  option ...", MessageBox.TYPE_INFO)
 
 
def main(session, **kwargs):
    session.open(Enigma2_STORE)

def Plugins(**kwargs):
    return [PluginDescriptor(
        name="Enigma2 Tools",
        description="PANEL for Enigma2 v1.0",
        icon="icon.png",
        where=[PluginDescriptor.WHERE_PLUGINMENU],
        fnc=main,
    )]