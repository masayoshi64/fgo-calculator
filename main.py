import sqlite3

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty


class Calculator(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.con = sqlite3.connect('data12.db')
        self.text = ''
        self.text2 = ''

    def calculate(self):
        atk = int(self.ids.atk.text)
        treasure_mag = float(self.ids.treasure_magnification.text)
        special_atk = float(self.ids.special_attack.text)
        class_corr = float(self.ids.class_correction.text)

        class_comp = float(self.ids.class_compatibility.text)
        servant_comp = float(self.ids.servant_compatibility.text)
        atk_buff = float(self.ids.attack_buff.text)
        card_buff = float(self.ids.card_buff.text)
        treasure_buff = float(self.ids.treasure_buff.text)
        special_def = float(self.ids.special_defense.text)

        damage = atk * treasure_mag * special_atk * \
            class_corr * class_comp * servant_comp * 0.23
        damage *= (1 + atk_buff) * (1 + card_buff) * \
            (1 + treasure_buff) * (1 - special_def)
        self.text = str(int(damage))


class CalculatorApp(App):
    def __init__(self, **kwargs):
        super(CalculatorApp, self).__init__(**kwargs)
        self.title = 'damage calculator'

    def build(self):
        return Calculator()


if __name__ == '__main__':
    CalculatorApp().run()
