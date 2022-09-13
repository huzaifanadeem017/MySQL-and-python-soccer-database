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


def NQ1():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("600x100")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT top_scorers, team, red_cards FROM Performance WHERE red_cards IN " \
            "(SELECT avg (top_scorers) FROM Performance);"
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


def NQ2():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("350x150")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT team_name, opponent_team FROM (SELECT * FROM Upcoming_matches " \
            "WHERE location = 'Wembley Stadium' OR location = 'Emirates Stadium') dt GROUP BY team_name, opponent_team;"
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


def NQ3():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("550x300")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT first_name, last_name, nationality, position FROM (SELECT * FROM players " \
            "WHERE nationality = 'Brazil' OR nationality = 'Argentina' OR position = 'LW' OR position = 'RW') dt"
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


def NQ4():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("500x450")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT name, team, salary FROM (SELECT * FROM member WHERE role = 'Manager') dt;"
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


def NQ5():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("1200x350")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT name, budget FROM (SELECT * FROM sponsors WHERE contract_start = '2021' OR " \
            "contract_start = '2019') dt;"
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


def NQ6():
    # creating popout window for displaying table
    my_w = Tk()
    my_w.geometry("900x400")
    # reading from database to display table
    cursor = mydb.cursor()
    query = "SELECT team_name, opponent_team, date, time, location FROM " \
            "(SELECT * FROM Upcoming_matches WHERE team_name = 'Real Madrid' OR team_name ='Paris Saint Germain' " \
            "OR team_name ='Barcelona' OR opponent_team = 'Real Madrid' OR opponent_team ='Paris Saint Germain' " \
            "OR opponent_team ='Barcelona') dt"
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

    tkinter.Button(tab4, text="Nested Query 1\n Lowest number of red cards\n "
                              "for players that are\n top scorers", width=25, height=6, command=lambda: NQ1()).grid(
        column=0,
        row=2,
        padx=30,
        pady=15)

    tkinter.Button(tab4, text="Nested Query 2\n Teams that have\nupcoming matches in \n"
                              "Wembley Stadium or\n Emirates Stadium", width=25, height=6, command=lambda: NQ2()).grid(
        column=0,
        row=3,
        padx=30,
        pady=15)

    tkinter.Button(tab4, text="Nested Query 3\n Players that are\n from Brazil or Argentina\n"
                              "or play position of\n RW or LW", width=25, height=6, command=lambda: NQ3()).grid(
        column=0,
        row=4,
        padx=30,
        pady=15)

    tkinter.Button(tab4, text="Nested Query 4\n Find members that are\n managers showing their"
                              "\n team and salary", width=25, height=6, command=lambda: NQ4()).grid(column=3,
                                                                                                    row=2,
                                                                                                    padx=30,
                                                                                                    pady=(
                                                                                                        50, 15))

    tkinter.Button(tab4, text="Nested Query 5\n Sponsors whose contract started in 2019 or 2021",
                   width=25, height=6, command=lambda: NQ5()).grid(column=3,
                                                                   row=3,
                                                                   padx=30,
                                                                   pady=15)

    tkinter.Button(tab4,
                   text="Nested Query 6\n Filtering upcoming matches \nby popular soccer teams with "
                        "\ndate, time and location",
                   width=25, height=6, command=lambda: NQ6()).grid(column=3,
                                                                   row=4,
                                                                   padx=30,
                                                                   pady=15)
