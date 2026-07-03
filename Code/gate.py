import cirq 
import cirq_web

qubit = cirq.NamedQubit.range(2, prefix= 'q')
circuit = cirq.Circuit()
circuit.append(cirq.X(qubit[0]))
# circuit.append(cirq.X(qubit[1]))
vec = cirq.final_state_vector(circuit, ignore_terminal_measurements= True)
ket = cirq.dirac_notation(vec)
blc = cirq_web.BlochSphere(state_vector= vec)
print(circuit)
print(vec)
print(ket)


