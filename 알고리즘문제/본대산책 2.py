board=[
        [0,1,1,0,0,0,0,0],
	[1,0,1,1,0,0,0,0],
	[1,1,0,1,0,1,0,0],
	[0,1,1,0,1,1,0,0],
	[0,0,0,1,0,1,1,0],
	[0,0,1,1,1,0,0,1],
	[0,0,0,0,1,0,0,1],
	[0,0,0,0,0,1,1,0]
    ]
lim=1000000007
n=int(input())
def mul(a,b):
    result=[[0 for _ in range(8)] for _ in range(8)]
    for x in range(8):
        for y in range(8):
            for z in range(8):
                result[x][y]=(result[x][y]+a[x][z]*b[z][y])%lim
    return result

def solve(b,n):
    if n==1:
        return b
    if n%2==1:
        tmp=mul(b,b)
        return mul(b,solve(tmp,n//2))
    else:
        tmp=mul(b,b)
        return solve(tmp,n//2)
board=solve(board,n)
print(board[0][0])
        
    
    
