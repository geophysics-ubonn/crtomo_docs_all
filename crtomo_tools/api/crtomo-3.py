import crtomo.configManager as CRconfig
config = CRconfig.ConfigManager(nr_of_electrodes=48)
config.gen_dipole_dipole(skipc=2)
fig, ax = config.plot_pseudodepths(
    spacing=0.3,
    ctypes=['dd', ],
)