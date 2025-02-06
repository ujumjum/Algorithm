import math

def calculate_fee(fees, time):
    base_time, base_fee, unit_time, unit_fee = fees
    # 기본요금
    if time <= base_time:
        return base_fee
    # 기본요금 + 단위시간별요금(올림)
    return base_fee + math.ceil((time - base_time) / unit_time) * unit_fee

def convert_time(time_str):
    h, m = map(int, time_str.split(":"))
    return h*60 + m 
    

def solution(fees, records):
    parking = {}
    total_time = {}
    
    for record in records:
        time, car_number, status = record.split()
        time = convert_time(time)
        
        if status == "IN":
            parking[car_number]=time
        else:
            in_time = parking.pop(car_number)
            total_time[car_number] = total_time.get(car_number, 0) + (time - in_time)
            

    # 출차기록 X
    for car_number, in_time in parking.items():
        total_time[car_number] = total_time.get(car_number, 0) + (convert_time("23:59") - in_time)
            
    return [calculate_fee(fees, total_time[car_number]) for car_number in sorted(total_time.keys())]