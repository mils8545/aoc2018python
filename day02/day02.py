from template import Day
from collections import Counter

class Day02(Day):
    def part1(self, lines : list[str]) -> str:
        result = 0
        twos = 0
        threes = 0
        for line in lines:
            counter = Counter(line)
            double = False
            triple = False
            for value in counter.values():
                if value == 2:
                    double = True
                elif value == 3:
                    triple = True
            if double:
                twos += 1
            if triple:
                threes += 1
        result = twos * threes

        return(f"Checksum of IDs is {result}.")

    def part2(self, lines : list[str]) -> str:
        for i in range(len(lines)):
            for j in range(i + 1, len(lines)):
                diff = 0
                common = ""
                for k in range(len(lines[i])):
                    if lines[i][k] != lines[j][k]:
                        diff += 1
                    else:
                        common += lines[i][k]
                if diff == 1:
                    return(f"Common letters between the two correct box IDs is {common}.")

        return(f"Result of Part 2.")