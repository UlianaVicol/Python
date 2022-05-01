
from matplotlib import pyplot
month_name  = "April"
days_name = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su", ]
month_temps = [
    # days ---->
    #   Mo  Tu   Wd   Th   Fr   Sa   Su        
    [ None,None,None,None, 5.0, 6.0, 7.0, ],    # |
    [  8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, ],    # |
    [  1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, ],    # |
    [  8.0, 9.0, 8.0, 7.0, 6.0, 5.0, 4.0, ],    # < week
    [  3.0, 2.0, 1.0, 2.0, 3.0, 4.0,None, ]
    #day

]

def brokenLines():
    print("-"*63)


month_temps_1d = []
for wi in range(5):
    for di in range(7):
        if month_temps[wi][di] != None:
            month_temps_1d.append( month_temps[wi][di] )
max_temp = max(month_temps_1d)
min_temp = min(month_temps_1d)
average_temp = sum(month_temps_1d) / len(month_temps_1d)


########### Display The Calendar #############
brokenLines()
print(f"| {month_name:54}|     |")
brokenLines()

# Day names
for di in range(7):
    print(f"| {days_name[di]}    " , end="")
print("|     |")    
brokenLines()

date = 1
# Loop through the weeks
for wi in range(5):
    # Temps for one week
    for di in range(7):
        if month_temps[wi][di] == None:
            date_str = " " * 6
        else:
            date_str = date
            date +=1    
        print(f"| {date_str:<6}", end="") 
    print("|     |") 

    print("|       "*7,f"{wi+1:^5}|",sep= "|")

    for di in range(7):
        if month_temps[wi][di] == None:
            temp = " "*6
        else:    
            temp = f"{month_temps[wi][di]:6.1f}"
        print(f"|{temp} " , end="")
    print(f"|     |")    
    brokenLines()

########### Display The Calendar #############

print(f"Max temp: {max_temp}")
print(f"Min temp: {min_temp}")
print(f"{month_name} : {average_temp:1.0f} °C")

pyplot.plot(month_temps)
pyplot.show()

