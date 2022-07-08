# def fibo(N):
#     if N == 1 or N == 2: return 1
#     else:   return fibo(N-2) + fibo(N-1)

def fibo(N):
    f = [0]*N
    for i in range(N):
        if i == 0 or i == 1: f[i] = 1
        else:   f[i] = f[i-2] + f[i-1]

    print(f[N-1])
N = int(input())
fibo(N)