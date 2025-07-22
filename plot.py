import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "cmssw_bench_output.csv"

df = pd.read_csv(filename)

result = df.groupby(['Algorithm', 'Level']).agg({'Compressed': ['mean', 'std'], 'Uncompressed': ['mean', 'std'], 'Time': ['mean', 'std']})

colors = {'LZMA': '#5790fc', 'ZLIB': '#f89c20', 'ZSTD': '#e42536', 'LZ4': '#7021dd'}


# Filter out rows where Level is 0
result_noL0 = result[result.index.get_level_values('Level') != 0]

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
for algo, group in result_noL0['Compressed'].groupby('Algorithm'):
    ax.errorbar(group.index.get_level_values('Level'), group['mean'], yerr=group['std'], label=algo, color=colors[algo], marker='.')
ax.set_xlabel('Compression Level')
ax.set_ylabel('Compressed Size (bytes)')
ax.set_title('Compressed Size by Level for Each Algorithm')
ax.legend()
plt.savefig('plots/compressed_size_by_level.png')

# Uncompressed size by level for each algorithm

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
for algo, group in result['Uncompressed'].groupby('Algorithm'):
    ax.errorbar(group.index.get_level_values('Level'), group['mean'], yerr=group['std'], label=algo, color=colors[algo], marker='.')
ax.set_xlabel('Compression Level')
ax.set_ylabel('Uncompressed Size (bytes)')
ax.set_title('Uncompressed Size by Level for Each Algorithm')
ax.legend()
plt.savefig('plots/uncompressed_size_by_level.png')

# Time by level for each algorithm

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
for algo, group in result['Time'].groupby('Algorithm'):
    ax.errorbar(group.index.get_level_values('Level'), group['mean'], yerr=group['std'], label=algo, color=colors[algo], marker='.')
ax.set_xlabel('Compression Level')
ax.set_ylabel('Time (s)')
ax.set_title('Time by Level for Each Algorithm')
ax.legend()
plt.savefig('plots/time_by_level.png')

# Compression ratio by level for each algorithm

result_noL0['CompressionRatio'] = (result_noL0['Compressed']['mean'] / result_noL0['Uncompressed']['mean']) * 100

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
for algo, group in result_noL0['CompressionRatio'].groupby('Algorithm'):
    ax.plot(group.index.get_level_values('Level'), group, label=algo, color=colors[algo], marker='.')
ax.set_xlabel('Compression Level')
ax.set_ylabel('Compression Ratio')
ax.set_title('Compression Ratio by Level for Each Algorithm')
ax.legend()
plt.savefig('plots/compression_ratio_by_level.png')

# Throughput by level for each algorithm

result_noL0['Throughput'] = result_noL0['Uncompressed']['mean'] / result_noL0['Time']['mean'] / 1024 / 1024

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
for algo, group in result_noL0['Throughput'].groupby('Algorithm'):
    ax.plot(group.index.get_level_values('Level'), group, label=algo, color=colors[algo], marker='.')
ax.set_xlabel('Compression Level')
ax.set_ylabel('Throughput (MB/sec)')
ax.set_title('Throughput by Level for Each Algorithm')
ax.legend()
plt.savefig('plots/throughput_by_level.png')

# Scatter plot of the throughput by compression ratio for each algorithm with level label on each point

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
for algo, group in result_noL0.groupby('Algorithm'):
    ax.scatter(group['CompressionRatio'], group['Throughput'], label=algo, color=colors[algo], marker='.')
    for level, row in group.iterrows():
        ax.text(row['CompressionRatio'], row['Throughput'], str(level[1]), fontsize=8, ha='right')
ax.set_xlabel('Compression Ratio')
ax.set_ylabel('Throughput (MB/sec)')
ax.set_title('Throughput by Compression Ratio for Each Algorithm')
ax.legend()
plt.savefig('plots/throughput_by_compression_ratio.png')

# Single figure with compression ratio by level, throughput by level, and throughput by compression ratio for each algorithm
# in a 2x2 grid with the last plot covering the last two columns

fig = plt.figure(figsize=(14, 12))
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax3 = plt.subplot2grid((2, 2), (1, 0), colspan=2)

suptitle = fig.suptitle('CMSSW Compression Results on RECO 1000 Events')
suptitle.set_fontsize(18)

for algo, group in result_noL0.groupby('Algorithm'):
    ax1.plot(group.index.get_level_values('Level'), group['CompressionRatio'], label=algo, color=colors[algo], marker='.')
ax1.set_xlabel('Compression Level')
ax1.set_ylabel('Compression Ratio')
ax1.set_title('Compression Ratio by Level for Each Algorithm')
ax1.legend()

for algo, group in result_noL0.groupby('Algorithm'):
    ax2.plot(group.index.get_level_values('Level'), group['Throughput'], label=algo, color=colors[algo], marker='.')
ax2.set_xlabel('Compression Level')
ax2.set_ylabel('Throughput (MB/sec)')
ax2.set_title('Throughput by Level for Each Algorithm')
ax2.legend()

for algo, group in result_noL0.groupby('Algorithm'):
    ax3.scatter(group['CompressionRatio'], group['Throughput'], label=algo, color=colors[algo], marker='.')
    for level, row in group.iterrows():
        ax3.text(row['CompressionRatio'], row['Throughput'], str(level[1]), fontsize=8, ha='right')
ax3.set_xlabel('Compression Ratio')
ax3.set_ylabel('Throughput (MB/sec)')
ax3.set_title('Throughput by Compression Ratio for Each Algorithm')
ax3.legend()

plt.savefig('plots/single_figure.png')
