import  PySimpleGUI as sg
import pyttsx3
sg.theme('DarkTeal5')

engine = pyttsx3.init()


layout = [
[sg.Text('Enter text:'),sg.InputText(),sg.Button('SPEAK')],
[sg.Text('Select Voice Type:'),sg.Radio("Male", "voice", default=True, key="-FEMALE-"),sg.Radio("Female", "voice", default=False, key="-MALE-")],


    
    

]

# create the window
window = sg.Window(('Text to Speech V1.0'),layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "SPEAK":
        text = values[0]
        voice = "male" if values["-MALE-"] else "female"
        if voice == "male":
            engine.setProperty('voice', engine.getProperty('voices')[0].id)
        else:
            engine.setProperty('voice', engine.getProperty('voices')[1].id)
        engine.say(text)
        engine.runAndWait()

window.close()