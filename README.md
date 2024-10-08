Sreyas Cafe Project
Overview
The Sreyas Cafe project is a web-based application built using Flask to manage cafe operations. It allows users to view the cafe's menu, place orders, and receive order confirmations. Additionally, an admin dashboard is provided where the cafe owner can log in, manage the menu, update prices, and track orders. The project also supports authentication for admin access.

Features
Menu Display: Users can browse the cafe's menu, which includes dishes, drinks, and desserts.
Order Placement: Users can place orders by selecting items from the menu, specifying the quantity, and submitting their order.
Order Confirmation: After placing an order, users are redirected to an order confirmation page displaying the total price of their order.
Admin Authentication: Admins can log in with a secure username and password to manage the cafe’s menu.
Admin Dashboard: Admins can view, edit, and add menu items along with their prices.
Menu Management: The admin can update or delete items from the menu directly from the admin panel.
Database Integration: Menu items and orders are stored in a SQLite database, and all operations are performed via SQLAlchemy.
Technology Stack
Backend: Flask (Python)
Frontend: HTML, CSS
Database: SQLite
Authentication: Flask sessions, password hashing with werkzeug.security

Sreyas-Cafe/
│
├── app.py               # Main Flask app with routes and business logic
├── templates/
│   ├── index.html       # Home page
│   ├── menu.html        # Menu page to display available items
│   ├── order_form.html  # Order form for users to place their order
│   ├── order_confirmation.html  # Order confirmation page
│   ├── admin_login.html  # Admin login page
│   ├── admin_dashboard.html  # Admin dashboard for menu management
│   ├── edit_item.html    # Page to edit menu items
│   ├── add_item.html     # Page to add new menu items
│
├── static/
│   ├── styles.css        # CSS styles for the web pages
│
├── cafe.db               # SQLite database file
├── add_sample_data.py    # Script to populate initial data into the database
└── README.md             # Project documentation

Functionality Breakdown
1. User Interface:
Menu Display: View dishes, drinks, and desserts.
Order Form: Select items and quantities, then place an order.
Order Confirmation: Displays the total price for the order.
2. Admin Interface:
Login: Admin authentication using a username and password.
Dashboard: View, edit, and add menu items with prices.
Menu Management: Update or delete items in the menu.
Future Improvements
Order Management: Add functionality for admins to view and manage orders.
Payment Integration: Add payment gateway integration for online payments.
User Accounts: Allow users to create accounts and track their order history.
