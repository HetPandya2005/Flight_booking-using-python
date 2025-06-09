import pandas as pd
import pymysql

# Establishing connection to the MySQL database
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='airlines'
)

# Function to display passenger and destination data
def disp():
    cursor = conn.cursor()
    
    # Display Passenger Details
    print("\n--- Passenger Records ---")
    cursor.execute("SELECT * FROM passengers;")
    for row in cursor.fetchall():
        print(row)

    # Display Destination Details
    print("\n--- Destination Records ---")
    cursor.execute("SELECT * FROM Destination;")
    for row in cursor.fetchall():
        print(row)

    print("\nThank you for flying with us!")
    menu()

# Function to input passenger details and save to database
def details():
    cursor = conn.cursor()
    passenger = []

    print("\n--- Enter Passenger Details ---")
    passenger.append(input("Serial Number: "))
    passenger.append(input("First Name: "))
    passenger.append(input("Last Name: "))
    passenger.append(input("Passport Number: "))
    passenger.append(input("Age: "))
    passenger.append(input("Gender: "))

    # Insert record into 'passengers' table
    sql = """
        INSERT INTO passengers 
        (Srno, First_Name, Last_Name, Passport_Number, Age, Gender) 
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, passenger)
    conn.commit()

    print("✔️ Passenger details registered successfully!")
    disp()

# Function to input destination details and call passenger details
def dest():
    cursor = conn.cursor()
    destination = []

    print("\n--- Enter Destination Details ---")
    destination.append(input("Serial Number: "))
    destination.append(input("Departure Location: "))
    destination.append(input("Arrival Location: "))
    destination.append(input("Travel Date (YYYY-MM-DD): "))

    # Insert record into 'Destination' table
    sql = """
        INSERT INTO Destination 
        (srno, Departure, Arrival, Date) 
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, destination)
    conn.commit()

    print("✔️ Destination details saved!")
    details()

# Function to display the main menu
def menu():
    print("\n" + "*" * 30)
    print("     FLIGHT BOOKING SYSTEM")
    print("*" * 30)
    print("1. Book a flight")
    print("2. View booked flights")
    print("3. Exit")
    print("*" * 30)

    choice = input("Enter your choice: ")

    if choice == '1':
        dest()
    elif choice == '2':
        disp()
    elif choice == '3':
        print("Exiting system. Goodbye!")
        exit()
    else:
        print("❌ Invalid choice. Please try again.")
        menu()

# Password-protected system entry
def pswd():
    password = input("Enter Admin Password: ")
    if password == "123":
        menu()
    else:
        print("❌ Incorrect password. Try again.")
        pswd()

# Program starts here
pswd()
