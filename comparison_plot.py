import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#type,events,format,algo,level,time_seconds,filesize_byte

filename = '../results/mc_timing_results_recompress.csv'

df = pd.read_csv(filename, sep=',', header=0)

df_rntuple = df[df['format'] == 'RNTuple']
df_ttree = df[df['format'] == 'TTree']

# uncompressed
# data,1,RNTuple,5.18,8520
# data,1,TTree,3.43,8652
# step3,1,RNTuple,4.90,9508
# step3,1,TTree,3.42,9644
# data,10,RNTuple,5.11,22996
# data,10,TTree,3.60,22980
# step3,10,RNTuple,5.12,26932
# step3,10,TTree,3.51,26924
# data,100,RNTuple,7.12,169348
# data,100,TTree,4.87,167908
# step3,100,RNTuple,7.46,198136
# step3,100,TTree,5.27,196712
# data,1000,RNTuple,27.28,1592368
# data,1000,TTree,21.05,1576692
# step3,1000,RNTuple,31.34,1938592
# step3,1000,TTree,23.92,1922968
# data,5000,RNTuple,153.19,7914028
# data,5000,TTree,83.13,7835084
# step3,5000,RNTuple,157.58,9634188
# step3,5000,TTree,96.10,9555456


rntuple_uncompressed = {1: 8520, 10: 22996, 100: 169348, 1000: 1938592, 5000: 7914028}
ttree_uncompressed = {1: 8652, 10: 22980, 100: 167908, 1000: 1922968, 5000: 7835084}

colors = {'LZMA': '#5790fc', 'ZLIB': '#f89c20', 'ZSTD': '#e42536', 'LZ4': '#7021dd'}

num_events = 1000
df_rntuple = df_rntuple[df_rntuple['events'] == num_events]
df_ttree = df_ttree[df_ttree['events'] == num_events]

df_rntuple['compression_ratio'] = df_rntuple['filesize_kB'] / rntuple_uncompressed[num_events]
df_rntuple['throughput_MBps'] = df_rntuple['filesize_kB'] / (df_rntuple['time_seconds'] * 1024)

df_ttree['compression_ratio'] = df_ttree['filesize_kB'] / ttree_uncompressed[num_events]
df_ttree['throughput_MBps'] = df_ttree['filesize_kB'] / (df_ttree['time_seconds'] * 1024)

fig, ax = plt.subplots(figsize=(10, 6))
# different colors for different compression algorithms
for algo in df_rntuple['algo'].unique():
    df_rntuple[df_rntuple['algo'] == algo].plot(x='compression_ratio', y='throughput_MBps', kind='scatter', color=colors[algo], label=algo, marker='.', ax=ax)
    # add a label for the point with the level
    for i, row in df_rntuple[df_rntuple['algo'] == algo].iterrows():
        ax.annotate(row['level'], (row['compression_ratio'], row['throughput_MBps']), textcoords="offset points", xytext=(-5, 5), ha='center', fontsize=8)

plt.xlabel('Compression Ratio')
plt.ylabel('Throughput (MB/s)')
plt.savefig("mc_compression_ratio_throughput_RNTuple.png")

fig, ax = plt.subplots(figsize=(10, 6))
# different colors for different compression algorithms
for algo in df_ttree['algo'].unique():
    df_ttree[df_ttree['algo'] == algo].plot(x='compression_ratio', y='throughput_MBps', kind='scatter', color=colors[algo], label=algo, marker='.', ax=ax)
    # add a label for the point with the level
    for i, row in df_ttree[df_ttree['algo'] == algo].iterrows():
        ax.annotate(row['level'], (row['compression_ratio'], row['throughput_MBps']), textcoords="offset points", xytext=(-5, 5), ha='center', fontsize=8)
plt.xlabel('Compression Ratio')
ax.ticklabel_format(axis='x', useOffset=False, style='plain')
plt.ylabel('Throughput (MB/s)')
plt.savefig("mc_compression_ratio_throughput_TTree.png")