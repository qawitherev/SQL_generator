from csv_generator import create_csv
from statement_generator import generate_insert_sql
import os

def main(): 
    create_csv()

    csv_file_name = 'users_data.csv'
    table_name = 'user'
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(script_dir, csv_file_name)

    if os.path.exists(csv_file_path):
        file_name = generate_insert_sql(csv_file_path, table_name)
        if file_name: 
            print(f"SQL file generated: {file_name}")
        else: 
            print("Failed to generate SQL file.")
    else: 
        print("The specified CSV file does not exist.")
        return

if __name__ == "__main__": 
    main()