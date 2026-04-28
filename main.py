from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window


Window.size = (300, 500)

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super(Calculator, self).__init__(orientation='vertical', **kwargs)
        
        self.result = TextInput(font_size=45,size_hint_y=0.2 , readonly=True, halign='right', multiline=False,background_color=[0.2,0.2,0.2,1],foreground_color=[1,1,1,1])
        self.add_widget(self.result)
        
        #Create buttons
        buttons = [['C','+/-','%','/'],
                   ['7','8','9','*'],
                   ['4','5','6','-'],
                   ['1','2','3','+'],
                   ['0','00','.','=']]
        grid = GridLayout(cols=4, spacing=5, padding=10)
        for row in buttons:
            for item in row:
                button = Button(text=item, font_size=32, background_color=self.button_color(item), on_press=self.button_click)
                
                grid.add_widget(button)
        self.add_widget(grid)
    
    def button_color(self, label):
        if label in ['C', '+/-', '%']:
            return [0.6,0.6,0.6,1]  # Orange for special functions
        elif label in ['/', '*', '-', '+', '=']:
            return [1,0.65,0.6,1]  # Blue for operators
        else:
            return [0.3,0.3,0.3,1]  # Dark gray for numbers
        
    def button_click(self, instance):
        text = instance.text
        if text == 'C':
            self.result.text = ''
        elif text == '=':
            self.calculate()
        elif text == '+/-':
            self.toggle_neg()           
        elif text == '%':
            self.convert_percent()
        else:
            self.result.text += text
        
        #Calculate 
    def calculate(self):
            try:
                self.result.text = str(eval(self.result.text))
            except Exception:
                self.result.text = 'ERROR!'
        
    def toggle_neg(self):
            if self.result.text:
                if self.result.text.startswith('-'):
                    self.result.text = self.result.text[1:]
                else:
                    self.result.text = '-' + self.result.text
        
    def convert_percent(self):
            try:
                self.result.text = str(float(self.result.text) / 100)
            except ValueError:
                self.result.text = 'ERROR!'
   

class CalculatorApp(App):
    def build(self):
        return Calculator()
    

if __name__ == '__main__':
    CalculatorApp(title="AV_Calculator").run() 
