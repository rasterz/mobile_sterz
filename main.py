import matplotlib.pyplot as plt
from kivy.app import App
import numpy as np
import matplotlib.animation as animation
from kivy.garden.matplotlib import NavigationToolbar2Kivy
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

L = 2.22
L11 = 0.36
L22 = 1.75

list_of_all = []  # список введеных токов
list_of_fluxxx = []  # готовый магнитный поток по L 1
list_of_fluxxx1 = []  # готовый магнитный поток по L 2
list_of_fluxxx2 = []  # готовый магнитный поток по L 3


plt.xlabel("Сила тока")
plt.ylabel("Магнитный поток")
plt.grid(True)
plt.legend(loc="upper left")


class Container(GridLayout):

    text_input = ObjectProperty()
    label_widget = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def gnrt_graph(self):

        plt.plot(list_of_all, list_of_fluxxx, marker="o", linestyle="-")
        plt.scatter(list_of_all, list_of_fluxxx, marker="o", linestyle="-", label=f"L = {L}")

        plt.scatter(list_of_all, list_of_fluxxx1, marker="o", linestyle="-")
        plt.plot(list_of_all, list_of_fluxxx1, marker="o", linestyle="-", label=f"L = {L11}")

        plt.scatter(list_of_all, list_of_fluxxx2, marker="o", linestyle="-")
        plt.plot(list_of_all, list_of_fluxxx2, marker="o", linestyle="-", label=f"L = {L22}")
        plt.xlabel("Сила тока")
        plt.ylabel("Магнитный поток")

        plt.legend(loc="upper left")
        plt.grid()
        canvas = FigureCanvasKivyAgg(plt.gcf())
        self.box = self.ids.box
        self.nav = NavigationToolbar2Kivy(canvas)
        self.box.add_widget(self.nav.actionbar)
        self.box.add_widget(canvas)

    def change_text(self):
        count = 0
        while count < 1:
            if len(list_of_all) >= 3:
                break
            self.label_widget.text = self.krokodil.text
            count += 1
            list_of_all.append(self.krokodil.text)

        self.krokodil.text = ''

        return print(list_of_all)



    def calculate_flux(self):

        for i in list_of_all:
            flux = round((float(i) * L), 2)
            flux11 = round((float(i) * L11), 2)
            flux22 = round((float(i) * L22), 2)
            list_of_fluxxx.append(flux)
            list_of_fluxxx1.append(flux11)
            list_of_fluxxx2.append(flux22)

        return print(list_of_fluxxx, list_of_fluxxx1, list_of_fluxxx2)


class MyApp(App):
    def build(self):

        return Container()

print(list_of_all)


if __name__ == "__main__":
    MyApp().run()