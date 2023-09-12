
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class MyApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Blanco
        layout = GridLayout(cols=10, rows=7, size=(610, 1080))
        for i in range(1, 71):
            btn = Button(text=str(i), size_hint=(None, None), size=(87, 108), background_color=[0, 0, 0.5, 1], font_name='Roboto', font_size=14)
            btn.bind(on_press=self.on_button_press)
            layout.add_widget(btn)
        return layout

    def on_button_press(self, instance):
        print('Has presionado el botón: {}'.format(instance.text))
        x = instance.text
        print(x)

if __name__ == '__main__':
    MyApp().run()
