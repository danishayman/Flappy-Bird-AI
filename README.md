# 🦅 Flappy Bird AI with NEAT 🧠

Train an AI to master Flappy Bird using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm! Watch as neural networks evolve and learn to navigate through pipes with increasing precision.

## 🎮 About the Project

This project implements an AI that learns to play Flappy Bird using NEAT, a genetic algorithm that evolves neural networks. The AI starts with no knowledge of the game and gradually learns optimal strategies through natural selection and evolution.

### 🌟 Features

- Neural network-controlled birds
- Real-time visualization of the learning process
- Generation counter and score tracking
- Population-based training
- Fitness-based evolution

## 🛠️ Requirements

- Python 3.x
- pygame
- neat-python

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/danishayman/Flappy-Bird-AI.git
cd Flappy-Bird-Ai
```

2. Install dependencies:
```bash
pip install pygame neat-python
```

## 🚀 Usage

Run the main script to start the training:
```bash
python main.py
```

## 🎯 How It Works

1. **Initialization**: Creates a population of birds, each controlled by a neural network
2. **Input Layer**: Each bird receives:
   - Current Y position
   - Distance to top pipe
   - Distance to bottom pipe

3. **Evolution**: 
   - Birds that survive longer and score more points have higher fitness
   - The best performing neural networks are selected for the next generation
   - Networks evolve through mutation and crossover

4. **Training**: 
   - Each generation improves upon the last
   - The process continues until birds consistently achieve high scores

## 🎮 Game Controls

- The AI controls everything! Just sit back and watch the birds learn
- Close the window to end the simulation

## 📊 Configuration

The `config_feedforward.txt` file contains all NEAT algorithm parameters:
- Population size
- Network architecture
- Mutation rates
- Species settings

## 🤝 Contributing

Feel free to contribute to this project! Here's how:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request



## 🙏 Acknowledgments

- Original Flappy Bird game by Dong Nguyen
- NEAT algorithm by Kenneth O. Stanley
- Pygame community for the excellent game development library





Happy training! 🎉