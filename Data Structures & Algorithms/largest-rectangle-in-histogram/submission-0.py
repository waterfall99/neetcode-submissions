class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        waiting_room = []
        max_area = 0
        for (current_index, current_height) in enumerate(heights):
            while len(waiting_room) > 0 and heights[waiting_room[-1]] > current_height:
                popped_index = waiting_room.pop()
                height = heights[popped_index]
                left_wall = waiting_room[-1] if waiting_room else -1
                width = current_index - left_wall - 1
                max_area = max(max_area, height * width)
            waiting_room.append(current_index)
        return max_area
        # how this works for first test case: waiting room is none so it appends index 0. then current height of next will be 1. the height of it will be 7 and it is bigger. so popped index will be 0. the height is 7. leftwall is -1. width is 0 so yea max area is 0