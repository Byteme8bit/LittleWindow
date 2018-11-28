__author__ = "byteme8bit"
# Program imports
from modules import people_class, Generators

# Module imports
import pymongo
import time
import random


def main():
    """
    Main piece of program. User provides URI to server, selects database and collection then decides to read/write.
    :return: None
    """
    print('\tWelcome to the MongoBytsistant program\n'
          'This will assist in connecting to cloud or local DBs and using the LittleWindow script to generate random'
          'details for "people" to be input into various collections.\n'
          'You will be able to select the database URI, specific DB, collection to connect to, how many'
          'entries you would like to add and then set a min and maximum\ndelay between entries. The delay is used '
          'because the entries are time stamped and it would be boring to see all of the same time. '
          'Also, the ID is generated based off\nof a unique equation using the time generated so having delays between '
          'each entry helps give more randomized IDs.\n\n')

    # time.sleep(6)
    reconnect = 'y'

    while reconnect == 'y':
        client = connect_to_uri()
        print('Connection to server/cluster completed.\n\n')

        database = choose_database(client)
        print(f'Opening database: {database}\n\n')

        chosen_collection = choose_collection(client, database)
        print(f'Opening or creating collection: {chosen_collection}\n\n')

        stay_in_current_db = 'y'

        while stay_in_current_db == 'y':
            w_r = write_or_read()
            if w_r == 'read':
                read_program(client, database, chosen_collection)

            else:
                write_program(client, database, chosen_collection)

            stay_in_current_db = input('Would you like to perform more actions in this database? (y or n): ')
            print()

        reconnect = input('Would you like to connect to another server/cluster?: ')
        print()


def double_check_function():
    """
    Used to double check user input
    :return: string value of 'y' or 'n'
    """

    double_check = input('Are you wanting to create a new entry?: ').lower().strip()
    print()
    pos_ans = 'yn'

    # Checks for valid answer
    while double_check not in pos_ans or double_check == ('' or ' ') or len(double_check) > 1:
        print('Please type a valid response (y or n)')
        double_check = input('Are you wanting to create a new entry?: ')
        print()

    return double_check


def connect_to_uri():
    """
    Used to retrieve mongoDB connection URI from user.
    :return: client variable
    """
    database_uri = input('What is the URI of the Server/Cluster you wish to connect to? (Note: Omit mongodb+srv://): ')
    print()

    # # Checks for valid URI
    # while database_uri[0:13] != 'mongodb+srv://':
    #     print('Please provide a valid database URI. It must start with: mongodb+srv://')
    #     database_uri = input('What is the URI of the Server/Cluster you wish to connect to?: ')

    return pymongo.MongoClient('mongodb+srv://' + database_uri)


def choose_database(client):
    """
    User selects or creates a database in the provided mongoDB connection URI
    :param client: User's provided URI for mongoDB
    :return: db_name variable
    """
    currently_avail = sorted(client.list_database_names())

    print('Select one of the currently available DBs or type a non-existent name to create a new entry.\n'
          f'The currently available DBs are:\n\n{currently_avail}')
    db_name = input('Your selection: ')
    print()

    # Checks to see if user is trying to create a new entry or not.
    if db_name not in currently_avail:
        double_check = double_check_function()

        if double_check == 'y':
            pass
        else:
            print('Please make sure you type the name of a currently available entry exactly as it appears.\n'
                  'Select one of the currently available DBs or type a non-existent name to create a new entry.\n'
                  f'The currently available DBs are:\n{currently_avail}\n')
            db_name = input('Your selection: ')

    return db_name


def choose_collection(client, db_name):
    """
    User selects or creates a collection in the chosen database.
    :param client: User's provided URI for mongoDB
    :param db_name: User's chosen database
    :return: chosen_collection variable
    """
    database = client[db_name]
    currently_available_collections = sorted(database.list_collection_names())

    print(f'Select one of the currently available collections in {db_name} or type a non-existent name to create'
          ' a new entry.\n'
          f'The currently available collections are:\n\n{currently_available_collections}')
    chosen_collection = input('Your selection: ')
    print()

    # Checks to see if user is trying to create a new entry or not.
    if chosen_collection not in currently_available_collections:
        double_check = double_check_function()

        if double_check == 'y':
            pass
        else:
            print('Please make sure you type the name of a currently available entry exactly as it appears.\n'
                  'Select one of the currently available DBs or type a non-existent name to create a new entry.\n'
                  f'The currently available collections are:\n{currently_available_collections}\n')
            chosen_collection = input('Your selection: ')

    return chosen_collection


