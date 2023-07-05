
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDIconButton
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import MDList, OneLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget

from kivy.animation import Animation
from kivy.uix.image import Image
from kivymd.uix.screen import MDScreen
from kivymd.uix.chip import MDChip
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

import requests


from kivymd.theming import ThemeManager

from kivymd.uix.menu import MDDropdownMenu
from kivy.core.text import LabelBase

from src import chart_plot

from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.utils import get_color_from_hex

from PyQt5 import QtCore, QtGui, QtWidgets

backend_ip='192.168.1.7'

class IntroScreen(Screen):

    def on_enter(self):
        # Create the logo image widget
        logo = Image(source='assets/images/logo.jpeg')

        # Set the initial opacity of the logo
        logo.opacity = 0.0

        # Calculate the position of the logo in the middle of the screen
        logo_size = (200, 200)  # Adjust the size as needed
        screen_width, screen_height = Window.size
        logo_pos = (0,0)

        # Set the initial position of the logo
        logo.pos = logo_pos

        # Create animation to fade in the logo
        animation = Animation(opacity=1.0, duration=2, t='out_quad')

        # Start the animation
        animation.start(logo)

        # Add the logo to the intro screen
        self.add_widget(logo)


class PieChartScreen(Screen):
    def on_enter(self):
        chart_obj = chart_plot.Charts()
        # Make an HTTP GET request to the endpoint
        res = requests.get('http://'+backend_ip+':5000/api/sales')

        if res.status_code == 200:
            # If the request was successful, extract the data from the response
            data = res.json()

        piechart = chart_obj.create_piechart(data)
        self.ids.chart_container.clear_widgets()
        self.ids.chart_container.add_widget(piechart)

        res = requests.get('http://'+backend_ip+':5000/api/monthlist')

        if res.status_code == 200:
            # If the request was successful, extract the data from the response
            data = res.json()
        
        dropdown_items = []

        for i in data:
            dropdown_items.append( {"text": str(i), "viewclass": "OneLineListItem", "on_release": lambda y=str(i): self.dropdown_item_callback(y),})

        dropdown_menu = MDDropdownMenu(
            caller=self.ids.dropdown_button,
            items=dropdown_items,
            width_mult=4,
        )
        
        dropdown_menu.open()

    def dropdown_item_callback(self, text):
        print("Selected item:", text)
        chart_obj = chart_plot.Charts()
        # Make an HTTP GET request to the endpoint
        res = requests.get('http://' + backend_ip + ':5000/api/month/' + text)
        
        if res.status_code == 200:
            # If the request was successful, extract the data from the response
            data = res.json()

        barschart = chart_obj.create_barschart(data)
        self.ids.chart_container.clear_widgets()
        self.ids.chart_container.add_widget(barschart)

class BarChartScreen(Screen):
    def on_enter(self):
        chart_obj = chart_plot.Charts()
        # Make an HTTP GET request to the endpoint
        res = requests.get('http://'+backend_ip+':5000/api/sales')

        if res.status_code == 200:
            # If the request was successful, extract the data from the response
            data = res.json()

        barschart = chart_obj.create_barschart(data)
        self.ids.chart_container.clear_widgets()
        self.ids.chart_container.add_widget(barschart)

        # Make an HTTP GET request to the endpoint
        res = requests.get('http://'+backend_ip+':5000/api/citylist')

        if res.status_code == 200:
            # If the request was successful, extract the data from the response
            data = res.json()
        
        chip_container = BoxLayout(orientation='vertical', size_hint=(1, None), spacing=dp(10), padding=dp(10))
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height - dp(100)))
        grid_layout = GridLayout(cols=4, spacing=dp(10), size_hint_y=None)
        
        for city in data:
            chip = MDChip(text=city, on_release=lambda chip: self.chip_callback(chip.text))
            chip.md_bg_color: "1, 0, 0, .5"
            grid_layout.add_widget(chip)

        grid_layout.bind(minimum_height=grid_layout.setter('height'))
        scroll_view.add_widget(grid_layout)
        chip_container.add_widget(scroll_view)

        self.ids.chip_container.clear_widgets()
        self.ids.chip_container.add_widget(chip_container)

    def chip_callback(self, text):
        print("Clicked chip:", text)
        chart_obj = chart_plot.Charts()
        # Make an HTTP GET request to the endpoint
        print('http://' + backend_ip + ':5000/api/city/' + text)
        res = requests.get('http://' + backend_ip + ':5000/api/city/' + text)
        
        if res.status_code == 200:
            # If the request was successful, extract the data from the response
            data = res.json()

        barschart = chart_obj.create_piechart(data)
        self.ids.chart_container.clear_widgets()
        self.ids.chart_container.add_widget(barschart)

class MyApp(MDApp):
    theme_cls = ThemeManager()
    theme_cls.font_styles['subtitle'] =  ['PatrickHand-Regular', 16]
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set window background color to white
        Window.size = (720,1280)  # Set initial window size
        self.theme_cls.theme_style = "Light"

        # Register the custom font
        LabelBase.register(name="PatrickHand-Regular", fn_regular="assets/fonts/PatrickHand-Regular.ttf")

        Builder.load_file('ui/ui.kv')

        sm = ScreenManager(transition=SlideTransition())
        intro_screen = IntroScreen(name='intro')
        pie_chart_screen = PieChartScreen(name='pie_chart')
        bar_chart_screen = BarChartScreen(name='bar_chart')

        sm.add_widget(intro_screen)
        sm.add_widget(pie_chart_screen)
        sm.add_widget(bar_chart_screen)

        # Create the navigation drawer
        nav_drawer = MDNavigationDrawer()
        nav_drawer_list = MDList()

         # Create and add items to the navigation drawer
        nav_drawer_list.add_widget(OneLineAvatarIconListItem(
            ImageLeftWidget(source="assets/icons/sales.png"),
            text="Pie Chart",
            on_release=lambda x: self.switch_screen('pie_chart',nav_drawer)
        ))
        nav_drawer_list.add_widget(OneLineAvatarIconListItem(
            ImageLeftWidget(source="assets/icons/map.png"),
            text="Bar Chart",
            on_release=lambda x: self.switch_screen('bar_chart',nav_drawer)
        ))

        # Move the item list to the top of the drawer
        nav_drawer_list.pos_hint = {'top': 1}
        nav_drawer.side_panel = nav_drawer_list
        nav_drawer.add_widget(nav_drawer_list)

        screen_width, screen_height = Window.size
        layout_width = screen_width * 0.8  # 80% of the screen width
        layout_height = screen_height * 0.8  # 80% of the screen height}

        self.sm = sm

        # Create the layout for the main screen
        root = FloatLayout(size=(layout_width, layout_height))

        # Set the content of the layout
        root.add_widget(sm)
        root.add_widget(nav_drawer)

        return root
    
    def switch_screen(self, screen_name, drawer):
        screen_manager = self.sm
        screen_manager.current = screen_name
        drawer.set_state("close")


if __name__ == '__main__':
    MyApp().run()

