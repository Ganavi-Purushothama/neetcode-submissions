class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1

        boats = 0

        while left <= right:

            # lightest + heaviest can fit together
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1

            # heaviest must go alone
            else:
                right -= 1

            boats += 1

        return boats