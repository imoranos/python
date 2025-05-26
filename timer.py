def add_time(start, duration,day = ''):
    #change : to . in start anad duration -------
    new_start = start.replace(":",".")
    new_duration = duration.replace(':','.')


    # detect period ------------ 
    if start.find('P') != -1:
        period_of_day = "PM"
        #print(period_of_day)
    else:
        
        period_of_day = "AM"
        #print(period_of_day)

    #delet period in start --------------------
    new_start = new_start.replace(period_of_day,"")

    print('start',new_start)
    print('durat',new_duration)

    # separted hour and minut of start --------
    start_hour = int(float(new_start))
    print('start_hour = ',start_hour)

    start_minut = float("{:.2f}".format(float(new_start)% 1))
    print('start_minut = ',start_minut)
    print('\n') 

    # separted hour and minut of duration --------
    duration_hour = int(float(new_duration))
    print('duration_hour = ',duration_hour)

    duration_minut = float("{:.2f}".format(float(new_duration)% 1))
    
    print('duration_minut = ',duration_minut)

    # sum hour and sum minutes ------------------- 
    print('\n')
    sum_hour = start_hour + duration_hour
    sum_minute = start_minut + duration_minut
    print('sum_hour   =',sum_hour)
    print('sum_minute =',sum_minute)

    #change period AM/PM -------------------------
    count_hour = sum_hour
    count_minute = (sum_minute /0.60) % 1 * 0.6 + int(sum_minute /0.60)
    count_total = count_hour + count_minute
    print(count_total)

    test = int(count_total / 12)
    
    print('test = ',test)
    if test % 2!= 0 :
        if period_of_day == "PM":
            period_of_day = "AM" 
        else:
            period_of_day = "PM"
    elif test % 2 == 0 :
        if period_of_day == "PM":
            period_of_day = "PM" 
        else:
            period_of_day = "AM"

    # custom next day ----------------------------
    next_day = ''
    if count_total > 23.59 and count_total < 47.59:
        next_day = ' ' + '(next day)'

    # custom next day ----------------------------

    days = ['Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday']
     
    # custom number of days ----------------------------
    days_text = ''
    #if sum_days > 23.59:
    sum_days = round (count_total / 24)    
    print('days',sum_days)
    
    days_text = ' ' + str(sum_days) + ' days later'

    if sum_hour > 12:
        #sum_hour = (sum_hour / 12 ) % 1 * 12
        sum_hour = float("{:.2f}".format((sum_hour / 12 ) % 1 * 12))
    print('sum_hour =',sum_hour)
    
    if sum_minute > 0.59:
        sum_minute = (sum_minute /0.60) % 1 * 0.6 + int(sum_minute /0.60)
    print('sum_minute', sum_minute)

    sum_of_times = "{:.2f}".format(sum_hour + sum_minute) 

    new_time = ''
    new_time = str(sum_of_times).replace('.',':') + ' ' + period_of_day + days_text

    return new_time
print(add_time('11:59 PM', '24:05'))
