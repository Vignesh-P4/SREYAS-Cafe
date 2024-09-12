from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# In-memory order storage
orders = []
order_id_counter = 1  # Counter for generating unique order IDs
ADMIN_PASSWORD = "123456"  # Change to your desired password

# SQLite database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Order(id={self.id}, items={self.items})"



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def place_order():
    global order_id_counter
    if request.method == 'POST':
        order_data = request.json
        order = {'id': order_id_counter, 'items': order_data['items']}
        orders.append(order)
        order_id_counter += 1
        return jsonify(id=order['id'])
    return render_template('order.html')

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/mark_completed/<int:order_id>', methods=['POST'])
def mark_order_as_completed(order_id):
    global orders
    orders = [order for order in orders if order['id'] != order_id]
    return jsonify(status='success')

@app.route('/remove_order/<int:order_id>', methods=['POST'])
def remove_order(order_id):
    global orders
    orders = [order for order in orders if order['id'] != order_id]
    return jsonify(status='success')

@app.route('/clear_orders', methods=['POST'])
def clear_orders():
    global orders
    orders = []
    return jsonify(status='success')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get('password')
        if password == ADMIN_PASSWORD:
            return render_template('admin.html', orders=orders)
        else:
            return render_template('admin_password.html', error_message="Incorrect password. Please try again.")
    return render_template('admin_password.html', error_message=None)


@app.route('/download_orders', methods=['GET'])
def download_orders():
    orders = Order.query.all()
    
    # Prepare CSV data
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Order ID', 'Items'])
    for order in orders:
        writer.writerow([order.id, order.items])
    
    # Set up response headers for CSV file download
    headers = {
        "Content-Disposition": "attachment; filename=orders.csv",
        "Content-Type": "text/csv"
    }
    
    return Response(
        output.getvalue(),
        headers=headers,
        mimetype="text/csv"
    )


@app.route('/admin_panel')
def admin_panel():
    return render_template('admin.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
