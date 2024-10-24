import random
num_trials = int(input("enter_no_of_trials"))
rolls_per_trial =int(input("for Each trail how many rolls"))
roll_up_value=int(input(" Enter rollup value"))
poss_outcomes=0
for i in range(num_trials):
    for j in range(rolls_per_trial):
        result = random.randint(1,6)
        print(result)
        if result == roll_up_value:
            poss_outcomes += 1
    print("--------")
total_outcomes = num_trials * rolls_per_trial
print(f"Number of times 6 appeared in {num_trials} trials of {rolls_per_trial} rolls each:  {poss_outcomes}")  

print("probability=",poss_outcomes / total_outcomes)
    