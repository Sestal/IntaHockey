from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDBoxLayout:

    MDNavigationRail:

        MDNavigationRailItem:
            text: "Смотреть"
            icon: "hockey-sticks"

        MDNavigationRailItem:
            text: "Добавить"
            icon: "hockey-puck"

        MDNavigationRailItem:
            text: "Изменить"
            icon: "human-edit"

        MDNavigationRailItem:
            text: "Выход"
            icon: "exit-run"

    MDScreen:
'''


class IntaHockey(MDApp):
    def build(self):
        return Builder.load_string(KV)


IntaHockey().run()