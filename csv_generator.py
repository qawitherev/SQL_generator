import csv 
from faker import Faker as fk 

ROWS_DATA = 5000
HEADERS = ['userTypeId', 'username', 'password', 'nickname', 'createdAt']
CSV_NAME = 'users_data.csv'

def g8_data(): 
    fake = fk()
    usr_name = g8_unique_username()
    return {
        'userTypeId': 7,
        'username': usr_name,
        'password': '18959BB5D775EC360E139FC7F60D53FDE6D31A6F6F3F434BF4FCDB5B91535A98', 
        'nickname': f"{usr_name} - nickname",
        'createdAt': '2025-03-14T00:00:00.000Z',
    }

def g8_unique_username(): 
    fake = fk()
    used_usernames = set()

    while True:
        username  = fake.user_name()
        if username not in used_usernames:
            used_usernames.add(username)
            return username

def create_csv():
    try: 
        with open(CSV_NAME, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=HEADERS)
            writer.writeheader()

            for _ in range(ROWS_DATA):
                data = g8_data()
                writer.writerow(data)
    except Exception as e:
        print(f"An error occurred while creating the CSV file: {e}")