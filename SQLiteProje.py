import sqlite3
import time


con = sqlite3.connect("APPDATA.db")

cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS USERDATA( Name TEXT , Surname TEXT, Phone INT ,Username TEXT UNIQUE, Password TEXT UNIQUE)")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS FAVOURITE(Book_name TEXT , Author TEXT, Publisher TEXT , Page_count INT)")
con.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS LIBRARY(Book_name TEXT , Author TEXT, Publisher TEXT , Page_count INT)")
con.commit()

def delete_book(book_name):
    try:
        cursor.execute("Delete From LIBRARY  WHERE  Book_name = ?",(book_name,))
        cursor.execute("DELETE FROM FAVOURITE WHERE Book_name = ?", (book_name,))
        con.commit()
        print("\033[034mThe book was successfully deleted.\033[0m ")
    except  Exception as e :
        con.rollback()
        print("An error occurred: ", e)    
        

def update_book_name(old_book_name,  new_book_name):
    try:
        cursor.execute("UPDATE LIBRARY SET Book_name = ? WHERE Book_name = ?",( old_book_name, new_book_name))
        cursor.execute("UPDATE FAVOURITE SET Book_name = ? WHERE Book_name = ?",( old_book_name, new_book_name))
        con.commit()
        print("\033[034mThe author's name was successfully updated.\033[0m")
    except Exception as e:
        con.rollback()
        print("An error occurred: ", e)

def update_author(book_name, old_author_name, new_author_name):
    try:
        cursor.execute("UPDATE LIBRARY SET Author = ? WHERE Book_name = ? AND Author = ?",(new_author_name, book_name, old_author_name))
        cursor.execute("UPDATE FAVOURITE SET Author = ? WHERE Book_name = ? AND Author = ?",(new_author_name, book_name, old_author_name))
        con.commit()
        print("\033[034mThe author's name was successfully updated.\033[0m")
    except Exception as e:
        con.rollback()
        print("An error occurred while updating the information, please try again: ", e)

def update_publisher(book_name, old_publisher, new_publisher):
    try:
        cursor.execute("UPDATE LIBRARY SET Publisher = ? WHERE Book_name = ? AND Publisher = ?",(new_publisher, book_name, old_publisher))
        cursor.execute("UPDATE FAVOURITE SET Publisher = ? WHERE Book_name = ? AND Publisher = ?",(new_publisher, book_name, old_publisher))
        con.commit()
        print("\033[034mThe publisher's name was successfully updated.\033[0m")
    except Exception as e:
        con.rollback()
        print("An error occurred while updating the information, please try again: ", e)

def update_page_count(book_name, old_page_count, new_page_count):
    try:
        cursor.execute("UPDATE LIBRARY SET Page_count = ? WHERE Book_name = ? AND Page_count = ?",(new_page_count,book_name, new_page_count))
        cursor.execute("UPDATE FAVOURITE SET Page_count = ? WHERE Book_name = ? AND Page_count = ?",(new_page_count, book_name,  new_page_count))
        con.commit()
        print("\033[034mThe page count was successfully updated.\033[0m")
    except Exception as e:
        con.rollback()
        print("An error occurred while updating the information, please try again: ", e)

def check_book_library(book_name):
    try:
        cursor.execute("SELECT 1 FROM LIBRARY WHERE Book_name = ?", (book_name,))
        result = cursor.fetchone()
        if result:
            print("The book exists in the database.")
            return True
        else:
            print("The book does not exist in the database.")
            return False
    except  Exception as e:
        print(f"An error occurred: {e}")
        return False   

def check_book_favourite(book_name):
    try:
        cursor.execute("SELECT 1 FROM FAVOURITE WHERE Book_name = ?", (book_name,))
        result = cursor.fetchone()
        if result:
            print("The book exists in the database.")
            return True
        else:
            print("The book does not exist in the database.")
            return False
    except  Exception as e:
        print(f"An error occurred: {e}")
        return False   

def add_favourite(book_name,author,publisher,page_count):
    try :
        cursor.execute("Insert into FAVOURITE Values(?,?,?,?)",(book_name,author,publisher,page_count))
        con.commit()
        print("\033[034mThe book was successfully added to the favorites.\033[0m ")
    except  Exception as e :
        con.rollback()
        print("An error occurred: ", e)
        
        
def add_library(book_name,author,publisher,page_count):
    try :
        cursor.execute("Insert into LIBRARY Values(?,?,?,?)",(book_name,author,publisher,page_count))
        con.commit()
        print("\033[034mThe book was successfully added to the library.\033[0m ")
    except  Exception as e :
        con.rollback()
        print("An error occurred: ", e)

def add(name,surname,phone,username,password):
    try:
        cursor.execute("Insert into USERDATA values(?,?,?,?,?)",(name,surname,phone,username,password))
        con.commit()
    except sqlite3.IntegrityError:
        print("\033[31mUsername already exists. Please try another.\033[0m")

def check_login(username, password):
    cursor.execute("SELECT Password FROM USERDATA WHERE Username = ?", (username,))
    result = cursor.fetchone()
    
    if result is None:
        print("\033[31mError: Username not found.\033[0m")
        return False
    elif result[0] == password:
        print("\033[32mLogin successful!\033[0m")
        return True
    else:
        print("\033[31mError: Incorrect password.\033[0m")
        return False

