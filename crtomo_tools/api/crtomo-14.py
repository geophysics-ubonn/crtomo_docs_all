import crtomo.configManager as CRconfig
config = CRconfig.ConfigManager(nr_of_electrodes=48)
config.gen_schlumberger(M=24, N=25)
fig, ax = config.plot_pseudodepths(
    spacing=1,
    ctypes=['schlumberger', ],
)