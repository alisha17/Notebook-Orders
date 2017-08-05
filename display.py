import csv

from books import get_best_price
from tabulate import tabulate


def display():
    """Output order summary in terms of number of each type
       of notebooks and their price breakdown"""       
    try:
        book_list = list()
        final_order = dict()
        bill = 0

        with open('records.csv') as f:
            for row in csv.DictReader(f):
                book_list.append(row)

        print "Welcome to Notebook Ordering system!\n"
        print "These are the box sizes available subjectwise with their price.\n"

        print tabulate([x.values() for x in book_list], headers=book_list[0].keys()), "\n"

        print "Let's proceed with the customer order now."

        subject_no = \
            raw_input('For how many subjects the customer wants to order?\n')

        for num in range(0, int(subject_no)):
            cost_by_number = dict()

            subject = raw_input('Enter the subject:\n')

            if not any(d['Subject'] == subject for d in book_list):
                print "Either your input is wrong or no books available for this subject."
                return

            cust_input = \
                raw_input('Enter the number of books the customer wants:\n')

            for item in book_list:
                if item['Subject'] == subject:
                    cost_by_number.update({
                        int(item['Books in box']): float(item['Price'])
                        })

            result = get_best_price(cost_by_number.keys(), int(cust_input),
                                    book_list, subject)

            bill = bill + result['sum']

            list_details = list()
            order_details = dict()

            for item in set(result['final_list']):
                counter = result['final_list'].count(item)
                order_details.update({
                    'count': counter,
                    'notebooks_box': item,
                    'each_cost': cost_by_number[item],
                    'total': cost_by_number[item] * counter,
                    })
                list_details.append(order_details.copy())

            subject_num = cust_input + ' ' + subject \
                + ' notebooks ----> Total Cost: $' + str(result['sum'])

            final_order.update({subject_num: list_details})

        # Display the order summary 
        for (k, v) in final_order.iteritems():
            print '\n For', k
            print '-------------------------------------------------------------------'
            for item in v:
                print item['count'], "boxes of", item['notebooks_box'], \
                    "notebooks costing $", item['each_cost'], \
                    "each -----> $", item['total']

        print "___________________________________________________________________"
        print "Total: $", bill

    except ValueError:
        print "Oh you gave some wrong value. Try again."

    except Exception:
        print "Something is wrong. Try again."








			