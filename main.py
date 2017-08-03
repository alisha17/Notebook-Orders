import csv

from books import get_best_combo
from tabulate import tabulate

def main():
    
   book_list = []
   books_in_box = []

   with open("book_record.csv") as f:
       records = csv.DictReader(f)
       for row in records:
            book_list.append(row) 
       print book_list

   headers = book_list[0].keys()
   rows =  [x.values() for x in book_list]
   print(tabulate(rows, headers=headers, tablefmt="grid"))

   subject = raw_input("Enter the subject.\n")
   if not subject:
       print ("Try again")
   else:
        cust_input = raw_input("Enter the number of books the customer wants.\n")
        for x in book_list:
            if x["subject"] == subject:
                books_in_box.append(int(x["no_of_books"]))

   result = get_best_combo(books_in_box, int(cust_input))

   final_sum = float('inf')

   for i in result:
        total_cost = 0
        for x in i: 
            for item in book_list:
                    if item['subject'] == subject and item['no_of_books'] == str(x):
                        price_book = int(item["price"])
                        total_cost = total_cost + price_book
        if total_cost < final_sum:
            final_sum = total_cost
            final_list = i
   print final_list,final_sum

if __name__== "__main__":
    main()
