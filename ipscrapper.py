#This python program recursively search all the files inside the directory passed as command line argument and create a csv file with extracted IP's
import csv,re,socket,sys
from os import listdir
from os.path import isfile,join
with open("output.csv","w",newline='') as csvfile:
    csvwrite=csv.writer(csvfile)
    csvwrite.writerow(["IP Address", "host or network name", "Path", "DNS Name"])
    def dirs(path):
        dirs_list=listdir(path)
        for i in  dirs_list:
            if isfile(join(path,i)):
                try:
                    with open(join(path,i),"r") as f:
                        for line in f:
                            test=re.search(r'(?<!\d)(?!0|127)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
                            if test:
                                try:
                                    host=socket.gethostbyaddr(test.group(0))[0]
                                except Exception:
                                    host="Not found"
                                print(test.group(0), host, join(path,i))
                                csvwrite.writerow([test.group(0), host, join(path,i)[27:], "DNS Name"])
                except:
                    with open(join(path,i),"rb") as f:
                        for line in f:
                            test = re.search(b'(?<!\d)(?!0|127)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                            if test:
                                print(test.group(0), "Not found", join(path,i)[27:])
                                csvwrite.writerow([test.group(0), "Not found", join(path,i)])
            else:
                dirs(join(path,i))
    dirs(sys.argv[1])