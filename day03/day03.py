from template import Day

def intersection(rect1 : tuple[int, int, int, int], rect2 : tuple[int, int, int, int]) -> tuple[bool, tuple[int, int, int, int]]:
    x1a, y1a, wa, ha = rect1
    x1b, y1b, wb, hb = rect2

    x2a = x1a + wa
    y2a = y1a + ha
    x2b = x1b + wb
    y2b = y1b + hb

    left = max(x1a, x1b)
    right = min(x2a, x2b)
    top = max(y1a, y1b)
    bottom = min(y2a, y2b)

    if left < right and top < bottom:
        return (True, (left, top, right - left, bottom - top))

    return (False, (0, 0, 0, 0))

class Day03(Day):
    def part1(self, lines : list[str]) -> str:
        result = 0
        claims : list[tuple[int, int, int, int]] = []
        for line in lines:
            coordstr = line.split(":")[0].split("@")[1].strip()
            sizestr = line.split(":")[1].strip()
            x, y = [int(i) for i in coordstr.split(",")]
            w, h = [int(i) for i in sizestr.split("x")]
            claims.append((x, y, w, h)) 

                    
        hit : set[tuple[int, int]] = set()
        doublehit : set[tuple[int, int]] = set()
        for claim in claims:
            x, y, w, h = claim
            for i in range(x, x + w):
                for j in range(y, y + h):
                    if (i, j) not in hit:
                        hit.add((i, j))
                    elif (i, j) not in doublehit:
                        doublehit.add((i, j))

        result = len(doublehit)

        return(f"The number of tiles that are double claimed is {result}.")

    def part2(self, lines : list[str]) -> str:
        result = 0

        claims : list[tuple[int, int, int, int]] = []
        for line in lines:
            coordstr = line.split(":")[0].split("@")[1].strip()
            sizestr = line.split(":")[1].strip()
            x, y = [int(i) for i in coordstr.split(",")]
            w, h = [int(i) for i in sizestr.split("x")]
            claims.append((x, y, w, h)) 
                    
        for i in range(len(claims)):
            found = False
            for j in range(len(claims)):
                if i == j:
                    continue
                inter, _ = intersection(claims[i], claims[j])
                if inter:
                    found = True
                    break
            if not found:
                result = i + 1
                break

        return(f"The only claim that doesn't conflict with another claim is {result}.")