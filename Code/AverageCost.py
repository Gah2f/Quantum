import cirq
import numpy as np
from math import radians 

# 1. Create the circuit
qubit = cirq.NamedQubit('q0')
circuit = cirq.Circuit()

circuit.append(cirq.rx(radians(45)).on(qubit))
circuit.append(cirq.measure(qubit, key='result'))


# 2. Simulate the circuit and unpack the results
sim = cirq.Simulator()
results = sim.run(circuit, repetitions = 100)

measurements = results.measurements['result']


# 3. Calculate the average (expected) state
average_state = np.mean(measurements, axis=0)
print('Average State: ', average_state)


# 4. Calculate the average (expected) cost
average_cost = 1 - average_state[0]


print('Average Cost: ', average_cost)