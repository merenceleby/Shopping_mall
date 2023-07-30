import sqlite3

con = sqlite3.connect("shopping_mall.db")

cursor = con.cursor()

while True:
    print("""
            Welcome to The Shopping mall

            1 : Music Store
            2 : Movie Store
            3 : Book Store
            4 : Smartphone Store
            5 : Coffee Store
            6 : See all page in one
            else : Exit from the program
            """
            )
    opt = int(input("What is your choice?"))
    if (opt == 1):
        print("""
                1: See All Music CDs
                2: Find by Artist Name and song number in stock
                3: filter by price
                """)
        opt_book = int(input("What is your option?"))
        if (opt_book == 1):
            cursor.execute("Select * From music_store")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif(opt_book == 2):
            cursor.execute("Select Artist, Count (*) as stock_number From music_store group by Artist")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif (opt_book == 3):
            print("enter min/max values")
            mini = int(input("Minimum Price"))
            maxi = int(input("Maximum Price"))
            cursor.execute("Select * From music_store where Price Between ? And ?",(mini,maxi))
            data = cursor.fetchall()
            for i in data:
                print(i)

    elif(opt ==2):
        print("""
                1: See All Movie CDs
                2: Find by Movie Genre
                3: filter by price
                """)
        opt_movie = int(input("What is your option?"))
        if (opt_movie == 1):
            cursor.execute("Select * From movie_store")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif(opt_movie == 2):
            cursor.execute("Select genre, Count (*) as stock_number From movie_store group by genre")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif (opt_movie == 3):
            print("enter min/max values")
            mini = int(input("Minimum Price"))
            maxi = int(input("Maximum Price"))
            cursor.execute("Select * From movie_store where Price Between ? And ?",(mini,maxi))
            data = cursor.fetchall()
            for i in data:
                print(i)
    elif(opt == 3):
        print("""
                1: See All Books
                2: Find by Author
                3: filter by price
                """)
        opt_book= int(input("What is your option?"))
        if (opt_book == 1):
            cursor.execute("Select * From book_store")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif(opt_book == 2):
            cursor.execute("Select author, Count (*) as stock_number From book_store group by author")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif (opt_book == 3):
            print("enter min/max values")
            mini = int(input("Minimum Price"))
            maxi = int(input("Maximum Price"))
            cursor.execute("Select * From book_store where Price Between ? And ?",(mini,maxi))
            data = cursor.fetchall()
            for i in data:
                print(i)
    elif (opt == 4):
        print("""
                1: See All Smartphones
                2: Find by Brands
                3: filter by price
                """)
        opt_smart= int(input("What is your option?"))
        if (opt_smart == 1):
            cursor.execute("Select * From smartphone_store")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif(opt_smart == 2):
            cursor.execute("Select Brand, Count (*) as stock_number From smartphone_store group by Brand")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif (opt_smart == 3):
            print("enter min/max values")
            mini = int(input("Minimum Price"))
            maxi = int(input("Maximum Price"))
            cursor.execute("Select * From smartphone_store where Price Between ? And ?",(mini,maxi))
            data = cursor.fetchall()
            for i in data:
                print(i)
    elif (opt == 5):
        print("""
                1: See All Coffies
                2: Find by kind
                3: filter by price
                """)
        opt_coffee = int(input("What is your option?"))
        if (opt_coffee == 1):
            cursor.execute("Select * From coffee_store")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif(opt_coffee == 2):
            cursor.execute("Select kind, Count (*) as stock_number From coffee_store group by kind")
            data = cursor.fetchall()
            for i in data:
                print(i)
        elif (opt_coffee == 3):
            print("enter min/max values")
            mini = int(input("Minimum Price"))
            maxi = int(input("Maximum Price"))
            cursor.execute("Select * From coffee_store where Price Between ? And ?",(mini,maxi))
            data = cursor.fetchall()
            for i in data:
                print(i)
    elif (opt == 6):
        
        cursor.execute("""
     SELECT t1.name, t1.kind, t1.price,
       t2.name, t2.kind, t2.price
    FROM coffee_store AS t1
    INNEr JOIN movie_store AS t2 ON t1.price = t2.price;


        """)
        data = cursor.fetchall()
        for row in data:
            
            print(row)
        
    else:
        print("Program has been ended")
        break
        
        
        
        








con.close()
                                                       
                                                       
