from operator import itemgetter
from collections import deque
from typing import List

class Solution:
    def timeFin(self, car, target):
        return (target - car["pos"]) / car["speed"] 
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [{}] * len(position)

        for i in range(len(position)):
            cars[i] = {"pos":position[i], "speed":speed[i]}

        cars.sort(reverse=True, key=itemgetter("pos"))

        stack = deque()
        stack.append(cars[0])

        for i in range(1, len(position)):
            if self.timeFin(stack[-1], target) < self.timeFin(cars[i], target):
                stack.append(cars[i])

        return len(stack)