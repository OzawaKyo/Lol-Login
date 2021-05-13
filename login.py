from os import O_APPEND
import time , subprocess
from pynput.keyboard import Key, Controller
from dearpygui.core import *
from dearpygui.simple import *
keyboard = Controller()



#the login function
def login(x,y):
    bb=open("clientDirectory.txt", "r")
    fileLines = bb.readlines()
    clientDirectory = fileLines[0].strip()
    subprocess.Popen( clientDirectory + '\\LeagueClient.exe' ) # <-- the league client directory 
    time.sleep(10)
    keyboard.type(x)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.type(y)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

#main buttons functions
def addAccount():
    idList = []
    id = get_value("id")
    idList.append(id + "\n")
    passwordsList = []
    password = get_value("password")
    passwordsList.append(password + "\n")
    f1=open("idSave.txt","a+")
    f1.writelines(idList)
    f2=open("passwordsSave.txt","a+")
    f2.writelines(passwordsList)

def account1():
    with open("idSave.txt",'r') as q:
        fileLines=q.readlines()
        account1Id=fileLines[0].strip()
    with open("passwordsSave.txt",'r') as w:
        fileLines2=w.readlines()
        account1Password=fileLines2[0].strip()
    login(account1Id, account1Password)    

def account2():
    with open("idSave.txt",'r') as q:
        fileLines=q.readlines()
        account2Id=fileLines[1].strip()
    with open("passwordsSave.txt",'r') as w:
        fileLines2=w.readlines()
        account2Password=fileLines2[1].strip()
    login(account2Id, account2Password)     

def account3():
    with open("idSave.txt",'r') as q:
        fileLines=q.readlines()
        account3Id=fileLines[2].strip()
    with open("passwordsSave.txt",'r') as w:
        fileLines2=w.readlines()
        account3Password=fileLines2[3].strip()
    login(account3Id, account3Password) 

def account4():
    with open("idSave.txt",'r') as q:
        fileLines=q.readlines()
        account4Id=fileLines[3].strip()
    with open("passwordsSave.txt",'r') as w:
        fileLines2=w.readlines()
        account4Password=fileLines2[3].strip()
    login(account4Id, account4Password) 

def clear():
    with open("idSave.txt","w") as g:
        g.close()
    with open("passwordsSave.txt","w") as g2:
        g2.close()    

def directory_picker(sender, data):
    select_directory_dialog(callback=apply_selected_directory)

def apply_selected_directory(sender, data):
    log_debug(data)  # so we can see what is inside of data
    directory = data[0]
    folder = data[1]
    set_value("directory", directory)
    set_value("folder", folder)
    set_value("folder_path", f"{directory}\\{folder}")
    k=open("clientDirectory.txt","a+")
    k.write(directory + "\n")
        
def clearDirectory():
    with open("clientDirectory.txt","w") as gg :
        gg.close()

    
show_logger()        

#window
set_main_window_size(540,720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30, 30)

#main page
with window("Lol login", width=520, height=677):
    print("running ...")
    set_window_pos("Lol login",0, 0)
    add_text("Choose the directory file of the league client :" , color=[232,163,33])
    add_spacing(count=12)
    add_text("exemple : C:\\Riot Games\\League of Legends ")
    add_spacing(count=12)
    add_button("Directory Selector", callback=directory_picker)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_text("Enter you id:", color = [232,163,33])
    add_spacing(count=12)
    add_input_text("id",width=415, default_value='')
    add_spacing(count=12)
    add_text("Enter you password:", color = [232,163,33])
    add_spacing(count=12)
    add_input_text("password",width=390, default_value='')
    add_spacing(count=12)
    add_button("Add account", callback=addAccount)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_button("account1",callback=account1)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_button("account2",callback=account2)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_button("account3",callback=account3)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_button("account4",callback=account4)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_button("clear accounts",callback=clear)
    add_spacing(count=12)
    add_separator()
    add_spacing(count=12)
    add_button("clear directory",callback=clearDirectory)




    #window loop
    start_dearpygui()
