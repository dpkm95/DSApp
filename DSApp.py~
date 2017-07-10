from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color,Line,Rectangle
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty
import math
from functools import partial

class Painter(Widget):        
    p_ix=NumericProperty()    
    p_iy=NumericProperty()
    p_fx=NumericProperty()
    p_fy=NumericProperty()
    nodef = [0]
    ptrf = [0]
    drawNode = False
    drawPtr = False
    new_ptr=False
    head = True
    value=[10]
    ptr_count=0
    def on_touch_down(self,touch):
        #if new_ptr:
                
        if self.ptr_count==0:
            self.p_ix=touch.x
            self.p_iy=touch.y
            self.p_fx=touch.x+100
            self.p_fy=touch.y
            #ptrf[ptr_count]=(touch.x+100,touch.y)
                
            
        self.renderCanvas(touch)            

    def on_touch_move(self,touch):
        self.p_fx=touch.x
        self.p_fy=touch.y        
        self.renderCanvas(touch)

##    def renderText():
##            TextInput(text='hello world')  

    def renderCanvas(self,touch):        
        self.canvas.clear()
        with self.canvas:
            if self.drawPtr:
                Color(0,1,0)
                #touch.ud['line'] = Line(points=(self.p_ix,self.p_iy,self.p_fx,self.p_fy))
                if self.p_fx>self.p_ix:                        
                    if(self.p_ix==self.p_fx):
                        theta1 = math.radians(120)
                        theta2 = -math.radians(30)
                    else:
                        theta1 = math.atan((self.p_fy-self.p_iy)/(self.p_fx-self.p_ix))+math.radians(30)
                        theta2 = -math.atan((self.p_fy-self.p_iy)/(self.p_fx-self.p_ix))+math.radians(30)
                    Line(points=(self.p_ix,self.p_iy,self.p_fx,self.p_fy))
                    Line(points=(self.p_fx - 30*math.cos(theta1),self.p_fy - 30*math.sin(theta1),self.p_fx,self.p_fy))
                    Line(points=(self.p_fx - 30*math.cos(theta2),self.p_fy + 30*math.sin(theta2),self.p_fx,self.p_fy))
                else:
                    if self.p_ix==self.p_fx:
                        theta1 = math.radians(120)
                        theta2 = -math.radians(30)
                    else:
                        theta1 = math.atan((self.p_fy-self.p_iy)/(self.p_fx-self.p_ix))+math.radians(30)
                        theta2 = -math.atan((self.p_fy-self.p_iy)/(self.p_fx-self.p_ix))+math.radians(30)
                    Line(points=(self.p_ix,self.p_iy,self.p_fx,self.p_fy))
                    Line(points=(self.p_fx + 30*math.cos(theta1),self.p_fy + 30*math.sin(theta1),self.p_fx,self.p_fy))
                    Line(points=(self.p_fx + 30*math.cos(theta2),self.p_fy - 30*math.sin(theta2),self.p_fx,self.p_fy))

        if self.drawNode:
            Color(1,.5,0)
            if(self.p_fx>self.p_ix):
                self.add_widget(TextInput(text=str(self.value[0]),pos=(self.p_fx,self.p_fy-25),size=(100,50)))
            elif self.p_fx<self.p_ix:
                self.add_widget(TextInput(text=str(self.value[0]),pos=(self.p_fx-100,self.p_fy-25),size=(100,50)))                    
                          
                    

class DSApp(App):
    def build(self):
        parent = Widget()
        painter = Painter()
        create_pointer = Button(text='Create pointer',pos=(0,0),size=(100,50))
        create_node = Button(text='Create node',pos=(100,0),size=(100,50))        
        txtbox = TextInput(pos=(500,0),size=(100,50))
        add_val = Button(text='Add value',pos=(600,0),size=(100,50))
        reset = Button(text='Reset',pos=(700,0),size=(100,50))
        parent.add_widget(painter)
        parent.add_widget(reset)
        parent.add_widget(create_pointer)
        parent.add_widget(create_node)
        parent.add_widget(txtbox)
        parent.add_widget(add_val)
        
        def clearCanvas(obj):
            painter.canvas.clear()
        reset.bind(on_release=clearCanvas)
        
        def createPointerTrigger(obj):
            painter.drawPtr=True
            painter.ptr_count+=1
            painter.new_ptr = True
        create_pointer.bind(on_release=createPointerTrigger)

        def createNodeTrigger(obj):
            painter.drawNode=True
            
        create_node.bind(on_release=createNodeTrigger)

        def addValueTrigger(self,obj):            
            painter.value[0]=(int(txtbox.text))
        add_val.bind(on_release=partial(addValueTrigger,self))

        return parent

if __name__=='__main__':
    DSApp().run()
