print("This Pogram will determine the number of days of a given month!")

month = ' '
year = ' '
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]


while month != -1:
    
    month = int(input("enter the month (1-12): "))
    year = int(input("please enter the year (e.g., 2023): "))
    if month == -1:
        print("Enter -1 to stop program")
        print(f"makasi udah pake program saya. sampai jumpa!")
        break
    elif month > 12 or month <1:
        print(f"*data invalid:( coba lagi?*\n")
        print("Enter -1 to stop program")
        continue
    elif (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
        days[2] = 29
    print(f""""in the year of {year} , {month} there are {days[month]} days
         
Enter -1 to stop program""")