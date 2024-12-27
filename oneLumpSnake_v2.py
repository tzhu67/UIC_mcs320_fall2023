def oneLump(n, seqs = []):
    """
    Generate all one-lump sequences of length n.
    Start with [n], attach m = n-1, n-2, ..., 1 at left or right of current sequences, 2^(n-1) many sequences in total.
    """
    if len(seqs) == 0:
        return oneLump(n-1, [[n]])
    elif n == 0:
        return [[(i+1,seq[i]) for i in range(len(seq))] for seq in seqs]
    else:
        seqs1 = [[n]+seq for seq in seqs]
        seqs2 = [seq+[n] for seq in seqs]
        return oneLump(n-1, seqs1+seqs2)

def snakeChecker(seq):
    """
    Check if a sequence satisfies Snake condition.
    Either return the rearrangement, or False.
    """
    for i in range(len(seq)):
        arr = [seq[i]] # Start with seq[i] == pair (i+1,k_{i+1})
        while arr[0][0] != arr[-1][1]:
            arr.append(seq[arr[-1][1]-1])
        if len(arr) == len(seq):
            return arr
    return False

counts = []
for n in range(3,100):
    print('n =',n)
    counter=0
    for seq in oneLump(n):
        if snakeChecker(seq):
            counter+=1
    counts.append(counter)
print(counts)
