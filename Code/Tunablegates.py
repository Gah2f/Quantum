import random
import matplotlib.pyplot as plt
import numpy as np
import sympy
from math import radians, degrees
from scipy.optimize import minimize
import cirq
from cirq_web import bloch_sphere
from cirq import Z, PauliSum

qubit = cirq.NamedQubit('q0')
circuit = cirq.Circuit()

circuit.append(cirq.rx(radians(400)).on(qubit))
circuit.append(cirq.ry(radians(583)).on(qubit))
circuit.append(cirq.rz(radians(122)).on(qubit))

bloch_sphere.BlochSphere(state_vector = cirq.final_state_vector(circuit))