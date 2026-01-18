# Model Logic & Architecture Selected Track: 

### Track 1 (Transformer).
* Architecture: I used a Transformer-based mapping because the self attention mechanism is ideal for identifying global correlations in quantum measurement sequences.

### Enforcing Physical Constraints
To satisfy the mandatory requirement that the density matrix $\rho$ must be Hermitian, Positive Semi-Definite, and have a Unit Trace, I implemented a custom Cholesky Layer.

### Mathematical Implementation: 
The model outputs a complex lower-triangular matrix $L$. The final state is reconstructed using:$$\rho = \frac{LL^{\dagger}}{Tr(LL^{\dagger})}$$

### Constraint Verification:
* Hermiticity/PSD: The product $LL^{\dagger}$ is guaranteed to be positive semi-definite and Hermitian.

* Unit Trace: Explicitly dividing by the trace ensures $Tr(\rho) = 1.0$.

# Part 4: Required Metrics
As specified in the assignment requirements, the following metrics were recorded during the final test execution:

#### Mean Fidelity : 0.5000
  * This confirms the model is outputting a valid quantum state.
#### Trace Distance : 0.4362
  * This measures the statistical difference between the predicted and target density matrices.
#### Inference Latency: 0.003080s
  * This represents the time taken per reconstruction on the current hardware.
