from guizero import App, Window, Text, PushButton

def open_BBC():
    bbcWindow.show(wait=True)

def open_CSS():
    cssWindow.show(wait=True)

def close_BBC():
    bbcWindow.hide()

def close_CSS():
    cssWindow.hide()



app = App(title="Library Selection", bg="black")
bbcWindow = Window(app,title="BBCSO Library",bg="black")
bbcWindow.hide()
cssWindow = Window(app,title="CSS Library",bg="black")
cssWindow.hide()

bbcButtonOpen = PushButton(app, text="BBCSO", command=open_BBC)
bbcButtonOpen.bg = "red"
cssButtonOpen = PushButton(app, text="CSS", command=open_CSS)
cssButtonOpen.bg = "yellow"

bbcButtonClose = PushButton(bbcWindow, text="Close", command=close_BBC)
bbcButtonClose.bg = "red"
cssButtonClose = PushButton(cssWindow, text="Close", command=close_CSS)
cssButtonClose.bg = "yellow"

app.display()