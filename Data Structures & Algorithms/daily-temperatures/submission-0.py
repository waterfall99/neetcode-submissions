class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for _ in range(len(temperatures)):
            result.append(0)
        waiting_room = []
        current_index = 0
        for temp in temperatures:
            while waiting_room and temperatures[waiting_room[-1]] < temp:
                prev_index = waiting_room.pop()
                result[prev_index] = current_index - prev_index
            waiting_room.append(current_index)
            current_index += 1
        return result