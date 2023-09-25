'''
mino stoto
3.4.23

An important facet of this project was creating a user-friendly databse environment, which I had already done in the
previous db assignment. Because I had already structured a pseuo-gui within console, it didn't take
very much abstraction to rebuild it within pysimplegui. I basically made the menu from the previous project into the
main window of the gui itself, and called each function very similarly.
I tested the code as I went, giving a few final sweeps toward the end. I am certain I missed a couple bugs, but the program 
manages to do value checks and avoids crashing with common bad user input.

There are 3 options: searching for entries, deleting entries, and adding/updating entries. Each has their own input boxes and
buttons, so there is very little to be confused by. It's a regular ol' database with no naming restrictions, so you could absolutely
create a vegetable called 'Boston'. Simply enter the name (and value, if applicable), then click the corresponding button. The result
will print toward the bottom of the window.
'''


import sqlite3
import PySimpleGUI as sg

#defines the gui parameters
layout = [
    [sg.Text('A Big List of Wonderful Veggies')],
    [sg.Input(size=(10,1), key='Veggie_1')],[sg.Button('Search')],
    [sg.Input(size=(10,1), key='Veggie_2')],[sg.Button('Remove All Entries')],
    [sg.Input(size=(10,1), key='Veggie_3'), sg.Input(size=(10,1), key='Number')], [sg.Button('Update or Add Veggies')],
    [sg.Text('                                                               ')], #do you like my haphazard window sizing?
    [sg.Text(key='result')],
    [sg.Text('                                                               ')], #here it is again
    [sg.StatusBar('veggies!', key='status')],
]

#variable to hold the program window
window = sg.Window('Veggies, Nothing Else.', layout)

#creates the sql table and inserts dummy data
def create_tables(conn, c):
    c.execute("CREATE TABLE IF NOT EXISTS vegetable (name, quantity)")

    c.execute("INSERT INTO vegetable VALUES ('carrot', 42), ('broccoli', 1), ('zucchini', 0)")
    conn.commit()
#core function that searches the db
def get_veg(conn, c, veg):
    c.execute("SELECT name, quantity FROM vegetable WHERE name=?", [veg])
    row = c.fetchone()
    return row
#utilizes get_veg to find and remove instances of input vegetables
def remove_veg(conn, c, veg):
    found = get_veg(conn, c, veg)

    if found:
        c.execute("DELETE FROM vegetable WHERE name=?", [veg])
        conn.commit() 
        return("We ditched the {} stock".format(veg))
    else:
        return("Nothing there to delete")
#utilizes get_veg to search for instances of input data, replace it, or creates a new entry if it isn't found
def add_update_veg(conn, c, veg, quant):

    quantity = quant or '0'
    found = get_veg(conn, c, veg)

    if found:
        c.execute("UPDATE vegetable SET quantity=? WHERE name=?", [quantity, veg])
    else:
        c.execute("INSERT INTO vegetable VALUES (?, ?)", [veg, quantity])

    conn.commit()
    return([veg,quantity])

#main function
def main():
    #calls sqlite, creates a cursor, and calls the table
    with sqlite3.connect(':memory:') as conn:
        c = conn.cursor()
        create_tables(conn, c)

    #the loop that runs the program
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Quit': #for quitting purposes
            break
        elif event == 'Search': #search function
            veg_1 = get_veg(conn, c, values['Veggie_1'].lower()) #runs get_veg for the search function
            if veg_1: #if veg_1 is true
                window['result'].update('look! {} {}(s)!'.format(veg_1[1], veg_1[0])) #let's talk about it
                window['status'].update('~found these~')
            else: #otherwise
                window['result'].update('We cannot find any of that :c') #we can move on
        elif event == 'Remove All Entries': #delete function
            veg_2 = remove_veg(conn, c, values['Veggie_2'].lower()) #runs get_veg 
            window['result'].update(veg_2) #the only instance of the function returning the formatted string
            window['status'].update('~none left~') #because it's late and I don't feel like fixing it (it works, ok?)
        elif event == 'Update or Add Veggies': #update function
            try: #try/except block
                quant = int(values['Number'].strip()) or '0'
            except ValueError:
                quant = None #in case the user doesn't enter an int
            if isinstance(quant, int): #checks that quant is an int
                veg_3 = add_update_veg(conn, c, values['Veggie_3'].lower(), quant) #and then outputs
                window['result'].update('you now have {} {}(s)!'.format(veg_3[1], veg_3[0])) #the values
                window['status'].update('lucky you!') #dot dot dot
            else: #unless
                window['result'].update('use a whole number!') #the user doesn't input
                window['status'].update('nothing else!') #an integer


    window.close()


if __name__ == '__main__':
    main()