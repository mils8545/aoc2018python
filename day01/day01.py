from template import Day


class Day01(Day):
    def part1(self, lines : list[str]) -> str:
        result = 0
        for line in lines:
            result += int(line)
        return(f"The final frequency is {result}.")

    def part2(self, lines : list[str]) -> str:
        result = 0
        seen : set[int] = set()

        i = 0
        while True:
            line = lines[i]
            result += int(line)
            if result in seen:
                return(f"The first frequency reached twice is {result}.")
            seen.add(result)
            i = (i + 1) % len(lines)

        return(f"This should be unreachable.")