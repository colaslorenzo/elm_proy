import os

with open('ip_localhost.txt', "r") as f_in:
  for line in f_in:
    ip = line.strip()

cmd = "rm ip_localhost.txt"
os.system(cmd)

print "Current IP localhost:"
print ip + "\n"

cmd = "elm-reactor --address " + ip
os.system(cmd)
