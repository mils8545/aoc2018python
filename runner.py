import time
import argparse
from template import Day
from day01.day01 import Day01
from day02.day02 import Day02

days: dict[str, type[Day]] = {
    "01": Day01,
    "02": Day02
}

def readFile(fileName : str) -> list[str]:
    # Reads the file at fileName and returns a list of lines stripped of newlines
    with open(fileName, "r") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()
    return lines

def main ():
    parser = argparse.ArgumentParser(description="AOC2018")

    parser.add_argument("day", type=int, help="Day to run")
    parser.add_argument("file", type=str, default="chris.txt", help="Input file_name")

    args = parser.parse_args()

    day = f"{args.day:02d}"
    filename = "day" + day + "/" + args.file

    lines = readFile(filename)

    day_runner = days[day]()

    p1StartTime = time.perf_counter()
    p1Result = day_runner.part1(lines)
    p1EndTime = time.perf_counter()
    p2StartTime = time.perf_counter()
    p2Result = day_runner.part2(lines)
    p2EndTime = time.perf_counter()
    print("Advent of Code 2019 Day " + day + ":")
    print("  Part 1 Execution Time: " + str(round((p1EndTime - p1StartTime)*1000,3)) + " milliseconds")
    print("  Part 1 Result: " + str(p1Result))
    print("  Part 2 Execution Time: " + str(round((p2EndTime - p2StartTime)*1000,3)) + " milliseconds")
    print("  Part 2 Result: " + str(p2Result))

main()