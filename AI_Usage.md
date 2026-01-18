# AI Usage Disclosure

I used Gemini (AI) as a learning assistant and debugger during this project to help me work through technical roadblocks.

### How I used AI for guidance:
* **Fixing Environment Issues**: I ran into a "Missing Import" error even after installing libraries. The AI helped me realize I was using the wrong Python interpreter in VS Code and guided me to switch to the 'Global' 3.13.4 version where Torch was actually installed.
* **Code Debugging**: I had a syntax error with a function called `m_conjugate`. The AI pointed out that this wasn't the correct PyTorch command and helped me find the right one, which is `.conj()`.
* **Understanding the Math**: I used the AI to help me figure out how to write the Cholesky layer. It explained how to turn the math formula ($\rho = \frac{LL^{\dagger}}{Tr(LL^{\dagger})}$) into actual code so my density matrix would be physical.
* **Structure Help**: I used it to double check the folder requirements (src, docs, outputs).

### Human Verification:
I personally ran all terminal commands, verified the Torch installation version manually, and checked that the final model file (`model.pt`) was generated correctly in the outputs folder.
