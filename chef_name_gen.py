'''
mino stoto

To use this program, input a number from 1-10 for each of the available input fields. Click the chef adventure button to generate
a custom chef name based off well-known chefs and an arbitrary adventure. The result is reminiscent of a goosebumps title.

It's really simple. User input is a series of 3 integers, and when the program is run it indexes each of the 3 lists for the corresponding integer
(minus one to account for a 0 start) and displays them on the GUI.
'''

import PySimpleGUI as sg

#list of first names
first = [
        'Gordon','Bobby','Anthony','Jamie','Emeril',
'Wolfgang','Paula','Julia','Giada','Guy'
]
#list of last names
last = [
        'Ramsey','Flay','Bourdain','Oliver','Lagasse',
'Puck','Dean','Child','De Laurentiis','Fieri'
    ]
    #list of adventures
and_the = [
        'Sugar Ladle','Brick of Chinese Teas Mixed With Hashish',
'Splenda-Salt-Scenario','Undercooked Lobster with Feelings',
'Drunken-Goose-Kitchen-Flap-About','Ratatouille, or Whatever Gary DellAbate Said',
'Chorizo Your Own Adventure Burger','Fire',
'Walk-In That is Bigger on the Inside Than It Is on the Outside',
'Saturday Night With No Dishwasher'
    ]
    
#about the program, displayed in a popup
ABOUT = '''
This program creates a custom title for a CHEF ADVENTURE!
'''

#menu options
menu_def = [
    ['&File', ['&Quit']],
    ['&Help', ['&About...']],
        ]

#GUI layout
layout = [
    [sg.Menu(menu_def)],
    [sg.Text("To generate your personalized CHEF ADVENTURE!, please input 3 numbers between 1 and 10.")],
    [sg.Input(size=(10,1), key='first'), sg.Input(size=(10,1), key='last')], [sg.Input(size=(10,1), key='and the')],
    [sg.Text('Result:'), sg.Text(key='result')],
    [sg.Button('Chef Adventure!'), sg.Button('Quit')],
    [sg.StatusBar('prepare for culinary chaos', key='status')]
]

#instantiate the window
window = sg.Window('CHEF ADVENTURE!', layout)

#main function, program runs in a while loop
def main():
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit': #all instances of quitting the program
            break
        elif event == 'Chef Adventure!':
            name1 = first[int(values['first'])-1] #first name
            name2 = last[int(values['last'])-1] #last name
            adventure = and_the[int(values['and the'])-1] #adventure!
            result = '{} {} and the {}!'.format(name1, name2, adventure) #final adventure title
            window['result'].update(result) #displays on the GUI
            window['status'].update('sounds like a shitty adventure.') #updates the status bar
        elif event == 'About...': #opens the about dialogue
            window['status'].update('about this program...') #updates the status bar
            sg.popup('This is what it is, aight?', ABOUT)
    window.close()

if __name__ == '__main__':
    main()