from math import ceil

def compute_read_count(reads, read_length, template, template_length, distance_threshold):

    # MAKE TEMPLATE LONG ENOUGH
    ###########################################################
    if read_length > template_length:
        times_to_copy = ceil(float(read_length)/float(template_length))
        template = template * int(times_to_copy)


    read_count = 0
    # COMPUTE DISTANCE
    ###########################################################
    for read in reads:
        for index in range(0, len(template) - read_length + 1):
            distance = 0
            for position, nucleotide in enumerate(read):
                if nucleotide != template[(position + index)]:
                    distance = distance + 1
                    if distance > distance_threshold:
                        break
            if distance < distance_threshold:
                read_count = read_count + 1
                break

    return read_count
