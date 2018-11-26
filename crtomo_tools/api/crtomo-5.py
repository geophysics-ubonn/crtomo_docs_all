import numpy as np
import crtomo.configManager as CRConfig
config = CRConfig.ConfigManager(nr_of_electrodes=48)
config.gen_dipole_dipole(skipc=1, stepc=2)
# generate random measurements
measurements = np.random.random(config.nr_of_configs)
mid = config.add_measurements(measurements)
config.plot_pseudosection_type1(mid, spacing=1)