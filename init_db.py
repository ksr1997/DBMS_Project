import psycopg2

# Connection parameters
dbname = 'postgres'
user = 'postgres'
password = 'Ksr199221@'
host = 'localhost'
port = '5432'  # Default PostgreSQL port is usually 5432

# Establish connection
try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database!")
    
    # Optionally, you can create a cursor to execute SQL queries
    cursor = conn.cursor()
    
    # Do your database operations here
    
    # Close cursor and connection when done
    cursor.close()
    conn.close()
    print("Connection closed.")
    
except psycopg2.Error as e:
    print("Unable to connect to the database:", e)
