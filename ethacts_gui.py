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

class EthActsApp(App):
    def build(self):
        self.title = "EthActs"
        Window.size = (800, 600)

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
        question_label = Label(text="What is the capital of France?", font_size=18)
        self.quiz_panel.add_widget(question_label)

        self.options = ["Berlin", "Madrid", "Paris", "Rome"]
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

        quiz_tab = TabbedPanelItem(text='Quiz')
        quiz_tab.add_widget(self.quiz_panel)
        self.tab_panel.add_widget(quiz_tab)

        return self.tab_panel

    def update_quotes(self):
        quotes = self.read_all_quotes()
        if quotes:
            self.quote_text.text = "".join(quotes)
        self.quote_text.scroll_y = 1.0  # Ensure the text starts from the top

    def read_all_quotes(self):
        try:
            with open("quotes.txt", "r") as file:
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
            popup = Popup(title='Quiz Result',
                          content=Label(text=f'You selected: {self.selected_option}'),
                          size_hint=(0.5, 0.5))
            popup.open()

if __name__ == '__main__':
    EthActsApp().run()