def write_or_read():
    """
    User decides to read or write to the selected database
    :return: string value 'read' or 'write'
    """
    question = input('Would you like to read or write to the database?: ')
    print()
    pos_ans = 'read', 'write'

    # Checks for valid input
    while question not in pos_ans or len(question) > 5 or question == ('' or ' '):
        print('Please type a valid response (read/write).')
        question = input('Would you like to read or write to the database?: ')
        print()

    return question


def read_program(client, db_name, collection):
    """
    User reads collection, filters and manipulates results
    :param client: The built client based on user's provided URI
    :param db_name: User's chosen database
    :param collection: User's chosen collection
    :return:
    """

    def iterate_over_results():
        if cached_names:
            for name in cached_names:
                print(f"ID: {name['id']}\n"
                      f"Name: {name['name']}\n"
                      f"BDay: {name['bday']}\n")

        else:
            print('None found.')

    database_continue = 'y'
    while database_continue == 'y':

        collection_continue = 'y'
        while collection_continue == 'y':

            database = client[db_name]
            c = database[collection]
            cached_entries = c.find({})
            total_entries = 0
            for entry in cached_entries:
                total_entries += 1

            print(f'+~~~\tCurrent db: {db_name} \t~~~+\n'
                  f'+~~~\tCurrent collection: {collection} \t~~~+\n'
                  f'+~~~\tThere are {total_entries} in this collection. \t~~~+\n\n')

            time.sleep(1)
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            print('You may do one of the following actions (type the word in brackets to make a selection):\n'
                  '\t* [Search] for specific name, bday, ID and return # of matches\n'
                  '\t\t With ability to create new database from results\n'
                  '\t* [Filter] and sort all databases into corresponding databases based on bday month\n'
                  '\t* [Filter] and sort all entries/DBs by ID and offer to export to local .txt or .csv\n'
                  '\t* [List] all entries in current collection to console, filtered or unfiltered.\n')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

            selection = input('Your selection (Search, Filter, List): ').lower().strip()
            print()
            pos_ans2 = 'search', 'filter', 'list'

            while selection not in pos_ans2 or len(selection) > 6 or selection == (
                    '' or ' ') or not selection.isalpha():
                print('Please select a valid answer. (Search, Filter, List)')
                selection = input('Your selection (Search, Filter, List): ').lower().strip()
                print()

            if selection == 'search':
                select_search_type = input('What do you want to search for? (Name, Bday, ID): ').lower().strip()
                print()
                pos_search_types = 'name', 'bday', 'id'

                while select_search_type not in pos_search_types or select_search_type == (
                        '' or ' ') or len(select_search_type) > 4 or not select_search_type.isalpha():
                    print('Please select a valid response. (Name, Bday, ID).')
                    select_search_type = input('What do you want to search for? (Name, Bday, ID): ').lower().strip()
                    print()

                if select_search_type == 'name':
                    search_param = input('What is the name you want to search for?: ')
                    print()
                    cached_names = c.find({'name': search_param})
                    iterate_over_results()

                elif select_search_type == 'bday':
                    search_param = input('What is the birthday you want to search for?: ')
                    print()
                    cached_names = c.find({'bday': search_param})
                    iterate_over_results()

                else:  # == 'id'
                    search_param = input('What is the ID you want to search for?: ')
                    print()
                    cached_names = c.find({'id': search_param})
                    iterate_over_results()

            elif selection == 'filter':
                pass

            elif selection == 'list':
                cached_entries = c.find({})
                item = 1
                for entry in cached_entries:
                    print('==========\n',
                          f'Entry #{item}\n',
                          f"ID#: {entry['id']}", '\n',
                          entry['name'], entry['bday'], '\n',
                          f"Added to collection on {entry['created']}", '\n'
                                                                        '==========\n')

            # else:
            #     item = 1
            #     for entry in cached_entries:
            #         print('==========\n',
            #               f'Entry #{item}\n',
            #               f"ID#: {entry['id']}", '\n',
            #               entry['name'], entry['bday'], '\n',
            #               f"Added to collection on {entry['created']}", '\n'
            #                                                             '==========\n')
            #         item += 1
                # filtered = input('Would you like to show filtered or unfiltered entries?: ').lower().strip()
                # print()
                # pos_ans = 'filtered', 'unfiltered'
                #
                # # Checks for valid input
                # while filtered not in pos_ans or filtered == ('' or ' ') or not filtered.isalpha():
                #     print('Please type either "filtered" or "unfiltered".')
                #     filtered = input('Would you like to show filtered or unfiltered entries?: ').lower().strip()
                #     print()
                #
                # # Checks user's selection
                # if filtered == 'filtered':
                #     pass
                #
                # else:  # Prints unfiltered results. (all entries one by one)
                #     item = 1
                #     for entry in cached_entries:
                #         print('==========\n',
                #               f'Entry #{item}\n',
                #               f"ID#: {entry['id']}", '\n',
                #               entry['name'], entry['bday'], '\n',
                #               f"Added to collection on {entry['created']}", '\n'
                #                                                             '==========\n')
                #         item += 1
            collection_continue = input('Continue reading from this same collection?: ')

        database_continue = input('Continue reading from this same database?: ')


