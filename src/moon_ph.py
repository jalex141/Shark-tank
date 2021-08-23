import math

#utilizando la fecha obtenemos la fase lunar
def slit(item):
    return item.split("-")

def num_month(month):
    if month == "Jan":
        return 1
    elif month == "Feb":
        return 2
    elif month == "Mar":
        return 3
    elif month == "Apr":
        return 4
    elif month == "May":
        return 5
    elif month == "Jun":
        return 6
    elif month == "Jul":
        return 7
    elif month == "Aug":
        return 8
    elif month == "Sep":
        return 9
    elif month == "Oct":
        return 10
    elif month == "Nov":
        return 11
    elif month == "Dec":
        return 12

def moon(item):
    try:
        date=item.split("-")
        m=int(num_month(date[1]))
        d=int(date[0]);  y=int(date[2]);

        return conway(d,m,y)
    except:
        display(item)


# This is based on a 'do it in your head' algorithm by John Conway.
# In its current form, it's only valid for the 20th and 21st centuries

def conway(day, month, year):
    phase = year % 100

    phase %= 19
    if phase > 9:
        phase -= 19
    

    phase = ((phase * 11) % 30) + month + day
    if month < 3:
        phase += 2
    
    if year < 2000:
        phase -= 4
    else:
        phase -= 8.3
    phase = math.floor(phase + 0.5) % 30

    if phase < 0:
        phase + 30
    return phase

