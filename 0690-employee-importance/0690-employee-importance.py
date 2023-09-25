"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        stack, result = [id], 0
        while stack:
            curr = stack.pop()
            for i in employees:
                if i.id == curr:
                    result += i.importance
                    for j in i.subordinates:
                        stack.append(j)
        return result
        