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


def insertPlayer(ssn_no, jersey, fname, lname, nation, team_name, position_name, salary):
    """
    Retrieves input from textfields, engages with database, and inserts info into database
    """
    # reading in all the textboxes
    ssn = ssn_no.get("1.0", "end-1c")
    jersey_number = jersey.get("1.0", "end-1c")
    first_name = fname.get("1.0", "end-1c")
    last_name = lname.get("1.0", "end-1c")
    nationality = nation.get("1.0", "end-1c")
    team = team_name.get("1.0", "end-1c")
    position = position_name.get("1.0", "end-1c")
    market_value = salary.get("1.0", "end-1c")
    # print(ssn, jersey_number, first_name, last_name, nationality, team, position, market_value)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "INSERT INTO football_database.players VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (ssn, jersey_number, first_name, last_name, nationality, team, position, market_value))
    mydb.commit()
    cursor.close()
    # print("Done")


def insertTeam(name, city, record, budget):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    name = name.get("1.0", "end-1c")
    city = city.get("1.0", "end-1c")
    record = record.get("1.0", "end-1c")
    budget = budget.get("1.0", "end-1c")
    # print(name, city, record, budget)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "INSERT INTO team VALUES (%s,%s,%s,%s);"
    cursor.execute(query, (name, city, record, budget))
    mydb.commit()
    cursor.close()
    # print("Done")


def insertLeague(name, season, country, organization, teams):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    name = name.get("1.0", "end-1c")
    season = season.get("1.0", "end-1c")
    country = country.get("1.0", "end-1c")
    organization = organization.get("1.0", "end-1c")
    teams = teams.get("1.0", "end-1c")
    # print(name, season, country, organization, teams)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "INSERT INTO league VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(query, (name, season, country, organization, teams))
    mydb.commit()
    cursor.close()
    # print("Done")


def insertMember(ssn, role, name, team, salary, contract):
    """
        Retrieves input from textfields, engages with database, and inserts info into database
        """
    # reading in all the textboxes
    ssn = ssn.get("1.0", "end-1c")
    role = role.get("1.0", "end-1c")
    name = name.get("1.0", "end-1c")
    team = team.get("1.0", "end-1c")
    salary = salary.get("1.0", "end-1c")
    contract = contract.get("1.0", "end-1c")
    # print(ssn, role, name, team, salary, contract)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "INSERT INTO member VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.execute(query, (ssn, role, name, team, salary, contract))
    mydb.commit()
    cursor.close()
    # print("Done")


