import numpy as np
import pandas as pd
from simulate_read_positions import simulate_read_and_error_positions
from matches import compute_read_count
import matplotlib.pyplot as plt

#data params
read_length = 75
read_number = 1000
template_length = 53
genome_length = 5000
copy_numbers = [1, 2, 3, 4, 5, 6, 7]
max_cn = 7

#simulation params
simulation_number = 500
read_error_rate = 0.05
distance_threshold = 5


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


print simulation_values


