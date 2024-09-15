class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        originalCapacity = capacity
        for i in range(len(plants)):
              if capacity == plants[i] or capacity > plants[i]:
                     capacity -= plants[i]
                     steps += 1
              elif capacity < plants[i]:
                     steps += ((i-1)+1)
                     capacity = originalCapacity
                     steps += (i+1)
                     capacity -= plants[i]
        return steps


        