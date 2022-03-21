hour_for_exam = int(input())
minutes_for_exam = int(input())
hour_for_arrive = int(input())
minutes_for_arrive = int(input())
exam_time_in_minutes = (hour_for_exam * 60) + minutes_for_exam
arrive_time_in_minutes = (hour_for_arrive * 60) + minutes_for_arrive
diff = abs(exam_time_in_minutes - arrive_time_in_minutes)
hour = diff // 60
minutes = diff % 60
if exam_time_in_minutes == arrive_time_in_minutes:
    print('on time')
elif exam_time_in_minutes > arrive_time_in_minutes:
    if diff <= 30:
        print('On time')
        print(f"{diff} minutes before start")
    elif 30 < diff <= 59:
        print("Early")
        print(f"{diff} minutes before start")
    else:
        print("Early")
        print(f"{hour}:{minutes:02d} hour before start")
elif exam_time_in_minutes < arrive_time_in_minutes:
    print('Late')
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        print(f"{hour}:{minutes:02d} hour after the start")