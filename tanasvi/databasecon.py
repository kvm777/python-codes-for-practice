from sqlalchemy import create_engine

# Replace 'mysql://user:password@host:port/database' with your MySQL connection string
engine = create_engine('C:\Users\korad\Desktop\python examples\tanasvi\dataY3kLBjpT3UDCRtfjlEig.sql')

# Establish a connection
connection = engine.connect()

try:
    # Execute a query to fetch data
    result = connection.execute("SELECT * FROM myTable")
    

    # Fetch all rows from the result
    rows = result.fetchall()

    # Print fetched rows
    for row in rows:
        print(row)
finally:
    # Close connection
    connection.close()

