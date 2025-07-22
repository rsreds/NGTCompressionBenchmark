import ROOT
import mplhep as hep
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(hep.style.CMS) #1
plt.rcParams['figure.facecolor'] = 'white' #2
hep.cms.text('Preliminary') #3
#type,events,format,algo,level,time_seconds,filesize_byte

filename = '../results/complete_timing_results_AVERAGED.csv'

df = pd.read_csv(filename, sep=',', header=0)

rntuple_data_uncompressed = {1: 8520, 10: 22992, 100: 169348, 1000: 1592364, 2000: 3169968, 3000: 4747684, 4000: 6331500, 5000: 7914028}
ttree_data_uncompressed = {1: 8676, 10: 23008, 100: 167936, 1000: 1576748, 2000: 3138564, 3000: 4700496, 4000: 6268524, 5000: 7835268}
rntuple_mc_uncompressed = {1: 9508, 10: 26888, 100: 197776, 1000: 1934148, 2000: 3847540, 3000: 5766776, 4000: 7684076, 5000: 9612704}
ttree_mc_uncompressed = {1: 9668, 10: 26908, 100: 196372, 1000: 1918584, 2000: 3816240, 3000: 5719736, 4000: 7621292, 5000: 9534180}
# DATA

df_rntuple = df[df['format'] == 'RNTuple']
df_ttree = df[df['format'] == 'TTree']

num_events = 5000
x_lims = [0.5,0.9]
y_lims = [0,100]

df_rntuple = df_rntuple[df_rntuple['events'] == num_events].copy()
df_ttree = df_ttree[df_ttree['events'] == num_events].copy()

df_rntuple_data = df_rntuple[df_rntuple['type'] == 'data'].copy()
df_ttree_data = df_ttree[df_ttree['type'] == 'data'].copy()
df_rntuple_mc = df_rntuple[df_rntuple['type'] == 'mc'].copy()
df_ttree_mc = df_ttree[df_ttree['type'] == 'mc'].copy()


colors = {'LZMA': '#5790fc', 'ZLIB': '#f89c20', 'ZSTD': '#e42536', 'LZ4': '#964a8b'}
markers = {'LZMA': 'o', 'ZLIB': 's', 'ZSTD': '^', 'LZ4': 'D'}

df_rntuple_data.loc[:, 'compression_ratio'] = df_rntuple_data.loc[:, 'avg_filesize_kB'] / rntuple_data_uncompressed[num_events]
df_rntuple_data.loc[:, 'throughput_MBps'] = df_rntuple_data.loc[:, 'avg_filesize_kB'] / (df_rntuple_data.loc[:, 'avg_time_seconds'] * 1024)
# given stdev_time the standard deviation of the time in seconds copute the error bar for the throughput
df_rntuple_data.loc[:, 'throughput_error_MBps'] = df_rntuple_data.loc[:, 'stdev_time'] * df_rntuple_data.loc[:, 'avg_filesize_kB'] / (1024 * df_rntuple_data.loc[:, 'avg_time_seconds'] ** 2)


df_ttree_data.loc[:, 'compression_ratio'] = df_ttree_data.loc[:, 'avg_filesize_kB'] / ttree_data_uncompressed[num_events]
df_ttree_data.loc[:, 'throughput_MBps'] = df_ttree_data.loc[:, 'avg_filesize_kB'] / (df_ttree_data.loc[:, 'avg_time_seconds'] * 1024)
df_ttree_data.loc[:, 'throughput_error_MBps'] = df_ttree_data.loc[:, 'stdev_time'] * df_ttree_data.loc[:, 'avg_filesize_kB'] / (1024 * df_ttree_data.loc[:, 'avg_time_seconds'] ** 2)

df_rntuple_mc.loc[:, 'compression_ratio'] = df_rntuple_mc.loc[:, 'avg_filesize_kB'] / rntuple_mc_uncompressed[num_events]
df_rntuple_mc.loc[:, 'throughput_MBps'] = df_rntuple_mc.loc[:, 'avg_filesize_kB'] / (df_rntuple_mc.loc[:, 'avg_time_seconds'] * 1024)
df_rntuple_mc.loc[:, 'throughput_error_MBps'] = df_rntuple_mc.loc[:, 'stdev_time'] * df_rntuple_mc.loc[:, 'avg_filesize_kB'] / (1024 * df_rntuple_mc.loc[:, 'avg_time_seconds'] ** 2)

