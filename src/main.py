import torch
import torch.nn as nn
import time


class QuantumLayer(nn.Module):
    def forward(self, x):
        real, imag = x.chunk(2, dim=-1)
        L = torch.complex(real, imag).view(-1, 2, 2)
        L = torch.tril(L)
        L_dag = L.conj().transpose(-2, -1)
        rho_unnorm = torch.matmul(L, L_dag)
        trace = torch.real(torch.vmap(torch.trace)(rho_unnorm)).view(-1, 1, 1)
        return rho_unnorm / trace


class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(8, 32), nn.ReLU(), nn.Linear(32, 8))
        self.physical = QuantumLayer()

    def forward(self, x):
        return self.physical(self.net(x))


def run_project():
    model = MyModel()

    target_rho = torch.tensor([[0.5, 0], [0, 0.5]], dtype=torch.complex64)
    test_input = torch.randn(1, 8)

    start = time.time()
    pred_rho = model(test_input).squeeze(0)
    latency = time.time() - start

    fidelity = torch.real(torch.trace(torch.matmul(pred_rho, target_rho)))

    trace_dist = 0.5 * torch.linalg.norm(pred_rho - target_rho, ord='nuc')

    print(f"--- Required Metrics ---")
    print(f"Mean Fidelity: {fidelity.item():.4f}")
    print(f"Trace Distance: {trace_dist.item():.4f}")
    print(f"Inference Latency: {latency:.6f}s")

    torch.save(model.state_dict(), "outputs/model.pt")


if __name__ == "__main__":
    run_project()
