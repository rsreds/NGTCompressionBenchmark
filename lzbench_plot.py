# Compressor name,Compression speed,Decompression speed,Original size,Compressed size,Ratio,Filename
# zpaq 7.15 -1,18.18,87.37,8103957968,6491983387,80.11,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# zpaq 7.15 -2,7.32,84.22,8103957968,6411319566,79.11,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# zpaq 7.15 -3,3.84,6.48,8103957968,5474677847,67.56,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# zpaq 7.15 -4,1.61,1.54,8103957968,5130537023,63.31,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# zpaq 7.15 -5,0.55,0.54,8103957968,4458304721,55.01,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -0,25.66,46.82,8103957968,5326343118,65.73,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -1,22.11,47.14,8103957968,5350502861,66.02,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -2,18.65,47.20,8103957968,5355117144,66.08,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -3,13.51,47.82,8103957968,5350832735,66.03,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -4,5.84,48.27,8103957968,5361519041,66.16,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -5,3.75,48.11,8103957968,4983973336,61.50,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -6,2.93,47.98,8103957968,4984110023,61.50,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -7,2.64,47.71,8103957968,4980376591,61.46,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -8,2.40,47.41,8103957968,4982640469,61.48,../compression/store/uncompressed/data_RAW_RNTuple_5000.root
# lzma 24.09 -9,2.41,49.35,8103957968,4982640469,61.48,../compression/store/uncompressed/data_RAW_RNTuple_5000.root

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = '../results/lzbench_zpaq-lzma_RNTuple_5000.csv'

df = pd.read_csv(filename, sep=',', header=0)
colors = {'LZMA': '#5790fc', 'ZLIB': '#f89c20', 'ZSTD': '#e42536', 'LZ4': '#7021dd', 'ZPAQ': '#ff7f0e'}

# Split Compressor name into Algorithm (lzma or zpaq) and level which is kjust the last number without the sign
# for example: lzma 24.09 -2 -> lzma, 2
df[['Algorithm', 'Level']] = df['Compressor name'].str.split(' ', n=1, expand=True)
df['Algorithm'] = df['Algorithm'].str.upper()
df['Level'] = df['Level'].str.split(' ').str[-1].astype(int).abs()

num_events = 5000  # Number of events to consider
y_lims = [0, 30]  # Throughput limits
x_lims = [0, 100]  # Compression ratio limits

# Plot Ratio vs Compression speed with different colors for different algorithms and labels for different levels
fig, ax = plt.subplots(figsize=(10, 6))
# different colors for different compression algorithms
for algo in df['Algorithm'].unique():
    df[df['Algorithm'] == algo].plot(
        x='Ratio', y='Compression speed', kind='scatter', 
        # yerr='throughput_error_MBps',  # Remove or update if error column exists
        color=colors[algo], label=algo, marker='.', 
        ax=ax)
    for i, row in df[df['Algorithm'] == algo].iterrows():
        ax.annotate(row['Level'], (row['Ratio'], row['Compression speed']), textcoords="offset points", xytext=(-5, 5), ha='center', fontsize=8)

plt.xlabel('Compression Ratio')
plt.ylabel('Throughput (MB/s)')
plt.ylim(y_lims)
plt.xlim(x_lims)
plt.title(f'p-p collsion data in RNTuple format ({num_events} events)')
plt.savefig(f"lzbench_data_compression_ratio_throughput_RNTuple_{num_events}.png")

