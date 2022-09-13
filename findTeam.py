import tkinter.ttk

import mysql.connector
from tkinter import *

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Ghostrider2001",
    port=3306,
    database="football_database"
)


def findPlayerByName(pName):
    # creating popout window for displaying table
    playerName = pName.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT * FROM players WHERE first_name = %s;"
    cursor.execute(query, [playerName])
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


def findPlayerBySSN(PSSN):
    playerSSN = PSSN.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    cursor = mydb.cursor()
    query = "SELECT * FROM players WHERE SSN = %s;"
    cursor.execute(query, [playerSSN])
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


def findLeagueByName(LName):
    leagueName = LName.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    cursor = mydb.cursor()
    query = "SELECT * FROM league WHERE name = %s;"
    cursor.execute(query, [leagueName])
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


def findLeagueByCountry(tCountry):
    leagueCountry = tCountry.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    cursor = mydb.cursor()
    query = "SELECT * FROM league WHERE country = %s;"
    cursor.execute(query, [leagueCountry])
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


def findTeamByName(tName):
    teamName = tName.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    cursor = mydb.cursor()
    query = "SELECT * FROM team WHERE name = %s;"
    cursor.execute(query, [teamName])
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


def findSponsorByName(sName):
    sponsorName = sName.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    cursor = mydb.cursor()
    query = "SELECT * FROM sponsors WHERE name = %s;"
    cursor.execute(query, [sponsorName])
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


def findSponsorByID(sID):
    sponsorID = sID.get("1.0", "end-1c")
    my_w = Tk()
    my_w.geometry("1200x700")
    cursor = mydb.cursor()
    query = "SELECT * FROM leagues WHERE name = %s;"
    cursor.execute(query, [sponsorID])
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


def tab5GUI(tab5):
    """
    Main function that executes where it inserts all GUI elements into tab
    """

    """*********************
        Find Tab Title
        *********************"""
    tkinter.Label(tab5, text="SQl CS 480 Project").grid(column=0,
                                                        row=0,
                                                        padx=30,
                                                        pady=25)

    tkinter.Label(tab5, text='Player').grid(column=0,
                                            row=2,
                                            padx=0,
                                            pady=(25, 5))

    tkinter.Label(tab5, text="Name").grid(column=0,
                                          row=3,
                                          padx=0,
                                          pady=0)

    playerName = tkinter.Text(tab5, height=1, width=20)
    playerName.grid(column=1,
                    row=3,
                    padx=0,
                    pady=0)

    tkinter.Label(tab5, text="SSN").grid(column=0,
                                         row=4,
                                         padx=0,
                                         pady=0)

    playerSSN = tkinter.Text(tab5, height=1, width=20)
    playerSSN.grid(column=1,
                   row=4,
                   padx=0,
                   pady=0)

    tkinter.Label(tab5, text='Team').grid(column=0,
                                          row=7,
                                          padx=0,
                                          pady=(60, 10))

    tkinter.Label(tab5, text="Name").grid(column=0,
                                          row=8,
                                          padx=0,
                                          pady=0)

    teamName = tkinter.Text(tab5, height=1, width=20)
    teamName.grid(column=1,
                  row=8,
                  padx=0,
                  pady=0)

    tkinter.Label(tab5, text='League').grid(column=5,
                                            row=2,
                                            padx=0,
                                            pady=(25, 5))

    tkinter.Label(tab5, text="Name").grid(column=5,
                                          row=3,
                                          padx=0,
                                          pady=0)

    leagueName = tkinter.Text(tab5, height=1, width=20)
    leagueName.grid(column=6,
                    row=3,
                    padx=0,
                    pady=0)

    tkinter.Label(tab5, text="Country").grid(column=5,
                                             row=4,
                                             padx=0,
                                             pady=0)

    leagueCountry = tkinter.Text(tab5, height=1, width=20)
    leagueCountry.grid(column=6,
                       row=4,
                       padx=0,
                       pady=0)

    tkinter.Label(tab5, text='Sponsor').grid(column=5,
                                             row=7,
                                             padx=0,
                                             pady=(60, 10))

    tkinter.Label(tab5, text="Name").grid(column=5,
                                          row=8,
                                          padx=0,
                                          pady=0)

    sponsorName = tkinter.Text(tab5, height=1, width=20)
    sponsorName.grid(column=6,
                     row=8,
                     padx=0,
                     pady=0)

    tkinter.Label(tab5, text="Sponsor ID").grid(column=5,
                                                row=9,
                                                padx=0,
                                                pady=0)

    sponsorID = tkinter.Text(tab5, height=1, width=20)
    sponsorID.grid(column=6,
                   row=9,
                   padx=0,
                   pady=0)

    """***********************
        Buttons for Deleting
        ***********************"""
    tkinter.Button(tab5, text="Find Player by Name", command=lambda: findPlayerByName(playerName)).grid(column=0,
                                                                                                        row=5,
                                                                                                        padx=0,
                                                                                                        pady=(20, 0))

    tkinter.Button(tab5, text="Find Player by SSN", command=lambda: findPlayerBySSN(playerSSN)).grid(column=1,
                                                                                                     row=5,
                                                                                                     padx=0,
                                                                                                     pady=(20, 0))

    tkinter.Button(tab5, text="Find Team by Name", command=lambda: findTeamByName(teamName)).grid(column=0,
                                                                                                  row=10,
                                                                                                  padx=0,
                                                                                                  pady=15)

    tkinter.Button(tab5, text="Find League by Name", command=lambda: findLeagueByName(leagueName)).grid(column=5,
                                                                                                        row=5,
                                                                                                        padx=(80, 0),
                                                                                                        pady=(20, 0))

    tkinter.Button(tab5, text="Find League by Country", command=lambda: findLeagueByCountry(leagueCountry)).grid(
        column=6,
        row=5,
        padx=0,
        pady=(20, 0))

    tkinter.Button(tab5, text="Find Sponsor by Name", command=lambda: findSponsorByName(sponsorName)).grid(column=5,
                                                                                                           row=10,
                                                                                                           padx=0,
                                                                                                           pady=15)

    tkinter.Button(tab5, text="Find Sponsor by Sponsor ID", command=lambda: findSponsorByID(sponsorID)).grid(column=6,
                                                                                                             row=10,
                                                                                                             padx=0,
                                                                                                             pady=15)
