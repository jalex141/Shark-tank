
def date_f(item):
    try:
        len(item.split("-")) ==3
        return item
    except:
        return "date not complete"
