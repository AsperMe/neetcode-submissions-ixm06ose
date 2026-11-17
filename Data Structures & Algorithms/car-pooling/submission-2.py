class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        for i in range(len(trips)):
            curr_pass = trips[i][0]
            for j in range(i):
                if trips[j][2] > trips[i][1]:
                    curr_pass += trips[j][0]
            if curr_pass > capacity:
                return False

        return True