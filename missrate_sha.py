import matplotlib.pyplot as plt

plt.figure()

# Sha benchmark
# LRU Miss Rate
x = [1,2, 4, 8]
total_miss_rate = [0.049225, 0.047756, 0.045998, 0.011583]
plt.plot(x, total_miss_rate, label="LRU")

# Random Performance
x = [2, 4, 8]
total_miss_rate = [0.055516, 0.059899, 0.041362] 
plt.plot(x, total_miss_rate, label="Random")

# My Policy(NMRU) Performance
x = [2, 4, 8]
total_miss_rate = [0.047756, 0.052512, 0.037947]
plt.plot(x, total_miss_rate, label="My Policy")


plt.xlabel('Associativity')
plt.ylabel('Total Miss Rates')
plt.title("Comparison in terms of Total Miss Rates on Sha")

plt.grid()
plt.legend()
plt.savefig('Total Miss Rate_Sha.png')
plt.close()
