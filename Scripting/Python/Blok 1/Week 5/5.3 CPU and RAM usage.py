import psutil
cpu_cores = psutil.cpu_percent(interval=1, percpu=True)

# Print the list of CPU cores and their usage
def mylist():
    for i in range(len(cpu_cores)):
        print("CPU core " + str(i+1) + ": " + str(cpu_cores[i]) + "%")

dict = {
  mylist(),
  "And the ram usage is: ", psutil.virtual_memory().percent, "%"
}

print(dict)


