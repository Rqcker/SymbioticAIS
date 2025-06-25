## 🧬🤖 SAIS: Symbiotic Artificial Immune Systems

<p align="left">
  <a href="https://dl.acm.org/doi/abs/10.1145/3638530.3664188"><img src="https://img.shields.io/badge/ACM%20GECCO-2024-orange?logo=acm" alt="ACM Paper"></a>
  <a href="https://arxiv.org/abs/2402.07244"><img src="https://img.shields.io/badge/arXiv-2402.07244-b31b1b.svg?logo=arxiv" alt="arXiv"></a>
  <a href="https://pypi.org/project/sais/"><img src="https://img.shields.io/pypi/v/sais.svg?color=blue" alt="PyPI version"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.8%2B-blue.svg?logo=python" alt="Python 3.8+"></a>
  <a href="https://github.com/Rqcker/SymbioticAIS/actions/workflows/flake8.yml"><img src="https://img.shields.io/badge/code%20style-flake8-brightgreen.svg?logo=python" alt="flake8"></a>
  <a href="http://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/github/license/Rqcker/SymbioticAIS.svg" alt="License"></a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Rqcker/ImageHosting/master/dissertation/symbio3.png" alt="Symbiotic">
</p>

### 🔬 Introduction
SAIS (Symbiotic Artificial Immune Systems) is a novel Artificial Immune System inspired by symbiotic relationships observed in biology. It leverages the three key stages of symbiotic relationships—mutualism, commensalism, and parasitism—for population updating, as seen in the Symbiotic Organisms Search (SOS) algorithm. This approach effectively tackles the challenges associated with large population sizes and enhances population diversity, issues that traditional AIS and SOS algorithms struggle to address efficiently. This project aims to provide an open-source implementation of the SAIS algorithm to foster innovation and research in bio-inspired computing and immune-inspired algorithms.

📦 **Official Python Package Index (PyPI) Package: [SAIS](https://pypi.org/project/sais/)**.

### 🏆 Publication

📚 The [paper](https://dl.acm.org/doi/abs/10.1145/3638530.3664188) has been published in the '[**ACM Proceedings of the Genetic and Evolutionary Computation Conference (GECCO '24 Companion)**](https://dl.acm.org/conference/gecco)'🎉.

🎊 The [preprint](https://arxiv.org/abs/2402.07244) is available on arXiv.

### ⚙️ Features

- Implementation of the Symbiotic Artificial Immune Systems algorithm.
- Easy to calculate the objective value of the function.
- Customizable for different optimisation needs.
- Support for multiple benchmark functions.

### 🚀 Quick Start

Ensure the following dependencies are installed on your system:
- Python 3.x
- numpy

📥 Install `sais` using pip:

```bash
pip install sais
```

🔥 Example usage, here's how to use SAIS to optimise a function:

```python
from sais import run

# define your benchmark number and population size
population_size = 2000
# number from Benchmarks List
benchmark_number = 1

run(population_size, benchmark_number)
```

📌 Example output:
```bash
Starting SAIS for benchmark 1 with population size 2000.
Iterations Number: 8
Running Time: 0.18377017974853516 Secounds
Best Fitness: 4.523554492464579e-10
Best Antibody: [2.9999822  0.49999976]
```

🎯 Function evaluation, get the function's value at a given point:
```python
import numpy as np
from sais import benchmark_result


x = np.random.uniform(np.pi, np.pi, 2)
y = sais.benchmark_result(x, 2)
print(x, y)
```

### 📊 Benchmark Functions
```
### Benchmarks (Name, Range, Global Minimum)
# F1 = Beale [-4.5; 4.5]; 0
# F2 = Easom [-100,100]; -1
# F3 = Matyas [-10,10]; 0
# F4 = Bochachvesky 1 [-100,100]; 0
# F5 = Booth [-10, 10]; 0
# F6 = Michalewicz 2[0,pi]; -1.8013
# F7 = Schaffer [-100; 100]; 0
# F8 = Six Hump Camel Back [-5; 5]; -1.03163
# F9 = Bochachvesky 2 [-100,100]; 0
# F10 = Bochachvesky 3 [-100,100]; 0
# F11 = Shubert [-10,10]; -186.73
# F12 = Colville [-10,10]; 0
# F13 = Michalewicz 5 [0,pi]; -4.6877
# F14 = Zakharov[-5,10]; 0
# F15 = Michalewicz 10 [0,pi]; -4.6877
# F16 = Step [-5.12; 5.12]; 0
# F17 = Sphere [-100,100]; 0
# F18 = SumSquares [-10, 10]; 0
# F19 = Quartic [-1.28,1.28]; 0
# F20 = Schwefel 2.22 [-10,10]; 0
# F21 = Schwefel 1.2 [-10,10]; 0
# F22 = Rosenbrock [-30,30]; 0
# F23 = Dixon-Price [-10, 10]; 0
# F24 = Rastrigin [-5.12; 5.12];
# F25 = Griewank [-600,600]; 0
# F26 = Ackley [-600; 600]; 0
# F27 = UserCustom [-60; -20]; 7500
```

### 🔄 SAIS Flowchart

<details>
  <summary>📌 Click to expand the flowchart.</summary>
  <p align="center">
    <img src="https://raw.githubusercontent.com/Rqcker/ImageHosting/master/dissertation/flowchart.png" alt="Flowchart">
  </p>
</details>

### 📬 Contact
For any questions or suggestions, please contact us via:
- 🔬 [The Bio-inspired Computing and Machine Learning (BCML) Lab](https://bioml.eu.org/).
- 🐛 [GitHub Issues](https://github.com/Rqcker/SymbioticAIS/issues).

### 📜 License
This project is licensed under the [Apache 2.0 License](LICENSE).

### 🔖 Citation
```bibtex
@inproceedings{song2024sais,
  title={SAIS: A Novel Bio-Inspired Artificial Immune System Based on Symbiotic Paradigm},
  author={Song, Junhao and Yuan, Yingfang and Pang, Wei},
  booktitle={Proceedings of the Genetic and Evolutionary Computation Conference Companion},
  pages={2115--2118},
  year={2024}
}
```

### 🎓 Acknowledgements

We extend our sincere thanks to 🏛️ **[Imperial College London](https://www.imperial.ac.uk/) & [Heriot-Watt University](https://www.hw.ac.uk/)** for their support and the academic environment that facilitated our research.
