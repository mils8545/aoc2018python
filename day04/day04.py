from template import Day

class Guard:
    def __init__(self, guard_id: int):
        self.guard_id = guard_id
        self.sleep_minutes: list[int] = [0 for _ in range(60)]
        self.total_sleep_time: int = 0

    def add_sleep(self, start_minute: int, end_minute: int):
        for minute in range(start_minute, end_minute):
            self.sleep_minutes[minute] += 1
            self.total_sleep_time += 1

    def most_slept_minute(self) -> int:
        max_minute = 0
        max_count = 0
        for minute, count in enumerate(self.sleep_minutes):
            if count > max_count:
                max_count = count
                max_minute = minute
        return max_minute

class Day04(Day):
    def solve(self, lines: list[str]) -> tuple[str, str]:
        return self.part1(lines), self.part2(lines)

    def part1(self, lines: list[str]) -> str:
        lines.sort()
        guards: dict[int, Guard] = {}
        guards[0] = Guard(0)
        current_guard: Guard = guards[0]
        sleep_start_minute = 0
        sleep_end_minute = 0
        for line in lines:
            if "Guard #" in line:
                guard_id = int(line.split("#")[1].split(" ")[0])
                if guard_id not in guards:
                    guards[guard_id] = Guard(guard_id)
                current_guard = guards[guard_id]
            elif "asleep" in line:
                sleep_start_minute = int(line.split(" ")[1].split(":")[1].split("]")[0])
            elif "wakes up" in line:
                sleep_end_minute = int(line.split(" ")[1].split(":")[1].split("]")[0])
                current_guard.add_sleep(sleep_start_minute, sleep_end_minute)

        guard_with_most_sleep = max(guards.values(), key=lambda g: g.total_sleep_time)    
        most_slept_minute = guard_with_most_sleep.most_slept_minute()

        return f"The product of the guard ID and the most slept minute is {guard_with_most_sleep.guard_id * most_slept_minute}."

    def part2(self, lines: list[str]) -> str:
        lines.sort()
        guards: dict[int, Guard] = {}
        guards[0] = Guard(0)
        current_guard: Guard = guards[0]
        sleep_start_minute = 0
        sleep_end_minute = 0
        for line in lines:
            if "Guard #" in line:
                guard_id = int(line.split("#")[1].split(" ")[0])
                if guard_id not in guards:
                    guards[guard_id] = Guard(guard_id)
                current_guard = guards[guard_id]
            elif "asleep" in line:
                sleep_start_minute = int(line.split(" ")[1].split(":")[1].split("]")[0])
            elif "wakes up" in line:
                sleep_end_minute = int(line.split(" ")[1].split(":")[1].split("]")[0])
                current_guard.add_sleep(sleep_start_minute, sleep_end_minute)

        guard_with_most_frequent_minute = max(guards.values(), key=lambda g: max(g.sleep_minutes))
        most_frequent_minute = guard_with_most_frequent_minute.most_slept_minute()

        return f"The product of the guard ID and the most frequently slept minute is {guard_with_most_frequent_minute.guard_id * most_frequent_minute}."