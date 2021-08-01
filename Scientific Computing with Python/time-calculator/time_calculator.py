# detects format of the time input
def detectFormat(time):
    formats = ["X:XX AM", "XX:XX AM", "X:XX PM", "XX:XX PM", "X:X", "X:XX", "X:XXX", "XX:X", "XX:XX", "XX:XXX", "XXX:X", "XXX:XX", "XXX:XXX"]
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',}
    rawList = list(time)
    formatShape = []
    for char in rawList:
        if char in numbers:
            formatShape.append("X")
        else:
            formatShape.append(char)
    return (formats.index("".join(formatShape)))
     

# converts time  without AM PM
def strip(time):
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ":"}
    rawList = list(time)
    strip = []
    for char in rawList:
        if char in numbers:
            strip.append(char)
    return "".join(strip)
            
# converts time to seconds
def seconds(time):
    seconds = 0
    secondsHour = 3600
    secondsMin = 60
    PM = 43200
    # "X:XX AM"
    if detectFormat(time) <=1:
        seconds += int(strip(time).split(":")[0]) * secondsHour
        seconds += int(strip(time).split(":")[1]) * secondsMin
        return seconds
    # "Xx:XX AM"
    elif detectFormat(time) <= 3:
        seconds += PM
        seconds += int(strip(time).split(":")[0]) * secondsHour
        seconds += int(strip(time).split(":")[1]) * secondsMin
        return seconds
    else:
        seconds += int(time.split(":")[0]) * secondsHour
        seconds += int(time.split(":")[1]) * secondsMin
        return seconds

# rough 24 time
def hour24(seconds):
    secondsMin  = 60
    secondsHour = 3600
    secondsDay  = 86400
    minutes = int((seconds % secondsHour)/secondsMin)
    hours = int((seconds % secondsDay)/secondsHour)
    days = seconds // secondsDay
    return str(days) + ":" + str(hours) + ":" + str(minutes)

def hour12(hour24):
    hour24 = hour24.split(":")
    hour12 = []
    if int(hour24[1])==0:
        hour12.append("12")
        hour12.append(":")
        hour12.append(hour24[2].zfill(2))
        hour12.append(" AM")
    elif int(hour24[1])<12:
        hour12.append(str(hour24[1]))
        hour12.append(":")
        hour12.append(hour24[2].zfill(2))
        hour12.append(" AM")
    elif int(hour24[1])==12:
        hour12.append("12")
        hour12.append(":")
        hour12.append(hour24[2].zfill(2))
        hour12.append(" PM")       
    elif int(hour24[1])>12:
        hour12.append(str(int(hour24[1])%12))
        hour12.append(":")
        hour12.append(hour24[2].zfill(2))
        hour12.append(" PM")
    # print (hour24)
    if int(hour24[0]) == 1:
        hour12.append(" (next day)")
    elif int(hour24[0])>1:
        hour12.append(" (")
        hour12.append(hour24[0])
        hour12.append(" days later)")
    # return "".join(hour12)  
    return hour12          


def add_time(start, duration, day="X"):
    daysWeek = [", Sunday", ", Monday", ", Tuesday", ", Wednesday", ", Thursday", ", Friday", ", Saturday"]
    daysWeekCheck = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
    out = (hour12(((hour24((seconds(start)) +seconds(duration))))))
    if day == "X":
        #print ("".join(out)) 
        return "".join(out)
    elif day.upper() in daysWeekCheck and len(out) > 4:
        if out[4] == " (next day)":
            out.insert(4, daysWeek[((daysWeekCheck.index(day.upper()))+1)%7])
        else:
            out.insert(4, daysWeek[((daysWeekCheck.index(day.upper()))+int(out[5]))%7])
    else:
        out.insert(5, daysWeek[daysWeekCheck.index(day.upper())])
    #print ("".join(out)) 
    return "".join(out)  