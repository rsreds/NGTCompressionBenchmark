import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Algorithm,Level,Events,Uncompressed,Compressed,Time,Filename,Iteration
# LZMA,0,1000,12947519112,12947477664,828.5167472362518,step4_LZMA0_1000.root,0
# LZMA,0,1000,12947593712,12947552264,832.8078739643097,step4_LZMA0_1000.root,1
# ...
# LZMA,0,1000,12947681679,12947640231,829.324205160141,step4_LZMA0_1000.root,7
# LZMA,0,1000,12947596692,12947555244,829.3294920921326,step4_LZMA0_1000.root,8
# LZMA,0,1000,12947562158,12947520710,831.7952272891998,step4_LZMA0_1000.root,9
# LZMA,1,1000,12457274089,4516780443,965.3104631900787,step4_LZMA1_1000.root,0
# LZMA,1,1000,12457293793,4517003733,964.7467947006226,step4_LZMA1_1000.root,1
# LZMA,1,1000,12457295819,4516808341,963.7011907100677,step4_LZMA1_1000.root,2
# ...
# LZ4,9,1000,12539261108,5658615828,867.0716798305511,step4_LZ49_1000.root,8
# LZ4,9,1000,12539313932,5658513079,868.8102641105652,step4_LZ49_1000.root,9
# ZSTD,0,1000,12947592701,12947551253,832.9600019454956,step4_ZSTD0_1000.root,0
# ZSTD,0,1000,12947589769,12947548321,839.8266215324402,step4_ZSTD0_1000.root,1
# ...

filename = "cmssw_bench_output.csv"

df = pd.read_csv(filename)

result = df.groupby(['Algorithm', 'Level']).agg({'Compressed': ['mean', 'std'], 'Uncompressed': ['mean', 'std'], 'Time': ['mean', 'std']})

colors = {'LZMA': '#5790fc', 'ZLIB': '#f89c20', 'ZSTD': '#e42536', 'LZ4': '#7021dd'}

# Plot
# the compressed size by level for each algorithm
# the uncompressed size by level for each algorithm
# the time by level for each algorithm
# the compression ratio by level for each algorithm
# the throughput by level for each algorithm
# a scatter plot of the throughput by compression ratio for each algorithm with level label on each point
# save the plot as a png file in the plots directory

# Compressed size by level for each algorithm

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
