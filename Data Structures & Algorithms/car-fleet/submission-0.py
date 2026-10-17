class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        slowest = 0
        cars = sorted(zip(position, speed), reverse=True)
        for p,s in cars:
            time = (target-p)/s
            if time > slowest:
                fleet += 1
                slowest = time
        return fleet