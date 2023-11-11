from modules import functions
import PySimpleGUI as sg

label = sg.Text("Enter a To-Do Item:")
input_box = sg.InputText(tooltip="Enter To-Do")
add_button = sg.Button("Add")

window = sg.Window("To-Do List App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
