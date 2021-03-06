# Import the function for compilation of models and the load_fmu method
from pymodelica import compile_fmu
from pyfmi import load_fmu

# Import the plotting library
import matplotlib.pyplot as plt

# Compile model
fmu_name = compile_fmu("VDP","VDP.mo")

# Load model
vdp = load_fmu(fmu_name)

res = vdp.simulate(final_time=10)

x1 = res['x1']
x2 = res['x2']
t  = res['time']

plt.figure(1)
plt.plot(t, x1, t, x2)
plt.legend(('x1','x2'))
plt.title('Van der Pol oscillator.')
plt.ylabel('Angle (rad)')
plt.xlabel('Time (s)')
plt.show()
