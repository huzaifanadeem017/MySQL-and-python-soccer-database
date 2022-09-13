from tkinter import *
# library for GUI
import tkinter.ttk
# library to
import mysql.connector

# creating connection with local database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Ghostrider2001",
    port=3306,
    database="football_database"
)


def listTeam():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("700x400")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM team"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    my_w.mainloop()


def listPlayers():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("1200x700")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM players"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    my_w.mainloop()


def listLeague():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("1050x300")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM league"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    my_w.mainloop()


def listMembers():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("1050x700")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM member"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    my_w.mainloop()


def listPerformances():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("1200x350")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM performance"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    print("Done")
    my_w.mainloop()


def listUM():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("1150x700")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM upcoming_matches"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    my_w.mainloop()


def listSponsors():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("900x400")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM sponsors"
    cursor.execute(query)
    # displaying column names and all rows
    column_names = [i[0] for i in cursor.description]
    for i in range(len(column_names)):
        e = Entry(my_w, width=25, fg='blue')
        e.grid(row=0, column=i)
        e.insert(END, column_names[i])
    i = 1
    for ele in cursor:
        for j in range(len(ele)):
            e = Entry(my_w, width=25, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, ele[j])
        i = i + 1
    cursor.close()
    my_w.mainloop()


def tab4GUI(tab4):
    """
    Main function that executes where it inserts all GUI elements into tab
    """

    """*********************
        List Tab Title
        *********************"""
    tkinter.Label(tab4, text="SQl CS 480 Project").grid(column=0,
                                                        row=0,
                                                        padx=30,
                                                        pady=15)

    tkinter.Button(tab4, text="Team", width=25, height=6, command=lambda: listTeam()).grid(column=0,
                                                                                           row=2,
                                                                                           padx=30,
                                                                                           pady=15)

    tkinter.Button(tab4, text="Player", width=25, height=6, command=lambda: listPlayers()).grid(column=0,
                                                                                                row=3,
                                                                                                padx=30,
                                                                                                pady=15)

    tkinter.Button(tab4, text="League", width=25, height=6, command=lambda: listLeague()).grid(column=0,
                                                                                               row=4,
                                                                                               padx=30,
                                                                                               pady=15)

    tkinter.Button(tab4, text="Sponsors", width=25, height=6, command=lambda: listSponsors()).grid(column=3,
                                                                                                   row=4,
                                                                                                   padx=30,
                                                                                                   pady=15)

    tkinter.Button(tab4, text="Performance", width=25, height=6, command=lambda: listPerformances()).grid(column=3,
                                                                                                          row=2,
                                                                                                          padx=30,
                                                                                                          pady=(50, 15))

    tkinter.Button(tab4, text="Upcoming Matches", width=25, height=6, command=lambda: listUM()).grid(column=3,
                                                                                                     row=3,
                                                                                                     padx=30,
                                                                                                     pady=15)
