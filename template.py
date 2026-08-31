from abc import ABC, abstractmethod


class Day(ABC):
    def solve(self, lines: list[str]) -> tuple[str, str]:
        return self.part1(lines), self.part2(lines)

    @abstractmethod
    def part1(self, lines: list[str]) -> str:
        raise NotImplementedError

    @abstractmethod
    def part2(self, lines: list[str]) -> str:
        raise NotImplementedError