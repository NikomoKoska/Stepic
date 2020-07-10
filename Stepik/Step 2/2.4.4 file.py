filename = 'dataset_24465_4.txt'
original_lines = []
with open(filename, 'r') as f:
    original_lines = [line for line in f.readlines()]

original_lines.reverse()
with open('write_file.txt', 'w') as f:
    f.writelines(original_lines)
