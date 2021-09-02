# Trying to debug my messages not appearing the TextBox,
# when this evidently works in this example. Huh.
# Scroll-to-end Tk trick from
# https://stackoverflow.com/questions/53900333/guizero-textbox-append-text-not-visible

from guizero import App, TextBox, PushButton

def append():
    textBoxTest.append('Appended text not visible without scrolling')
    textBoxTest.tk.see('end')

app = App(title="Test")
textBoxTest = TextBox(app, width=300, height=5, multiline=True, scrollbar=True, text="1\n2\n3")
appendButton = PushButton(app, command=append, text="Append")

app.display()
