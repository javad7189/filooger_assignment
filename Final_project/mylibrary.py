from book import Book


class Mylibrary:
    def __init__(self):
        self.booklist=[]

    def load_books(self):
        with open("D:/filoger/final_project/book.txt",'a+') as file:
            file.seek(0)
            lines=file.readlines()
            for line in lines:
                list1=line.split(",")
                list1[6]=list1[6].replace("\n","")
                book=Book(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],int(list1[6]))
                self.booklist.append(book)
    
    def update_books_database(self):
            with open("D:/filoger/final_project/book.txt",'w') as file:
                for i in self.booklist:
                    file.write(f"{i.name},{i.author},{i.language},{i.field},{i.publication_date},{i.unique_ID},{i.number_of_book_in_library}\n")
                print("book database updated.")


    def check_id(self,id):
        for i,book in enumerate(self.booklist):
            if id==book.unique_ID:
                return i
        return -1
    

    




