import numpy as np
import crtomo.configManager as CRConfig
configs = CRConfig.ConfigManager(nr_of_electrodes=48)
configs.gen_dipole_dipole(skipc=1, stepc=2)
measurements = np.random.random(configs.nr_of_configs)
mid = configs.add_measurements(measurements)
configs.plot_pseudosection_type2(
    mid,
    cblabel='this label',
    xlabel='xlabel',
    ylabel='ylabel',
)