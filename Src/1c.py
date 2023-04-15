import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the diabetes dataset
df = pd.read_csv('diabetes.csv')

# extract the BloodPressure variable
bp = df['BloodPressure']

# population statistics
pop_mean = bp.mean()
pop_std = bp.std()
pop_pct = np.percentile(bp, 95)

# bootstrap sampling
np.random.seed(123)
bootstrap_means = []
bootstrap_stds = []
bootstrap_pcts = []
for i in range(500):
    bootstrap_sample = np.random.choice(bp, size=150, replace=True)
    bootstrap_means.append(bootstrap_sample.mean())
    bootstrap_stds.append(bootstrap_sample.std())
    bootstrap_pcts.append(np.percentile(bootstrap_sample, 95))

# plot the distributions
fig, axs = plt.subplots(3, figsize=(8, 12))
axs[0].hist(bp, bins=20, alpha=0.5)
axs[0].set_title('Population Distribution')
axs[0].axvline(pop_mean, color='red', label='Population Mean')
axs[0].legend()
axs[1].hist(bootstrap_means, bins=20, alpha=0.5)
axs[1].set_title('Bootstrap Mean Distribution')
axs[1].axvline(np.mean(bootstrap_means), color='red', label='Bootstrap Mean')
axs[1].legend()
axs[2].hist(bootstrap_stds, bins=20, alpha=0.5)
axs[2].set_title('Bootstrap Standard Deviation Distribution')
axs[2].axvline(np.mean(bootstrap_stds), color='red', label='Bootstrap Standard Deviation')
axs[2].legend()
plt.show()

# print the statistics
print('Population Mean: {:.2f}'.format(pop_mean))
print('Bootstrap Mean: {:.2f}'.format(np.mean(bootstrap_means)))
print('Population Standard Deviation: {:.2f}'.format(pop_std))
print('Bootstrap Standard Deviation: {:.2f}'.format(np.mean(bootstrap_stds)))
print('Population 95th Percentile: {:.2f}'.format(pop_pct))
print('Bootstrap 95th Percentile: {:.2f}'.format(np.mean(bootstrap_pcts)))