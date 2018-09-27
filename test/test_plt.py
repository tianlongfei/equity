import matplotlib.pyplot as plt
import numpy as np


'matplotlib'
'整体风格，style'
# print(plt.style.available)
# ['bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test']

# plt.style.use('bmh')
# plt.style.use('classic')
# plt.style.use('dark_background')
# plt.style.use('fast')
# plt.style.use('fivethirtyeight')
# plt.style.use('ggplot')
# plt.style.use('grayscale')
# plt.style.use('seaborn-bright')
# plt.style.use('seaborn-colorblind')
# plt.style.use('seaborn-dark-palette')
# plt.style.use('seaborn-dark')
# plt.style.use('seaborn-darkgrid')
# plt.style.use('seaborn-deep')
# plt.style.use('seaborn-muted')
# plt.style.use('seaborn-notebook')
# plt.style.use('seaborn-paper')
# plt.style.use('seaborn-pastel')
# plt.style.use('seaborn-poster')
# plt.style.use('seaborn-talk')
# plt.style.use('seaborn-ticks')
# plt.style.use('seaborn-white')
# plt.style.use('seaborn-whitegrid')
# plt.style.use('seaborn')
# plt.style.use('Solarize_Light2')
# plt.style.use('tableau-colorblind10')
# plt.style.use('_classic_test')

'各部分颜色，color，density=True后，坐标加起来不等于1，返回值'


'透明度，alpha'
# 从0-1的数字


np.random.seed(19680801)

dt = 0.01
t = np.arange(0, 30, dt)
nse1 = np.random.randn(len(t))                 # white noise 1
nse2 = np.random.randn(len(t))                 # white noise 2

# Two signals with a coherent part at 10Hz and a random part
s1 = np.sin(2 * np.pi * 10 * t) + nse1
s2 = np.sin(2 * np.pi * 10 * t) + nse2

fig, axs = plt.subplots(2, 2)
axs[0][0].plot(t, s1, t, s2)
axs[0][0].set_xlim(0, 2)
axs[0][0].set_xlabel('time, this is a test of title length, when the title is too long, what will happen', 
	fontsize='medium', wrap=True, bbox=dict(facecolor='g', edgecolor='blue', alpha=0.65 ))
axs[0][0].set_ylabel('s1 and s2')
axs[0][0].grid(True)

cxy, f = axs[0][1].cohere(s1, s2, 256, 1. / dt)
axs[0][1].set_ylabel('coherence')

fig.tight_layout()
plt.show()




