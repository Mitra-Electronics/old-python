import PySimpleGUI as psg
import os.path

#Step 1: Layout of the window
file_list_column = [
    [
        psg.Text("Image Folder"),
        psg.In(size=(30, 1), enable_events=True, key="-FOLDER-"),
        psg.FolderBrowse(),
    ],
    [
        psg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]
#Step 2: Image Viewer Column
image_viewer_column = [
    [psg.Text("Choose an image from list on left:")],
    [psg.Text(size=(40, 1), key="-TOUT-")],
    [psg.Image(key="-IMAGE-")],
]
#Step 3: Total Layout

layout = [
    [
        psg.Column(file_list_column),
        psg.VSeperator(),
        psg.Column(image_viewer_column),
    ]
]

# Step 4: Window setup
window = psg.Window(title="Ishan's image viewer", layout=layout, margins=(100, 50), resizable=True)

while True:
    event, values = window.read()
    if event == "Exit" or event == psg.WIN_CLOSED:
        break
#Step 5: Folder option
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
               and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass
window.close()