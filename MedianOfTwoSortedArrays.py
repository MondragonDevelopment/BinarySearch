# The main idea here is to create two partitions of length = total length // 2 (when combined)

def median(n, m):
    total_len = len(n) + len(m)
    middle = (total_len)//2
    if len(n) > len(m):
        n, m = m, n

    lp, rp = 0, len(n) - 1
    while True:
        mp = (lp + rp)//2
        mp2 = middle - mp - 2
        nl = n[mp] if mp >= 0 else float("-infinity")
        nr = n[mp + 1] if (mp + 1) < len(n) else float("infinity")
        ml = m[mp2] if mp2 >= 0 else float("-infinity")
        mr = m[mp2 + 1] if (mp2 + 1) < len(m) else float("infinity")
        if ml <= nr and nl <= mr:
            if total_len % 2 == 1:
                return min(nr, mr)
            return (max(ml, nl) + min(mr, nr)) / 2
        elif ml > nr:
            lp = mp + 1
        else: rp = mp -1

n, m = [1,2], [3,4]
print(median(n,m))
