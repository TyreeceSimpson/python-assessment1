#Function receives start date(year, month, day) and outputs the 12 week term dates
def term_dates(year, month, day):
    #Declares the days in each month, the no. weeks and a list to hold the dates
    days = [31,28,31,30,31,30,31,31,30,31,30,31]
    weeks = 12
    dates = []

    #If year inputted is a leap year make February have 29 days
    if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
        days[1] = 29

    #If invalid date is inputted, output invalid        
    if day > days[month-1] or day < 1 or month < 1 or month > 12:
        print("invalid")
    else:
        #While the month is within the year
        while month <= 12:
            #While the day is within the month and 12 weeks have not been calculated
            while day <= days[month - 1] and weeks != 0:
                #Add dates to dates list
                dates.append([year, month, day])
                #Decrease the weeks left to calculate by 1
                weeks = weeks - 1
                #Add 7 to day
                day += 7
            #Will reach here when day will exceed that of a month
            #Calculates date a week after previuos in next month
            day = 7 - (days[month - 1] - (day - 7))
            #increments the month by 1
            month += 1
        #If 12 weeks were not calculated its due to the end of the year preventing it    
        if weeks != 0:
            print(dates, end= " Term never crosses a year boundary")
        #Else print 12 week term dates
        else:
            print(dates)

#Calls term_dates function with year, month and day    
term_dates(2019, 1, 7)