def tab1GUI(tab1):
    """
    Main function that executes where it inserts all GUI elements into tab
    """

    """***********************
    Update Team Elements
    ***********************"""
    tkinter.Label(tab1, text='Team').grid(column=0,
                                          row=2,
                                          padx=0,
                                          pady=25)

    tkinter.Label(tab1, text="Name").grid(column=0,
                                          row=3,
                                          padx=0,
                                          pady=0)

    teamName = tkinter.Text(tab1, height=1, width=20)
    teamName.grid(column=1,
                  row=3,
                  padx=0,
                  pady=0)

    tkinter.Label(tab1, text="City").grid(column=0,
                                          row=4,
                                          padx=0,
                                          pady=0)
    teamCity = tkinter.Text(tab1, height=1, width=20)
    teamCity.grid(column=1,
                  row=4,
                  padx=0,
                  pady=0)

    tkinter.Label(tab1, text="WDL Record").grid(column=0,
                                                row=5,
                                                padx=0,
                                                pady=0)
    teamRecord = tkinter.Text(tab1, height=1, width=20)
    teamRecord.grid(column=1,
                    row=5,
                    padx=0,
                    pady=0)

    tkinter.Label(tab1, text="Budget").grid(column=0,
                                            row=6,
                                            padx=0,
                                            pady=0)
    teamBudget = tkinter.Text(tab1, height=1, width=20)
    teamBudget.grid(column=1,
                    row=6,
                    padx=0,
                    pady=0)

    """***********************
        Update Player Elements
        ***********************"""
    tkinter.Label(tab1, text='Player').grid(column=0,
                                            row=15,
                                            padx=0,
                                            pady=25)

    tkinter.Label(tab1, text="SSN").grid(column=0,
                                         row=16,
                                         padx=0,
                                         pady=0)

    playerSSN = tkinter.Text(tab1, height=1, width=20)
    playerSSN.grid(column=1,
                   row=16,
                   padx=0,
                   pady=0)

    tkinter.Label(tab1, text="Jersey Number").grid(column=0,
                                                   row=17,
                                                   padx=0,
                                                   pady=0)
    playerJerseyNo = tkinter.Text(tab1, height=1, width=20)
    playerJerseyNo.grid(column=1,
                        row=17,
                        padx=0,
                        pady=0)

    tkinter.Label(tab1, text="First Name").grid(column=0,
                                                row=18,
                                                padx=0,
                                                pady=0)
    playerFName = tkinter.Text(tab1, height=1, width=20)
    playerFName.grid(column=1,
                     row=18,
                     padx=0,
                     pady=0)

    tkinter.Label(tab1, text="Last Name").grid(column=0,
                                               row=19,
                                               padx=0,
                                               pady=0)
    playerLName = tkinter.Text(tab1, height=1, width=20)
    playerLName.grid(column=1,
                     row=19,
                     padx=0,
                     pady=0)

    tkinter.Label(tab1, text="Nationality").grid(column=0,
                                                 row=20,
                                                 padx=0,
                                                 pady=0)
    playerNationality = tkinter.Text(tab1, height=1, width=20)
    playerNationality.grid(column=1,
                           row=20,
                           padx=0,
                           pady=0)

    tkinter.Label(tab1, text="Team").grid(column=0,
                                          row=21,
                                          padx=0,
                                          pady=0)

    playerTeam = tkinter.Text(tab1, height=1, width=20)
    playerTeam.grid(column=1,
                    row=21,
                    padx=0,
                    pady=0)

    tkinter.Label(tab1, text="Position").grid(column=0,
                                              row=22,
                                              padx=0,
                                              pady=0)
    playerPosition = tkinter.Text(tab1, height=1, width=20)
    playerPosition.grid(column=1,
                        row=22,
                        padx=0,
                        pady=0)

    tkinter.Label(tab1, text="Yearly Salary").grid(column=0,
                                                   row=23,
                                                   padx=0,
                                                   pady=0)
    playerSalary = tkinter.Text(tab1, height=1, width=20)
    playerSalary.grid(column=1,
                      row=23,
                      padx=0,
                      pady=0)

    """***********************
        Update League Elements
        ***********************"""
    tkinter.Label(tab1, text='League').grid(column=2,
                                            row=2,
                                            padx=100,
                                            pady=25)

    tkinter.Label(tab1, text="Name").grid(column=2,
                                          row=3,
                                          padx=0,
                                          pady=0)

    leagueName = tkinter.Text(tab1, height=1, width=20)
    leagueName.grid(column=3,
                    row=3,
                    padx=0,
                    pady=0)

    tkinter.Label(tab1, text="Season Year").grid(column=2,
                                                 row=4,
                                                 padx=0,
                                                 pady=0)
    leagueSeason = tkinter.Text(tab1, height=1, width=20)
    leagueSeason.grid(column=3,
                      row=4,
                      padx=0,
                      pady=0)

    tkinter.Label(tab1, text="Country").grid(column=2,
                                             row=5,
                                             padx=0,
                                             pady=0)
    leagueCountry = tkinter.Text(tab1, height=1, width=20)
    leagueCountry.grid(column=3,
                       row=5,
                       padx=0,
                       pady=0)

    tkinter.Label(tab1, text="Organization").grid(column=2,
                                                  row=6,
                                                  padx=0,
                                                  pady=0)
    leagueOrganization = tkinter.Text(tab1, height=1, width=20)
    leagueOrganization.grid(column=3,
                            row=6,
                            padx=0,
                            pady=0)

    tkinter.Label(tab1, text="Number of Teams").grid(column=2,
                                                     row=7,
                                                     padx=0,
                                                     pady=0)
    leagueNumTeam = tkinter.Text(tab1, height=1, width=20)
    leagueNumTeam.grid(column=3,
                       row=7,
                       padx=0,
                       pady=0)

    """***********************
        Update Member Elements
        ***********************"""
    tkinter.Label(tab1, text='Member').grid(column=2,
                                            row=15,
                                            padx=20,
                                            pady=25)

    tkinter.Label(tab1, text="SSN").grid(column=2,
                                         row=16,
                                         padx=0,
                                         pady=0)

    memberSSN = tkinter.Text(tab1, height=1, width=20)
    memberSSN.grid(column=3,
                   row=16,
                   padx=0,
                   pady=0)

    tkinter.Label(tab1, text="Role").grid(column=2,
                                          row=17,
                                          padx=0,
                                          pady=0)
    memberRole = tkinter.Text(tab1, height=1, width=20)
    memberRole.grid(column=3,
                    row=17,
                    padx=0,
                    pady=0)

    tkinter.Label(tab1, text="name").grid(column=2,
                                          row=18,
                                          padx=0,
                                          pady=0)
    memberName = tkinter.Text(tab1, height=1, width=20)
    memberName.grid(column=3,
                    row=18,
                    padx=0,
                    pady=0)

    tkinter.Label(tab1, text="Team").grid(column=2,
                                          row=19,
                                          padx=0,
                                          pady=0)
    memberTeam = tkinter.Text(tab1, height=1, width=20)
    memberTeam.grid(column=3,
                    row=19,
                    padx=0,
                    pady=0)

    tkinter.Label(tab1, text="Salary").grid(column=2,
                                            row=20,
                                            padx=0,
                                            pady=0)
    memberSalary = tkinter.Text(tab1, height=1, width=20)
    memberSalary.grid(column=3,
                      row=20,
                      padx=0,
                      pady=0)

    tkinter.Label(tab1, text="Contract Duration").grid(column=2,
                                                       row=21,
                                                       padx=0,
                                                       pady=0)
    memberContract = tkinter.Text(tab1, height=1, width=20)
    memberContract.grid(column=3,
                        row=21,
                        padx=0,
                        pady=0)

    """***********************
    Tab Title
    ***********************"""
    tkinter.Label(tab1,
                  text="SQl CS 480 Project").grid(column=0,
                                                  row=0,
                                                  padx=30,
                                                  pady=15)
    """***********************
        Buttons for to trigger functions
        that read in the textfields and insert into
        database
        ***********************"""
    tkinter.Button(tab1, text="Insert Team", command=lambda: insertTeam(teamName, teamCity, teamRecord,
                                                                        teamBudget)).grid(column=0,
                                                                                            row=11,
                                                                                            padx=0,
                                                                                            pady=25)

    tkinter.Button(tab1, text="Insert League", command=lambda: insertLeague(leagueName, leagueSeason,
                                                                            leagueCountry, leagueOrganization,
                                                                            leagueNumTeam)).grid(column=2,
                                                                                                   row=11,
                                                                                                   padx=0,
                                                                                                   pady=25)

    tkinter.Button(tab1, text="Insert Member", command=lambda: insertMember(memberSSN, memberRole, memberName,
                                                                            memberTeam, memberSalary,
                                                                            memberContract)).grid(column=2,
                                                                                                    row=27,
                                                                                                    padx=0,
                                                                                                    pady=25)

    tkinter.Button(tab1, text="Insert Player",
                   command=lambda: insertPlayer(playerSSN, playerJerseyNo, playerFName, playerLName,
                                                playerNationality,
                                                playerTeam, playerPosition, playerSalary)).grid(column=0,
                                                                                                  row=27,
                                                                                                  padx=0,
                                                                                                  pady=25)
