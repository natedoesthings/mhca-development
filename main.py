from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ColoredBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.5, 0.7, 0.9, 1)  # Set the background color (R, G, B, A)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

class HomePage(ColoredBoxLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Create a title label
        title_label = Label(text='Welcome', font_size='24sp', size_hint=(None, None), size=(200, 50), halign='left', valign='middle')
        title_label.bind(size=title_label.setter('text_size'))

        # Create a BoxLayout to hold the title in the top-left corner
        top_layout = BoxLayout(orientation='horizontal', size_hint=(1, None), height=title_label.height)
        top_layout.add_widget(title_label)

        # Add an empty widget to push the title to the top left
        top_layout.add_widget(Widget())

        # Use AnchorLayout to place the top_layout in the top left corner
        anchor_layout = AnchorLayout(anchor_x='left', anchor_y='top')
        anchor_layout.add_widget(top_layout)
        self.add_widget(anchor_layout)

       


class MentalHealthApp(App):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    MentalHealthApp().run()
