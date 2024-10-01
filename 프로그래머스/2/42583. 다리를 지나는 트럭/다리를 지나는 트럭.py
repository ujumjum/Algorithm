def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    cur_weight = 0
    answer = 0
    
    truck_index = 0
    
    while truck_index < len(truck_weights) or cur_weight > 0:
        answer += 1
        
        pass_truck = bridge.pop(0)
        cur_weight -= pass_truck
        
        if truck_index < len(truck_weights):
            if cur_weight + truck_weights[truck_index] <= weight:
                entering_truck = truck_weights[truck_index]
                bridge.append(entering_truck)
                cur_weight += entering_truck
                truck_index += 1
            else:
                bridge.append(0)
        else:
            bridge.append(0)
        
    return answer