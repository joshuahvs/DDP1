# Sample data
data = [
    ["Name", "Age", "City"],
    ["John", 25, "New love"],
    ["Alice", 30, "San Francisco"],
    ["Bob", 22, "Los Angeles"]
]

# Specify the file path
csv_file_path = "output.csv"

# Open the file in write mode
with open(csv_file_path, mode='w') as file:
    # Write the header
    file.write(','.join(map(str, data[0])) + '\n')

    # Write the data rows
    for row in data[1:]:
        file.write(','.join(map(str, row)) + '\n')

print(f"Data has been successfully written to {csv_file_path}")

