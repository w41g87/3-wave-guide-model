import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def heat3x3(input):
    input = input.reshape((3, 3))
    x, y = 0, 0
    sx, sy = 3, 3
    
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(25, 10), dpi=50)
    
    heatMap_mag = sns.heatmap(np.abs(input[x:sx + x, y:sy + y]), ax = ax[0], linewidth = 0, annot = False, cmap = "viridis")
    heatMap_mag.set_title("Magnitude Plot")
    heatMap_mag.set_xticks(np.arange(x, x + sx, int(np.ceil(sx / 20))))
    heatMap_mag.set_xticklabels(np.arange(x, x + sx, int(np.ceil(sx / 20))))
    heatMap_mag.set_yticks(np.arange(y, y + sy, int(np.ceil(sy / 20))))
    heatMap_mag.set_yticklabels(np.arange(-y, -y - sy, int(-np.ceil(sy / 20))), rotation = 0)

    heatMap_ph = sns.heatmap(np.angle(input[x:sx + x, y:sy + y]), ax = ax[1], vmin = 0, vmax = np.pi * 2, linewidth = 0, annot = False, cmap = sns.color_palette("blend:#491C62,#8E2E71,#C43F66,#E3695C,#EDB181,#E3695C,#C43F66,#8E2E71,#491C62", as_cmap=True))
    heatMap_ph.set_title("Phase Plot")
    heatMap_ph.set_xticks(np.arange(x, x + sx, int(np.ceil(sx / 20))))
    heatMap_ph.set_xticklabels(np.arange(x, x + sx, int(np.ceil(sx / 20))))
    heatMap_ph.set_yticks(np.arange(y, y + sy, int(np.ceil(sy / 20))))
    heatMap_ph.set_yticklabels(np.arange(-y, -y - sy, int(-np.ceil(sy / 20))), rotation = 0)
    try:
        fig.canvas.layout.width = '100%'
        fig.canvas.layout.height = '100%'
        fig.canvas.layout.overflow = 'scroll'
        fig.canvas.layout.padding = '0px'
        fig.canvas.layout.margin = '0px'
    except:
        pass

    return fig