list = ["abc","cde","fgh"]

#print list[2][0]

# reads = []
# left_boundary = where_repeat_starts - (2 * read_length)
# right_boundary = where_repeat_starts + (template_length * copy_number) + (2 * read_length)
#
# for read in range(read_number):
#     position = randrange(0, genome_length - read_length, 1)
#
#     if (position < left_boundary) or (position > right_boundary):
#         reads.append(genome[position:position + read_length])





for position,y in enumerate(list):
    print x, y