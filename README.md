# SAIS: Symbiotic Artificial Immune Systems

## Introduction
SAIS (Symbiotic Artificial Immune Systems) is a novel Artificial Immune System inspired by symbiotic relationships observed in biology. It leverages the three key stages of symbiotic relationships—mutualism, commensalism, and parasitism—for population updating, as seen in the Symbiotic Organisms Search (SOS) algorithm. This approach effectively tackles the challenges associated with large population sizes and enhances population diversity, issues that traditional AIS and SOS algorithms struggle to address efficiently. This project aims to provide an open-source implementation of the SAIS algorithm to foster innovation and research in bio-inspired computing and immune-inspired algorithms.

## Features
- Innovative population update mechanism inspired by biological symbiosis.
- Comparable performance to the state-of-the-art SOS algorithm and superior to other popular AIS methods and evolutionary algorithms across 26 benchmark problems.
- Efficient handling of larger population sizes with fewer generations required.

## Quick Start
### Installation
Ensure the following dependencies are installed on your system:
- Python 3.x
- numPy
- pandas

Installation steps:
```bash
git clone https://github.com/Rqcker/SymbioticAIS.git
cd SymbioticAIS
pip install -r requirements.txt
```

## Benchmarks List
```
### Benchmarks
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
```
## Contact
For any questions or suggestions, please contact us via:
- Email
- GitHub Issue

## License
This project is licensed under the [Apache License Version 2.0](LICENSE). Please make sure you understand its terms before using it.

## Citation
If you use SAIS in your research, please cite our paper:
```
@misc{song2024sais,
      title={SAIS: A Novel Bio-Inspired Artificial Immune System Based on Symbiotic Paradigm}, 
      author={Junhao Song and Yingfang Yuan and Wei Pang},
      year={2024},
      eprint={2402.07244},
      archivePrefix={arXiv},
      primaryClass={cs.NE}
}
```
