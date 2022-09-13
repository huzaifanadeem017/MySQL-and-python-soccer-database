# library for GUI
import tkinter.ttk
from tkinter import *

# importing all the seperate files
# that contain GUI and database manipulation
# for all our different tasks
import deleteTeam
import insertTeam
import nestedQueries
import updateTeam
import listTeam
import findTeam

# creating main window
window = Tk()
window.title('Fútbol Database - CS480')
window.geometry("800x650+10+20")

# creating all the tabs for all our different
# tasks, so it can be accessed from one window
tabControl = tkinter.ttk.Notebook(window)
tab1 = Frame(tabControl)
tab2 = Frame(tabControl)
tab3 = Frame(tabControl)
tab4 = Frame(tabControl)
tab5 = Frame(tabControl)
tab6 = Frame(tabControl)

# add all tabs to a main controller of all
# tabs
tabControl.add(tab1, text='Insert')
tabControl.add(tab2, text='Delete')
tabControl.add(tab3, text='Update')
tabControl.add(tab4, text='List')
tabControl.add(tab5, text='Find')
tabControl.add(tab6, text='Nested Queries')
tabControl.pack(expand=1, fill="both")

# calling functions from all the different
# files that help us execute our tasks
insertTeam.tab1GUI(tab1)
deleteTeam.tab2GUI(tab2)
updateTeam.tab3GUI(tab3)
listTeam.tab4GUI(tab4)
findTeam.tab5GUI(tab5)
nestedQueries.tab4GUI(tab6)
window.mainloop()
