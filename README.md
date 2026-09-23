# Cafe Billing System

A desktop-based cafe billing application designed to simplify order management, bill generation, and bill retrieval through a graphical interface.

## Overview

The Cafe Billing System provides an interactive interface for handling customer orders and generating bills. It supports item-wise billing, automatic calculations, receipt generation, and retrieval of previously generated bills.

The application uses a CSV-based price catalogue and local file storage to manage billing data.

## Key Features

* Customer information and order management
* Dynamic item and quantity selection
* Automatic calculation of item-wise and category-wise totals
* Bill generation with customer and order details
* Local storage and retrieval of generated bills
* Search functionality for previously generated bills
* Price management through a CSV-based catalogue
* Input validation and error handling
* Graphical user interface for easy interaction

## Technologies

* Python
* Tkinter
* CSV-based data handling
* File handling

## Project Structure

```text
cafe-billing-system/
│
├── cafe_billing.py
├── ITEM PRICES.csv
├── README.md
└── screenshots/
```

## Getting Started

### Prerequisites

* Python 3.x

### Running the Application

1. Clone the repository.
2. Ensure the required CSV and image files are present in the project directory.
3. Run: python cafe_billing.py

## Screenshots

Screenshots demonstrating the application's interface, billing workflow, search functionality, and generated receipts are included in the `screenshots` folder.

## Future Improvements

* Introduce a database for persistent data management
* Refactor the application into a more modular architecture
* Improve the user interface and user experience
* Add authentication and role-based access
* Generate digital receipts in additional formats
* Improve portability across operating systems
