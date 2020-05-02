import sqlite3


database = 'business_card_catalog.db'


def create_db_and_table():
    query = """
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        full_name VARCHAR(30) UNIQUE NOT NULL,
        email VARCHAR(30) UNIQUE NOT NULL,
        age INTEGER NOT NULL,
        phone VARCHAR(10) NOT NULL,
        additional_info TEXT
    );
    """

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(query)

    connection.commit()
    connection.close()


def add():
    name = input('Enter user name: ')
    email = input('Enter email: ')
    age = input('Enter age: ')
    phone = input('Enter phone: ')
    additional = input('Enter addional info (optional): ')

    query = """
    INSERT INTO Users (full_name, email, age, phone, additional_info)
    VALUES(?, ?, ?, ?, ?);
    """

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(query, (name, email, age, phone, additional if additional != '' else "NULL"))

    connection.commit()
    connection.close()


def list_():
    print('##############')
    print('###Contacts###')
    print('##############')

    query = """
    SELECT * FROM Users;
    """

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(query)

    for contact in cursor.fetchall():
        print(f'ID: {contact[0]}, Email: {contact[2]}, Full name: {contact[1]}')

    cursor.execute(query)

    connection.close()


def get():
    id = input('Enter id: ')

    query = f"""
    SELECT * FROM Users WHERE id = {id};
    """

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(query)

    contact = cursor.fetchone()

    print('\nContact info:\n')

    print('###############')
    print(f'Id: {contact[0]}')
    print(f'Full name: {contact[1]}')
    print(f'Email: {contact[2]}')
    print(f'Age: {contact[3]}')
    print(f'Phone: {contact[4]}')
    print(f'Additional info: {contact[5]}')
    print('##############')


def delete():
    id = input('Enter id: ')

    query = f"""
    SELECT * FROM Users WHERE id = {id};
    """

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute(query)

    contact = cursor.fetchone()

    query = """
    DELETE FROM Users WHERE id = ?;
    """

    cursor.execute(query, id)

    connection.commit()
    connection.close()

    print('\nFollowing contact is deleted successfully::\n')

    print('###############')
    print(f'Id: {contact[0]}')
    print(f'Full name: {contact[1]}')
    print(f'Email: {contact[2]}')
    print(f'Age: {contact[3]}')
    print(f'Phone: {contact[4]}')
    print(f'Additional info: {contact[5]}')
    print('##############')


def help_():
    print('#############')
    print('###Options###')
    print('#############\n')

    print('1. `add` - insert new business card')
    print('2. `list` - list all business cards')
    print('3. `delete` - delete a certain business card (`ID` is required)')
    print('4. `get` - display full information for a certain business card (`ID` is required)')
    print('5. `help` - list all available options')
    print('6. `exit` - exit')


def main():
    create_db_and_table()
    print('Hello! This is your business card catalog. What would you like? (enter "help" to list all available options)')
    command = ''
    while command != 'exit':
        command = input('>>> Enter command: ')

        if command == 'add':
            add()
        elif command == 'list':
            list_()
        elif command == 'delete':
            delete()
        elif command == 'get':
            get()
        elif command == 'exit':
            exit()
        elif command == 'help':
            help_()
        else:
            print('Invalid command')


if __name__ == '__main__':
    main()
