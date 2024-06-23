from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout


class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super(HomePage, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Create a title label
        title_label = Label(text='Mental Health Tips', font_size='24sp', size_hint=(1, 0.1))
        self.add_widget(title_label)

        # Create a layout for videos and articles
        content_layout = GridLayout(cols=1, size_hint_y=None)
        content_layout.bind(minimum_height=content_layout.setter('height'))

        # Add video section
        video_section = BoxLayout(orientation='vertical', size_hint_y=None)
        video_section.bind(minimum_height=video_section.setter('height'))

        video_title = Label(text='Latest Videos', font_size='20sp', size_hint_y=None, height=40)
        video_section.add_widget(video_title)

        # Example video thumbnails (replace with actual video widgets in a real app)
        for i in range(3):
            video_button = Button(text=f'Video {i+1}', size_hint_y=None, height=100)
            video_section.add_widget(video_button)

        content_layout.add_widget(video_section)

        # Add articles section
        articles_section = BoxLayout(orientation='vertical', size_hint_y=None)
        articles_section.bind(minimum_height=articles_section.setter('height'))

        articles_title = Label(text='Latest Articles', font_size='20sp', size_hint_y=None, height=40)
        articles_section.add_widget(articles_title)

        # Example article links (replace with actual article widgets in a real app)
        for i in range(5):
            article_button = Button(text=f'Article {i+1}', size_hint_y=None, height=40)
            articles_section.add_widget(article_button)

        content_layout.add_widget(articles_section)

        # Add the ScrollView
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(content_layout)
        self.add_widget(scroll_view)


class MentalHealthApp(App):
    def build(self):
        return HomePage()


if __name__ == '__main__':
    MentalHealthApp().run()
