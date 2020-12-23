

def is_iterable(curr_item, str_is_iterable):

    try:
        iter(curr_item)
    except:
        return False
    else:
        if isinstance(curr_item, str):
            if str_is_iterable and len(curr_item) > 1:
                return True
            else:
                return False
        else:
            return True



def flatten_gen(curr_item, *, str_is_iterable=True):

    if is_iterable(curr_item, str_is_iterable=str_is_iterable):
        for item in curr_item:
            yield from flatten_gen(item, str_is_iterable= str_is_iterable)

    else:
        yield curr_item


if __name__ == "__main__":
    
    l = ["abc", 1, 2, 3, (4,(5,6))]
    print(list(flatten_gen(l)))
