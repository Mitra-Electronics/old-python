import PySimpleGUI as psg

layout = [[psg.Text("Hello Ishan")], [psg.Button("Close")]]
window = psg.Window(title="Ishan's program", layout=layout, margins=(100, 50), resizable=True).read()


while True:
    event, values = window.read()
    if event == "Close" or event == psg.WIN_CLOSED:
        break
window.close()