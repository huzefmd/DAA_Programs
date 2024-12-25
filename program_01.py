#Program -1:
# Simple probability
# Probability of rolling a 4 on a six-sided die
total_outcomes = 6
favorable_outcomes = 1 # Rolling a 4
probability_4 = favorable_outcomes / total_outcomes
print(f"Probability of rolling a 4:  {probability_4} ")



#program1(a)
#1. A) Calculating the simple probabilities
# import random
# num_trials = int(input("enter_no_of_trials"))
# rolls_per_trial =int(input("for Each trail how many rolls"))
# roll_up_value=int(input(" Enter rollup value"))
# poss_outcomes=0
# for i in range(num_trials):
#     for j in range(rolls_per_trial):
#         result = random.randint(1,6)
#         print(result)
#         if result == roll_up_value:
#             poss_outcomes += 1
#     print("--------")
# total_outcomes = num_trials * rolls_per_trial
# print(f"Number of times 6 appeared in {num_trials} trials of {rolls_per_trial} rolls each:  {poss_outcomes}")  

# print("probability=",poss_outcomes / total_outcomes)
    
   
      
#program 1(b)
#1. b) Applications of Probability distributions to real life problems
# Binomial Distribution - Decision Making example
# estimating probability of success or failure in fixed number of trials
# from scipy.stats import binom

# n=10# Number of trials
# p=0.5 # probablity of successs
# k_succes=2
# prob_02_succes=binom.pmf(k_succes,n,p)
# print(f"the probablity of  2 succces out of 10 trial is : {prob_02_succes}")