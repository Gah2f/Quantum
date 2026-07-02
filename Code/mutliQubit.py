import cirq
import matplotlib.pyplot as plt

my_qubit = cirq.NamedQubit.range(3 ,prefix = 'q')
# print(my_qubit[0])
circuit = cirq.Circuit()
circuit.append(cirq.X(my_qubit[2]))
circuit.append(cirq.H(my_qubit[2]))
circuit.append(cirq.Z(my_qubit[2]))

my_qubits = cirq.NamedQubit.range( 5, prefix = "q")
circuit = cirq.Circuit()
for i in range(5):
  circuit.append(cirq.X(my_qubits[i]))
print(circuit)


my_qubits = cirq.NamedQubit.range( 5, prefix = "q")
circuit = cirq.Circuit()
circuit.append(cirq.X(my_qubits[0]))
circuit.append(cirq.Z(my_qubits[1]))
circuit.append(cirq.H(my_qubits[2]))
print(circuit)

print(circuit)
