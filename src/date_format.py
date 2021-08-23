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

def fix_time(item):
    l= item.split("@")
    t=l[0]; a=l[1]; f=l[2]
    if t== "UNKNOWN" or t== "afternoon":
        if a == "UNKNOWN" and (f== "Y" or f=="UNKNOWN"):
            return "evening"
        else:
            return t
    else:
        return t


def daytime(item):
    if re.match("(\d{2})",item):
        if int(re.match("(\d{2})",item).group(0)) > 18 and int(re.match("(\d{2})",item).group(0))<=4:
            return "Night"
        else:
            return "Day"
    elif item == "evening":
        return "Night"
    elif item == "UNKNOWN":
        return "UNKNOWN"
    else:
        return "Day"
