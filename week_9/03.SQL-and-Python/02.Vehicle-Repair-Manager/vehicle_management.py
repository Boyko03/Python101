import sqlite3


database = 'vehicle_management.db'


def create_tables():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS BaseUser(
        id INTEGER PRIMARY KEY,
        user_name VARCHAR(20),
        email VARCHAR(30),
        phone_number INTEGER,
        address VARCHAR(30)
    );

    CREATE TABLE IF NOT EXISTS Client(
        base_id INTEGER,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    );

    CREATE TABLE IF NOT EXISTS Mechanic(
        base_id INTEGER,
        title VARCHAR(20),
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    );

    CREATE TABLE IF NOT EXISTS Vehicle(
        id INTEGER PRIMARY KEY,
        category VARCHAR(20),
        make VARCHAR(20),
        model VARCHAR(20),
        register_number VARCHAR(8),
        gear_box VARCHAR(20),
        owner INTEGER,
        FOREIGN KEY(owner) REFERENCES Client(base_id)
    );

    CREATE TABLE IF NOT EXISTS Service(
        id INTEGER PRIMARY KEY,
        name VARCHAR(20)
    );

    CREATE TABLE IF NOT EXISTS MechanicService(
        id INTEGER PRIMARY KEY,
        mechanic_id INTEGER,
        service_id INTEGER,
        FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id),
        FOREIGN KEY(service_id) REFERENCES Service(id)
    );

    CREATE TABLE IF NOT EXISTS RepairHour(
        id INTEGER PRIMARY KEY,
        date VARCHAR(10),
        start_hour VARCHAR(5),
        vehicle INTEGER,
        bill REAL,
        mechanic_service INTEGER,
        FOREIGN KEY(vehicle) REFERENCES Vehicle(id),
        FOREIGN KEY(mechanic_service) REFERENCES Mechanic_services(id)
    );
    """

    cursor.executescript(query)

    connection.commit()
    connection.close()


class BaseUser:
    def __init__(self, name):
        self.name = name

    def exists(self):
        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        query = """
        SELECT id FROM BaseUser WHERE user_name = ?;
        """

        cursor.execute(query, (self.name, ))

        return cursor.fetchone()

    def create_user(self):
        user_type = ''
        while user_type.lower() not in ['client', 'mechanic']:
            print('Are you a client or mechanic?')
            user_type = input('>>> ')

        user_type = user_type.lower()

        print('Provide user_name:')
        name = input('>>> ')

        print('Provide phone_number:')
        phone = input('>>> ')

        print('Provide email:')
        email = input('>>> ')

        print('Provide address:')
        address = input('>>> ')

        query = """
        INSERT INTO BaseUser
        (user_name, email, phone_number, address)
        VALUES(?, ?, ?, ?);
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (name, email, phone, address))

        query = """
        SELECT id FROM BaseUser ORDER BY id DESC LIMIT 1;
        """
        cursor.execute(query)
        user_id = cursor.fetchone()[0]

        query = """
        INSERT INTO {user_type} (base_id) VALUES(?);
        """.format(user_type=user_type)
        cursor.execute(query, (user_id, ))

        connection.commit()
        connection.close()

        print(f'\nThank you, {name}!')
        print('Welcome to Vehicle Services!')
        print('Next time you try to login, provide your user_name!')

        if user_type == 'client':
            return Client(self.name, user_id)
        else:
            return Mechanic(self.name, user_id)

    def get_type(self):
        query = """
        SELECT base_id
        FROM Client
        JOIN BaseUser ON Client.base_id = BaseUser.id
        WHERE BaseUser.user_name = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (self.name, ))
        result = cursor.fetchone()
        if result is not None:
            return ('client', result[0])
        else:
            query = """
            SELECT base_id
            FROM Mechanic
            JOIN BaseUser ON Mechanic.base_id = BaseUser.id
            WHERE BaseUser.user_name = ?;
            """
            cursor.execute(query, (self.name, ))
            result = cursor.fetchone()
            return ('mechanic', result[0])

        connection.close()

    @staticmethod
    def draw_table(header, titles):
        widths = [len(cell) for cell in header]
        for row in titles:
            for i, cell in enumerate(row):
                widths[i] = max(len(str(cell)), widths[i])

        formatted_row = ' '.join('| {:%d}' % width for width in widths)

        line = [f"+{'-' * (width + 2)}" for width in widths]
        line += '+'
        line = ''.join(line)
        print(line)
        print(formatted_row.format(*header), end=' |\n')
        print(line)
        for row in titles:
            print(formatted_row.format(*row), end=' |\n')
            print(line)

    @staticmethod
    def list_all_free_hours():
        query = """
        SELECT id, date, start_hour FROM RepairHour WHERE vehicle IS NULL;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query)

        all_free_hours = cursor.fetchall()

        header = ("id", "date", "start_hour")

        if all_free_hours is not None and all_free_hours != []:
            BaseUser.draw_table(header, all_free_hours)
        else:
            print('No free hours')

        connection.close()

    @staticmethod
    def list_free_hours(date):
        query = """
        SELECT id, date, start_hour
        FROM RepairHour
        WHERE vehicle IS NULL AND date = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (date, ))

        free_hours = cursor.fetchall()

        header = ("id", "date", "start_hour")

        if free_hours is None or free_hours == []:
            print(f'No free hours on {date}')
        else:
            BaseUser.draw_table(header, free_hours)

        connection.close()


class Client(BaseUser):
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id

    def save_repair_hour(self, hour_id):
        query = """
        SELECT vehicle FROM RepairHour WHERE id = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (hour_id, ))
        vehicle = cursor.fetchone()

        if vehicle[0] is not None:
            print('This hour is already saved.')
            return

        query = """
        SELECT id, make, model, register_number FROM Vehicle WHERE owner = ?
        """

        cursor.execute(query, (self.id, ))
        vehicles = cursor.fetchall()

        if vehicles is None or vehicles == []:
            print('You need a vehicle to save a repair hour.')
            return
        else:
            print('Choose Vehicle to repair:')
            header = ("id", "vehicle")
            if type(vehicles) != tuple:
                for i, row in enumerate(vehicles):
                    vehicles[i] = (vehicles[i][0], f"{' '.join(vehicles[i][1:3])} with RegNumber: {vehicles[i][3]}")
            else:
                vehicles = [(vehicles[0], f"{' '.join(vehicles[1:3])} with RegNumber: {vehicles[i][3]}")]

            Client.draw_table(header, vehicles)

        vehicle_id = input('>>> ')

        print('Choose Service:')
        query = """
        SELECT * FROM Service;
        """

        cursor.execute(query)

        services = cursor.fetchall()
        if services is None or services == []:
            print('Curently no services are available')
            return
        else:
            header = ("id", "Services")

            Client.draw_table(header, services)

        service_id = input('>>> ')

        # Get service date and hour
        query = """
        SELECT date, start_hour FROM RepairHour WHERE id = ?;
        """
        cursor.execute(query, (hour_id, ))
        hour = cursor.fetchone()

        # Get service name
        query = """
        SELECT name FROM Service WHERE id = ?;
        """
        cursor.execute(query, (service_id, ))
        service = cursor.fetchone()

        # Get mechanic_service id
        query = """
        SELECT id FROM MechanicService WHERE service_id = ? LIMIT 1;
        """
        cursor.execute(query, (service_id, ))
        mechanic_service_id = cursor.fetchone()[0]

        # Get vehicle make, model, register number and id
        query = """
        SELECT make, model, register_number, id FROM Vehicle WHERE id = ?;
        """
        cursor.execute(query, (vehicle_id, ))
        vehicle = cursor.fetchone()

        # Write service into db
        query = """
        UPDATE RepairHour SET vehicle = ?, mechanic_service = ? WHERE id = ?;
        """
        cursor.execute(query, (vehicle[3], mechanic_service_id, hour_id))

        print(f'Thank you! You saved an hour on {hour[0]} at {hour[1]} for {service[0]}!')
        print(f'Vehicle: {vehicle[0]} {vehicle[1]} with RegNumber: {vehicle[2]}')

        connection.commit()
        connection.close()

    def update_repair_hour(self, hour_id):
        query = """
        SELECT
            date,
            start_hour,
            Vehicle.make,
            Vehicle.model,
            Vehicle.register_number
        FROM RepairHour
        JOIN Vehicle ON RepairHour.vehicle = Vehicle.id
        WHERE RepairHour.id = ? AND vehicle IS NOT NULL;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (hour_id, ))

        repair_hour = cursor.fetchone()
        if repair_hour is None or repair_hour == []:
            print('Invalid hour id.')
            return

        print(f'You have saved an hour for {repair_hour[0]} at {repair_hour[1]}')
        print(f'Vehicle: {repair_hour[2]} {repair_hour[3]} with RegNumber: {repair_hour[4]}')
        print('Are you sure you want to update this hour?')
        answer = ''
        while answer not in ['y', 'yes', 'n', 'no']:
            answer = input('>>> ').lower()

        if answer in ['y', 'yes']:
            while True:
                print('Choose one of the following:')
                print('1 - Change vehicle')
                print('2 - Change service')
                print('3 - Return to main menu')

                command = ''
                while command not in ['1', '2', '3']:
                    command = input('>>> ')

                if command == '1':
                    query = """
                    SELECT id, make, model, register_number
                    FROM Vehicle
                    WHERE owner = ?;
                    """

                    connection = sqlite3.connect(database)
                    cursor = connection.cursor()

                    cursor.execute(query, (self.id, ))
                    vehicles = cursor.fetchall()

                    if vehicles is None or vehicles == []:
                        print('You need a vehicle to save a repair hour.')
                        return
                    else:
                        print('Choose Vehicle to repair:')
                        header = ("id", "vehicle")
                        if type(vehicles) != tuple:
                            for i, row in enumerate(vehicles):
                                vehicles[i] = (vehicles[i][0], f"{' '.join(vehicles[i][1:3])} with RegNumber: {vehicles[i][3]}")
                        else:
                            vehicles = [(vehicles[0], f"{' '.join(vehicles[1:3])} with RegNumber: {vehicles[i][3]}")]

                        Client.draw_table(header, vehicles)

                        vehicle_id = input('>>> ')

                        query = """
                        UPDATE RepairHour
                        SET vehicle = ?
                        WHERE id = ?;
                        """

                        cursor.execute(query, (vehicle_id, hour_id))
                elif command == '2':
                    print('Choose Service:')
                    query = """
                    SELECT * FROM Service;
                    """

                    cursor.execute(query)

                    services = cursor.fetchall()
                    if services is None or services == []:
                        print('Curently no services are available')
                        return
                    else:
                        header = ("id", "Services")

                        Client.draw_table(header, services)

                    service_id = input('>>> ')

                    query = """
                    SELECT id
                    FROM MechanicService
                    WHERE service_id = ? LIMIT 1;
                    """
                    cursor.execute(query, (service_id, ))
                    mechanic_service_id = cursor.fetchone()[0]

                    query = """
                    UPDATE RepairHour
                    SET mechanic_service = ?
                    WHERE id = ?;
                    """
                    cursor.execute(query, (mechanic_service_id, hour_id))
                else:
                    break

        connection.commit()
        connection.close()

    def delete_repair_hour(self, hour_id):
        query = """
        SELECT date, start_hour
        FROM RepairHour
        WHERE id = ? AND vehicle IS NOT NULL;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (hour_id, ))

        repair_hour = cursor.fetchone()
        if repair_hour is None or repair_hour == []:
            print('Invalid hour id.')
            return

        print(f'You have saved an hour on {repair_hour[0]} at {repair_hour[1]}')
        print('Are you sure you want to delete this hour?')
        answer = ''
        while answer not in ['y', 'yes', 'n', 'no']:
            answer = input('>>> ').lower()

        if answer in ['y', 'yes']:
            query = """
            UPDATE RepairHour
            SET vehicle = NULL,
            mechanic_service = NULL
            WHERE id = ?;
            """

            cursor.execute(query, (hour_id, ))

        connection.commit()
        connection.close()

    def list_personal_vehicles(self):
        query = """
        SELECT id, make, model, register_number FROM Vehicle WHERE owner = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (self.id, ))
        vehicles = cursor.fetchall()

        if vehicles is None or vehicles == []:
            print('You need do not have any vehicles.')
            return
        else:
            print('Choose Vehicle to repair:')
            header = ("id", "vehicle")

            if type(vehicles) != tuple:
                for i, row in enumerate(vehicles):
                    vehicles[i] = (vehicles[i][0], ' '.join(vehicles[i][1:]))
            else:
                vehicles = [(vehicles[0], ' '.join(vehicles[1:]))]

            Client.draw_table(header, vehicles)

    def add_vehicle(self):
        print('Vehicle category:')
        category = input('>>> ')

        print('Vehicle make:')
        make = input('>>> ')

        print('Vehicle model:')
        model = input('>>> ')

        print('Vehicle register number:')
        register_number = input('>>> ')

        print('Vehicle gear box:')
        gear_box = input('>>> ')

        query = """
        INSERT INTO Vehicle
        (category, make, model, register_number, gear_box, owner)
        VALUES(?, ?, ?, ?, ?, ?)
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (category, make, model, register_number, gear_box, self.id))

        connection.commit()
        connection.close()

    def update_vehicle(self, vehicle_id):
        query = """
        SELECT category, make, model, register_number, gear_box
        FROM Vehicle
        WHERE id = ? AND owner = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (vehicle_id, self.id))
        vehicle = cursor.fetchone()

        if vehicle is None or vehicle == []:
            print('Invalid input. You do not have that vehicle.')
            return

        while True:
            query = """
            SELECT category, make, model, register_number, gear_box
            FROM Vehicle
            WHERE id = ? AND owner = ?;
            """
            cursor.execute(query, (vehicle_id, self.id))
            vehicle = cursor.fetchone()

            print(f'Vehicle category: {vehicle[0]}')
            print(f'Vehicle make: {vehicle[1]}')
            print(f'Vehicle model: {vehicle[2]}')
            print(f'Vehicle register number: {vehicle[3]}')
            print(f'Vehicle gear box: {vehicle[4]}\n')

            print('Choose one of the following:')
            print('1 - change vehicle category')
            print('2 - change vehicle make')
            print('3 - change vehicle model')
            print('4 - change vehicle register number')
            print('5 - change vehicle gear box')
            print('6 - return to main menu')

            command = ''
            while command not in ['1', '2', '3', '4', '5', '6']:
                command = input('>>> ')

            if command == '1':
                print(f'Vehicle category is {vehicle[0]}')
                print('Enter new category:')
                new_category = input('>>> ')

                query = """
                UPDATE Vehicle
                SET category = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_category, vehicle_id))
            elif command == '2':
                print(f'Vehicle make is {vehicle[1]}')
                print('Enter new make:')
                new_make = input('>>> ')

                query = """
                UPDATE Vehicle
                SET make = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_make, vehicle_id))
            elif command == '3':
                print(f'Vehicle model is {vehicle[2]}')
                print('Enter new model:')
                new_model = input('>>> ')

                query = """
                UPDATE Vehicle
                SET model = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_model, vehicle_id))
            elif command == '4':
                print(f'Vehicle register number is {vehicle[3]}')
                print('Enter new register number:')
                new_reg_number = input('>>> ')

                query = """
                UPDATE Vehicle
                SET register_number = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_reg_number, vehicle_id))
            elif command == '5':
                print(f'Vehicle gear box is {vehicle[4]}')
                print('Enter new gear box:')
                new_gear_box = input('>>> ')

                query = """
                UPDATE Vehicle
                SET gear_box = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_gear_box, vehicle_id))
            else:
                break

            connection.commit()

        connection.commit()
        connection.close()

    def delete_vehicle(self, vehicle_id):
        query = """
        SELECT category, make, model, register_number, gear_box
        FROM Vehicle
        WHERE id = ? AND owner = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (vehicle_id, self.id))
        vehicle = cursor.fetchone()

        if vehicle is None or vehicle == []:
            print('Invalid input. You do not have that vehicle.')
            return

        print(f'Vehicle category: {vehicle[0]}')
        print(f'Vehicle make: {vehicle[1]}')
        print(f'Vehicle model: {vehicle[2]}')
        print(f'Vehicle register number: {vehicle[3]}')
        print(f'Vehicle gear box: {vehicle[4]}\n')

        answer = ''
        print('Are you sure you want to delete this vehicle?')
        while answer not in ['y', 'n', 'yes', 'no']:
            answer = input('>>> ').lower()

        if answer == 'y' or answer == 'yes':
            query = """
            DELETE FROM Vehicle
            WHERE id = ?;
            """

            cursor.execute(query, (vehicle_id, ))
        else:
            print('Vehicle has not been deleted.')

        connection.commit()
        connection.close()

    def listen(self):
        while True:
            Client.print_options()
            command = input('command> :').lower()
            if command == 'list_all_free_hours':
                Client.list_all_free_hours()
            elif 'list_free_hours' in command:
                if len(command.split(' ')) == 2:
                    Client.list_free_hours(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif 'save_repair_hour' in command:
                if len(command.split(' ')) == 2:
                    self.save_repair_hour(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif 'update_repair_hour' in command:
                if len(command.split(' ')) == 2:
                    self.update_repair_hour(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif 'delete_repair_hour' in command:
                if len(command.split(' ')) == 2:
                    self.delete_repair_hour(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif command == 'list_personal_vehicles':
                self.list_personal_vehicles()
            elif command == 'add_vehicle':
                self.add_vehicle()
            elif 'update_vehicle' in command:
                if len(command.split(' ')) == 2:
                    self.update_vehicle(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif 'delete_vehicle' in command:
                if len(command.split(' ')) == 2:
                    self.delete_vehicle(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif command == 'exit':
                exit()
            else:
                print('Invalid command')

    @staticmethod
    def print_options():
        print('\nYou can choose from the following commands:')
        print('list_all_free_hours')
        print('list_free_hours <date>')
        print('save_repair_hour <hour_id>')
        print('update_repair_hour <hour_id>')
        print('delete_repair_hour <hour_id>')
        print('list_personal_vehicles')
        print('add_vehicle')
        print('update_vehicle <vehicle_id>')
        print('delete_vehicle <vehicle_id>')
        print('exit\n')


class Mechanic(BaseUser):
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id

    def listen(self):
        while True:
            Mechanic.print_options()
            command = input('command> :').lower()
            if command == 'list_all_free_hours':
                Mechanic.list_all_free_hours()
            elif 'list_free_hours' in command:
                if len(command.split(' ')) == 2:
                    Mechanic.list_free_hours(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif command == 'list_all_busy_hours':
                self.list_all_busy_hours()
            elif 'list_busy_hours' in command:
                if len(command.split(' ')) == 2:
                    self.list_busy_hours(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif command == 'add_new_repair_hour':
                self.add_new_repair_hour()
            elif command == 'add_new_service':
                self.add_new_service()
            elif 'update_repair_hour' in command:
                if len(command.split(' ')) == 2:
                    self.update_repair_hour(command.split(' ')[1])
                else:
                    print('Invalid command')
            elif command == 'exit':
                exit()
            else:
                print('Invalid command')

    def list_all_busy_hours(self):
        query = """
        SELECT RepairHour.id, date, start_hour FROM RepairHour
        JOIN MechanicService
            ON RepairHour.mechanic_service = MechanicService.id
        WHERE vehicle IS NOT NULL AND MechanicService.mechanic_id = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (self.id, ))
        result = cursor.fetchall()

        header = ("id", "date", "start_hour")

        if result is not None and result != []:
            Mechanic.draw_table(header, result)
        else:
            print('There are no busy hours now.')

        connection.close()

    def list_busy_hours(self, date):
        query = """
        SELECT RepairHour.id, date, start_hour FROM RepairHour
        JOIN MechanicService
            ON RepairHour.mechanic_service = MechanicService.id
        WHERE
            vehicle IS NOT NULL
            AND date = ?
            AND MechanicService.mechanic_id = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (date, self.id))
        result = cursor.fetchall()

        header = ("id", "date", "start_hour")

        if result is not None and result != []:
            Mechanic.draw_table(header, result)
        else:
            print(f'There are no busy hours on {date}.')

        connection.close()

    def add_new_repair_hour(self):
        print('Repair hour date:')
        date = input('>>> ')

        print('Start Hour:')
        hour = input('>>> ')

        query = """
        INSERT INTO RepairHour (date, start_hour) VALUES(?, ?)
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (date, hour))

        connection.commit()
        connection.close()

    def add_new_service(self):
        print('Provide New service name:')
        service_name = input('>>> ')

        query = """
        SELECT id FROM Service WHERE name = ? LIMIT 1;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (service_name, ))
        service_id = cursor.fetchone()

        if service_id is None:
            query = """
            INSERT INTO Service (name) VALUES(?);
            """

            cursor.execute(query, (service_name, ))

            query = """
            SELECT id FROM Service WHERE name = ? LIMIT 1;
            """
            cursor.execute(query, (service_name, ))
            service_id = cursor.fetchone()[0]

        query = """
        SELECT id
        FROM MechanicService
        WHERE mechanic_id = ? AND service_id = ?;
        """

        cursor.execute(query, (self.id, service_id))
        result = cursor.fetchone()

        if result is None:
            query = """
            INSERT INTO MechanicService (mechanic_id, service_id)
            VALUES(?, ?);
            """

            cursor.execute(query, (self.id, service_id))

        connection.commit()
        connection.close()

    def update_repair_hour(self, hour_id):
        query = """
        SELECT
            RepairHour.date,
            RepairHour.start_hour,
            BaseUser.user_name,
            Vehicle.make,
            Vehicle.model,
            RepairHour.bill
        FROM RepairHour
        JOIN Vehicle ON RepairHour.vehicle = Vehicle.id
        JOIN Client ON Vehicle.owner = Client.base_id
        Join BaseUser ON Client.base_id = BaseUser.id
        WHERE RepairHour.id = ?;
        """

        connection = sqlite3.connect(database)
        cursor = connection.cursor()

        cursor.execute(query, (hour_id, ))

        result = cursor.fetchone()

        while True:
            query = """
            SELECT
                RepairHour.date,
                RepairHour.start_hour,
                BaseUser.user_name,
                Vehicle.make,
                Vehicle.model,
                RepairHour.bill
            FROM RepairHour
            JOIN Vehicle ON RepairHour.vehicle = Vehicle.id
            JOIN Client ON Vehicle.owner = Client.base_id
            Join BaseUser ON Client.base_id = BaseUser.id
            WHERE RepairHour.id = ?;
            """
            cursor.execute(query, (hour_id, ))
            result = cursor.fetchone()

            print(f'\nOn {result[0]} at {result[1]}:')
            print(f'Client: {result[2]}')
            print(f'Vehicle: {result[3]} {result[4]}')
            print(f'Current Bill: {result[5]}$')

            print('Choose one of the following:')
            print('1 - change start hour')
            print('2 - change bill')
            print('3 - return to main menu\n')

            command = ''
            while command not in ['1', '2', '3']:
                command = input('>>> ')

            if command == '1':
                print(f'Current start hour is {result[1]}')
                print('Enter new start hour:')
                new_start_hour = input('>>> ')

                query = """
                UPDATE RepairHour
                SET start_hour = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_start_hour, hour_id))
            elif command == '2':
                print(f'Current Bill is: {result[5]}$')
                print('New Bill:')
                new_bill = input('>>> ')

                new_bill = int(''.join(new_bill.split('$')))

                query = """
                UPDATE RepairHour
                SET bill = ?
                WHERE id = ?;
                """

                cursor.execute(query, (new_bill, hour_id))
            else:
                break

            connection.commit()

        connection.commit()
        connection.close()

    @staticmethod
    def print_options():
        print('\nYou can choose from the following commands:')
        print('list_all_free_hours')
        print('list_free_hours <date>')
        print('list_all_busy_hours')
        print('list_busy_hours <date>')
        print('add_new_repair_hour')
        print('add_new_service')
        print('update_repair_hour <hour_id>')
        print('exit\n')


def main():
    create_tables()

    print('Hello!')
    print('Provide user name:')
    name = input('>>> ')

    base_user = BaseUser(name)
    user = None

    if not base_user.exists():
        print('Unknown user!')
        inp = ''
        while inp not in ['Y', 'N', 'YES', 'NO']:
            print('Would you like to create new user?')
            inp = input().upper()
        if inp in ['YES', 'Y']:
            user = base_user.create_user()
        else:
            print('Goodbye!')
            exit()
    else:
        base_user_type, base_user_id = base_user.get_type()
        if base_user_type == 'client':
            user = Client(name, base_user_id)
        else:
            user = Mechanic(name, base_user_id)

    user.listen()


if __name__ == '__main__':
    main()
