import subprocess
import fcntl
import os
import time

# Start the subprocess to run 'ls -l' command
process = subprocess.Popen(
    ["ls", "-l"],  # Command to run
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Set the stdout file descriptor to non-blocking mode
fd = process.stdout.fileno()
flags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

output = []

def read_nonblocking(process, output):
    try:
        while True:
            line = process.stdout.readline()
            if line:
                output.append(line)
            else:
                break  # No more lines available to read
    except:
        pass  # Handle the case where readline() would block

# Continuously read from the process output
for i in range(10):  # Iterate a few times to ensure all output is captured
    read_nonblocking(process, output)
    
    if i < len(output):
        print(i, output[i].strip())
    else:
        print(f"No new output at iteration {i}")
    
    # Optionally add a small sleep to prevent busy-waiting
    time.sleep(0.1)

# After the loop, print all the captured output
print("\nFinal Output:")
print("".join(output))
