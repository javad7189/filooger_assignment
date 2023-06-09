


class Book:
    def __init__(self,name,author,language,field,publication_date,unique_ID,number_of_book_in_library):
        self.name=name
        self.author=author
        self.language=language
        self.field=field
        self.publication_date=publication_date
        self.unique_ID=unique_ID
        self.number_of_book_in_library=number_of_book_in_library

    def show_book_info(self):
        print(50*"-")
        print(f"name: {self.name}")
        print(f"author: {self.author}")
        print(f"language: {self.language}")
        print(f"field: {self.field}")
        print(f"publication_date: {self.publication_date}")
        print(f"unique_ID: {self.unique_ID}")
        print(f"number of book in library: {self.number_of_book_in_library}")