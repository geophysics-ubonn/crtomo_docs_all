import crtomo.grid as CRGrid
grid = CRGrid.crt_grid.create_surface_grid(
    nr_electrodes=30, spacing=1
)
import crtomo.tdManager as CRman
man = CRman.tdMan(grid=grid)
pid_mag, pid_pha = man.add_homogeneous_model(magnitude=100, phase=-5)
man.parman.modify_area(
    pid_mag, 1, 5, -5, -2, value=10
)
r = man.plot.plot_elements_to_ax(
    pid_mag,
    plot_colorbar=True,
    cblabel=r'$\rho~[\Omega m]$',
)
fig = r[0]
# fig.savefig('model_mag.png', dpi=300)

r = man.plot.plot_elements_to_ax(
    pid_pha,
    plot_colorbar=True,
    cblabel=r'$\phi~[mrad]$',
)