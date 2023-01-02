M,N = input().split()
M=int(M)
N=int(N)
if M>=1 and M<=N:
    if N<=16:
        print((M*N)//2)
