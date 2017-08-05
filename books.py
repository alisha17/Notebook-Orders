
def get_best_price(
    books_in_box,
    cust_input,
    book_list,
    subject,
    ):
    """Get the combination of boxes with best value to the
    customer"""
    result = get_all_combination(books_in_box, cust_input)

    final_order = dict()
    final_sum = float('inf')

    for i in result:
        total_cost = 0
        for var in i:
            for item in book_list:
                if item['Subject'] == subject and item['Books in box'] \
                    == str(var):
                    price_book = float(item['Price'])
                    total_cost = total_cost + price_book
        if total_cost < final_sum:
            final_sum = total_cost
            final_list = i

    # Return best combination with it's price 
    final_order.update({'subject': subject, 'final_list': final_list,
                       'sum': final_sum})
    return final_order


def get_all_combination(books_in_box, cust_input):
    """Return all valid combinations of boxes for the customer input"""
    # Check if sum is obtainable without repeating the box sizes
    result = a(books_in_box, cust_input)
    if len(result) > 0:
        return result
    elif len(result) == 0:
          # Check if some is obtainable by repeating box sizes
        result1 = a(books_in_box, cust_input, True)
        if len(result1) > 0:
            return result1
        else:
              # Since no perfect combination, increase the input recursively
              # by 1 to find best fit
            flag = True
            result2 = []
            while flag:
                result2 = a(books_in_box, cust_input, True)
                if len(result2) > 0:
                    flag = False
                    break
                else:
                    cust_input += 1
            return result2


def a(lst, target, with_repeatition = False):
    """Recursive function to find combination of boxes for the target input"""  
    def _a(idx, l, r, t, w):
        if t == sum(l):
            r.append(l)
        elif t < sum(l):
            return
        for u in range(idx, len(lst)):
            _a((u if w else u + 1), l + [lst[u]], r, t, w)
        return r

    return _a(0, [], [], target, with_repeatition)



			