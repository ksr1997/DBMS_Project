Drug Store Management System
Overview
The Drug Store Management System is designed to assist Stores in tracking and managing their daily sales data effectively. This project utilizes a database system to store information about stores, customers, sellers, orders, and products. Through the implementation of CRUD operations using Python Flask and PostgreSQL SQL, users can interact with the system to perform various tasks related to managing Drug Store operations.

Features
Store Management: Store information such as store name, address, city, country, and phone number is stored in the database. This allows for efficient management of multiple pharmacy locations.
Customer Management: The system maintains records of customers including their names, contact details, and addresses, facilitating personalized services and communication.
Seller Management: Information about sellers or employees working at the pharmacy is stored, enabling effective workforce management and tracking of seller-related activities.
Product Inventory: Details of drugs or products available at the pharmacy, including their names, brands, prices, quantities in stock, manufacturing dates, expiration dates, manufacturers, and associated diseases, are recorded in the database. This helps in managing inventory levels and product details.
Sales Tracking: The system records sales transactions, capturing data such as sale date, order ID, product ID, price, store ID, seller ID, and customer ID. This enables the monitoring of sales patterns, identification of trends, and analysis of customer behavior.

Installation
To set up the Drug Store Management System locally, follow these steps:
Clone the repository: git clone https://github.com/ksr1997/DBMS_Project.git
Navigate to the project directory: cd DBMS_Project
Install dependencies: pip install -r requirements.txt
Set up PostgreSQL database with the provided schema.
Configure the database connection in the Flask application.
Run the Flask application: python app.py
Usage
Once the application is running, users can perform CRUD operations through the provided endpoints. These operations include adding new records, retrieving existing data, updating information, and deleting entries within the system.

Contributing
Contributions to the project are welcome! If you'd like to contribute, please fork the repository, create a new branch for your feature or fix, and submit a pull request.

## Credits

- Siva Reddy Kanala (@ksr1997) - Project Lead

## Changelog

### Version 1.0.0 (2024-04-15)

- **Fixed Bugs**

  - Fixed few bugs. [Commit: 3f86f89](link_to_commit_3f86f89) (Apr 14, 2024)

- **Updates**

  - Updated products.html. [Commit: 6b371ce](link_to_commit_6b371ce) (Apr 12, 2024)

- **Additions**
  - Added sellers.html. [Commit: 69515d8](link_to_commit_69515d8) (Apr 11, 2024)
  - Added home page. [Commit: f28e391](link_to_commit_f28e391) (Apr 10, 2024)
  - Added SQL table details. [Commit: a84a52b](link_to_commit_a84a52b) (Mar 31, 2024)
  - Added two features in home page. [Commit: fe3ca26](link_to_commit_fe3ca26) (Mar 31, 2024)

Youtube Link:
https://youtu.be/Zy_TT2kkMuQ

License
This project is licensed under the MIT License. See the LICENSE file for details.
