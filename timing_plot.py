import ROOT
import mplhep as hep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use(hep.style.CMS) #1
plt.rcParams['figure.facecolor'] = 'white' #2
hep.cms.text('Preliminary') #3
#type,events,format,algo,level,avg_time_seconds,filesize_byte

reading_timing = "../results/data_timing_results_reading.csv"
generation_timing = "../results/data_timing_results_generation.csv"

df_reading = pd.read_csv(reading_timing, sep=',', header=0)
df_generation = pd.read_csv(generation_timing, sep=',', header=0)
# df_uncompressed = pd.read_csv(uncompressed_timing, sep=',', header=0)

colors = ['#5790fc', '#f89c20', '#e42536', '#964a8b']

fig, ax = plt.subplots()
hep.cms.text('Preliminary', loc=1) #3

# Plot TTree points and error bars
df_tt = df_reading[df_reading['format']=='TTree']
ax.errorbar(
    df_tt['events'],
    df_tt['avg_time_seconds'],
    yerr=df_tt['stdev_time'] if 'stdev_time' in df_tt else None,
    fmt='o',
    color=colors[0],
    capsize=2,
    label='TTree'
)
# Fit line
x = np.array(df_tt['events'])
y = np.array(df_tt['avg_time_seconds'])
p = np.polyfit(x, y, 1)
ax.plot(x, p[0] * x + p[1], color=colors[0], linestyle='--', label='TTree fit')

# Plot RNTuple points and error bars
df_rn = df_reading[df_reading['format']=='RNTuple']
ax.errorbar(
    df_rn['events'],
    df_rn['avg_time_seconds'],
    yerr=df_rn['stdev_time'] if 'stdev_time' in df_rn else None,
    fmt='s',
    color=colors[1],
    capsize=2,
    label='RNTuple'
)
# Fit line
x = np.array(df_rn['events'])
y = np.array(df_rn['avg_time_seconds'])
p = np.polyfit(x, y, 1)
ax.plot(x, p[0] * x + p[1], color=colors[1], linestyle='--', label='RNTuple fit')

plt.ylim(0,3)
plt.xlabel('Number of events')
plt.ylabel('Time (s)')
ax.legend()
plt.savefig("data_reading_timing.pdf", bbox_inches='tight')
plt.savefig("data_reading_timing.png", bbox_inches='tight')

# fig, ax = plt.subplots()
# hep.cms.text('Preliminary') #3
# df_generation[df_generation['format']=='TTree'].plot(x='events', y='avg_time_seconds', kind='scatter', color=colors[0], label='TTree', marker='o', ax=ax)

# x = np.array(df_generation[df_generation['format']=='TTree']['events'])
# y = np.array(df_generation[df_generation['format']=='TTree']['avg_time_seconds'])
# p = np.polyfit(x, y, 1)
# ax.plot(x, p[0] * x + p[1], color=colors[0], linestyle='--', label='TTree fit')

# df_generation[df_generation['format']=='RNTuple'].plot(x='events', y='avg_time_seconds', kind='scatter', color=colors[1], label='RNTuple', marker='s', ax=ax)
# # fitline
# x = np.array(df_generation[df_generation['format']=='RNTuple']['events'])
# y = np.array(df_generation[df_generation['format']=='RNTuple']['avg_time_seconds'])
# p = np.polyfit(x, y, 1)
# ax.plot(x, p[0] * x + p[1], color=colors[1], linestyle='--', label='RNTuple fit')
# plt.savefig("data_generation_timing.png")

