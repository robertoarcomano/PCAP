# import subprocess

# output = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
# print(output.stdout.decode('utf-8'))
for line in open("/var/log/syslog", "rt"):
    field = line[:16]
    print(field)
