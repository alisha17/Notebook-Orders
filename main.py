import csv

from books import get_best_combo
from tabulate import tabulate


def main():
    book_list = []
    books_in_box = []
    order = []

    with open('book_record.csv') as f:
        records = csv.DictReader(f)
        for row in records:
            book_list.append(row)

    headers = book_list[0].keys()
    rows = [x.values() for x in book_list]

    print 'Welcome to Notebook Ordering system!\n'
    print 'These are the number of books in box available subjectwise with their price.'

    print tabulate(rows, headers=headers)

    print "Let's proceed with the customer order now."

    subject_no = \
        raw_input('For how many subjects the customer wants to order?')

    for i in range(0, int(subject_no)):
        subject = raw_input('Enter the subject.\n')
        if not subject:
            print 'Try again'
        else:
            cust_input = \
                raw_input('Enter the number of books the customer wants.\n'
                          )
            for x in book_list:
                if x['subject'] == subject:
                    books_in_box.append(int(x['no_of_books']))

        a = get_final_price(books_in_box, int(cust_input), book_list,
                            subject)
        order.append(a)

    for i in order:
        if i["subject"] == subject:
            for x in i["final_list"]:
                i



def get_final_price(
    books_in_box,
    cust_input,
    book_list,
    subject,
    ):

    result = get_best_combo(books_in_box, cust_input)

    final_order = dict()
    final_sum = float('inf')

    for i in result:
        total_cost = 0
        for x in i:
            for item in book_list:
                if item['subject'] == subject and item['no_of_books'] \
                    == str(x):
                    price_book = int(item['price'])
                    total_cost = total_cost + price_book
        if total_cost < final_sum:
            final_sum = total_cost
            final_list = i

    final_order.update({'subject': subject, 'final_list': final_list,
                       'final_sum': final_sum})
    return final_order


if __name__ == '__main__':
    main()
