def add_time (start_time , duration_time ,day =None):

    time,period    = start_time.split()
    initial_period = period



    hour_start    , minute_start    = time.split (':')
    hour_duration , minute_duration = duration_time.split (':')


    new_minute =  int(minute_start) + int(minute_duration)
    new_hour   =  int(hour_start)   + int(hour_duration)


    time, period   = start_time.split()
    initial_period = period

    periods_later = 0
    days_later   = 0

    Days_of_the_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    if new_minute  > 59:
        new_minute -= 60
        new_hour  += 1

    Hour_new_period = new_hour

    while new_hour > 12:
        new_hour  -= 12

    while Hour_new_period > 11:
        Hour_new_period  -= 12

        period = "PM" if period == "AM" else "AM"
        periods_later = periods_later +1

    if periods_later % 2 != 0 :
        if initial_period == "PM":
            periods_later  += 1
        else:
            periods_later  -= 1

    days_later = periods_later /2

    new_time = f"{new_hour}:{str(new_minute).zfill(2)} {period}"


    if day:
       day_index = Days_of_the_week.index(day.title())
       new_day_index = int((day_index + days_later) % 7)
       new_time += f", {Days_of_the_week[new_day_index]}"


    if days_later == 1:
       new_time += " (next day)"

    if days_later > 1:
       new_time += f" ({int(days_later)} days later)"




    return new_time
