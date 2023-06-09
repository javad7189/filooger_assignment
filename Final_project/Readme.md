
# Library project with OOP
In these projects I write a library with python.

The library has admins and users.

new user can register in library, and then they can borrow a book.
When a user register in library, he should enter his emai and phone number. I check the phone and email that he entered
and if both email and phone number in valid, the user regitered is finished successfully.
when a user register im library, his information is saved in users.txt file. this file is used as user database.
users can borrow book and see the informatoin of users.


borrowing book has a law. when a user borrow a book, he must give it back to library in 10 days. 
If he doesn't give it back, the library send him an reminder email to remind him that he forgot to return lirary's book.
The information of borrowed books is stored in users.txt file too. books id and borrowed date and remained time to end deadline are stored in front of each user in database. we use this information to send reminder email to users.


default username and password for admins is admin,admin. This means that if there is no admins data in admins database,
the library makes a default username=admin and password=admin automatically.
admins informations stored in admins.txt file.
book information stored in book.txt file.
if you login as admin you can add new admins and you can do below operatios:

add book: enter 1
edit book: enter 2
remove book: enter 3
search book: enter 4
show books: enter 5
add admin:enter 6
change user or password:enter 7
show last edited:enter 8

As you can see, you must enter a number for each operation.
remember: if you edit the information of a book, your task saved automatically in edits.txt file. this file is used as edit database.

## How to install
Run following command :

pip install -r requirements.txt


## How to Run
execute this command in terminal:
python main.py



## Results

We see a picture that I screenshot from my desktop to show my email page.
there are four email that the library send to me to remind me to give back a specific book to library :)

output:











