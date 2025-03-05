# Convertor gui using PySimpleGUI
# import FreeSimpleGUI as fsg

# fsg.theme("DarkAmber")
# layout = [
#     [fsg.Text('Convert')],
#     [fsg.Text("Feet"), fsg.Input(key='feet')],
#     [fsg.Text("Inches"), fsg.Input(key='inches')],
#     [fsg.Button('Convert'), fsg.Button('Exit')]
# ]

# window = fsg.Window('Converter', layout)

# while True:
#     event, values = window.read()
#     if event in (fsg.WINDOW_CLOSED, 'Exit'):
#         break
#     try:
#         feet = int(values['feet'])
#         inches = int(values['inches'])
#     except ValueError:
#         fsg.popup("Please enter valid numbers for feet and inches.")
#         continue

#     total_inches = inches + feet * 12
#     feet = total_inches // 12
#     inches = total_inches % 12    
#     fsg.popup(f"{feet} feet {inches} inches")

# window.close()
# Bug fixing excercise
# import FreeSimpleGUI as sg
 
# label = sg.Text("What are dolphins?")
# option1 = sg.Radio("Amphibians", group_id="question1")
# option2 = sg.Radio("Fish", group_id="question1")
# option3 = sg.Radio("Mammals", group_id="question1")
# option4 = sg.Radio("Birds", group_id="question1")
 
# window = sg.Window("File Compressor",
#                    layout=[[label],
#                            [option1], 
#                             [option2], 
#                             [option3], 
#                             [option4],
#                            ])
 
# window.read()
# window.close()