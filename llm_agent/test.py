import subprocess
import fcntl
import os
import time

# https://stackabuse.com/pythons-os-and-subprocess-popen-commands/ # TODO
process = subprocess.Popen(
    ["/bin/bash"], # this is to keep the process running
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    stdin=subprocess.PIPE,
    shell=True, # security risk, https://stackoverflow.com/questions/12605498/how-to-use-subprocess-popen-python
    text=True,
    bufsize=-1
)

# set the stdout file descriptor to non-blocking mode
# https://docs.python.org/3/library/fcntl.html
# https://man7.org/linux/man-pages/man2/fcntl.2.html
fcntl.fcntl(process.stdout, fcntl.F_SETFL, os.O_NONBLOCK) # flag will be 2048

try:
    while True:
        command = input("Enter command: ")
        if command.lower() == "exit":
            break
        else:
            process.stdin.write(command + "\n")
            process.stdin.flush()

            
            output = []
            while True:
                try:
                    line = process.stdout.readline()
                    if not line:
                        break
                    output.append(line)
                    # output = [line for line in process.stdout]
                except BlockingIOError: # just in case file read gets blocked
                    break
            
            print("".join(output))
finally:
    process.terminate()
    process.wait()



# ===========================================================================