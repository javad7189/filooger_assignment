import re
# importing yagmail and its packages
import yagmail
# define my error
class Invalidnumber(Exception):
    pass

class Person:
    def __init__(self,f_name,l_name):
        self.firstname=f_name
        self.lastname=l_name

    def personal_information(self):
        print(f"first name is: {self.firstname}")
        print(f"last name is: {self.lastname}")


class User(Person):
    def __init__(self,first_name,last_name,email,phone_number,unique_id,borrowed_book,borrowed_time,deadline):
        Person.__init__(self,first_name,last_name)
        self.email=email
        self.phone_number=phone_number
        self.unique_id=unique_id
        self.borrowed_book=borrowed_book
        self.borrowed_time=borrowed_time
        self.deadline=deadline
        self.users=[]


    def reminder_email(self,lib):
        user_deadline_finish=[]
        book_deadline_finish=[]
        for i in self.users:
            for j,deadline in enumerate(i.deadline):
                if deadline==-1:
                    index=lib.check_id(i.borrowed_book[j])
                    book_deadline_finish.append(f"name:{lib.booklist[index].name}-author:{lib.booklist[index].author}")
                    user_deadline_finish.append(i.email)
        for i in range(len(user_deadline_finish)):
            yag = yagmail.SMTP("torang7189@gmail.com",
                            "wiwxpztulbefzowj")
            # Adding Content and sending it
            yag.send(user_deadline_finish[i],
                    "Borrowed deadline expired",
                    f"Deadline for book with below information is expired:\n{book_deadline_finish[i]}\nPlease give it back to library as soon as possible.\nthanks")
            print(f"A reminder email send to {user_deadline_finish[i]} for book {book_deadline_finish[i]}")


    def validat_email(self,s):
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat,s):
            return True
        print("Email is invalid\n")
        return False

    def validat_phone(self,s):
        pat = "^(0|0098|\+98)9(0[1-5]|[1 3]\d|2[0-2]|98)\d{7}$"
        if re.match(pat,s):
            return True
        print("phone number is invalid\n")
        return False
    def show_user_info(self):
        for j in self.users:
            print(50*"-")
            j.personal_information()
            print(f"email: {j.email}")
            print(f"phone_number: {j.phone_number}")
            print(f"unique_ID: {j.unique_id}")
            if len(j.borrowed_book)!=0:
                for i in range(len(j.borrowed_book)):
                    print(f"borrowed_book{i+1}: {j.borrowed_book[i]}",end=",")
                    print(f" borrowed_time: {j.borrowed_time[i]}",end=",")
                    print(f" deadline: {j.deadline[i]}")     
            else:   
                print(f"borrowed_book: 0")    


    def load_users(self):
        with open("D:/filoger/final_project/users.txt",'a+') as file:
            file.seek(0)
            lines=file.readlines()
            # print(lines)
            # if len(lines)==1 and lines[0]=="":
            #     ...
            for line in lines:
                
                list1=line.split(",")
                if len(list1[5])!=0:
                    list1[5]=list1[5].split("+")
                    list1[6]=list1[6].split("+")
                    list1[7]=list1[7].replace("\n","")
                    list1[7]=list1[7].split("+")
                else:
                    list1[7]=list1[7].replace("\n","")
                
                user=User(list1[0],list1[1],list1[2],list1[3],int(list1[4]),list(list1[5]),list(list1[6]),list(list1[7]))
                self.users.append(user)
            if len(lines)==0:
                last_id=99
            else:
                last_id=list1[4]
        return last_id
    
    def update_users_database(self):
            with open("D:/filoger/final_project/users.txt",'w') as file:
                for i in self.users:
                    file.write(f"{i.firstname},{i.lastname},{i.email},{i.phone_number},{i.unique_id},")
                    if len((i.borrowed_book))!=0:
                        for j,book in enumerate(i.borrowed_book):
                            if j==len(i.borrowed_book)-1:
                                file.write(f"{book},")
                            else:
                                file.write(f"{book}+")
                        for j,time in enumerate(i.borrowed_time):
                            if j==len(i.borrowed_time)-1:
                                file.write(f"{time},")
                            else:
                                file.write(f"{time}+")
                        for j,deadline in enumerate(i.deadline):
                            if j==len(i.deadline)-1:
                                file.write(f"{deadline}\n")
                            else:
                                file.write(f"{deadline}+")
                    else:
                        file.write(f",,\n")
                print("users database updated.")


    def update_deadlines(self,date):
        year=int(date[0])
        month=int(date[1])
        day=int(date[2])
        deadline_p=0
        for user in self.users:
            if len(user.borrowed_time)>0:
                for time_index,b_time in enumerate(user.borrowed_time):
                    time_list=b_time.split("/")
                    year_b=int(time_list[0])
                    month_b=int(time_list[1])
                    day_b=int(time_list[2])
                    user.deadline[time_index]=int(user.deadline[time_index])
                    if year-year_b>0 or month-month_b>1:
                        user.deadline[time_index]=-1
                    elif month-month_b==1:
                        if month_b>6:
                            deadline_p=30-day_b+day
                        elif month_b<7:
                            deadline_p=31-day_b+day
                    elif month-month_b==0:
                        deadline_p=day-day_b
                    if deadline_p>10:
                        user.deadline[time_index]=-1
                    elif deadline_p<=10:
                        user.deadline[time_index]-=deadline_p

                     

    def register(self,last_id):
        register_check=0
        while True:
            user_info=input("please enter your information same as template: firstname,lastname,email,phone_number\nBack: enter 3\n")
            if user_info=="3":
                break
            if user_info!="":
                info_list=user_info.split(",")
                if len(info_list)==4:
                    for i in info_list:
                        if i=="":
                            register_check+=1
                    if register_check==0: 
                        e=self.validat_email(info_list[2]);p=self.validat_phone(info_list[3])
                        if e==True and p==True:
                            user_o=User(info_list[0],info_list[1],info_list[2],info_list[3],last_id+1,[],[],[])
                        # print(len(user_o.borrowed_book));print(len(user_o.borrowed_time));print(len(user_o.deadline))
                            self.users.append(user_o)
                            print(f"Your unique id is {last_id+1}. Your registration is complete.\n")
                            break


                    elif register_check>1:
                        print(f"registration failed because {register_check} fields are empty.\n")
                        try:
                            check=int(input("Try again: enter 1\nback: enter 3"))
                            if check==1:
                                register_check=0
                                continue
                            elif check==3:
                                break
                            else:
                                break
                        except:
                            break
                           


    def check_id(self,id):
        for i,user in enumerate(self.users): 
            if id==user.unique_id:
                return i
        return -1        

    def borrow_book(self,book_obj,date,user_index):
        date_list=[]
        borrowed_list=[]
        deadline_list=[]
        while True:
            search_list=[]            
            try:
                search=int(input("search book by name: enter 1\nsearch book by author: enter 2\nback: enter 3\n"))
                if search==1:
                    name=input("Enter the name book:\n")
                    for i in book_obj.booklist:
                        if i.name==name:
                            search_list.append(i)                   
                elif search==2:
                    author=input("Enter the author book:\n")
                    for i in book_obj.booklist:
                        if i.author==author:
                            search_list.append(i) 
                elif search==3:
                    raise Invalidnumber
                else:
                    raise Invalidnumber
                print(f"search result:\n{len(search_list)}")
                if len(search_list)!=0:
                    for j,i in enumerate(search_list):
                        print(f"{j+1}. {i.name}-(author={i.author})-(language={i.language})-(field={i.field})-(publication_date={i.publication_date}) \n===> The inventory of this book in the library: {i.number_of_book_in_library}")
                    try:
                        index_b=int(input("please enter the number that is shown beside the name of book:\n"))
                        if index_b>0 and index_b<len(search_list)+1:
                            if search_list[index_b-1].number_of_book_in_library>0:
                                borrowed_list.append(search_list[index_b-1].unique_ID)
                                date_s=date[0]+'/'+date[1]+'/'+date[2]
                                date_list.append(date_s)
                                deadline_list.append(10)
                                search_list[index_b-1].number_of_book_in_library-=1
                                print(f"{search_list[index_b-1].name} is borrowed by {self.users[user_index].firstname}.")
                            else:
                                print("The inventory of this book is currently zero.")
                        else:
                            print("The number you enter is out of range\n")
                
                    except Exception as e:
                        print(e)
                        print("book number you enter is out of range\n")    
                    del search_list        
            except ValueError:
                if len(borrowed_list)!=0:
                    for i in range(len(borrowed_list)):
                        self.users[user_index].borrowed_book.append(borrowed_list[i])
                        self.users[user_index].borrowed_time.append(date_list[i])
                        self.users[user_index].deadline.append(deadline_list[i])
                    print(f"chosen books are add to {self.users[user_index].firstname}{self.users[user_index].lastname} information\n")
                break
            except Invalidnumber:
                print(borrowed_list)
                print(date_list)
                print(deadline_list)
                if len(borrowed_list)!=0:
                    for i in range(len(borrowed_list)):
                        self.users[user_index].borrowed_book.append(borrowed_list[i])
                        self.users[user_index].borrowed_time.append(date_list[i])
                        self.users[user_index].deadline.append(deadline_list[i])
                    print(f"chosen books are add to {self.users[user_index].firstname}{self.users[user_index].lastname} information\n")
                break
        