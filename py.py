source = ["X", "Y", "Z"]
target = []
through = []
def hanoi(n, source, target, through):
    if (n > 0):
        hanoi(n-1, source, through, target)
        target.append(source.pop())
        hanoi(n-1, through, target, source)

        
hanoi(len(source), source, target, through)
print(source)
print(through)
print(target)
