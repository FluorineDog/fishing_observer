from math import gcd
ban_list = [
    set([(1, 0), (0, 1)]),  # b-c ratio ban
    set([(1, 0), (0, 1)]),  # c-a ratio ban
    set([(1, 0), (0, 1)])   # a-b ratio ban
]

tags = ["b, c", "c, a", "a, b"]
def simplify(a, b):
    gg = gcd(a, b)
    if gg == 0:
        return (a, b)
    return (a // gg, b // gg)

print("\nNOTE: when there is a new ban, the observer must be the sum\n")
for round in range(2):
    for people in range(3):
        new_ban_set = set()    
        target = ban_list[people]
        src1 = ban_list[(people + 1) % 3]
        src2 = ban_list[(people + 2) % 3]
        # "me, other, another" in turn
        for (another, me) in src1:
            # generate new ban
            other = another + me
            new_ban = simplify(other, another) 
            if new_ban not in target:
                new_ban_set.add(new_ban)

        for (me, other) in src2:
            # generate new ban
            another = other + me
            new_ban = simplify(other, another) 
            if new_ban not in target:
                new_ban_set.add(new_ban)
         
        print("round {} observer {}, generate new ban with ratio of {{{}}} is {}".format(round, people, tags[people], new_ban_set))
        ban_list[people] = target.union(new_ban_set)
