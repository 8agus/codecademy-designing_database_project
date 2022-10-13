import data
import sqlite3
import random

cur = sqlite3.connect("store.db",
                      check_same_thread=False)
db = cur.cursor()


def populate_tables():
    # Populating 20 customer names and last names into customer table
    for count in range(20):
        add_fn = data.first_names[count]
        add_ln = data.last_names[count]
        db.execute("INSERT INTO customer (name, last_name)"
                   "VALUES (?, ?)", (add_fn, add_ln))
        cur.commit()

    # Populate 100 products into item table
    for numb in range(100):
        p_id = data.prod_id[numb]
        p_name = data.prod_name[numb]
        p_desc = data.prod_desc[numb]
        p_price = data.prod_price[numb]
        db.execute("INSERT INTO items (item_id, item_name, item_description, price)"
                   "VALUES (?, ?, ?, ?)", (p_id, p_name, p_desc, p_price))
        cur.commit()

    # Using Primary Key of each customer in customer table
    # to link to other tables
    cu_id = list(db.execute("SELECT cu_id FROM customer"))
    for ele in cu_id:
        for id_numb in ele:

            # Populate address table
            id_to_cu = id_numb
            st_numb = random.randrange(1, 1000)
            st_name = random.choice(data.str_names)
            city_name = random.choice(data.city_names)
            db.execute("INSERT INTO address (cu_id, str_numb, str_name, city)"
                       "VALUES (?, ?, ?, ?)", (id_to_cu, st_numb, st_name, city_name))
            cur.commit()

            # Populate Credit Card table
            id_to_cc = id_numb
            cc_numb = random.randrange(1000, 9999)
            exp = data.create_date(2023, 2025)
            cvv = random.randrange(100, 999)
            db.execute("INSERT INTO credit_card (cu_id, card_number, exp_date, cvv_number)"
                       "VALUES (?, ?, ?, ?)", (id_to_cc, cc_numb, exp, cvv))
            cur.commit()

            # Populate purchase history table with 5 orders for each customer
            numb_orders = 5
            prod_numb = list(db.execute("SELECT item_id FROM items"))
            while numb_orders:
                item_id = random.choice(prod_numb)
                numb_items = random.randrange(1, 5)
                date = data.create_date(2021, 2022)
                db.execute("INSERT INTO purchase_history (cu_id, item_id, quantity, order_date)"
                           "VALUES (?, ?, ?, ?)", (id_numb, item_id[0], numb_items, date))
                cur.commit()
                numb_orders -= 1


# Generates a list of customers
def get_cust_list():
    print("Here is a list of customers: ")
    cust_list = db.execute('SELECT cu_id,  name,  last_name FROM customer;')
    for cust in cust_list:
        print(list(cust))

    cust_sales = input('\nInput the number of the customer to see sales: ')
    get_sales_figures(cust_sales)

    next_search = input('Wanted to do another search? (Y or N)')
    while next_search not in ('y', 'Y', 'N', 'n'):
        print('\nIncorrect option selected, please try again. ')
        next_search = input('\nWanted to do another search? (Y or N)')

    if next_search in ('y', 'Y'):
        get_cust_list()


# Generate details of customer selected
def get_sales_figures(cust_numb):
    sales_info = list(db.execute("SELECT customer.name, customer.last_name, purchase_history.ord_id, items.item_name, "
                                 "items.price FROM customer, purchase_history, items WHERE customer.cu_id = "
                                 "purchase_history.cu_id AND purchase_history.item_id = items.item_id AND "
                                 "customer.cu_id = ?", [cust_numb]))
    for column in sales_info:

        print('Name: ', column[0])
        print('Sure Name: ', column[1])
        print('Order #: ', column[2])
        print('Item Name: ', column[3])
        print('Price: ', column[4], '\n')


# Clear all rows from tables after use
def clear_table_data():
    list_of_tables = ['address', 'customer', 'purchase_history', 'credit_card', 'items']
    for table in list_of_tables:
        db.execute(f'DELETE FROM {table}')
        cur.commit()


def main():
    # insert data from csv files into tables
    print('Loading data...\n' * 3)
    populate_tables()
    print('Loading Completed.')

    get_cust_list()

    print('\nGood Bye!!\n')
    print('Shutting Down...\n' * 3)
    clear_table_data()


main()
