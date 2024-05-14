from kivy.config import Config

Config.set('graphics', 'width', '420')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window


class CalculatorApp(App):
    def build(self):
        # Layout principal da calculadora
        layout = BoxLayout(orientation='vertical')

        # Campo de texto para exibir o resultado
        self.result_display = Label(font_size=40, size_hint=(1, 0.2), color=(1, 1, 1, 1))  # Definindo a cor do texto como branco
        layout.add_widget(self.result_display)

        # Adicionando a calculadora
        calculator_layout = GridLayout(cols=4)
        for i in range(1, 10):
            button = Button(text=str(i))
            button.bind(on_press=self.add_to_equation)
            calculator_layout.add_widget(button)

        # Botão de zero
        zero_button = Button(text='0')
        zero_button.bind(on_press=self.add_to_equation)
        calculator_layout.add_widget(zero_button)

        # Botões de operações
        operations = ['+', '-', '*', '/']
        for op in operations:
            button = Button(text=op)
            button.bind(on_press=self.add_to_equation)
            calculator_layout.add_widget(button)
        
        # Botão de limpar
        clear_button = Button(text='C')
        clear_button.bind(on_press=self.clear_equation)
        calculator_layout.add_widget(clear_button)
        
        # Botão de igual
        equals_button = Button(text='=')
        equals_button.bind(on_press=self.calculate_result)
        calculator_layout.add_widget(equals_button)

        layout.add_widget(calculator_layout)

        self.equation = ""
        self.result = "0"

        # Adicionar manipuladores de eventos de teclado
        Window.bind(on_key_down=self.on_key_down)

        return layout

    def on_key_down(self, window, key, *args):
        if key.isdigit():
            self.equation += key
            self.update_result_display()
        elif key in ['+', '-', '*', '/']:
            self.equation += key
            self.update_result_display()
        elif key == 'enter':
            self.calculate_result(None)
        elif key == 'backspace':
            self.clear_equation(None)

    def add_to_equation(self, instance):
        self.equation += instance.text
        self.update_result_display()

    def calculate_result(self, instance):
        try:
            self.result = str(eval(self.equation))
        except Exception as e:
            self.result = "Error"
        self.update_result_display()
        self.equation = self.result

    def clear_equation(self, instance):
        self.equation = ""
        self.result = "0"
        self.update_result_display()

    def update_result_display(self):
        self.result_display.text = self.equation if self.equation else self.result


if __name__ == '__main__':
    CalculatorApp().run()