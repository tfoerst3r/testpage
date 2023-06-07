import arrr
import numpy as np
import matplotlib.pyplot as plt

def translate(english):
    return arrr.translate(english)

def function(val:int):
    r = np.arange(0, 2, 0.01)
    theta = val * np.pi * r
    return theta,r

def plot_image(val:int):
    
    radius = val
    theta,r = function(radius)

    fig, ax = plt.subplots(
      subplot_kw = {'projection': 'polar'}
    )

    ax.plot(theta, r)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.grid(True)
    
    return fig
    #pyscript.write('lineplot',fig)
    #display(fig, target="")
    #pyscript.write('lineplot',fig)
    #display(fig, target="output")
