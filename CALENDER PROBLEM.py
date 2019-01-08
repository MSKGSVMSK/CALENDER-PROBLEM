#calender month program

"""#init
terminate=False
print("THIS PROGRAM WILL DISPLAY A CALENDER MONTH BETWEEN 1800 AND 2099")

while not terminate:
    #get month and year
    month=int(input("ENTER THE MONTH FROM 1-12(-1 to quit):"))
    if(month==-1):
        terminate=True
    else:
        while(month<1 or month>12):
            month=int(input("OH NO! NO MONTH EXIST.TRY AGAIN:"))

        year=int(input("ENTER AN YEAR BETWEEN 1800 AND 2099 AS YYYY:"))
        while(year<1800 or year>2099):
            year=int(input("OH! INVALID YEAR. ENTER YEAR(1800-2099):"))

        #DETERMINE IF LEAP YEAR

        if((year%4==0) and (not(year%100==0) or (year%400==0))):
            leapyear=True
        else:
            leapyear=False

        #DETERMINE THE NO OF DAYS
        if month in (1,3,5,7,8,10,12):
            num_days=31
        elif(month in(4,6,9,11)):
            num_days=30
        elif(leapyear):
            num_days=29
        else:
            num_days=28
        print("\n",month,"/",year,"has",num_days,"days")
        if(leapyear):
            print(year,"is a leap year\n")
        else:
            print(year,"is NOT a leap yer\n")
        break"""
#second stage calender month

terminate=0

print("THIS PROGRAM WILL DISPLAY A CALENDER MONTH BETWEEN 1800 AND 2019")

while not terminate:
    #get month year
    month=int(input("ENTER THE MONTH FROM 1-12(-1 to quit):"))
    if(month==-1):
        terminate=True
    else:
        while(month<1 or month>12):
            month=int(input("OH NO! NO MONTH EXIST.TRY AGAIN:"))

        year=int(input("ENTER AN YEAR BETWEEN 1800 AND 2099 AS YYYY:"))
        while(year<1800 or year>2099):
            year=int(input("OH! INVALID YEAR. ENTER YEAR(1800-2099):"))

        #DETERMINE IF LEAP YEAR

        if((year%4==0) and (not(year%100==0) or (year%400==0))):
            leapyear=True
        else:
            leapyear=False
        #DETERMINE THE NO OF DAYS
        if month in (1,3,5,7,8,10,12):
            num_days=31
        elif(month in(4,6,9,11)):
            num_days=30
        elif(leapyear):
            num_days=29
        else:
            num_days=28
        print("\n",month,"/",year,"has",num_days,"days")
        if(leapyear):
            print(year,"is a leap year\n")
        else:
            print(year,"is NOT a leap yer\n")

        #determine the day of the week

        century_digit=year//100
        year_digit=year%100
        value=year_digit+(year_digit//4)

        if(century_digit==18):
            value=value+2
        elif(century_digit==20):
            value=value+6
        if(month==1 and not leapyear):
            value=value+1
        elif(month==2):
            if(leapyear):
                value+=3
            else:
                value+=4
        if(month==3 or month==11):
            value+=4
        elif(month==5):
            value+=2
        elif(month==6):
            value+=5
        elif(month==8):
            value+=3
        elif(month==9 or month==12):
            value+=6
        elif(month==10):
            value+=1
        day=(value+1)%7
        #1-sun,2-mon,3-tue,4-wed,5-thu,6-fri,0-sat

        #determine the month name

        if month==1:
            month_name='JANUARY'
        elif month==2:
            month_name='FEBRUARY'
        elif month==3:
            month_name='MARCH'
        elif month==4:
            month_name='APRIL'
        elif month==5:
            month_name='MAY'
        elif month==6:
            month_name='JUNE'
        elif month==7:
            month_name='JULY'
        elif month==8:
            month_name='AUGUST'
        elif month==9:
            month_name='SEPTEMBER'
        elif month==10:
            month_name='OCTOBER'
        elif month==11:
            month_name='NOVEMBER'
        else:
            month_name='DECEMBER'

        #DISPLAY MONTH YEAR

        print('\n',' '+month_name,year)

        #DISPLAY ROWS OF DATES

        if(day==0):
            start=0
        else:
            start=day

        current_col=1
        columnwidth=4
        blank_char=' '
        blank_column=format(blank_char,str(columnwidth))

        while(current_col<=start):
            print(blank_column,end=" ")
            current_col+=1

        current_day=1

        while(current_day<=num_days):
            if(current_day<10):
                print(format(blank_char,'3')+str(current_day),end=' ')
            else:
                print(format(blank_char,'2')+str(current_day),end=' ')
            if(current_col<7):
                current_col=current_col+1
            else:
                current_col=1
                print()
            current_day+=1
        print('\n')
        
                      
                

    
            
