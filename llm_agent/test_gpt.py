# # import subprocess
# # import fcntl
# # import os
# # import time

# # process = subprocess.Popen(
# #     ["/bin/bash"],
# #     stdout=subprocess.PIPE,
# #     stderr=subprocess.PIPE,
# #     stdin=subprocess.PIPE,
# #     text=True,
# #     # bufsize=3
# # )

# # fcntl.fcntl(process.stdout, fcntl.F_SETFL, os.O_NONBLOCK)

# # try:
# #     while True:
# #         command = input("Enter command: ")
# #         if command.lower() == "exit":
# #             break
# #         else:
# #             process.stdin.write(command + "\n")
# #             process.stdin.flush()

# #             output = []
# #             while True:
# #                 try:
# #                     line = process.stdout.readline()
# #                     if not line:
# #                         break
# #                     output.append(line)
# #                 except BlockingIOError:
# #                     break

# #             # time.sleep(0.1) # ensure buffer fills and flushed
# #             # while True:
# #             #     try:
# #             #         line = process.stdout.readline()
# #             #         if not line:
# #             #             break
# #             #         output.append(line)
# #             #     except BlockingIOError:
# #             #         break

# #             print("".join(output))
# # finally:
# #     process.terminate()
# #     process.wait()


# import subprocess
# import fcntl
# import os
# cmd = ["/bin/bash"]
# pipe = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin = subprocess.PIPE)
# # out, err = pipe.communicate()
# # result = out.decode()
# # print (result) 

# pipe.stdin.write("ls -a".encode())
# pipe.stdin.flush()
# # out, err = pipe.communicate()
# fcntl.fcntl(pipe.stdout, fcntl.F_SETFL, os.O_NONBLOCK)
# out = pipe.stdout
# print([o for o in out])