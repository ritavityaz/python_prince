from string_generator import generate_random_sequence, mutate_nucleotide
from random import randrange
from matches import compute_read_count

def simulate_read_and_error_positions(genome_length, template_length, read_length, read_number, copy_number, error_rate):
    # GENERATE GENOME
    ###########################################################
    template_sequence = generate_random_sequence(template_length)
    repeat_site_sequence = template_sequence * copy_number

    genome_without_repeats_length = genome_length - template_length * copy_number

    where_repeat_starts = randrange(1, genome_without_repeats_length + 1, 1)


    genome_left_sequence = generate_random_sequence(where_repeat_starts - 1)

    genome_right_sequence = generate_random_sequence(genome_without_repeats_length - where_repeat_starts)

    genome = genome_left_sequence + repeat_site_sequence + genome_right_sequence

    # GENERATE READS
    ###########################################################
    reads = []
    read_count = 0
    left_boundary = where_repeat_starts - (2 * read_length)
    right_boundary = where_repeat_starts + (template_length * copy_number) + (2 * read_length)


    for read in range(read_number):
        position = randrange(0, genome_length - read_length, 1)
        if (left_boundary < position) and (position < right_boundary):
            reads.append(genome[position:position + read_length])
            read_count = read_count + 1

    # ADD ERRORS
    ###########################################################
    total_positions = read_count * read_length
    mutation_number = int(total_positions * error_rate)

    for mutation in range(mutation_number):
        error_read = randrange(0, read_count, 1)
        error_position =randrange(0, read_length, 1)
        reads[error_read][error_position] = mutate_nucleotide(reads[error_read][error_position])

    return template_sequence, reads
