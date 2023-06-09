from user import Person



class Edit(Person):
    def __init__(self, f_name, l_name,admin_user,book_name,book_id,edit_part,edit_date):
        super().__init__(f_name, l_name)
        self.admin_user=admin_user
        self.book_name=book_name
        self.book_id=book_id
        self.edit_part=edit_part
        self.edit_date=edit_date
        self.edits=[]

    def show_edit_info(self):
        if len(self.edits)!=0:
            for i,j in enumerate(self.edits):
                print(50*"-")
                print(f"Edit{i+1}. The book of {j.book_name} was edited by {j.firstname} {j.lastname} on the {j.edit_date}.\nAdmin username is {j.admin_user}\nBook ID is {j.book_id}")  
                print("edit part is: ") 
                edited_p=j.edit_part.split("-")
                for k in edited_p:
                    print(k)
        else:   
            print("There is not any edit yet.")   

    def load_edits(self):
        with open("D:/filoger/final_project/edits.txt",'a+') as file:
            file.seek(0)
            lines=file.readlines()
            for line in lines:
                list1=line.split(",")
                list1[6]=list1[6].replace("\n","")
                edit=Edit(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6])
                self.edits.append(edit)
    
    def update_edits_database(self):
            with open("D:/filoger/final_project/edits.txt",'w') as file:
                for i in self.edits:
                    file.write(f"{i.firstname},{i.lastname},{i.admin_user},{i.book_name},{i.book_id},{i.edit_part},{i.edit_date}\n")
                print("edit database updated.")       

    def update_edit_list(self,firstname,lastname,admin_user,book_name,book_id,edit_part,edit_date):
        new_edit=Edit(firstname,lastname,admin_user,book_name,book_id,edit_part,edit_date)
        self.edits.append(new_edit)