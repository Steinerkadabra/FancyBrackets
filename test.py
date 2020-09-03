import matplotlib.pyplot as plt
import numpy as np
import FancyBrackets.brackets as fb
import lightkurve as lk


lc = lk.search_lightcurvefile('QW Pup').download_all().PDCSAP_FLUX.stitch().remove_nans()

fig, ax = plt.subplots(figsize = (16,10))
ax.plot(lc.time, lc.flux, 'ko', ms = 0.75)

ax.set_ylabel('Flux')
ax.set_xlabel('Time')
ax.set_ylim(0.985, 1.025)

y_sector = 1.02
sector_num= 6
orbit_num= 19
y_orbit = 0.989
x_orbits = [[1465.21262, 1477.01998], [1478.11304,1490.04359], [1491.62553, 1503.03803], [1504.69775, 1516.08524], [1517.34150, 1529.06510], [1530.25816,1541.99982]]
x_sectors = [[1468.270, 1490.044], [1491.626, 1516.085], [1517.342, 1542.000]]
for sector in x_sectors:
    fb.CurlyBracket([sector[1], y_sector],  [sector[0], y_sector], 0.001, ax, color = 'k')
    ax.text((sector[1] + sector[0])/2, y_sector + 0.0025, f"Sector {sector_num}", va = 'center', ha = 'center')
    sector_num = sector_num +1
for orbit in x_orbits:
    fb.CurlyBracket([orbit[0], y_orbit], [orbit[1], y_orbit], 0.001, ax, color = 'red')
    ax.text((orbit[1] + orbit[0])/2, y_orbit - 0.0025, f"Orbit {orbit_num}", va = 'center', ha = 'center', color = 'r')
    orbit_num = orbit_num +1
plt.tight_layout()

plt.show()