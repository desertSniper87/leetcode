from typing import List 
 
class Solution:
    def average(self, salary: List[int]) -> float:
        salary = sorted(salary)

        return sum(salary[1:-1]) / (len(salary) - 2)

if __name__ == "__main__":
    s = Solution()
    print(s.average([4000,3000,1000,2000]))
