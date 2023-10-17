import pymysql


# Create a connection to the MySQL server
connection = pymysql.connect(host="localhost", user="root", password="123456", database="test")

# Create a cursor object to interact with the database
cursor = connection.cursor()

# List of dictionaries
data = [
    {
        "Date": "2023-09-28",
        "Open": 8.15,
        "Close": 7.98,
        "High": 7.96,
        "Low": 8.18,
        "Volume": 1250172,
    },
    {
        "Date": "2023-09-27",
        "Open": 8.03,
        "Close": 8.00,
        "High": 7.98,
        "Low": 8.05,
        "Volume": 754604,
    },
    {
        "Date": "2023-09-26",
        "Open": 8.00,
        "Close": 7.98,
        "High": 7.96,
        "Low": 8.03,
        "Volume": 891332,
    }
]

# Define the SQL query to insert data
insert_query = "INSERT INTO gupiao (Date, Open, Close, High, Low, Volume) VALUES (%s, %s, %s, %s, %s, %s)"

# Loop through the data list and insert each dictionary into the database
for entry in data:
    values = (entry["Date"], entry["Open"], entry["Close"], entry["High"], entry["Low"], entry["Volume"])
    cursor.execute(insert_query, values)

# Commit the changes to the database
connection.commit()

# Close the cursor and the connection
cursor.close()
connection.close()
