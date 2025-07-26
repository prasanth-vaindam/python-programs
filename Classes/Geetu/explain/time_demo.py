import time

total_start_time = time.time()

print(total_start_time)

for i in range(1, 6):
    print(f"Processing step {i}...")
    time.sleep(1)  # Simulate some processing time
total_end_time = time.time()

print(f"All steps completed. end time is {total_end_time}")

print(f"Total processing time: {total_end_time - total_start_time:.2f} seconds")