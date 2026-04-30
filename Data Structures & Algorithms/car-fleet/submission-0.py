class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, (target - p) / s) for p, s in zip(position, speed)]

        pairs.sort(reverse=True)
        
        fleets = 0
        last_time = 0
        
        for p, time in pairs:
            if time > last_time:
                fleets += 1
                last_time = time
        
        return fleets 