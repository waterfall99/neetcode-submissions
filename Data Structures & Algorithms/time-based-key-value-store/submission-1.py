class TimeMap:

    def __init__(self):
        self.mapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mapping:
            self.mapping[key].append([timestamp, value])
        elif key not in self.mapping:
            self.mapping[key] = []
            self.mapping[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapping:
            return ""
        elif key in self.mapping:
            answer = ""
            left = 0
            right = len(self.mapping[key]) - 1
            while left <= right:
                mid = (left + right) // 2
                if self.mapping[key][mid][0] == timestamp:
                    return self.mapping[key][mid][1]
                elif self.mapping[key][mid][0] < timestamp:
                    answer = self.mapping[key][mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
        return answer

