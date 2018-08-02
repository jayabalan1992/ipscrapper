#This python program recursively search all the files inside the directory passed as argument and create a csv file with extracted hostnames
import csv,re,sys
from os import listdir
from os.path import isfile,join
with open("output_hosts.csv","w",newline='') as csvfile:
    csvwrite=csv.writer(csvfile)
    csvwrite.writerow(["Hostname", "What is it?", "Path to the file"])
    def dirs(path):
        dirs_list=listdir(path)
        for i in  dirs_list:
            if isfile(join(path,i)):
                try:
                    with open(join(path,i),"r") as f:
                        for line in f:
                            test=re.search(r'(^([a-zA-Z0-9-_]+).*\.com)',line)
                            if test:
                                csvwrite.writerow([test.group(1).split()[-1]," ",join(path,i)[27:], test.group()])
                except UnicodeDecodeError:
                    pass
            else:
                dirs(join(path,i))
    dirs(sys.argv[1])
