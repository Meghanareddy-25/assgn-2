import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt

# load the diabetes data
diabetes = pd.read_csv('diabetes.csv')

# set a seed for reproducibility
random.seed(123)

# take a random sample of 25 observations
sample = diabetes.sample(n=25)

# calculate the mean and highest glucose values of the sample
sample_mean = sample['Glucose'].mean()
sample_highest = sample['Glucose'].max()

# calculate the population mean and highest glucose values
population_mean = diabetes['Glucose'].mean()
population_highest = diabetes['Glucose'].max()

# plot the comparison between the sample and population means and highest values
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
axs[0].bar(['Sample Mean', 'Population Mean'], [sample_mean, population_mean])
axs[0].set_title('Comparison of Sample and Population Means')
axs[1].bar(['Sample Highest', 'Population Highest'], [sample_highest, population_highest])
axs[1].set_title('Comparison of Sample and Population Highest Values')
plt.show()

# find the 98th percentile of BMI for the sample and population
sample_98th = np.percentile(sample['BMI'], 98)
population_98th = np.percentile(diabetes['BMI'], 98)

# plot the comparison between the sample and population 98th percentiles
fig, axs = plt.subplots(figsize=(8, 5))
axs.bar(['Sample 98th Percentile', 'Population 98th Percentile'], [sample_98th, population_98th])
axs.set_title('Comparison of Sample and Population 98th Percentiles of BMI')
plt.show()

# bootstrap sampling
n_samples = 500
sample_size = 150
bootstrap_means = []
bootstrap_stds = []
bootstrap_50th_percentiles = []
bootstrap_95th_percentiles = []

for i in range(n_samples):
    bootstrap_sample = diabetes.sample(n=sample_size, replace=True)
    bootstrap_means.append(bootstrap_sample['BloodPressure'].mean())
    bootstrap_stds.append(bootstrap_sample['BloodPressure'].std())
    bootstrap_50th_percentiles.append(np.percentile(bootstrap_sample['BloodPressure'], 50))
    bootstrap_95th_percentiles.append(np.percentile(bootstrap_sample['BloodPressure'], 95))

# calculate the population mean, std, and percentiles for BloodPressure
population_mean_bp = diabetes['BloodPressure'].mean()
population_std_bp = diabetes['BloodPressure'].std()
population_50th_percentile_bp = np.percentile(diabetes['BloodPressure'], 50)
population_95th_percentile_bp = np.percentile(diabetes['BloodPressure'], 95)

# define a function to calculate the average mean, standard deviation, and percentile for a variable from bootstrap samples
def bootstrap_stats(data, n_bootstrap_samples, sample_size, statistic_func):
    bootstrap_stats = []
    for i in range(n_bootstrap_samples):
        sample = data.sample(sample_size, replace=True)
        bootstrap_statistic = statistic_func(sample)
        assert isinstance(bootstrap_statistic, object)
        bootstrap_stats.append(bootstrap_statistic)
    bootstrap_mean = np.mean(bootstrap_stats)
    bootstrap_std = np.std(bootstrap_stats)
    bootstrap_percentile = np.percentile(bootstrap_stats, 95)
    return bootstrap_mean, bootstrap_std, bootstrap_percentile

# define a function to calculate the mean BloodPressure of a sample
def mean_blood_pressure(sample):
    return sample["BloodPressure"].mean()

# calculate the average mean, standard deviation, and 95th percentile for BloodPressure from bootstrap samples
n_bootstrap_samples = 500