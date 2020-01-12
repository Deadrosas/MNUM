# O objetivo é ver o gráfico das funções nos intervalos pedidos. Se estes tiverem declive menor que 1 então são aceites
#a) X1 e X2
#b) Nenhum
#c) X1 e X2


#Alínea b) & c)
import math as m

def rec(x):
    return 2*m.log(2*x)

def picard_peano(x,num_iterations):
    for i in range(num_iterations):
        x=rec(x)
        print("{} iteration value: {}".format(i+1,x))
    return x

print("Resíduo = {}".format(picard_peano(1.1,0)-picard_peano(1.1,1)))