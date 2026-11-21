class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []
        for car_pos, car_sp in zip(position, speed):
            combined.append((car_pos, car_sp))
        combined.sort(reverse=True)
        
        fleet_no = 0
        temp_arr_time = 0
        for combo in combined:
            if ((target - combo[0]) / combo[1]) > temp_arr_time:
                fleet_no += 1
                temp_arr_time = ((target - combo[0]) / combo[1])
            else:
                continue
        return fleet_no