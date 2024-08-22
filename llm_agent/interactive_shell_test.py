# import subprocess
# import select
# import fcntl
# import os

# process = subprocess.Popen(
#     ["/bin/bash"],
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )


# # https://docs.python.org/3/library/fcntl.html
# # set the stdout file descriptor to non-blocking mode
# fd = process.stdout.fileno() # file descriptor id
# flags = fcntl.fcntl(fd, fcntl.F_GETFL) # https://man7.org/linux/man-pages/man2/fcntl.2.html
# # fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
# fcntl.fcntl(fd, fcntl.F_SETFL, os.O_NONBLOCK)

# while True:
#     command = input("Enter command: ")
#     # command = "ls -l"
#     if command.lower() == "exit":
#         break
#     else:
#         process.stdin.write(command + "\n")
#         process.stdin.flush()

#         output = [line for line in process.stdout]
#         print("".join(output))
#         break # TODO

# # Function to send commands and get output
# # def interact_with_shell(command):
# #     process.stdin.write(command + "\n")
# #     process.stdin.flush()
    
# #     output = []
    
# #     while True:
# #         ready, _, _ = select.select([process.stdout], [], [], 5) # read, write, exceptions, timeout
# #         if ready:
# #             line = process.stdout.readline()
# #             if line:
# #                 output.append(line)
# #             else:
# #                 break
# #         else:
# #             break
# #     output = output[::-1]
# #     return ''.join(output)

# # try:
# #     while True:
# #         # Get command from the user
# #         user_command = input("Enter command: ")
# #         if user_command.lower() in ["exit", "quit"]:
# #             break 

# #         result = interact_with_shell(user_command)
# #         print(result)

# # except KeyboardInterrupt:
# #     print("Shell terminated by user.")

# # finally:
# #     process.terminate()  # Terminate the shell process when done





# # # parent_process.py
# # from subprocess import Popen, PIPE

# # with Popen(["/bin/bash"], stdout=PIPE, stdin = PIPE) as p:
# #     while True:
# #         # Use read1() instead of read() or Popen.communicate() as both blocks until EOF
# #         # https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1
# #         text = p.stdout.read1().decode("utf-8")
# #         print(text, end='', flush=True)


# # # child_process.py
# # from time import sleep

# # while True:
# #     # Make sure stdout writes are flushed to the stream
# #     print("Spam!", end=' ', flush=True)
# #     # Sleep to simulate some other work
# #     sleep(1)