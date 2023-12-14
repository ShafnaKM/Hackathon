# import json
# import mysql.connector
#
# # MySQL database configuration
# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     port=3306,
#     user='root',
#     password='',
#     database='Flights'
# )
# cursor = conn.cursor()
#
# # Define the path to the local JSON file
# json_file_path = "C:/Users/248762/Downloads/flightsDB.routes_v2.json"
#
# # Define the criteria for identifying similar routes
# def is_similar_route_in_db(code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first, common_duration, flights_per_day, flights_per_week, airport_from_code, airport_to_code, airport_via_code, airline_code):
#     query = """
#     SELECT id FROM flight_route
#     WHERE code_from = %s
#       AND code_to = %s
#       AND day1 = %s
#       AND day2 = %s
#       AND day3 = %s
#       AND day4 = %s
#       AND day5 = %s
#       AND day6 = %s
#       AND day7 = %s
#       AND class_business = %s
#       AND class_economy = %s
#       AND class_first = %s
#       AND common_duration = %s
#       AND flights_per_day = %s
#       AND flights_per_week = %s
#       AND airport_from_code = %s
#       AND airport_to_code = %s
#       AND airport_via_code = %s
#       AND airline_code = %s
#     """
#     cursor.execute(query, (
#         code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first,
#         common_duration, flights_per_day, flights_per_week, airport_from_code, airport_to_code, airport_via_code,
#         airline_code))
#     return cursor.fetchone() is not None
#
# try:
#     # Open the local JSON file and load its contents
#     with open(json_file_path, 'r', encoding='utf-8', errors="ignore") as json_file:
#         data = json.load(json_file)
#
#     print("JSON Data loaded successfully")
#
#     # Check if "data" key exists in JSON
#     for route_data in data:
#         code_from = route_data.get('iata_from', 'N/A')
#         code_to = route_data.get('iata_to', 'N/A')
#         day1 = route_data.get('day1', 'N/A')
#         day2 = route_data.get('day2', 'N/A')
#         day3 = route_data.get('day3', 'N/A')
#         day4 = route_data.get('day4', 'N/A')
#         day5 = route_data.get('day5', 'N/A')
#         day6 = route_data.get('day6', 'N/A')
#         day7 = route_data.get('day7', 'N/A')
#         class_business = route_data.get('class_business', 'N/A')
#         class_economy = route_data.get('class_economy', 'N/A')
#         class_first = route_data.get('class_first', 'N/A')
#         common_duration = route_data.get('common_duration', 'N/A')
#         flights_per_day = route_data.get('flights_per_day', 'N/A')
#         flights_per_week = route_data.get('flights_per_week', 'N/A')
#         airport_from_code = route_data.get('iata_from', 'N/A')
#         airport_to_code = route_data.get('iata_to', 'N/A')
#         airport_via_code = route_data.get('airport_via_code', 'N/A')
#         airline_code = route_data.get('airline', {}).get('IATA', 'N/A')
#
#         # Define the SQL INSERT statement
#         insert_statement = "INSERT INTO flight_route (code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first, common_duration, flights_per_day, flights_per_week, airport_from_code, airport_to_code, airport_via_code, airline_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
#
#         # Check if a similar route already exists in the database
#         if not is_similar_route_in_db(code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first, common_duration, flights_per_day, flights_per_week, airport_from_code, airport_to_code, airport_via_code, airline_code):
#             # Proceed with insertion
#             try:
#                 cursor.execute(insert_statement, (
#                     code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first,
#                     common_duration, flights_per_day, flights_per_week, airport_from_code, airport_to_code, airport_via_code,
#                     airline_code))
#                 conn.commit()
#                 print("Data inserted successfully")
#             except mysql.connector.Error as e:
#                 print(f"MySQL Error: {e}")
#                 conn.rollback()  # Rollback changes on error
#             except Exception as e:
#                 print(f"Error inserting data: {e}")
#         else:
#             print("Similar route already exists, skipping insertion")
#
# except FileNotFoundError:
#     print(f"File not found: {json_file_path}")
# except json.JSONDecodeError as json_error:
#     print(f"JSON decoding error: {json_error}")
# except Exception as e:
#     print(f"General Error: {str(e)}")
#
# # Close the database connection
# conn.close()


import json
import mysql.connector

# MySQL database configuration
conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='',
    database='Flights'
)
cursor = conn.cursor()

# Define the path to the local JSON file
json_file_path = "C:/Users/248762/Downloads/flightsDB.routes_v2.json"

try:
    # Open the local JSON file and load its contents
    with open(json_file_path, 'r', encoding='utf-8', errors="ignore") as json_file:
        data = json.load(json_file)

    print("JSON Data loaded successfully")

    # Initialize the ID
    id_counter = 1

    # Check if "data" key exists in JSON
    for route_data in data:
        code_from = route_data.get('iata_from', 'N/A')
        code_to = route_data.get('iata_to', 'N/A')

        day1 = route_data.get('day1', 'no').lower() == 'yes'
        day2 = route_data.get('day2', 'no').lower() == 'yes'
        day3 = route_data.get('day3', 'no').lower() == 'yes'
        day4 = route_data.get('day4', 'no').lower() == 'yes'
        day5 = route_data.get('day5', 'no').lower() == 'yes'
        day6 = route_data.get('day6', 'no').lower() == 'yes'
        day7 = route_data.get('day7', 'no').lower() == 'yes'

        class_business = route_data.get('class_business', False)
        class_economy = route_data.get('class_economy', False)
        class_first = route_data.get('class_first', False)
        common_duration = route_data.get('common_duration', 'N/A')
        flights_per_day = route_data.get('flights_per_day', 'N/A')
        flights_per_week = route_data.get('flights_per_week', 'N/A')
        airline_code = route_data.get('airline', {}).get('IATA', 'N/A')

        # Define the SQL INSERT statement
        insert_statement = "INSERT INTO routes (id, code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first, common_duration, flights_per_day, flights_per_week, airline_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        # Try inserting the data with the current ID
        try:
            cursor.execute(insert_statement, (id_counter, code_from, code_to, day1, day2, day3, day4, day5, day6, day7, class_business, class_economy, class_first, common_duration, flights_per_day, flights_per_week, airline_code))
            conn.commit()
            print(f"Data inserted successfully for ID: {id_counter}")
        except mysql.connector.Error as e:
            print(f"MySQL Error: {e}")
            conn.rollback()  # Rollback changes on error
        except Exception as e:
            print(f"Error inserting data: {e}")

        # Increment the ID
        id_counter += 1

except FileNotFoundError:
    print(f"File not found: {json_file_path}")
except json.JSONDecodeError as json_error:
    print(f"JSON decoding error: {json_error}")
except Exception as e:
    print(f"General Error: {str(e)}")

# Close the database connection
conn.close()