df_ttree_mc.loc[:, 'compression_ratio'] = df_ttree_mc.loc[:, 'avg_filesize_kB'] / ttree_mc_uncompressed[num_events]
df_ttree_mc.loc[:, 'throughput_MBps'] = df_ttree_mc.loc[:, 'avg_filesize_kB'] / (df_ttree_mc.loc[:, 'avg_time_seconds'] * 1024)
df_ttree_mc.loc[:, 'throughput_error_MBps'] = df_ttree_mc.loc[:, 'stdev_time'] * df_ttree_mc.loc[:, 'avg_filesize_kB'] / (1024 * df_ttree_mc.loc[:, 'avg_time_seconds'] ** 2)

def plot_compression_vs_throughput(df, colors, data_format, x_lims, y_lims):
    fig, ax = plt.subplots()
    hep.cms.text('Preliminary', loc=1)
    annotations = {}
    for algo in df['algo'].unique():
        annotations[algo] = []
        df_filtered_algo = df[df['algo'] == algo]
        ax.errorbar(
            x=df_filtered_algo['compression_ratio'],
            y=df_filtered_algo['throughput_MBps'],
            yerr=df_filtered_algo['throughput_error_MBps'],
            color=colors[algo],
            capsize=3,
            label=algo,
            fmt=markers[algo]
        )
        for i, row in df_filtered_algo.iterrows():
            a = ax.annotate(
                row['level'],
                (row['compression_ratio'], row['throughput_MBps']),
                textcoords="offset points",
                xytext=(-10, 0),
                ha='center',
                va='center',
                fontsize=16
            )
            annotations[algo].append(a)

    legend_title = f'{data_format}'
    ax.legend(title=legend_title)
    ax.set_xlabel('Compression Ratio')
    ax.set_ylabel('Throughput (MB/s)')
    ax.set_ylim(y_lims)
    ax.set_xlim(x_lims)
    # ax.set_title(title, pad=16)
    return fig, ax, annotations

fig, ax, annotations = plot_compression_vs_throughput(
    df_rntuple_data,
    colors,
    "RNTuple",
    x_lims,
    y_lims,
)
[annotations['LZ4'][i].set_position((10, 0)) for i in [0, 4, 6, 8]]
[annotations['ZLIB'][i].set_position((10, 0)) for i in [6, 8]]
[annotations['LZMA'][i].set_text('') for i in [1,2,4,5,6,7,8]]
annotations['LZMA'][0].set_text('1-3')
annotations['LZMA'][0].set_ha('right')
annotations['LZMA'][3].set_text('4-9')
annotations['LZMA'][3].set_ha('right')   
fig.savefig(f"data_compression_ratio_throughput_RNTuple_{num_events}.pdf", bbox_inches='tight')
fig.savefig(f"data_compression_ratio_throughput_RNTuple_{num_events}.png", bbox_inches='tight')

fig, ax, annotations = plot_compression_vs_throughput(
    df_ttree_data,
    colors,
    "RNTuple",
    x_lims,
    y_lims,
)
[annotations['LZ4'][i].set_position((10, 0)) for i in [0, 6]]
annotations['LZ4'][1].set_position((-10, -5))
annotations['LZ4'][2].set_position((-10, 5))
[annotations['ZLIB'][i].set_position((10, 0)) for i in [0, 7]]
[annotations['LZMA'][i].set_text('') for i in [1,2,4,5,6,7,8]]
annotations['LZMA'][0].set_text('1-3')
annotations['LZMA'][0].set_ha('right')
annotations['LZMA'][3].set_text('4-9')
annotations['LZMA'][3].set_ha('right') 
fig.savefig(f"data_compression_ratio_throughput_TTree_{num_events}.pdf", bbox_inches='tight')
fig.savefig(f"data_compression_ratio_throughput_TTree_{num_events}.png", bbox_inches='tight')

fig, ax, annotations = plot_compression_vs_throughput(
    df_rntuple_mc,
    colors,
    "TTree",
    x_lims,
    y_lims,
)
fig.savefig(f"mc_compression_ratio_throughput_RNTuple_{num_events}.pdf", bbox_inches='tight')
fig.savefig(f"mc_compression_ratio_throughput_RNTuple_{num_events}.png", bbox_inches='tight')

fig, ax, annotations = plot_compression_vs_throughput(
    df_ttree_mc,
    colors,
    "TTree",
    x_lims,
    y_lims,
)
fig.savefig(f"mc_compression_ratio_throughput_TTree_{num_events}.pdf", bbox_inches='tight')
fig.savefig(f"mc_compression_ratio_throughput_TTree_{num_events}.png", bbox_inches='tight')