#Program 2: Test of significance
import pandas as pd
from scipy import stats
titanic_data = pd.read_csv('train.csv')
# One Sample T-Test: Checking mean age against a hypothetical mean
hypothetical_mean_age = 30
ttest_one_sample = stats.ttest_1samp(titanic_data['Age'].dropna(),
hypothetical_mean_age)
print("One Sample T-Test:")
print("T-statistic:", ttest_one_sample.statistic)
print("p-value:", ttest_one_sample.pvalue)


# Two Independent Samples T-Test: Comparing ages of male and female passengers
male_ages = titanic_data[titanic_data['Sex'] == 'male']['Age'].dropna()
female_ages = titanic_data[titanic_data['Sex'] == 'female']['Age'].dropna()
ttest_two_ind_samples = stats.ttest_ind(male_ages, female_ages)
print("\nTwo Independent Samples T-Test:")
print("T-statistic:", ttest_two_ind_samples.statistic)
print("p-value:", ttest_two_ind_samples.pvalue)

# Paired T-Test: Comparing fares before and after
before_fares = titanic_data['Fare'].dropna()
after_fares = before_fares * 1.2 # Assuming a 20% increase in fares
ttest_paired = stats.ttest_rel(before_fares, after_fares)
print("\nPaired T-Test:")
print("T-statistic:", ttest_paired.statistic)
print("p-value:", ttest_paired.pvalue)


# ANOVA Test: Impact of passenger class on fares
anova_result = stats.f_oneway(titanic_data[titanic_data['Pclass'] == 1]['Fare'].dropna(),
titanic_data[titanic_data['Pclass'] == 2]['Fare'].dropna(),
titanic_data[titanic_data['Pclass'] == 3]['Fare'].dropna())
print("\nANOVA Test Result:")
print("F-statistic:", anova_result.statistic)
print("p-value:", anova_result.pvalue)


# Chi-Square Test: Relationship between survival status and passenger class
chi2_table = pd.crosstab(titanic_data['Survived'], titanic_data['Pclass'])
chi2_result = stats.chi2_contingency(chi2_table)
print("\nChi-Square Test Result:")
print("Chi-Square statistic:", chi2_result[0])
print("p-value:", chi2_result[1])



# output:
# One Sample T-Test:
# T-statistic: -0.5534583115970276
# p-value: 0.5801231230388639
# Two Independent Samples T-Test:
# T-statistic: 2.499206354920835
# p-value: 0.012671296797013709
# Paired T-Test:
# T-statistic: -19.344277455944212
# p-value: 7.255925461999272e-70
# ANOVA Test Result:
# F-statistic: 242.34415651744814
# p-value: 1.0313763209141171e-84
# Chi-Square Test Result:
# Chi-Square statistic: 102.88898875696056
# p-value: 4.549251711298793e-23