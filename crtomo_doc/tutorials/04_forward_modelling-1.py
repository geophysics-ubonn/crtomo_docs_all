import crtomo.mpl
plt, mpl = crtomo.mpl.setup()

import crtomo.grid as CRGrid
grid = CRGrid.crt_grid.create_surface_grid(
    nr_electrodes=30, spacing=1
)
import crtomo.tdManager as CRman
man = CRman.tdMan(grid=grid)
pid_mag, pid_pha = man.add_homogeneous_model(magnitude=100, phase=-5)
man.parman.modify_area(pid_mag, 1, 5, -5, -2, value=10)
r = man.plotman.plot_elements_to_ax(
    pid_mag,
    title='Forward model',
    plot_colorbar=True,
    cblabel=r'$|\rho|~[\Omega m]$',
)
fig = r[0]
# fig.savefig('model_mag.png', dpi=300)
r = man.plotman.plot_elements_to_ax(
    pid_pha,
    title='Forward model',
    plot_colorbar=True,
    cblabel=r'$\phi~[mrad]$',
)
fig = r[0]
# fig.savefig('model_mag.png', dpi=300)
man.configs.gen_dipole_dipole(skipc=0)
rmag_rpha = man.measurements()
K = man.configs.compute_K_factors(spacing=1)
rhoa = rmag_rpha[:, 0] * K
cid_rho = man.configs.add_measurements(rhoa)
r = man.configs.plot_pseudosection_type2(
    cid_rho,
    cblabel=r'$\rho_a~[\Omega m]$',
)
import numpy as np
maglog = np.log10(rmag_rpha[:, 0])
cid = man.configs.add_measurements(maglog)
mid_mag, mid_pha = man.assignments['measurements']
r = man.configs.plot_pseudosection_type2(
    mid_mag,
    cblabel=r'$|Z|~[\Omega]$',
)
fig = r[0]
# fig.savefig('pseudosection_mag.png', dpi=300)

r = man.configs.plot_pseudosection_type2(
    maglog,
    cblabel=r'$log_{10}(|Z|~[\Omega])$',
)