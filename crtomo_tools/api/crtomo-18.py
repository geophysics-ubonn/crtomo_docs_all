import numpy as np
from crtomo.mpl_setup import *
import crtomo.configManager as CRConfig

configs = CRConfig.ConfigManager(nr_of_electrodes=48)
configs.gen_dipole_dipole(skipc=1, stepc=2)
K = configs.compute_K_factors(spacing=1)
measurements = np.random.random(configs.nr_of_configs)
mid = configs.add_measurements(measurements)

fig, axes = plt.subplots(1, 2)

configs.plot_pseudosection_type2(
    mid,
    ax=axes[0],
    cblabel='this label',
    xlabel='xlabel',
    ylabel='ylabel',
)
configs.plot_pseudosection_type2(
    K,
    ax=axes[1],
    cblabel='K factor',
    xlabel='xlabel',
    ylabel='ylabel',
)
fig.tight_layout()