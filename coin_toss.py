from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector

# The probability distribution for an unbiased coin is 1/2 for both heads and tails.
# This can be respresented as (1/sqrt(2) |0> ) + (1/sqrt(2) |1> ) where 0 represents heads and 1 represents tails.
# This then says that we get 0 (heads) with probability | 1/sqrt(2) | ^ 2 = 1/2.

backend = BasicAer.get_backend('qasm_simulator')


q = QuantumRegister(1)
c = ClassicalRegister(1)

# Initialy q is set at |0> and to transform it to the state given above, we can use Hadamard transform.

circuit = QuantumCircuit(q,c)

circuit.h(q)
circuit.measure(q,c)

# To draw the circuit use:
circuit.draw()

# Shots implies the number of times we want the circuit to be executed
# In this case it means how many times we should toss the coin
job = execute(circuit, backend, shots=1024)

result = job.result()
counts = result.get_counts(circuit)

print(counts)

plot_histogram(counts)
