def a(lst, target, with_replacement=False):
    
    def _a(
        idx,
        l,
        r,
        t,
        w,
        ):

        if t == sum(l):
            r.append(l)
        elif t < sum(l):
            return
        for u in range(idx, len(lst)):
            _a((u if w else u + 1), l + [lst[u]], r, t, w)
        return r

    return _a(0, [], [], target, with_replacement)


def get_best_combo(mylist, mysum):
    res = a(mylist, mysum)
    if len(res) > 0:
        return res
    elif len(res) == 0:
        res1 = a(mylist, mysum, True)
        if len(res1) > 0:
            return res1
        else:
            flag = True
            res2 = []
            while flag:
                res2 = a(mylist, mysum, True)
                if len(res2) > 0:
                    flag = False
                    break
                else:
                    mysum += 1
            return res2