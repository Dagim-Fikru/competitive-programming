class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible(cap, weights, days):
            on_ship = 0 
            passed_days = 1
            for weight in weights:
                if on_ship + weight > cap:
                    passed_days += 1
                    on_ship = 0
                on_ship += weight
            
            return True if passed_days <= days else False

        low = max(weights)
        high = 2**32

        while low <high:
            mid = (low + high)//2
            if possible(mid, weights, days):
                high = mid
            else:
                low = mid + 1

        return low
