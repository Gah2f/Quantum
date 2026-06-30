import cirq
import matplotlib.pyplot as plt 

qubit = cirq.NamedQubit('q0')
sim = cirq.Simulator()

circuit = cirq.Circuit()
for i in range(4):
    circuit.append(cirq.X(qubit))
circuit.append(cirq.H(qubit))
circuit.append(cirq.M(qubit))

result = sim.run(circuit, repetitions= 30)
hist = cirq.plot_state_histogram(result, plt.subplot(), title= 'Qubit States', xlabel= 'states', ylabel= 'occurances') 
print(circuit)
print(result)
plt.show()