from collections import Counter
import re
import csv


def generate_substrings(text, min_length=3, max_length=50):
    words = text.split()  # Split by whitespace to get individual words
    substrings = []

    # Generate substrings of varying lengths
    for start in range(len(words)):
        for end in range(start + 1, len(words) + 1):
            substring = ' '.join(words[start:end])
            if len(substring) >= min_length and len(substring) <= max_length:
                substrings.append(substring)

    return substrings


def find_common_substrings(lines, min_length=3, max_length=50):
    substr_counter = Counter()

    for line in lines:
        line_substrings = generate_substrings(line, min_length, max_length)
        substr_counter.update(line_substrings)

    return substr_counter

def get_sorted_common_substrings(substr_counter, min_count=2):
    filtered_substr = {substr: count for substr, count in substr_counter.items() if count >= min_count}
    sorted_substr = sorted(filtered_substr.items(), key=lambda x: x[1], reverse=True)
    return sorted_substr

def find_common_substrings1(lines, min_length=5):
    substr_counter = Counter()

    for line in lines:
        line = line.lower()  # Convert to lowercase for case-insensitive comparison
        for length in range(min_length, len(line) + 1):
            for i in range(len(line) - length + 1):
                substring = line[i:i + length]
                substr_counter[substring] += 1

    # Filter out substrings that occur fewer than 2 times or are very short
    common_substr = {substr: count for substr, count in substr_counter.items() if count > 1}

    # Sort substrings by frequency (descending)
    sorted_common_substr = sorted(common_substr.items(), key=lambda x: x[1], reverse=True)

    return sorted_common_substr


def split_lines_by_substrings(lines, substrings):
    results = []

    for line in lines:
        line_results = []
        start = 0
        for substr in substrings:
            while substr in line[start:]:
                index = line.find(substr, start)
                if index > start:
                    line_results.append(line[start:index].strip())
                line_results.append(substr)
                start = index + len(substr)
        if start < len(line):
            line_results.append(line[start:].strip())
        results.append(line_results)

    return results


def write_to_csv(csv_file_path, split_results):
    # Write data to CSV
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)

        # Optionally write header
        writer.writerow(['train_line'])

        # Write rows
        for row in split_results:
            writer.writerow([row])

    print(f"Data has been written to {csv_file_path}")

# Function to join strings in forward direction
def join_strings_forward(strings):
    joined_strings = []
    for i in range(len(strings) - 1):
        j = i+1
        val = strings[i] + ' ' + strings[j]
        val = val.strip(" ")
        val = val.strip(",")
        val = val.strip(".")
        val = val.strip(" ")
        val = val.strip('"')
        # print(val)
        joined_strings.append(val)
    # print(joined_strings)
    return joined_strings


def generate_csv_storyline():
    with open('train_storyline.txt', 'r') as file:
        lines_stripped = file.readlines()
    # Print each line
    lines = [line.strip() for line in lines_stripped]  # Use strip() to remove the trailing newline character
    common_substrings = find_common_substrings(lines, min_length=10, max_length=30)
    common_substrings = get_sorted_common_substrings(common_substrings, 2)
    # print(common_substrings)
    # Use the top 5 common substrings for splitting (adjust as needed)
    top_substrings = [substr for substr, _ in common_substrings[:200]]
    split_results = split_lines_by_substrings(lines, top_substrings)
    for result in split_results:
        # print(result)
        pass
    final_strings = []
    for sublist in split_results:
        final_strings.extend(join_strings_forward(sublist))
    # print(final_strings)
    csv_file_path = '../data_storyline.csv'
    write_to_csv(csv_file_path, final_strings)


def generate_csv_cause():
    with open('train_cause.txt', 'r') as file:
        lines_stripped = file.readlines()
    # Print each line
    lines = [line.strip() for line in lines_stripped]  # Use strip() to remove the trailing newline character
    common_substrings = find_common_substrings(lines, min_length=10, max_length=30)
    common_substrings = get_sorted_common_substrings(common_substrings, 2)
    # print(common_substrings)
    # Use the top 5 common substrings for splitting (adjust as needed)
    top_substrings = [substr for substr, _ in common_substrings[:200]]
    split_results = split_lines_by_substrings(lines, top_substrings)
    for result in split_results:
        # print(result)
        pass
    final_strings = []
    for sublist in split_results:
        final_strings.extend(join_strings_forward(sublist))
    # print(final_strings)
    csv_file_path = '../data_cause.csv'
    write_to_csv(csv_file_path, final_strings)


if __name__ == '__main__':
    # Open the file for reading
    generate_csv_storyline()
    generate_csv_cause()
