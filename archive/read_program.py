__author__ = "byteme8bit"

import pymongo

database_uri = "mongodb+srv://mx1:brain!!@cluster0-bmfcx.gcp.mongodb.net/test?retryWrites=true"
client = pymongo.MongoClient(database_uri)
database = client['LittlePeople']
# collection = database['People Group 1']
for entry in database.list_collection_names():      # TODO turn this method into a list?
    collection = database[entry]
    print(f'Current collection: {collection}')
    cached_posts = collection.find({})
    may_ppl = []
    for post in cached_posts:
        if 'May' in post['bday']:
            may_ppl.append({'name': post['name']})
            may_ppl.append({'bday': post['bday']})
    print(f'People with May birthdays in {collection}:\n{may_ppl}')
    line_count = 1
    for i in range(0, len(may_ppl), 2):
        print(may_ppl[i], may_ppl[i + 1])
# for person in may_ppl:
#     print(person['name'], person['bday'])

# with open('testDB8_dict.csv') as file:
#     reader = csv.DictReader(file)
#     line_count = 0
#     data = []
#     if line_count == 0:
#         headers = file.readline()
#         split_headers = headers.replace(old=',', new=' ').split()
#         print(split_headers[0])
#     else:
#         pass
#     for row in file:
#         print(f'Line #{line_count} ', row)
#         data.append(row)
#         line_count += 1
#         # if line_count == 0:
#         #     print(f'Column names are {", ".join(row)}')
#         #     line_count += 1
#
#         # else:
#         # print(f'\t{row[0]} was born on {row[1]}. Entry created @ {row[2]} with UID: {row[3]}.')
#     print(headers[1])
#     print(f'Processed {line_count} lines.')
#
    # TODO Below is to print rows again
    # time.sleep(3)
    # for item in data:
    #     print(item, end='\n')
