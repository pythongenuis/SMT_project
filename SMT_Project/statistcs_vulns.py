import os
import time
import statistics
import matplotlib.pyplot as plt
import numpy as np
# list_file_to_execute = ["10vulns.smt", "20vulns.smt", "30vulns.smt", "40vulns.smt", "50vulns.smt", "100vulns.smt", "200vulns.smt",
#                         "300vulns.smt", "400vulns.smt", "500vulns.smt",
#                         "1000vulns.smt", "2000vulns.smt",
#                         "3000vulns.smt", "4000vulns.smt",  "5000vulns.smt", "10000vulns.smt", ]
list_file_to_execute = ["10vulns.smt", "20vulns.smt", "30vulns.smt", "40vulns.smt", "50vulns.smt", "100vulns.smt"]
list_time = list()
list_file = list()
for e in list_file_to_execute:
    file_to_execute = e
    list_time_execution = list()
    i = 0
    while i < 10:
        start_time = time.time()
        os.system('cvc4-1.6-win64-opt.exe --lang smt '+file_to_execute)
        list_time_execution.append(time.time() - start_time)
        i = i + 1
    mean_time = statistics.mean(list_time_execution)
    list_time.append(mean_time)
    list_file.append(int(str(file_to_execute)[0:-9]))
print("la list du tesmps est: " + str(list_time))
print("la list des fichier est: " + str(list_file))
plt.plot(list_file, list_time)
plt.xlabel('vulns (v)')
plt.ylabel('time (s)')
plt.title('number of vulns in functions of exucution time')
plt.grid(True)
plt.savefig("test.png")
plt.show()
