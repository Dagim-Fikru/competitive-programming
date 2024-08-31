class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for op in ops:
            if op=='D':
                record.append(2*record[-1])
            elif op=='C':
                record.pop()
            elif op=='+':
                record.append(record[len(record)-1] + record[len(record)-2])
            else:
                record.append(int(op))
        return sum(record)