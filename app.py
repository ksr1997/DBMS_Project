from flask import Flask, jsonify, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
dbname = 'postgres'
user = 'postgres'
password = 'Ksr199221@'
host = 'localhost'
port = '5432'

# Connect to the PostgreSQL database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# Routes
@app.route('/')
def home():
    cur.execute("SELECT customer_id FROM Customer")
    customers = cur.fetchall()
    return render_template('index.html', customers=customers)

@app.route('/stores')
def stores():
    cur.execute("SELECT * FROM Store")
    stores = cur.fetchall()
    return render_template('stores.html', stores=stores)

@app.route('/add_store', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        store_id = request.form['store_id']
        store_name = request.form['store_name']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        phone_number = request.form['phone_number']
        cur.execute("INSERT INTO Store (store_id, store_name, address, city, country, phone_number) VALUES (%s, %s, %s, %s, %s, %s)", (store_id, store_name, address, city, country, phone_number))
        conn.commit()
        return redirect(url_for('stores'))
    else:
        return render_template('add_store.html')

@app.route('/edit_store/<string:store_id>', methods=['GET', 'POST'])
def edit_store(store_id):
    if request.method == 'POST':
        store_name = request.form['store_name']
        address = request.form['address']
        city = request.form['city']
        country = request.form['country']
        phone_number = request.form['phone_number']
        cur.execute("UPDATE Store SET store_name = %s, address = %s, city = %s, country = %s, phone_number = %s WHERE store_id = %s", (store_name, address, city, country, phone_number, store_id))
        conn.commit()
        return redirect(url_for('stores'))
    else:
        cur.execute("SELECT * FROM Store WHERE store_id = %s", (store_id,))
        store = cur.fetchone()
        return render_template('edit_store.html', store=store)

@app.route('/delete_store/<string:store_id>', methods=['POST'])
def delete_store(store_id):
    cur.execute("DELETE FROM Store WHERE store_id = %s", (store_id,))
    conn.commit()
    return redirect(url_for('stores'))


@app.route('/customers')
def view_customers():
    cur.execute("SELECT * FROM Customer")
    customers = cur.fetchall()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        customer_id = request.form['customer_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phone_number']
        cur.execute("INSERT INTO Customer (customer_id, first_name, last_name, email, address, phone_number) VALUES (%s, %s, %s, %s, %s, %s)", (customer_id, first_name, last_name, email, address, phone_number))
        conn.commit()
        return redirect(url_for('view_customers'))
    else:
        return render_template('add_customer.html')

@app.route('/edit_customer/<string:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        address = request.form['address']
        phone_number = request.form['phone_number']
        cur.execute("UPDATE Customer SET first_name = %s, last_name = %s, email = %s, address = %s, phone_number = %s WHERE customer_id = %s", (first_name, last_name, email, address, phone_number, customer_id))
        conn.commit()
        return redirect(url_for('view_customers'))
    else:
        cur.execute("SELECT * FROM Customer WHERE customer_id = %s", (customer_id,))
        customer = cur.fetchone()
        return render_template('edit_customer.html', customer=customer)

@app.route('/delete_customer/<string:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    cur.execute("DELETE FROM Customer WHERE customer_id = %s", (customer_id,))
    conn.commit()
    return redirect(url_for('view_customers'))


@app.route('/get_customer_data/<customer_id>')
def get_customer_data(customer_id):
    # Fetch customer details from the database based on the provided customer ID
    cur.execute("SELECT * FROM Customer WHERE customer_id = %s", (customer_id,))
    customer_data = cur.fetchone()
    if customer_data:
        customer_dict = {
            'customer_id': customer_data[0],
            'first_name': customer_data[1],
            'last_name': customer_data[2],
            'email': customer_data[3],
            'address': customer_data[4],
            'phone_number': customer_data[5]
        }
        return jsonify(customer_dict)
    else:
        return jsonify({'error': 'Customer not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
