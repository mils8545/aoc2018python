from template import Day

def react(polymer: str) -> str:
    stack : list[str] = []
    for unit in polymer:
        if stack and unit.swapcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(unit)
    return ''.join(stack)

def fully_react(polymer: str) -> str:
    current_length = len(polymer)
    future_length = 0
    while current_length != future_length:
        current_length = len(polymer)
        polymer = react(polymer)
        future_length = len(polymer)
    return polymer

class Day05(Day):
    def solve(self, lines: list[str]) -> tuple[str, str]:
        return self.part1(lines), self.part2(lines)

    def part1(self, lines: list[str]) -> str:
        current = lines[0]

        result = len(fully_react(current))
        return f"The length after fully reacting the polymer is {result}."

    def part2(self, lines: list[str]) -> str:
        start = lines[0]
        min_length = len(start)
        for unit in set(start.lower()):
            modified_polymer = start.replace(unit, '').replace(unit.upper(), '')
            reacted_polymer = fully_react(modified_polymer)
            min_length = min(min_length, len(reacted_polymer))

        return f"The minimum length after removing a single unit is {min_length}."