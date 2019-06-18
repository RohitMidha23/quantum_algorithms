from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute, Aer

def bitwise_and(circuit,a,b,c,N):
    for i in range(N):
        circuit.ccx(a[i],b[i],c[i])

def bitwise_or(circuit,a,b,c,N):
    for i in range(N):
        circuit.ccx(a[i],b[i],c[i])
        circuit.cx(a[i],b[i])
        circuit.cx(b[i],c[i])

# Bitwise AND


# Registers and circuit.
a = QuantumRegister(4)
b = QuantumRegister(4)
c = QuantumRegister(4)
ca = ClassicalRegister(4)
cb = ClassicalRegister(4)
cc = ClassicalRegister(4)
circuit = QuantumCircuit(a, b, c, ca, cb, cc)

# Inputs
# a = 1010
# b = 1011
circuit.x(a[1])
circuit.x(a[3])
circuit.x(b[0])
circuit.x(b[1])
circuit.x(b[3])

# Take the bitwise AND.
bitwise_and(circuit, a, b, c, 4)

# Measure.
circuit.measure(a, ca)
circuit.measure(b, cb)
circuit.measure(c, cc)

# Simulate the circuit.
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(circuit, backend_sim)
result_sim = job_sim.result()

# Expected Output : 1010 1011 1010
# NOTE: In qiskit, little endian is followed and hence the output is actually c b a
#       where c in the bitwise and of a and b
print("Bitwise AND : ")
print(result_sim.get_counts(circuit))

# Bitwise OR
# Registers and circuit.
a = QuantumRegister(4)
b = QuantumRegister(4)
c = QuantumRegister(4)
ca = ClassicalRegister(4)
cb = ClassicalRegister(4)
cc = ClassicalRegister(4)
circuit = QuantumCircuit(a, b, c, ca, cb, cc)

# Inputs
# a = 1010
# b = 1011
circuit.x(a[1])
circuit.x(a[3])
circuit.x(b[0])
circuit.x(b[1])
circuit.x(b[3])

# Take the bitwise AND.
bitwise_or(circuit, a, b, c, 4)

# Measure.
circuit.measure(a, ca)
circuit.measure(b, cb)
circuit.measure(c, cc)

# Simulate the circuit.
backend_sim = Aer.get_backend('qasm_simulator')
job_sim = execute(circuit, backend_sim)
result_sim = job_sim.result()

# Expected Output : 1011 1011 1010
# NOTE: In qiskit, little endian is followed and hence the output is actually c b a
#       where c in the bitwise and of a and b
print("Bitwise OR : ")
print(result_sim.get_counts(circuit))
