# Data Mining Project - Group B

This repository contains the **Data Mining Project** undertaken by **Jiaying Cheng and Ziyi Liu** at the University of Kassel for the Intelligent Embedded Systems course in Data Mining. The project explores data analysis, clustering, and classification using various data mining techniques.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)

## Project Overview

This project applies a structured approach to data mining, focusing on three main sections:
1. **Data Analysis**: Including JSON to CSV conversion, data standardization, principal component analysis (PCA), and handling of outliers.
2. **Clustering**: Using PCA-based feature selection and metrics like the Silhouette Coefficient and Davies-Bouldin Index to determine optimal cluster numbers.
3. **Classification**: Implementing and evaluating multiple classification models, such as SVM, Multivariate Bernoulli Models, Gaussian Mixture Models, and neural networks.

Each section employs Python and popular data science libraries to preprocess data, conduct analysis, and evaluate models.

## Features

- **Data Analysis**:
  - Conversion from JSON to CSV
  - Standardization of features
  - Principal Component Analysis (PCA)
  - Outlier detection and replacement
- **Clustering**:
  - Selection of optimal cluster numbers
  - C-means clustering with k-means++ initialization
- **Classification**:
  - Models implemented: SVM, Multivariate Bernoulli, Gaussian Mixture, and Neural Networks
  - Performance evaluation using accuracy metrics

## Requirements

To run this project, you need the following libraries:

- Python (>=3.6)
- pandas
- numpy
- scikit-learn
- matplotlib
- PyTorch (for neural network models)

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Data-Mining-Project.git
   cd Data-Mining-Project
   ```

2. Install required packages.

## Usage

1. Navigate to the `code` directory containing scripts and notebooks.
2. Run analysis, clustering, and classification steps as needed.
   ```bash
   jupyter notebook
   ```

## Project Structure

```plaintext
Data-Mining-Project/
├── code/               # Contains main scripts and notebooks
├── data/               # Dataset(s) used in analysis
├── results/            # Directory for saving output results
├── README.md           # Project documentation
└── requirements.txt    # List of required packages
```

## Results

### Classification Model Performance

Each classification model’s accuracy for different datasets is summarized below:

| Model                | Dataset x0 | Dataset x1 | Dataset x2 |
|----------------------|------------|------------|------------|
| SVM                  | 79.75%     | 97.23%     | 72.39%     |
| Bernoulli            | 97.04%     | 96.93%     | 74.23%     |
| Gaussian Mixture     | 4.74%      | 9.29%      | 0.9%       |
| Neural Network       | 97.31%     | 97.62%     | 84.25%     |

The neural network and SVM showed strong performance across datasets, with lower results for Gaussian Mixture due to data distribution.

## Contributing

Contributions are welcome! Please submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License.

## Authors

- **Jiaying Cheng**
- **Ziyi Liu**

