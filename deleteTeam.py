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

def deletePlayer(ssn, fname, lname):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    ssn = ssn.get("1.0", "end-1c")
    fname = fname.get("1.0", "end-1c")
    lname = lname.get("1.0", "end-1c")
    # print(ssn, fname, lname)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "DELETE FROM players WHERE ssn = %s AND first_name = %s AND last_name = %s;"
    cursor.execute(query, (ssn, fname, lname))
    mydb.commit()
    cursor.close()
    # print("Done")


def deleteTeam(name, city):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    name = name.get("1.0", "end-1c")
    city = city.get("1.0", "end-1c")
    # print(name, city)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "DELETE FROM team WHERE name = %s AND city = %s;"
    cursor.execute(query, (name,city))
    cursor.close()
    mydb.commit()
    # print("Done")


def deleteLeague(name, season, country):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    name = name.get("1.0", "end-1c")
    season = season.get("1.0", "end-1c")
    country = country.get("1.0", "end-1c")
    # print(name, season, country)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "DELETE FROM football_database.league WHERE name = %s AND season_year = %s AND country = %s;"
    cursor.execute(query, (name, season, country))
    mydb.commit()
    cursor.close()
    # print("Done")


def deleteMember(ssn, role, team):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    ssn = ssn.get("1.0", "end-1c")
    role = role.get("1.0", "end-1c")
    team = team.get("1.0", "end-1c")
    # print(ssn, role, team)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "DELETE FROM football_database.member WHERE ssn = %s AND role = %s AND team = %s;"
    cursor.execute(query, (ssn, role, team))
    mydb.commit()
    cursor.close()
    # print("Done")


def tab2GUI(tab2):
    """
    Main function that executes where it inserts all GUI elements into tab
    """

    """*********************
    Tab 2 Title 
    *********************"""
    tkinter.Label(tab2,text="SQl CS 480 Project").grid(column=0,
                                                  row=0,
                                                  padx=30,
                                                  pady=15)

    """***********************
        Delete Team Elements
        ***********************"""
    tkinter.Label(tab2, text='Team').grid(column=0,
                                          row=2,
                                          padx=0,
                                          pady=25)

    tkinter.Label(tab2, text="Name").grid(column=0,
                                          row=3,
                                          padx=0,
                                          pady=0)

    teamName = tkinter.Text(tab2, height=1, width=20)
    teamName.grid(column=1,
                  row=3,
                  padx=0,
                  pady=0)

    tkinter.Label(tab2, text="City").grid(column=0,
                                          row=4,
                                          padx=0,
                                          pady=0)
    teamCity = tkinter.Text(tab2, height=1, width=20)
    teamCity.grid(column=1,
                  row=4,
                  padx=0,
                  pady=0)

    """***********************
        Delete Player Elements
        ***********************"""
    tkinter.Label(tab2, text='Player').grid(column=0,
                                            row=15,
                                            padx=0,
                                            pady=25)

    tkinter.Label(tab2, text="SSN").grid(column=0,
                                         row=16,
                                         padx=0,
                                         pady=0)

    playerSSN = tkinter.Text(tab2, height=1, width=20)
    playerSSN.grid(column=1,
                   row=16,
                   padx=0,
                   pady=0)

    tkinter.Label(tab2, text="First Name").grid(column=0,
                                                row=18,
                                                padx=0,
                                                pady=0)
    playerFName = tkinter.Text(tab2, height=1, width=20)
    playerFName.grid(column=1,
                     row=18,
                     padx=0,
                     pady=0)

    tkinter.Label(tab2, text="Last Name").grid(column=0,
                                               row=19,
                                               padx=0,
                                               pady=0)
    playerLName = tkinter.Text(tab2, height=1, width=20)
    playerLName.grid(column=1,
                     row=19,
                     padx=0,
                     pady=0)

    """***********************
        Delete League Elements
        ***********************"""
    tkinter.Label(tab2, text='League').grid(column=2,
                                            row=2,
                                            padx=100,
                                            pady=25)

    tkinter.Label(tab2, text="Name").grid(column=2,
                                          row=3,
                                          padx=0,
                                          pady=0)

    leagueName = tkinter.Text(tab2, height=1, width=20)
    leagueName.grid(column=3,
                    row=3,
                    padx=0,
                    pady=0)

    tkinter.Label(tab2, text="Season Year").grid(column=2,
                                                 row=4,
                                                 padx=0,
                                                 pady=0)
    leagueSeason = tkinter.Text(tab2, height=1, width=20)
    leagueSeason.grid(column=3,
                      row=4,
                      padx=0,
                      pady=0)

    tkinter.Label(tab2, text="Country").grid(column=2,
                                             row=5,
                                             padx=0,
                                             pady=0)
    leagueCountry = tkinter.Text(tab2, height=1, width=20)
    leagueCountry.grid(column=3,
                       row=5,
                       padx=0,
                       pady=0)

    """***********************
        Delete Member Elements
        ***********************"""
    tkinter.Label(tab2, text='Member').grid(column=2,
                                            row=15,
                                            padx=20,
                                            pady=25)

    tkinter.Label(tab2, text="SSN").grid(column=2,
                                         row=16,
                                         padx=0,
                                         pady=0)

    memberSSN = tkinter.Text(tab2, height=1, width=20)
    memberSSN.grid(column=3,
                   row=16,
                   padx=0,
                   pady=0)

    tkinter.Label(tab2, text="Role").grid(column=2,
                                          row=17,
                                          padx=0,
                                          pady=0)
    memberRole = tkinter.Text(tab2, height=1, width=20)
    memberRole.grid(column=3,
                    row=17,
                    padx=0,
                    pady=0)

    tkinter.Label(tab2, text="Team").grid(column=2,
                                          row=18,
                                          padx=0,
                                          pady=0)
    memberTeam = tkinter.Text(tab2, height=1, width=20)
    memberTeam.grid(column=3,
                    row=18,
                    padx=0,
                    pady=0)


    """***********************
            Buttons for Deleting
            ***********************"""
    tkinter.Button(tab2, text="Delete Team", command=lambda: deleteTeam(teamName, teamCity)).grid(column=0,
                                                                                                  row=11,
                                                                                                  padx=0,
                                                                                                  pady=25)

    tkinter.Button(tab2, text="Delete League", command=lambda: deleteLeague(leagueName, leagueSeason,
                                                                            leagueCountry)).grid(column=2,
                                                    row=11,
                                                    padx=0,
                                                    pady=25)

    tkinter.Button(tab2, text="Delete Member", command=lambda: deleteMember(memberSSN, memberRole,
                                                                            memberTeam)).grid(column=2,
                                                    row=27,
                                                    padx=0,
                                                    pady=25)

    tkinter.Button(tab2, text="Delete Player",
                   command=lambda: deletePlayer(playerSSN, playerFName, playerLName)).grid(column=0,
                                                                                           row=27,
                                                                                           padx=0,
                                                                                           pady=25)