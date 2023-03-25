def its_magic():
    n, k = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))
    d = list(map(int, input().split()))
    chars = 'abcdefghijklmnopqrstuvwxyz'
    chrs_dct = {chars[i]: i for i in range(len(chars))}
    power = 0
    for i in range(n):
        my_set = set()
        idx = p[i]-1
        chrs_count = {}
        for j in range(k):
            chrs_count[s[idx]] = chrs_count.get(s[idx], 0) + 1
            if chrs_count[s[idx]] == 1:
                my_set.add(s[idx])
            else:
                if d[idx] != 0:
                    my_set.add(chars[(chrs_dct[s[idx]] +
                                      (chrs_count[s[idx]] - 1) * d[idx]) % 26])
                else:
                    chrs_count[s[idx]] += 1
            if len(my_set) == 26:
                power += len(my_set) * (k - j)
                break
            power += len(my_set)
            idx = p[idx]-1
    return power


print(its_magic())
