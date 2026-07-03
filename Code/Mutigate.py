import cirq
  
my_qubits = cirq.NamedQubit.range(3, prefix = 'q')
circuit = cirq.Circuit()
for i in range(3):
   circuit.append(cirq.H(my_qubits[i]))
   
circuit.append(cirq.M(my_qubits))
print(circuit)