import numpy as np
import pandas as pd
from simulate_read_positions import simulate_read_and_error_positions
from matches import compute_read_count
import matplotlib.pyplot as plt

import matplotlib
matplotlib.style.use('ggplot')

import sklearn
from sklearn import cross_validation
from sklearn.cross_validation import train_test_split
from sklearn.cluster import KMeans

from sklearn import linear_model


#data params
read_length = 75
read_number = 10000
template_length = 60
genome_length = 5000
copy_numbers = [1, 2, 3, 4, 5, 6, 7]
max_cn = 7

#simulation params
simulation_number = 500
read_error_rate = 0.05
distance_threshold = 10


#create dataframe to store simulation values
simulation_values = pd.DataFrame(index=range(0, simulation_number * 7),
                                 columns=["cn", "value"], dtype='int')

print simulation_values
row = 0
for copy_number in copy_numbers:
    print "copy number", copy_number
    for i in range(simulation_number):

        generated_template, generated_reads = \
            simulate_read_and_error_positions(genome_length, template_length,
                                              read_length, read_number, copy_number, read_error_rate)

        read_count = compute_read_count(generated_reads, read_length,
                                        generated_template, template_length, distance_threshold)

        simulation_values.set_value(row, "cn", copy_number)

        simulation_values.set_value(row, "value", read_count)
        row = row + 1


#print simulation_values

# #pretty plot
# simulation_values.plot.scatter(x="cn", y="value")
# plt.show()

#linear regression
x = simulation_values["value"].values.reshape(-1, 1)
y = simulation_values["cn"].values

reg = linear_model.LinearRegression()
reg.fit(x, y)


print('Coefficients: \n', reg.coef_)

plt.scatter(x, y,  color='black')
plt.plot(x, reg.predict(x), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()








# # KMEANS
# train, test = sklearn.cross_validation.train_test_split(simulation_values, train_size=0.6)

# cluster = sklearn.cluster.KMeans(n_clusters=7, init='k-means++', n_init=10, max_iter=300, tol=0.0001,
#                                  precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=1)
#
# cluster.fit(train)
# result = cluster.predict(test)







#plt.scatter(simulation_values, y)
#plt.show()
