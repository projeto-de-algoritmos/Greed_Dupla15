# Questão "Cutting Boards" do HackerRank
# https://www.hackerrank.com/challenges/board-cutting/problem

def boardCutting(cost_y, cost_x):
    cost_ax = []
    mod = int(10e8+7)
    
    cost_ax.extend([(x,1) for x in cost_y])
    cost_ax.extend([(x,0) for x in cost_x])    

    cost_ax.sort(key=lambda x: x[0],reverse=True)
    
    print(cost_ax)
    
    v,h,cost=0,0,0
    
    for i in range(len(cost_ax)):
        ax = cost_ax[i][1]
        if ax==1:
            cost = (cost+(cost_ax[i][0]*(v+1))%mod)%mod;
            h+=1
        else:
            cost = (cost+(cost_ax[i][0]*(h+1))%mod)%mod;
            v+=1
    
    return cost