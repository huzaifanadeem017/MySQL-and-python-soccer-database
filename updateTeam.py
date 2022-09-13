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


def updateTeam(name, city, record, budget):
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
    query = "UPDATE team SET city = %s, wdl_record = %s, budget = %s WHERE name = %s;"
    cursor.execute(query, (city, record, budget, name))
    mydb.commit()
    cursor.close()


def updateUM(id, team, season, opponent, date, time, location):
    """
                Retrieves input from textfields, engages with database, and inserts info into database
                """
    # reading in all the textboxes
    id = id.get("1.0", "end-1c")
    team = team.get("1.0", "end-1c")
    season = season.get("1.0", "end-1c")
    opponent = opponent.get("1.0", "end-1c")
    date = date.get("1.0", "end-1c")
    time = time.get("1.0", "end-1c")
    location = location.get("1.0", "end-1c")
    # print(id, team, season, opponent, date, time, location)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "UPDATE upcoming_matches SET team_name = %s, season_year = %s, opponent_team = %s," \
            "date = %s, time = %s, location = %s WHERE match_id = %s;"
    cursor.execute(query, (team, season, opponent, date, time, location, id))
    mydb.commit()
    cursor.close()
    print("Done")


def updateP(id, season, team, ts, ta, tsr, yc, rc):
    """
                Retrieves input from textfields, engages with database, and inserts info into database
                """
    # reading in all the textboxes
    id = id.get("1.0", "end-1c")
    season = season.get("1.0", "end-1c")
    team = team.get("1.0", "end-1c")
    ts = ts.get("1.0", "end-1c")
    ta = ta.get("1.0", "end-1c")
    tsr = tsr.get("1.0", "end-1c")
    yc = yc.get("1.0", "end-1c")
    rc = rc.get("1.0", "end-1c")
    # print(id, season, team, ts, ta, tsr, yc, rc)
    # engages with database and runs query to insert elements
    cursor = mydb.cursor()
    query = "UPDATE performance SET season_year = %s, team = %s, top_scorers = %s," \
            "top_assists = %s, tackle_success_rate = %s, yellow_cards = %s, red_cards = %s WHERE performance_id = %s;"
    cursor.execute(query, (season, team, ts, ta, tsr, yc, rc, id))
    mydb.commit()
    cursor.close()
    print("Done")


