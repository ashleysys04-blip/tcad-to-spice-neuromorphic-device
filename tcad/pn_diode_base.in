go atlas

# ============================================================
# Baseline Silicon PN Junction Simulation
# Purpose:
#   - Build a simple 2D silicon PN junction
#   - Simulate forward and reverse I-V characteristics
#   - Prepare for breakdown analysis
# ============================================================

mesh space.mult=1

# x-direction mesh, unit: micrometer
x.mesh loc=0.0 spac=0.02
x.mesh loc=0.2 spac=0.002
x.mesh loc=0.5 spac=0.01
x.mesh loc=2.0 spac=0.05

# y-direction mesh, unit: micrometer
y.mesh loc=0.0 spac=0.05
y.mesh loc=1.0 spac=0.05

# Silicon region
region num=1 silicon x.min=0.0 x.max=2.0 y.min=0.0 y.max=1.0

# Electrodes
electrode name=anode   x.min=0.0 x.max=0.05 y.min=0.0 y.max=1.0
electrode name=cathode x.min=1.95 x.max=2.0 y.min=0.0 y.max=1.0

# Doping profile
# p+ region: 0.0 to 0.2 um
# n region:  0.2 to 2.0 um
doping uniform p.type conc=1e19 x.min=0.0 x.max=0.2 y.min=0.0 y.max=1.0
doping uniform n.type conc=1e16 x.min=0.2 x.max=2.0 y.min=0.0 y.max=1.0

# Physics models
models srh fermi bgn fldmob impact selb

# Output quantities
output con.band val.band e.field qfn qfp

# Initial solution
solve init

# Save structure
save outf=pn_diode_base.str

# Forward bias sweep
log outf=pn_forward_iv.log
solve name=anode vstep=0.05 vfinal=0.8
log off

# Re-initialize before reverse sweep
solve init

# Reverse bias sweep
log outf=pn_reverse_iv.log
solve name=anode vstep=-0.2 vfinal=-20
log off

quit