def chcek_choice1(choice):
    try:
        if choice == 1 :
            return True
    except   Exception as e :
         print("An error occurred: ", e)
                     
def chcek_choice2(choice):
    try:
        if choice == 2 :
            return True
    except   Exception as e :
         print("An error occurred: ", e)

def chcek_choice3(choice):
    try:
        if choice == 3 :
            return True
    except   Exception as e :
         print("An error occurred: ", e)
                  
while True:
    print("**********WELLCOME**********")
    print("1-LOG IN \n2-SIGN UP \n3-EXIT")
    try:
        choice = int(input("Choice: "))  
    except ValueError:  
        print("Invalid input. Please enter a number between 1 and 3.")
        continue 
    
    if choice == 3 :
        print("Exiting the program.",flush=True)
        for i in range(5):
            print( end=".", flush= True)
            time.sleep(1)
        break
    
    if choice == 1 :
        while True:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if check_login(username, password):
                
                break  
            else:
                print("Incorrect username or password. Please try again.")
        
        
        while True:
            print("**********WELLCOME**********")
            print("1-Add a book \n2-Delete a Book \n3-Edit a Book \n4-Search Books \n5-Add to Favorites \n6-EXIT")
            try:
                choice2 = int(input("Enter your choice: "))
            except ValueError : 
                print("Invalid input. Please enter a number between 1 and 6.")
                continue 
            if choice2 == 1:
                print("\033[034m-->Enter the book information you want to save.\033[0m")
                while True:
                    try:
                        book_name =input("Book Name: ")
                        author = input("Author: ")
                        publisher = input("Publisher: ")
                        page_count = int(input("Page Count: "))
                        add_library(book_name,author,publisher,page_count)
                        break
                    except ValueError :
                        print("Invalid input.Please try again.") 
                        continue                   
            elif choice2 == 2 :
                print("\033[034m-->Enter the name of the book you want to delete.\033[0m ")
                book_name = input("Book Name: ")
                delete_book(book_name)
            elif choice2 == 3 :
                print("\033[034m-->Select the book information you want to change\033[0m")
                print("1-Book Name \n2-Author \n3-Publisher \n4-Page Count ")
                choice3 = int(input("Enter your choice: "))
                if choice3 == 1:
                    old_book_name = input("Old Book Name: ")
                    new_book_name = input("New Book Name: ")
                    update_book_name(old_book_name,new_book_name)
                
                elif choice3 == 2 :
                    book_name = input("Book Name: ")
                    while True:    
                        try:    
                            old_author_name = input("Old Author: ")
                            new_author_name = input("New Author: ")
                            update_author(book_name,old_author_name,new_author_name)
                            break 
                        except ValueError: 
                            print("Invalid input.Please enter a name.")
                            continue
                elif choice3 == 3 :
                   book_name = input("Book Name: ")
                   old_publisher = input("Old Publisher: ")
                   new_publisher = input("New Publisher: ")
                   update_publisher(book_name,old_publisher,new_publisher)
                    
                elif choice3 == 4 :
                    while True:     
                        try:                
                            book_name = input("Book Name: ")
                            old_page_count = input("Old Page Count: ")
                            new_page_count = input("New Page Count: ")
                            update_page_count(book_name, old_page_count, new_page_count)
                            break
                        except ValueError :
                            print("Invalid input.Please enter a number.")
                            continue
            elif choice2 == 4 :
                book_name = input("Book Name: ")
                check_book_library(book_name)
                check_book_favourite(book_name)
                
            elif choice2 == 5:
                    print("\033[034m-->Enter the book information you want to save.\033[0m")
                    while True:    
                        try:
                            book_name =input("Book Name: ")
                            author = input("Author: ")
                            publisher = input("Publisher: ")
                            page_count = int(input("Page Count: "))
                            add_favourite(book_name,author,publisher,page_count)           
                            break
                        except ValueError:
                            print("Invalid input.Please try again.") 
                            continue            
            elif choice2 == 6 :
                print("Exiting the program.",flush=True)
                for i in range(5):
                    print( end=".", flush= True)
                    time.sleep(1)
                break
                        
    elif choice == 2 :
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        phone = input("Enter your phone: ")
        
        print("!Create a username! \n!It must consist of letters and numbers!")
        username = input("Username: ")
        while not username.isalnum():  
            print("\033[031m!!!Username must consist of only letters and numbers!!!\033[0m")
            username = input("Username: ")

        print("\033[34mUsername has been created successfully..\033[0m")
        print(f"Username: {username}")
                    
        print("!Create a password! \n!!It must consist of only numbers!!")
        password = input("Password: ")
        if password.isdigit():
           print("\033[34mPassword has been created successfully..\033[0m")
           print(f"Password: {password}")
        else :
            while not  password.isdigit():
                print("\033[031m!!!It must consist of only numbers!!!\033[0m")
                username = input("Password: ")
                if username.isdigit():
                    print("\033[34mPassword has been created successfully..\033[0m")
                    print(f"Password: {password}")
                    break
        add(name,surname,phone,username,password)                    
                      



