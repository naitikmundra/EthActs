import wx
import wx.lib.agw.aui as aui

class EthActsApp(wx.App):
    def OnInit(self):
        frame = EthActsFrame(None, title="EthActs", size=(800, 600))
        frame.Show()
        return True

class EthActsFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(EthActsFrame, self).__init__(*args, **kw)

        # Apply a dark theme
        self.SetBackgroundColour(wx.Colour(45, 45, 48))
        self.SetForegroundColour(wx.Colour(240, 240, 240))

        self.notebook = aui.AuiNotebook(self, style=aui.AUI_NB_TOP | aui.AUI_NB_CLOSE_ON_ALL_TABS)
        self.notebook.SetArtProvider(aui.AuiSimpleTabArt())

        self.quotes_panel = QuotesPanel(self.notebook)
        self.quiz_panel = QuizPanel(self.notebook)

        self.notebook.AddPage(self.quotes_panel, "Quotes")
        self.notebook.AddPage(self.quiz_panel, "Quiz")

        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.update_quotes()

    def update_quotes(self):
        quotes = self.read_all_quotes()
        if quotes:
            self.quotes_panel.update_quotes(quotes)

    def read_all_quotes(self):
        try:
            with open("quotes.txt", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return ["No quotes available."]

    def on_close(self, event):
        self.Destroy()

class QuotesPanel(wx.Panel):
    def __init__(self, parent):
        super(QuotesPanel, self).__init__(parent)

        self.SetBackgroundColour(wx.Colour(30, 30, 30))
        self.SetForegroundColour(wx.Colour(240, 240, 240))

        self.quote_text = wx.TextCtrl(self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.BORDER_NONE)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.quote_text, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(sizer)

    def update_quotes(self, quotes):
        self.quote_text.SetValue("".join(quotes))

class QuizPanel(wx.Panel):
    def __init__(self, parent):
        super(QuizPanel, self).__init__(parent)

        self.SetBackgroundColour(wx.Colour(30, 30, 30))
        self.SetForegroundColour(wx.Colour(240, 240, 240))

        sizer = wx.BoxSizer(wx.VERTICAL)

        # Add a question
        question = wx.StaticText(self, label="What is the capital of France?")
        question.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        sizer.Add(question, 0, wx.ALL, 10)

        # Add multiple choice options
        self.options = ["Berlin", "Madrid", "Paris", "Rome"]
        self.radio_box = wx.RadioBox(self, choices=self.options, style=wx.RA_SPECIFY_COLS)
        sizer.Add(self.radio_box, 0, wx.ALL, 10)

        # Add a submit button
        submit_button = wx.Button(self, label="Submit")
        submit_button.Bind(wx.EVT_BUTTON, self.on_submit)
        sizer.Add(submit_button, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        self.SetSizer(sizer)

    def on_submit(self, event):
        selected_option = self.radio_box.GetStringSelection()
        print(f"Selected option: {selected_option}")
        wx.MessageBox(f"You selected: {selected_option}", "Quiz Result", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = EthActsApp()
    app.MainLoop()
