import psutil
cpu_cores = psutil.cpu_percent(interval=1, percpu=True)

# Print the list of CPU cores and their usage
for i in range(len(cpu_cores)):
    print("CPU core " + str(i+1) + ": " + str(cpu_cores[i]) + "%")