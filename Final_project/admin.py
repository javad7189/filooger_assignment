from user import Person
from book import Book



class Invalidnumber(Exception):
    pass


class Admin(Person):
    def __init__(self,first_name,last_name,username,password):
        Person.__init__(self,first_name,last_name)
        self.username=username
        self.password=password
        self.admins=[]



    def load_admins(self):
        with open("D:/filoger/final_project/admins.txt",'a+') as file:
            file.seek(0)
            lines=file.readlines()
            if len(lines)==0:
                file.write("default_user,default_user,admin,admin\n")
                lines.append("default_user,default_user,admin,admin")
            for line in lines:
                list1=line.split(",")
                list1[3]=list1[3].replace("\n","")
                admin=Admin(list1[0],list1[1],list1[2],list1[3])
                self.admins.append(admin)
    
    def update_admins_database(self):
            with open("D:/filoger/final_project/admins.txt",'w') as file:
                for i in self.admins:
                    file.write(f"{i.firstname},{i.lastname},{i.username},{i.password}\n")
                print("admins database updated.")

    def verify_admin(self,user,password):
            for j,i in enumerate(self.admins):
                if i.username==user and i.password==password:
                    return j
            return -1
    
    def add_admin(self):
        while True:
            try:
                admin_info= input("Enter information of new Admin:\n Example format: firstname,lastname,username,password\n")
                ad_list=admin_info.split(",")
                check=self.verify_admin(ad_list[2],ad_list[3])
                if check!=-1:
                    print("Both of username and password are already exist.\ntry again: enter 1\nback: enter 2\n")
                elif check==-1:
                    admin=Admin(ad_list[0],ad_list[1],ad_list[2],ad_list[3])
                    self.admins.append(admin)
                    print("new admin added.\n")
                    print("Add another admin: enter 1\nback: enter 2\n")
                check_try=int(input())
                if check_try==2:
                    break
                elif check_try==1:
                    continue
            except:
                print("something wrong,Try again.")

    def change_user_password(self):
        try:
            change_info=input("Enter old username and password:\n Example format: username,password\n")
            change_list=change_info.split(",")
            check=self.verify_admin(change_list[0],change_list[1])
            if check==-1:
                print("The username and password you entered are not exist.\n")
            else:
                while True:
                    change_info1=input("Enter new username and password:\n Example format: username,password\n")
                    change_list1=change_info1.split(",")
                    change_info2=input("Enter new username and password again:\n Example format: username,password\n")
                    change_list2=change_info2.split(",")
                    if change_list1[0]==change_list2[0] and change_list1[1]==change_list2[1]:
                        self.admins[check].username=change_list1[0]
                        self.admins[check].password=change_list1[1]
                        print("username and password updated.\n")
                        break
                    else:
                        print("username or password are not match\n(try again: enter 1)  (back: enter 2)\n")
                        check_try=int(input())
                        if check_try==2:
                            break
                        elif check_try==1:
                            continue
        except:
            print("somthing wrong,Try again.")



    def add_book(self,book_obj):
        try:
            book_info= input("Enter information of new book:\n Example format:\n name,author,language,field,publication_date,unique_ID,number_of_book_in_library\n ")
            info= book_info.split(",")
            index=book_obj.check_id(info[5])
            if index==-1:
                book= Book(info[0],info[1],info[2],info[3],info[4],info[5],int(info[6]))
                book_obj.booklist.append(book)
                print("book added successfully\n")
            else:
                print("The unique ID is already exist.\n")
        except:
            print("somthing wrong,Try again.")

    def edit_book(self,book_obj,edit_obj,index_admin,date):
        id=input("enter the ID of book you want to edit\n")
        edit_part=""
        index=book_obj.check_id(id)
        if index != -1:
            try:
                new_book_info=input("enter new information of book: \nexample format: name,author,language,field,publication_date,unique_ID,number_of_book_in_library\n")
                info_book=new_book_info.split(",")
                # book_obj.booklist[index].name = info_book[0] or book_obj.booklist[index].name
                # book_obj.booklist[index].author = info_book[1] or book_obj.booklist[index].author
                # book_obj.booklist[index].language = info_book[2] or book_obj.booklist[index].language
                # book_obj.booklist[index].field = info_book[3] or book_obj.booklist[index].field
                # book_obj.booklist[index].publication_date = info_book[4] or book_obj.booklist[index].publication_date
                # book_obj.booklist[index].unique_ID = info_book[5] or book_obj.booklist[index].unique_ID
                # book_obj.booklist[index].number_of_book_in_library = info_book[6] or book_obj.booklist[index].number_of_book_in_library
                if info_book[0]!="":
                    edit_part=edit_part+f"(name:{book_obj.booklist[index].name}=>{info_book[0]})-"
                    book_obj.booklist[index].name = info_book[0]
                if info_book[1]!="":
                    edit_part=edit_part+f"(author:{book_obj.booklist[index].author}=>{info_book[1]})-"
                    book_obj.booklist[index].author = info_book[1]
                if info_book[2]!="":
                    edit_part=edit_part+f"(language:{book_obj.booklist[index].language}=>{info_book[2]})-"
                    book_obj.booklist[index].language = info_book[2]
                if info_book[3]!="":
                    edit_part=edit_part+f"(field:{book_obj.booklist[index].field}=>{info_book[3]})-"
                    book_obj.booklist[index].field = info_book[3]
                if info_book[4]!="":
                    edit_part=edit_part+f"(publication_date:{book_obj.booklist[index].publication_date}=>{info_book[4]})-"
                    book_obj.booklist[index].publication_date = info_book[4]
                if info_book[5]!="":
                    edit_part=edit_part+f"(unique_ID:{book_obj.booklist[index].unique_ID}=>{info_book[5]})-"
                    book_obj.booklist[index].unique_ID = info_book[5]
                if info_book[6]!="":
                    edit_part=edit_part+f"(number_of_book_in_library:{book_obj.booklist[index].number_of_book_in_library}=>{info_book[6]})"
                    book_obj.booklist[index].number_of_book_in_library = info_book[6]
                if edit_part!="":
                    edit_obj.update_edit_list(self.admins[index_admin].firstname,self.admins[index_admin].lastname,self.admins[index_admin].username,book_obj.booklist[index].name,book_obj.booklist[index].unique_ID,edit_part,date)
                print("Book information updated.\n")
            except Exception as e:
                print(e)
                print("somthing wrong,Try again.")        
        else:
            print('The unique id you entered is not exist\n')

    def remove_book(self,book_obj):
        id=input("enter the ID of book you want to remove\n")
        index=book_obj.check_id(id)
        if index == -1:
            print('The unique id you entered is not exist\n')
        else:
            book_obj.booklist.pop(index)
            print('The book with id you entered is removed successfully.\n')

    def search_book(self,book_obj):
        search_list=[]
        try:
            keyword=int(input("Enter type you want to search:\nbased on name: enter 1\nbased on author: enter 2\n "))
            if keyword==1:
                name=input("Enter the name you want to search:\n")
                for i in book_obj.booklist:
                    if i.name==name:
                        search_list.append(i)
                print(f"search result:\n{len(search_list)}")
                if len(search_list)!=0:
                    for j,i in enumerate(search_list):
                        print(f"{j+1}.{i.unique_ID}===> The number of this book in the library: {i.number_of_book_in_library}")
                    del search_list
            elif keyword==2:
                author=input("Enter the author you want to search:\n")
                for i in book_obj.booklist:
                    if i.author==author:
                        search_list.append(i)
                print(f"search result:\n{len(search_list)}")
                if len(search_list)!=0:
                    for j,i in enumerate(search_list):
                        print(f"{j+1}.{i.unique_ID}===> The number of this book in the library: {i.number_of_book_in_library}")
                    del search_list
            else:
                raise Invalidnumber
        except ValueError:
            print("your input is invalid")
        except Invalidnumber:
            print("your input is invalid")

    def view_books(self,book_obj):
        for i in book_obj.booklist:
            i.show_book_info()