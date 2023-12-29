with open('data.txt', 'r') as file:
    # Read and print each line with line numbers
    for i, line in enumerate(file, start=1):
        print(f"Line {i}: {line.strip()}")
