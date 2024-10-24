from scipy.stats import binom

n=10
p=0.5 # probablity of successs
k_succes=2
prob_02_succes=binom.pmf(k_succes,n,p)
print(f"the probablity of  2 succces out of 10 trial is : {prob_02_succes}")
