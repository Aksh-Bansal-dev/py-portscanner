import socket
import sys
from multiprocessing import Process
import os, time


def isValidIP(addr):
    try:
        nums = addr.split(".")
        if len(nums)!=4:
            return False
        else:
            for i in range(4):
                if int(nums[i])>255 or int(nums[i])<0:
                    return False
            return True
    except:
        return False

def portScan(port, target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, int(port)))
        return True
    except: 
        return False

def search(port, target):
    if port!=0:
        if portScan(port, target):
            print(f"port {port} is open on IP {target}")
        else:
            print(f"port {port} is closed on IP {target}")
    else:
        def ranger(start, end):
            for i in range(start,end):
                if portScan(i, target):
                    print(f"port {i} is open on IP {target}")
        processes = []
        cpuCount = os.cpu_count()
        maxRange = 65536
        for i in range(cpuCount):
            start = int(1+i*(maxRange/cpuCount))
            end = int(1+(i+1)*(maxRange/cpuCount));
            print(f"Utilizing core {i+1}")
            processes.append(Process(target=ranger, args=[start, end]))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

def main():
    args = sys.argv
    n = len(args)
    port = 0
    target = "127.0.0.1"

    try:
        if n==2 and args[1]=="-h":
            print("Use -p <port_number> to specify the port.\nUse -i <ip_addr> to scan on that IP Address.\n")
        elif n<=5 and n>2:
            gogo = False
            allGood = True
            for i,flag in enumerate(args):
                if i<1:
                    continue
                if flag=="-p":
                    if i<len(args)-1 and int(args[i+1])>0:
                        port = int(args[i+1])
                        gogo = True

                    else:
                        raise Exception("Error")
                elif flag=="-i":
                    if i<len(args)-1:
                        allGood = isValidIP(args[i+1])
                        if not allGood:
                            print("Invalid Ip Address.\nWe currently support IPv4 addresses only.")
                            break
                        else:
                            target = args[i+1]
                            gogo = True
                    else:
                        raise Exception("Error")
                else:
                    if gogo:
                        gogo = False
                        continue
                    else:
                        raise Exception("Error")
            if allGood:
                search(port, target)

        elif n==1:
            search(port, target)
        
        else:
            print("Invalid arguments! \nUse -h to get help")
    except:
        print("Invalid arguments! \nUse -h to get help")

startTime = time.time()
main()
endTime = time.time()
print(f"\nExecuted in {int(1000*(endTime-startTime))} ms.\n")
