import re

def date_f(item):
    if len(item.split("-")) ==3:
        return item
    else:
        return "date not complete"

def get_year(item):
    l=re.findall("(\d{4})", item)
    if l:
        return l[0]
    else:
        return "error"

def date_r(item):
    s = re.search("(\d+\-\w{3}\-\d+)",item)
    if s:
        return s[0]
    else:
        return "date not complete"