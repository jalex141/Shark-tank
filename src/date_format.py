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

def fix_time(time, age, fatal):
    if time== "unknown" or time== "afternoon":
        if age == "unknown" and fatal== "Y":
            return "evening"
    else:
        return time

def daytime(item):
    if re.search("(\d{2})h",item):
        if int(re.search("(\d{2})h",item)) > 18 and int(re.search("(\d{2})h",item))<=4:
            return "Night"
        else:
            return "Day"
    elif item == "evening":
        return "Night"
    elif item == "unknown":
        return "unknown"
    else:
        return "Day"
