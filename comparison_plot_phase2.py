import ROOT
import mplhep as hep
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(hep.style.CMS) #1
plt.rcParams['figure.facecolor'] = 'white' #2
hep.cms.text('Preliminary') #3
#type,events,format,algo,level,time_seconds,filesize_byte

filename = '../results/complete_timing_results_Phas2_AVERAGED.csv'

df = pd.read_csv(filename, sep=',', header=0)

# $ du ~/data/compression/store/uncompressed/* | grep Phase
# 223892	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_RNTuple_10.root
# 2181344	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_RNTuple_100.root
# 10878852	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_RNTuple_500.root
# 100135952	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_RNTuple_5000.root
# 284396	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_TTree_10.root
# 2799124	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_TTree_100.root
# 13982768	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_TTree_500.root
# 128761956	/afs/cern.ch/user/s/srossiti/data/compression/store/uncompressed/mc_Phase2_TTree_5000.root


rntuple_mc_uncompressed = {10: 223892, 100: 2181344, 500: 10878852, 5000: 100135952}
ttree_mc_uncompressed = {10: 284396, 100: 2799124, 500: 13982768, 5000: 128761956}
# DATA

df_rntuple = df[df['format'] == 'RNTuple']
df_ttree = df[df['format'] == 'TTree']

num_events = 500
x_lims = [0.1,0.5]
y_lims = [0,70]

df_rntuple = df_rntuple[df_rntuple['events'] == num_events].copy()
df_ttree = df_ttree[df_ttree['events'] == num_events].copy()

df_rntuple_mc = df_rntuple[df_rntuple['type'] == 'mc'].copy()
df_ttree_mc = df_ttree[df_ttree['type'] == 'mc'].copy()

colors = {'LZMA': '#5790fc', 'ZLIB': '#f89c20', 'ZSTD': '#e42536', 'LZ4': '#964a8b'}
markers = {'LZMA': 'o', 'ZLIB': 's', 'ZSTD': '^', 'LZ4': 'D'}

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
    ax.legend(title=legend_title, loc='lower left')
    ax.set_xlabel('Compression Ratio')
    ax.set_ylabel('Throughput (MB/s)')
    ax.set_ylim(y_lims)
    ax.set_xlim(x_lims)
    # ax.set_title(title, pad=16)
    return fig, ax, annotations

fig, ax, annotations = plot_compression_vs_throughput(
    df_rntuple_mc,
    colors,
    "RNTuple",
    x_lims,
    y_lims,
)

[annotations['LZ4'][i].set_position((10, 0)) for i in [0]]
annotations['LZ4'][1].set_position((-10, -5))
annotations['LZ4'][2].set_position((-10, 5))
[annotations['ZSTD'][i].set_position((0, -12)) for i in [6, 7, 8]]
[annotations['ZLIB'][i].set_position((10, 0)) for i in [4,6, 7, 8]]
[annotations['LZMA'][i].set_text('') for i in [4,5,6,7,8]]
annotations['LZMA'][0].set_position((-10, 6))
annotations['LZMA'][2].set_position((-10, -7))
annotations['LZMA'][4].set_text('5-9')
annotations['LZMA'][4].set_ha('right')   

fig.savefig(f"phase2_compression_ratio_throughput_RNTuple_{num_events}.pdf", bbox_inches='tight')
fig.savefig(f"phase2_compression_ratio_throughput_RNTuple_{num_events}.png", bbox_inches='tight')

fig, ax, annotations = plot_compression_vs_throughput(
    df_ttree_mc,
    colors,
    "TTree",
    x_lims,
    y_lims,
)

[annotations['LZMA'][i].set_text('') for i in [4,5,6,7,8]]
annotations['LZMA'][0].set_position((-10, 5))
annotations['LZMA'][2].set_position((-10, -2))
annotations['LZ4'][1].set_position((10, 0))
annotations['LZMA'][4].set_text('5-9')
annotations['LZMA'][4].set_ha('right') 

fig.savefig(f"phase2_compression_ratio_throughput_TTree_{num_events}.pdf", bbox_inches='tight')
fig.savefig(f"phase2_compression_ratio_throughput_TTree_{num_events}.png", bbox_inches='tight')
