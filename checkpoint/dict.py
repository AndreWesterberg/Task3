import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dictionary1",
   user="postgres",
   password="Andre9119"
)

<<<<<<< HEAD
def read_dict(connection):#returns a list with all the words in the database
=======
def read_dict(connection):
>>>>>>> development
    cur = connection.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
<<<<<<< HEAD
def add_word(connection, word, translation): # Add new word
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(connection, ID): #deletes word from database
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(connection): # saves the dictionary
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()
def insert_word(connection, word, translation): # print word without connecting to database
=======
def add_word(connection, word, translation):
    cur = connection.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(connection, ID):
    cur = connection.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(connection):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()
def insert_word(connection, word, translation):
>>>>>>> development
    print(word,translation)

while True: ## REPL - Read Execute Program Loop
    cmd = input("Options add,delete,list,quit,print enter your command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
    elif cmd == "print":
        word = input("  Word: ")
        translation = input("  Translation: ")
        insert_word(conn, word, translation)
        
