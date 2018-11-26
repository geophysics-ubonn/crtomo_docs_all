import crtomo.configManager as CRconfig
config = CRconfig.ConfigManager(nr_of_electrodes=10)
config.gen_dipole_dipole(skipc=2)
config.plot_pseudodepths()