def print_permutations(s):
    perms = [''.join(p) for p in itertools.permutations(s)]
    print("\n".join(perms))

def solve(numlegs, numheads):
    for rabbits in numheads+1:
        chickens = numheads - rabbits
    if 2* chickens + 4 * rabbits == numlegs:
        return chickens, rabbits 
    return None, None