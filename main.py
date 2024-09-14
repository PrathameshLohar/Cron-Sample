from datetime import datetime

# Define the filename where timestamps will be appended
filename = 'timestamps.txt'

# Get the current date and time
now = datetime.now()
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

# Open the file in append mode and write the timestamp
with open(filename, 'a') as file:
    file.write(f'{timestamp}\n')

print(f'Timestamp {timestamp} appended to {filename}')
