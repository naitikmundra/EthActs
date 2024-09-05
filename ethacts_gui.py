from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.tabbedpanel import TabbedPanelItem
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.popup import Popup
from kivy.core.window import Window
import sys
from kivy.uix.image import Image

class EthActsApp(App):
    def __init__(self, initial_tab=1, **kwargs):
        super().__init__(**kwargs)
        self.initial_tab = initial_tab

    def build(self, initial_tab=1, **kwargs):
        self.title = "EthActs"
        Window.size = (800, 600)
        Window.bind(on_request_close=self.on_request_close)  # Bind the close event

        # Main Tabbed Panel
        self.tab_panel = TabbedPanel()

        # Quotes Tab
        self.quotes_panel = BoxLayout(orientation='vertical')
        self.quote_text = TextInput(readonly=True, font_size=14)
        self.quote_text.background_color = (0.18, 0.18, 0.18, 1)  # Background color
        self.quote_text.foreground_color = (0.94, 0.94, 0.94, 1)  # Text color

        self.quotes_panel.add_widget(self.quote_text)

        quotes_tab = TabbedPanelItem(text='Quotes')
        quotes_tab.add_widget(self.quotes_panel)
        self.tab_panel.add_widget(quotes_tab)

        self.update_quotes()

        # Quiz Tab
        self.quiz_panel = BoxLayout(orientation='vertical')
        question_label = Label(text="Did you get angry today?", font_size=18)
        self.quiz_panel.add_widget(question_label)

        self.options = ["Yes", "No"]
        self.option_checkboxes = []
        self.selected_option = None

        for option in self.options:
            box_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30)
            checkbox = CheckBox(group='quiz')
            checkbox.bind(active=self.on_option_selected)
            label = Label(text=option)

            box_layout.add_widget(checkbox)
            box_layout.add_widget(label)

            self.quiz_panel.add_widget(box_layout)
            self.option_checkboxes.append((checkbox, option))

        submit_button = Button(text="Submit")
        submit_button.bind(on_release=self.on_submit)
        self.quiz_panel.add_widget(submit_button)

        quiz_tab = TabbedPanelItem(text='Day Report')
        quiz_tab.add_widget(self.quiz_panel)
        self.tab_panel.add_widget(quiz_tab)
        self.tab_panel.default_tab_text = 'Being Ethical'
        todo = TabbedPanelItem(text='To Do')
        self.tab_panel.add_widget(todo)

        # Create an Image widget
        image = Image(source='assets/Ethical.png')

        # Set the image as the content of the default tab
        self.tab_panel.default_tab_content = image

        # Set the default tab based on the initial_tab argument
        if self.initial_tab == 2:
            self.tab_panel.switch_to(quiz_tab)
        else:
            self.tab_panel.switch_to(quotes_tab)
            
        return self.tab_panel

    def update_quotes(self):
        quotes = self.read_all_quotes()
        if quotes:
            self.quote_text.text = "".join(quotes)
        self.quote_text.scroll_y = 1.0  # Ensure the text starts from the top

    def read_all_quotes(self):
        try:
            with open("assets/quotes.txt", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return ["No quotes available."]

    def on_option_selected(self, checkbox, value):
        if value:
            for cb, option in self.option_checkboxes:
                if cb == checkbox:
                    self.selected_option = option
                    break

    def on_submit(self, instance):
        if self.selected_option:
            popup = Popup(title='Day report!',
                          content=Label(text=f'You selected: {self.selected_option}'),
                          size_hint=(0.5, 0.5))
            popup.open()

    def on_request_close(self, *args):
        # This method will be called when the close button is clicked
        self.stop()  # Stop the application cleanly
        return True  # Return True to indicate that the window can be closed

    

if __name__ == '__main__':
    # Parse command-line arguments
    initial_tab = 1
    if len(sys.argv) > 1:
        try:
            initial_tab = int(sys.argv[1])
        except ValueError:
            pass  # Use default if argument is not an integer

    EthActsApp(initial_tab=initial_tab).run()
