from upf_tools.projectors import Projectors
from pathlib import Path
import matplotlib.pyplot as plt

for projfile in Path().glob('*.dat'):
    proj = Projectors.from_file(projfile)
    ax = proj.plot()
    ax.set_xlim([0, 10])
    plt.savefig(projfile.with_suffix('.png'), format='png')

