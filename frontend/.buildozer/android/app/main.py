
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.list import MDList, OneLineAvatarIconListItem
from kivymd.uix.list import ImageLeftWidget
import requests

from kivymd.theming import ThemeManager

from src import chart_plot

backend_ip='192.168.74.63'
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

class MyApp(MDApp):
    theme_cls = ThemeManager()
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)  # Set window background color to white
        Window.size = (720,1280)  # Set initial window size
        self.theme_cls.theme_style = "Light"
        Builder.load_file('ui/ui.kv')

        sm = ScreenManager(transition=SlideTransition())
        pie_chart_screen = PieChartScreen(name='pie_chart')
        bar_chart_screen = BarChartScreen(name='bar_chart')

        sm.add_widget(pie_chart_screen)
        sm.add_widget(bar_chart_screen)

        # Create the navigation drawer
        nav_drawer = MDNavigationDrawer()
        nav_drawer_list = MDList()

         # Create and add items to the navigation drawer
        nav_drawer_list.add_widget(OneLineAvatarIconListItem(
            ImageLeftWidget(source="assets/icons/sales.png"),
            text="Pie Chart",
            on_release=lambda x: self.switch_screen('pie_chart')
        ))
        nav_drawer_list.add_widget(OneLineAvatarIconListItem(
            ImageLeftWidget(source="assets/icons/map.png"),
            text="Bar Chart",
            on_release=lambda x: self.switch_screen('bar_chart')
        ))

        nav_drawer.side_panel = nav_drawer_list
        nav_drawer.add_widget(nav_drawer_list)

        screen_width, screen_height = Window.size
        layout_width = screen_width * 0.8  # 80% of the screen width
        layout_height = screen_height * 0.8  # 80% of the screen height

        self.sm = sm

        # Create the layout for the main screen
        root = FloatLayout(size=(layout_width, layout_height))

        # Set the content of the layout
        root.add_widget(sm)
        root.add_widget(nav_drawer)
        return root
    
    def switch_screen(self, screen_name):
        screen_manager = self.sm
        screen_manager.current = screen_name

if __name__ == '__main__':
    MyApp().run()
