import re
import subprocess
import time 
waytoscript="/test/start"
waytolist="/test/apt_list.txt"
waytologs="/test/logs_net"
inst_net="/test/inst_net"
start = "net-tools" 
end = "[installed]"
middle = "stable,now" 
subprocess.run(["bash", waytoscript])
time.sleep(5)
with open(waytolist, "r") as file: 
    content = file.read()
    x = re.search("^start'/'*middle' 'end$", content)
    if x: 
        subprocess.run(["bash", waytologs]) 
        time.sleep(3)
    else:
        subprocess.run(["bash", inst_net])
        time.sleep(5)
        subprocess.run(["bash", waytologs])
        time.sleep(3)
print("Ready!")
