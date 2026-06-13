# Artificial-Intelligence: Machine Learning & Core AI Laboratory

A collection of high-performance artificial intelligence lab implementations, neural network architectures, genetic algorithms, and predictive regression models built using Python and Jupyter Notebooks.

![Language](https://img.shields.io/badge/Language-Python%203.10+-blue?logo=python&logoColor=white)
![Framework](https://img.shields.io/badge/Environment-Jupyter%20Notebook-orange?logo=jupyter&logoColor=white)
![Domain](https://img.shields.io/badge/Domain-Machine%20Learning%20%2F%20AI-red)
![Models](https://img.shields.io/badge/Architecture-NN%20%2F%20GA%20%2F%20Classifiers-green)
![Data](https://img.shields.io/badge/Dataset-MNIST%20%2F%20Regression-lightgrey)

---

## 🌐 Engine Overview

The Artificial-Intelligence repository serves as a modular framework for testing, validating, and deploying machine learning pipelines. Covering foundational classification algorithms, multi-layer artificial neural networks (ANNs), heuristic genetic optimization templates, and regression metrics, this workspace decouples exploratory training routines from core data pre-processing mechanisms.

---

## 📍 Quick Navigation

* [🌐 Project Overview](#-engine-overview)
* [💻 Languages & Technologies Used](#%EF%B8%8F-tech-stack)
* [📁 Repository Structure and Module Index](#-repository-structure-and-module-index)
* [🧱 Document Structure (`Amzi_Musfira_Hadiya.ipynb`)](#-repository-structure-and-module-index)
* [⚙️ Application Logic (`Lab5.py`)](#-architectural-highlights)

---

## 📦 System Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                    DATA INGESTION LAYER                      │
├──────────────────────────────────────────────────────────────┤
│               Raw Datasets / Image Matrices                  │
│               (MNIST Digits, Regression Vectors)             │
└──────────────────────────────┬───────────────────────────────┘
                               ↓
┌──────────────────────────────────────────────────────────────┐
│                MODEL EVALUATION & TRAINING LAYER             │
├────────────┬─────────────┬────────────┬─────────────┬────────┤
│ Classifier │ Neural Net  │ Genetic    │ Regression  │ Loss   │
│ Training   │ Hidden Layer│ Algorithm  │ Fit Engine  │ Weight │
│ Engines    │ Weight Sync │ Mutators   │ Matrices    │ Tuning │
└────────────┴─────────────┴────────────┴─────────────┴────────┘
                               ↓
┌──────────────────────────────────────────────────────────────┐
│                   PERFORMANCE OUTPUT METRICS                 │
├──────────────────────────────────────────────────────────────┤
│         Validation Matrix Profiles (Accuracy, Loss, Loss Curves)│
└──────────────────────────────────────────────────────────────┘

```

| Architectural Layer | Core Components & Strategies | Quick Links / Reference |
| --- | --- | --- |
| **Top: Data Arrays** | Feature scaling pipelines and structured source image matrices | [Setup & Execution Guide](https://www.google.com/search?q=%23-setup--execution-guide) |
| **Middle: Optimization Core** | Supervised learning modules, evolutionary selection nodes, and weight adjustments | [Repository Structure](https://www.google.com/search?q=%23-repository-structure-and-module-index) |
| **Bottom: Statistics** | Loss optimization graphs and final validation scoring matrices | [Application Core Interfaces](https://www.google.com/search?q=%23-application-core-interfaces) |

---

## ✨ Key Architecture Features

✅ **Multi-Class Classification Matrices** - Trains deterministic classification models to map inputs into categorical target bins while evaluating confusion arrays.

✅ **Custom Neural Network Topologies** - Features production-grade hidden layer weight transformations tracking state optimizations over backpropagation passes.

✅ **Heuristic Evolutionary Exploration** - Implements modular genetic algorithms that evaluate chromosomal fit values alongside parent mutation pipelines.

✅ **Rigorous Continuous Validation** - Segregates raw source arrays cleanly into independent train, test, and evaluation buckets to eliminate target optimization leakage.

---

## 📁 Repository Structure and Module Index

The codebase spans multi-paradigm exploratory scripts and structured execution layers:

### 🔬 Core Jupyter Machine Learning Classrooms

* **`Amzi_Musfira_Hadiya.ipynb`** - Collaborative model configuration notebook managing custom classification, evaluation, and design checks.
* **`COMP360_NN_Student_Notebook_v2.ipynb`** - Deep neural network framework evaluating layers, forward propagation mechanics, and loss backpropagation.
* **`COMP360_Regression_Lab_Student_Notebook.ipynb`** - Continuous function fit model implementing numeric linear and polynomial evaluations.
* **`GA_Lab_student_template.ipynb`** - Abstract heuristic workspace modeling population generation, selection cuts, and genetic cross-over boundaries.
* **`MNIST_Assignment_Skeleton (2) (1).ipynb`** - Core image recognition skeleton handling digit feature extractions over highly dimensional spaces.

### 🐍 Production Python Operational Scripts

* **`280048443Lab.py` & `280048443Comp360Lab.ipynb**` - Dedicated lab delivery tracking scripts mapping distinct feature parameters.
* **`lab2AI (1).py` & `lab3introAI.py**` - Early stage foundations introducing algorithmic heuristics and localized heuristic bounds.
* **`lab5.py` & `Lab5.ipynb**` - Intermediate matrix manipulation engines evaluating clustering limits and custom validation routines.

---

## 🛠️ Tech Stack

| Component | Technology | Quick Links |
| --- | --- | --- |
| **Core Ecosystem** | Python 3.10+ Standard Implementation | [python.org](https://www.python.org/) |
| **Scientific Processing** | NumPy & Pandas Vector Computation Libraries | [numpy.org](https://www.google.com/search?q=https://numpy.org/) |
| **Machine Learning Core** | Scikit-Learn Framework Architectures | [scikit-learn.org](https://www.google.com/search?q=https://scikit-learn.org/) |
| **Visualization Layer** | Matplotlib & Seaborn Diagnostic Plot Engines | [matplotlib.org](https://www.google.com/search?q=https://matplotlib.org/) |
| **Interactive Runtime** | Jupyter Client Subsystems | [jupyter.org](https://www.google.com/search?q=https://jupyter.org/) |

---

## 💻 System Requirements

Ensure your training or execution environment meets these minimum performance metrics:

* **Hardware Architecture:** Multi-core modern CPU baseline configuration; minimum 8GB RAM footprint recommended for large data matrix conversions.
* **Environment Drivers:** Active Jupyter Server running over modern web browsers (Chrome, Edge, Firefox).
* **Package Distributions:** Python environment with standard scientific compilation dependencies verified.

---

## 🚀 Setup & Execution Guide

### Step 1: Clone the Laboratory Workspace

Pull the repository collection directly onto your local testing machine:

```bash
git clone [https://github.com/MoNsT3R-code/Artificial-Intelligence-.git](https://github.com/MoNsT3R-code/Artificial-Intelligence-.git)
cd Artificial-Intelligence-

```

### Step 2: Establish Virtual Environment and Drivers

Construct an isolated virtual environment shell and inject the required machine learning dependencies:

```bash
python3 -m venv ai_env
source ai_env/bin/activate  # Windows: .\ai_env\Scripts\activate

pip install --upgrade pip
pip install jupyter numpy pandas scikit-learn matplotlib seaborn

```

### Step 3: Initialize the Interactive Server

Launch the local notebook connection directly to begin step-by-step feature execution tracking:

```bash
jupyter notebook

```

---

## 📊 Application Core Interfaces

The workspace profiles model parameters directly through highly isolated analytical tracking buckets:

| Exploration Node | Algorithmic Context | Functional Objective | Target Verification Metric |
| --- | --- | --- | --- |
| **Classifiers** | Supervised Categorization | Maps numeric multi-feature tokens into strict distinct sets. | F1-Score / Accuracy Matrix |
| **Neural Networks** | Deep Layer Backpropagation | Coordinates structural weight updates across layered neural webs. | Categorical Cross-Entropy Loss |
| **Genetic Loops** | Evolutionary Optimization | Traverses vast parametric zones using randomized chromosomal operations. | Population Generation Fitness |

---

## 🏗️ Architectural Highlights

### 📉 Matrix Multi-Layer Backpropagation

Neural architectures manipulate weights by evaluating instantaneous partial derivatives across hidden layer nodes. This gradient tracking routine maps model changes to lower overall loss values over time:

$$\Delta W = -\eta \frac{\partial \mathcal{L}}{\partial W}$$

### 🔐 Pure Structural Feature Separation

All input vectors undergo complete isolation checks. Normalization parameters use statistical properties derived solely from training arrays. This isolates testing metrics from data leakage, ensuring model generalizability checks remain accurate.

---

## 📄 License & Terms

This project is open-source. Feel free to copy, modify, and redistribute the artificial intelligence modules and laboratory scripts as required.
```

```
