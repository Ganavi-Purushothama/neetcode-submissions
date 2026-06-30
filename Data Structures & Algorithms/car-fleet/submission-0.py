class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        cars.sort()
        stack=[]

        # Start from the car closest to the target
        for pos, time in reversed(cars):
            # New fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Else:
            # time <= stack[-1]
            # This car catches the fleet ahead,
            # so don't make a new fleet.
        return len(stack)

       
