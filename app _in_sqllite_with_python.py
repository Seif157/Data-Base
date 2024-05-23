# database project using SQLlite handling with python
import sqlite3


# connect to the file of database 
db=sqlite3.connect(r"C:\Users\DELL\Desktop\course python elzeroo\basic of database\app _database_with_python.db") # the path for the database file

# define cursor
cursor=db.cursor()

# creat table and fields
db.execute("create table if not exists skilles (name text, progress integer, user_id)")

# define methodes
def commit ():
    """ commit changes database """
    db.commit()
    print("Changing is done")
    


def show_skills():
    cursor.execute(f"Select * from skilles where user_id='{my_user_id}'")
    results=cursor.fetchall()
    if results:
        print(f"You have {len(results)} skilles ")
        print("The skilles with progresses ")
        for row in results:
            print(f"Skill => {row[0]}" ,end=(" - "))
            print(f"Progress => {row[1]}")
        commit()
    else:
        the_option="""
        Please enter one option (add skill or No)
        y for add 
        n for Not add
        """
        new_input=input(f"{the_option} is : ")
        if new_input == "a":
            add_skill()
        elif new_input =="n":
            pass
        else:
            print(" This not valid ")
            pass
        commit()


def add_skill():
    skill_name=input("Write skill name : ").strip().capitalize()
    cursor.execute(f"Select * from skilles where user_id='{my_user_id}' and name ='{skill_name}'")
    check=cursor.fetchone()
    if check:
        print("This skill is actualy exist ")
        what_should_done="""Do you update or not
'u'for updating
'n' for not
"""
        what_should_done_value=input(f"{what_should_done} chose one option : ")
        if what_should_done_value=="u":
            update_skill()
        elif what_should_done_value=="n":
            commit()
        else:
            print(" This not valid try again later ")
            commit()
    else:
        progress=input("Write skill progress : ").strip()
        cursor.execute(f"Insert into skilles (name ,progress ,user_id) values('{skill_name}','{progress}','{my_user_id}')")
        commit()


def delete_skill():
    skill_name=input("Write skill name : ").strip().capitalize()
    cursor.execute(f"Select * from skilles where user_id='{my_user_id}' and name ='{skill_name}'")
    check=cursor.fetchone()
    if check:
        cursor.execute(f"Delete from skilles where name='{skill_name}' and user_id='{my_user_id}'")
        commit()
    else:
        print(f"{skill_name} isn't exist ")
        commit()


def update_skill():
    skill_name=input("What is the name of skill you will update its progress : ").strip().capitalize()
    cursor.execute(f"Select * from skilles where user_id='{my_user_id}' and name ='{skill_name}'")
    check=cursor.fetchone()
    if check:
        new_progress=input(f"What is new progress : ")
        cursor.execute(f"Update skilles set progress ='{new_progress}' where name ='{skill_name}' and user_id = '{my_user_id}'")
        commit()
    else:
        print("This skill isn't exist ")
        what_should_done="""Do you add or not
'a'for adding
'n' for not
"""
        what_should_done_value=input(f"{what_should_done}chose one option : ")
        if what_should_done_value=="a":
            add_skill()
        elif what_should_done_value=="n":
            commit()
        else:
            print(" This not valid try again later ")
            commit()

user_input=True

while user_input:
    my_user_id=input("Please enter your id  : ")

    input_message ="""
what do you want to do ?
"s" for shown all skill
"a" for add new skill
"d" for delete a skill
"u" for update skill progress
"q" for quit the app                     
choose option :  
"""

    user_input= input(input_message.strip().lower())

    command_list=["s","a","d","u","q"]

    if user_input in command_list:
        if user_input=="s":
            show_skills()
        elif user_input=="a":
            add_skill()
        elif user_input=="d":
            delete_skill()
        elif user_input=="u":
            update_skill()
        else:
            commit()
            print("App is closed ")
    
    else:
        print(f"Sorry this command : {user_input} isn't found ")
        user_input=input("Please enter a valid character : ")
    
    print("#"*50)
    my_user_id=input("Please enter your id  : ")
    user_input= input(input_message.strip().lower())

# when user_input is None
db.close()