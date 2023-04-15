import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# read the diabetes.csv file into a pandas dataframe
diabetes = pd.read_csv('diabetes.csv')

# set a seed value for reproducibility
np.random.seed(12345)

# take a random sample of 25 observations from the population
sample = diabetes.sample(n=25)

# calculate the mean and highest glucose values of the sample
sample_mean = sample['Glucose'].mean()
sample_max = sample['Glucose'].max()

# calculate the population mean and highest glucose values
population_mean = diabetes['Glucose'].mean()
population_max = diabetes['Glucose'].max()

# create a bar chart to compare the mean glucose values of the sample and population
plt.bar(['Sample', 'Population'], [sample_mean, population_mean])
plt.xlabel('Population vs Sample')
plt.ylabel('Mean Glucose')
plt.title('Comparison of Mean Glucose in Sample and Population')
plt.show()

# create a bar chart to compare the highest glucose values of the sample and population
plt.bar(['Sample', 'Population'], [sample_max, population_max])
plt.xlabel('Population vs Sample')
plt.ylabel('Highest Glucose')
plt.title('Comparison of Highest Glucose in Sample and Population')
plt.show()
