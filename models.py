from flask import Flask, request, jsonify
import psycopg2

# Initialize Flask app
app = Flask(__name__)

# PostgreSQL database configuration
DB_HOST = 'localhost'
DB_NAME = 'creds'
DB_USER = 'john'
DB_PASSWORD = 'rkpr7c20##11'

# Function to connect to PostgreSQL database
def connect_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return conn
    except:
        return None

# Function to check if the 'users' table exists in the database
def check_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'users')")
    table_exists = cur.fetchone()[0]
    cur.close()
    conn.close()
    return table_exists

# Function to create the 'users' table in the database
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(50) UNIQUE, password VARCHAR(50))")
    conn.commit()
    cur.close()
    conn.close()

# Check if the 'users' table exists in the database, and create it if it doesn't
if not check_table():
    create_table()
    print("Table 'users' created successfully")

# Route for login_user request
@app.route('/login_user', methods=['POST'])
def login_user():
    # Get user input from request body
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Connect to database and fetch user data
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username=%s", (username,))
    user_data = cur.fetchone()

    # Verify user password and send response
    if user_data and user_data[2] == password:
        response = {
            'success': True,
            'message': 'Login successful'
        }
    else:
        response = {
            'success': False,
            'message': 'Incorrect username or password'
        }

    # Close database connection and return response
    cur.close()
    conn.close()
    return jsonify(response)

# Run Flask app
# if __name__ == 'main':
#     app.run(debug=True)

# Run Flask app
if __name__ == 'main':
    # Check if the 'users' table exists in the database, and create it if it doesn't
    if not check_table():
        create_table()
        print("Table 'users' created successfully")
    app.run(debug=True)