def write_program(client, db_name, collection):
    """
    User selects an amount of entries to add to the chosen database. As well as the range of possible delays between
    entry creation.
    :param client: The built client based on user's provided URI
    :param db_name: User's chosen database
    :param collection: User's chosen collection
    :return: Executes script, returns no values or variables other than text to UI.
    """

    def amount_of_entries():
        """
        User selects amount of entries to add
        :return: integer value
        """
        # nta = number to add
        nta = input('How many entries should the script add?: ')
        print()

        while not nta.isnumeric():
            print('Please select a valid response - some sort of number. E.g. 457, 1000, 948372, etc')
            nta = input('How many entries should the script add?: ')
            print()

        return int(nta)

    def choose_delays():
        """
        User selects the minimum and maximum possible values for the delay between entries
        :return: two integer values
        """

        def min_delay():
            """
            Minimum possible value for delay between entries
            :return: integer value
            """
            d1 = input('Minimum time delay between entry additions (in seconds): ')
            print()

            while not d1.isnumeric():
                print('Please select a valid response - some sort of number. E.g. 457, 1000, 948372, etc')
                d1 = input('Minimum time delay between entry additions (in seconds): ')
                print()

            return int(d1)
            # return int(input('Select a minimum delay, in seconds. Please enter numerical characters.: '))

        def max_delay():
            """
            Maximum possible value for delay between entries
            :return: integer value
            """
            d2 = input('Maximum time delay between entry additions (in seconds): ')
            print()

            while not d2.isnumeric():
                print('Please select a valid response - some sort of number. E.g. 457, 1000, 948372, etc')
                d2 = input('Minimum time delay between entry additions (in seconds): ')
                print()

            return int(d2)
            # return int(input('Select a maximum delay, in seconds. Please enter numerical characters.: '))

        return min_delay(), max_delay()

    num_to_add = amount_of_entries()
    delay_1, delay_2 = choose_delays()
    database = client[db_name]
    c = database[collection]

    print(f'Adding {num_to_add} new items to {collection} collection.'
          f' With delay: min {delay_1} - max {delay_2} seconds\n')

    # Loops over the desired number of times
    for i in range(1, num_to_add + 1):  # Starts at 1 for itemization print outs
        chosen_delay = random.uniform(delay_1, delay_2)
        print(f'Adding entry #{i} out of {num_to_add} total entries with a delay of {chosen_delay} seconds before '
              f'next entry.')
        person = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
        c.insert_one({'name': person.name,
                      'bday': person.bday,
                      'created': person.created_time,
                      'id': person.id})
        time.sleep(chosen_delay)


if __name__ == "__main__":
    main()
    print('Finalizing changes to collection(s)...\n')
    time.sleep(1)
    print('Closing connection to server/cluster...\n')
    time.sleep(1)
    print('Exiting program.')
