from admin import Admin
from user import User
from mylibrary import Mylibrary
import keyboard
from datetime import datetime
from edit import Edit



# define my error
class Invalidnumber(Exception):
    pass

print(20*'*'+"Welcome to my library"+20*'*'+"\n\n")
now = datetime.utcnow()
year_month_day_format ="%Y-%m-%d"
date_get=now.strftime(year_month_day_format)
date_list=date_get.split("-")
# print(date_list)

# print("Enter to my library as Admin: Enter 1\nEnter to my library as User: Enter 2\nExit: Enter 3")
lib=Mylibrary()
lib.load_books()
admin_object=Admin('a','a','a','a')
admin_object.load_admins()
user_obj=User('a','a','a','a','1','a','a','a')
last_db_id=int(user_obj.load_users())
new_edit=Edit('a','a','a','a','a','a','a')
new_edit.load_edits()
# print(last_db_id)
user_obj.update_deadlines(date_list)
user_obj.reminder_email(lib)
identify=0
previous_step=False
admin_login_ok=-10
user_login_ok=-10
while True:
    try:
        identify=input("Enter to my library as User: Enter 1\nEnter to my library as Admin: Enter 2\nExit: Enter 3\n")
        if int(identify)==1:
            user_login_ok=1
            print("you are login as user.")
        elif int(identify)==2:
            while True:
                user=input("Enter your username:  ")
                password=input("Enter your password:  ")
                admin_login_ok=admin_object.verify_admin(user,password)
                if admin_login_ok>=0:
                    print(f"you are login as {user}")
                    break
                elif admin_login_ok==-1:
                    print("username or password is incorrect.\ntry again=press space\nBack=press escap")
                    while True:
                            if keyboard.read_key(suppress=True)=="space":
                                break
                            elif keyboard.read_key(suppress=True)=="esc":
                                previous_step=True                          
                                break
                            else:
                                print("press space or Esc")
                if previous_step==True:
                    previous_step=False                          
                    break
        elif int(identify)==3:
            admin_object.update_admins_database()
            lib.update_books_database()
            user_obj.update_users_database()
            new_edit.update_edits_database()
            break
        else:
            raise Invalidnumber
    except ValueError:
        print(f"({identify}) is not a valid input!")
        print("Please enter a valid input:")
    except Invalidnumber:
        print(f"({identify}) is not a valid input!")
        print("Please enter a valid input:")
    while admin_login_ok>=0:
        try:
            admin_command=int(input("please enter your command:\nadd book: enter 1\nedit book: enter 2\nremove book: enter 3\nsearch book: enter 4\nshow books: enter 5\nadd admin:enter 6\nchange user or password:enter 7\nshow last edited:enter 8\nback: enter 9\n"))
            if admin_command==1:
                admin_object.add_book(lib)
            elif admin_command==2:
                admin_object.edit_book(lib,new_edit,admin_login_ok,date_get)
            elif admin_command==3:
                admin_object.remove_book(lib)
            elif admin_command==4:
                admin_object.search_book(lib)
            elif admin_command==5:
                admin_object.view_books(lib)
            elif admin_command==6:
                admin_object.add_admin(lib)
            elif admin_command==7:
                admin_object.change_user_password()
            elif admin_command==8:
                new_edit.show_edit_info()
            elif admin_command==9:
                admin_login_ok=-10
            else:
                raise Invalidnumber
        except ValueError:
            print(f"({identify}) is not a valid input!")
            print("Please enter a valid input:")
        except Invalidnumber:
            print(f"({identify}) is not a valid input!")
            print("Please enter a valid input:")
    while user_login_ok>0:
        try:
            user_command=int(input("login to account: enter your id\nregister in library: enter 1\nBack: enter 3\n"))
            if user_command==1:
                user_obj.register(last_db_id)
            elif 99<user_command:
                index_user=user_obj.check_id(user_command)
                if index_user!=-1:
                    print(f"you are login as {user_obj.users[index_user].firstname} {user_obj.users[index_user].lastname}")
                    while True:
                        try:
                            login_command=int(input("please enter your command:\nborrow book: enter 1\show information: enter 2\Back: enter 3\n"))
                            if login_command==1:
                                user_obj.borrow_book(lib,date_list,index_user)
                            elif login_command==2:
                                user_obj.show_user_info()
                            elif login_command==3:
                                break
                            else:
                                print("command not found.\n")
                        except  Exception as e:
                            print(e)
                            print("command not found.\n")
                elif index_user==-1:
                    print("your id not found.\n")
                # user_obj.borrow_book(lib,date_list)
            elif user_command==3:
                user_login_ok=-10
            else:
                raise Invalidnumber
        except ValueError:
            print(f"({identify}) is not a valid input!")
            print("Please enter a validddd input:")
        except Invalidnumber:
            print(f"({identify}) is not a valid input!")
            print("Please enter a valid input:")