def tab3GUI(tab3):
    """
    Main function that executes where it inserts all GUI elements into tab
    """

    """*********************
    Update Tab Title
    *********************"""
    tkinter.Label(tab3, text="SQl CS 480 Project").grid(column=0,
                                                        row=0,
                                                        padx=30,
                                                        pady=15)

    """*********************
        Update Team Elements
        *********************"""
    tkinter.Label(tab3, text='Team').grid(column=0,
                                          row=2,
                                          padx=0,
                                          pady=25)

    tkinter.Label(tab3, text="Name").grid(column=0,
                                          row=3,
                                          padx=0,
                                          pady=0)

    teamName = tkinter.Text(tab3, height=1, width=20)
    teamName.grid(column=1,
                  row=3,
                  padx=0,
                  pady=0)

    tkinter.Label(tab3, text="City").grid(column=0,
                                          row=4,
                                          padx=0,
                                          pady=0)
    teamCity = tkinter.Text(tab3, height=1, width=20)
    teamCity.grid(column=1,
                  row=4,
                  padx=0,
                  pady=0)

    tkinter.Label(tab3, text="WDL Record").grid(column=0,
                                                row=5,
                                                padx=0,
                                                pady=0)
    teamRecord = tkinter.Text(tab3, height=1, width=20)
    teamRecord.grid(column=1,
                    row=5,
                    padx=0,
                    pady=0)

    tkinter.Label(tab3, text="Budget").grid(column=0,
                                            row=6,
                                            padx=0,
                                            pady=0)
    teamBudget = tkinter.Text(tab3, height=1, width=20)
    teamBudget.grid(column=1,
                    row=6,
                    padx=0,
                    pady=0)

    """*****************************
    Update Upcoming Matches Elements
    *****************************"""

    tkinter.Label(tab3, text='Upcoming Matches').grid(column=3,
                                                      row=2,
                                                      padx=0,
                                                      pady=25)

    tkinter.Label(tab3, text="Match ID").grid(column=3,
                                              row=3,
                                              padx=0,
                                              pady=0)

    UM_matchID = tkinter.Text(tab3, height=1, width=20)
    UM_matchID.grid(column=4,
                    row=3,
                    padx=0,
                    pady=0)

    tkinter.Label(tab3, text="Team Name").grid(column=3,
                                               row=4,
                                               padx=0,
                                               pady=0)
    UM_team = tkinter.Text(tab3, height=1, width=20)
    UM_team.grid(column=4,
                 row=4,
                 padx=0,
                 pady=0)

    tkinter.Label(tab3, text="Season Year").grid(column=3,
                                                 row=5,
                                                 padx=0,
                                                 pady=0)
    UM_season = tkinter.Text(tab3, height=1, width=20)
    UM_season.grid(column=4,
                   row=5,
                   padx=0,
                   pady=0)

    tkinter.Label(tab3, text="Opponent Name").grid(column=3,
                                                   row=6,
                                                   padx=0,
                                                   pady=0)
    UM_opponent = tkinter.Text(tab3, height=1, width=20)
    UM_opponent.grid(column=4,
                     row=6,
                     padx=0,
                     pady=0)

    tkinter.Label(tab3, text="Date").grid(column=3,
                                          row=7,
                                          padx=0,
                                          pady=0)
    UM_date = tkinter.Text(tab3, height=1, width=20)
    UM_date.grid(column=4,
                 row=7,
                 padx=0,
                 pady=0)

    tkinter.Label(tab3, text="Time").grid(column=3,
                                          row=8,
                                          padx=0,
                                          pady=0)
    UM_time = tkinter.Text(tab3, height=1, width=20)
    UM_time.grid(column=4,
                 row=8,
                 padx=0,
                 pady=0)

    tkinter.Label(tab3, text="Location").grid(column=3,
                                              row=9,
                                              padx=0,
                                              pady=0)
    UM_location = tkinter.Text(tab3, height=1, width=20)
    UM_location.grid(column=4,
                     row=9,
                     padx=0,
                     pady=0)

    """***********************
    Update Performance Elements
    ***********************"""
    tkinter.Label(tab3, text='Performance').grid(column=0,
                                                 row=15,
                                                 padx=0,
                                                 pady=25)

    tkinter.Label(tab3, text="Performance ID").grid(column=0,
                                                    row=16,
                                                    padx=0,
                                                    pady=0)

    P_id = tkinter.Text(tab3, height=1, width=20)
    P_id.grid(column=1,
              row=16,
              padx=0,
              pady=0)

    tkinter.Label(tab3, text="Season Year").grid(column=0,
                                                 row=17,
                                                 padx=0,
                                                 pady=0)
    P_season = tkinter.Text(tab3, height=1, width=20)
    P_season.grid(column=1,
                  row=17,
                  padx=0,
                  pady=0)

    tkinter.Label(tab3, text="Team").grid(column=0,
                                          row=18,
                                          padx=0,
                                          pady=0)
    P_team = tkinter.Text(tab3, height=1, width=20)
    P_team.grid(column=1,
                row=18,
                padx=0,
                pady=0)

    tkinter.Label(tab3, text="Top Scorers").grid(column=0,
                                                 row=19,
                                                 padx=0,
                                                 pady=0)
    P_topS = tkinter.Text(tab3, height=1, width=20)
    P_topS.grid(column=1,
                row=19,
                padx=0,
                pady=0)

    tkinter.Label(tab3, text="Top Assists").grid(column=0,
                                                 row=20,
                                                 padx=0,
                                                 pady=0)
    P_topA = tkinter.Text(tab3, height=1, width=20)
    P_topA.grid(column=1,
                row=20,
                padx=0,
                pady=0)

    tkinter.Label(tab3, text="Tackle Success Rate").grid(column=0,
                                                         row=21,
                                                         padx=0,
                                                         pady=0)
    P_TSR = tkinter.Text(tab3, height=1, width=20)
    P_TSR.grid(column=1,
               row=21,
               padx=0,
               pady=0)

    tkinter.Label(tab3, text="Yellow Cards").grid(column=0,
                                                  row=22,
                                                  padx=0,
                                                  pady=0)
    P_yc = tkinter.Text(tab3, height=1, width=20)
    P_yc.grid(column=1,
              row=22,
              padx=0,
              pady=0)

    tkinter.Label(tab3, text="Red Cards").grid(column=0,
                                               row=23,
                                               padx=0,
                                               pady=0)
    P_rc = tkinter.Text(tab3, height=1, width=20)
    P_rc.grid(column=1,
              row=23,
              padx=0,
              pady=0)

    """***********************
    Buttons for Deleting
    ***********************"""
    tkinter.Button(tab3, text="Update Team", command=lambda: updateTeam(teamName, teamCity,
                                                                        teamRecord, teamBudget)).grid(column=0,
                                                                                                      row=11,
                                                                                                      padx=0,
                                                                                                      pady=15)

    tkinter.Button(tab3, text="Update Upcoming Matches", command=lambda: updateUM(UM_matchID, UM_team, UM_season,
                                                                                  UM_opponent, UM_date,
                                                                                  UM_time, UM_location
                                                                                  )).grid(column=3,
                                                                                          row=11,
                                                                                          padx=0,
                                                                                          pady=15)

    tkinter.Button(tab3, text="Update Performance", command=lambda: updateP(P_id, P_season, P_team,
                                                                            P_topS, P_topA, P_TSR,
                                                                            P_yc, P_rc)).grid(column=0,
                                                                                              row=27,
                                                                                              padx=0,
                                                                                              pady=15)
