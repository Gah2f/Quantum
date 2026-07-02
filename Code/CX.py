import cirq 

my_qubits = cirq.NamedQubit.range(2, prefix= 'q')
circuit = cirq.Circuit()
circuit.append(cirq.CNOT(my_qubits[0],my_qubits[1]))
# Not the first arg is control and the 2nd is target

my_qubits = cirq.NamedQubit.range(2, prefix= 'q')
circuit = cirq.Circuit()
circuit.append(cirq.H(my_qubits[0]))
circuit.append(cirq.CNOT(my_qubits[0],my_qubits[1]))
print(circuit)

print(circuit)