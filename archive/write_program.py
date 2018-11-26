__author__ = "byteme8bit"

# Module Imports
import random
import pymongo
import time

# Program Imports
from modules import people_class, Generators

# DB Cluster
database_uri = "mongodb+srv://mx1:brain!!@cluster0-bmfcx.gcp.mongodb.net/test?retryWrites=true"
client = pymongo.MongoClient(database_uri)

print('Connection to server cluster complete')

# Asks what DB to connect to
db_question = input('Would you like to connect to non-default DB?: ').lower().rstrip()
pos_ans = 'yn'

# Double checks answer for valid response
while len(db_question) > 1 or db_question == ('' or ' ') or db_question not in pos_ans:
    print('Please select a valid response: Y or N')
    db_question = input('Would you like to connect to non-default DB?: ').lower().rstrip()

# If user wants to select non-default DB:
if db_question == 'y':
    print('Current DBs: \n', client.list_database_names())
    db_name = input('Please type the DB name: ')
    database = client[db_name]

# Default database chosen:
else:
    print('Connecting to default DB')
    db_name = 'LittlePeople'
    database = client[db_name]

print(f'Opening database: {db_name}')

# Shows current tables/collections in the chosen DB
print(f'Current collections in {db_name}: \n', sorted(database.list_collection_names()))
collection_name = input('Type the name of the collection you wish to connect to. (To create new entry '
                        'just type non-existent name): ')
collection = database[collection_name]
print(f'Opening or creating collection: {collection_name}')

num_to_add = input('How many entries should the script add?: ')
while not num_to_add.isnumeric():
    print('Please select a valid response - some sort of number. E.g. 457, 1000, 948372, etc')
    num_to_add = input('How many entries should the script add?: ')

num_to_add = int(num_to_add)
delay_1 = input('Minimum time delay between entry additions (in seconds): ')
while not delay_1.isnumeric():
    print('Please select a valid response - some sort of number. E.g. 457, 1000, 948372, etc')
    delay_1 = input('Minimum time delay between entry additions (in seconds): ')
delay_1 = int(delay_1)

delay_2 = input('Maximum time delay between entry additions (in seconds): ')
while not delay_2.isnumeric():
    print('Please select a valid response - some sort of number. E.g. 457, 1000, 948372, etc')
    delay_2 = input('Minimum time delay between entry additions (in seconds): ')
delay_2 = int(delay_2)

# Meat and Potatoes
print(f'Adding {num_to_add} new items to {collection_name} table. With delay: min {delay_1} - max {delay_2} seconds\n')
for i in range(1, num_to_add + 1):
    chosen_delay = random.uniform(delay_1, delay_2)
    print(f'Adding entry #{i} out of {num_to_add} total entries with a delay of {chosen_delay} seconds before '
          f'next entry')
    person = people_class.Person(Generators.pick_a_name(), Generators.create_bday())
    collection.insert_one({'name': person.name,
                           'bday': person.bday,
                           'created': person.created_time,
                           'id': person.id})
    time.sleep(chosen_delay)
