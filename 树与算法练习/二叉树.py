while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break
    if M > N:
        print("0")
        continue
    else:
        ret = 1
        curlevelmin, curlevelmax = M, M
        while True:
            nextlevelmin = 2 * curlevelmin
            nextlevelmax = 2 * curlevelmax + 1

            if nextlevelmax <= N:
                ret += (nextlevelmax - nextlevelmin + 1)
                if nextlevelmax == N:
                    break
            elif nextlevelmin <= N:
                ret += (N - nextlevelmin + 1)
                break
            else:
                break

            curlevelmin = nextlevelmin
            curlevelmax = nextlevelmax

        print(ret)
