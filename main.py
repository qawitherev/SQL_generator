import csv 
import os 
import pandas as pd

def generate_insert_sql(file_path, table_name): 
    # Read CSV using pandas for easy processing 
    try: 
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Get columns from dataframe 
    columns = df.columns.tolist()
    columns_stripped = [col.strip() for col in columns]
    columns = ", ".join(columns_stripped)

    # Prepare for the insert statement, the goal is INSERT INTO table_name (col1, col2, ...)
    insert_statement = f"INSERT INTO {table_name} ({columns})"


    # Prepare for the values part of the insert statement
    values_list = []
    for _, row in df.iterrows():
        col_values  = []
        for col_value in row: 
            if pd.isna(col_value): 
                col_values.append("NULL")
            elif isinstance(col_value, (int, float)): 
                col_values.append(str(col_value))
            else:
                escaped_str = str(col_value).replace("'", "''")
                col_values.append(f"'{escaped_str}'")
        values_list.append(f"({', '.join(col_values)})")

    sql_statement = f"{insert_statement} {', '.join(values_list)};"

    # Write sql_statemtent to a file
    output_file = f"{table_name}_inserts.sql"
    with open(output_file, 'w') as f: 
        f.write(sql_statement)
    print(f"SQL insert statements written to {output_file}")

    return output_file

if __name__ == "__main__": 
    csv_path = input("Enter the path to the CSV file: ")
    table_name = input("Enter the table name: ")

    if os.path.exists(csv_path): 
        file_name = generate_insert_sql(csv_path, table_name)
        if (file_name): 
            print(f"SQL file generated: {file_name}")
        else: 
            print("Failed to generate SQL file.")
    else: 
        print("The specified CSV file does not exist.")


