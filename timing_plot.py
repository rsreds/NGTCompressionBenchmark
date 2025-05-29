import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#type,events,format,algo,level,time_seconds,filesize_byte

reading_timing = "../results/fixed_mc_timing_results_reading.csv"
generation_timing = "../results/mc_timing_results_generation.csv"

df_reading = pd.read_csv(reading_timing, sep=',', header=0)
df_generation = pd.read_csv(generation_timing, sep=',', header=0)
df_uncompressed = pd.read_csv(uncompressed_timing, sep=',', header=0)

colors = ['#5790fc', '#f89c20', '#e42536', '#7021dd']

fig, ax = plt.subplots(figsize=(10, 6))
df_reading[df_reading['format']=='TTree'].plot(x='events', y='time_seconds', kind='scatter', color=colors[0], label='TTree', marker='o', ax=ax)
# fitline
x = np.array(df_reading[df_reading['format']=='TTree']['events'])
y = np.array(df_reading[df_reading['format']=='TTree']['time_seconds'])
p = np.polyfit(x, y, 1)
ax.plot(x, p[0] * x + p[1], color=colors[0], linestyle='--', label='TTree fit')

df_reading[df_reading['format']=='RNTuple'].plot(x='events', y='time_seconds', kind='scatter', color=colors[1], label='RNTuple', marker='x', ax=ax)
# fitline
x = np.array(df_reading[df_reading['format']=='RNTuple']['events'])
y = np.array(df_reading[df_reading['format']=='RNTuple']['time_seconds'])
p = np.polyfit(x, y, 1)
ax.plot(x, p[0] * x + p[1], color=colors[1], linestyle='--', label='RNTuple fit')

plt.savefig("mc_reading_timing.png")

fig, ax = plt.subplots(figsize=(10, 6))
df_generation[df_generation['format']=='TTree'].plot(x='events', y='time_seconds', kind='scatter', color=colors[0], label='TTree', marker='o', ax=ax)
# fitline
x = np.array(df_generation[df_generation['format']=='TTree']['events'])
y = np.array(df_generation[df_generation['format']=='TTree']['time_seconds'])
p = np.polyfit(x, y, 1)
ax.plot(x, p[0] * x + p[1], color=colors[0], linestyle='--', label='TTree fit')

df_generation[df_generation['format']=='RNTuple'].plot(x='events', y='time_seconds', kind='scatter', color=colors[1], label='RNTuple', marker='x', ax=ax)
# fitline
x = np.array(df_generation[df_generation['format']=='RNTuple']['events'])
y = np.array(df_generation[df_generation['format']=='RNTuple']['time_seconds'])
p = np.polyfit(x, y, 1)
ax.plot(x, p[0] * x + p[1], color=colors[1], linestyle='--', label='RNTuple fit')
plt.savefig("mc_generation_timing.png")

