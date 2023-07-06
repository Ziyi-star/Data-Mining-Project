import torch
import torch.nn as nn
import numpy as np
from abc import ABC, abstractmethod
import pandas as pd
from utils.paths import *

# train = pd.read_csv('train.csv')
# train_tensor = torch.tensor(train.values)

# define hyperparameters of NN
input_size = 9
layer_1 = 64
layer_2 = 32
layer_3 = 16
num_classes = 30
num_epochs = 50
learning_rate = 0.0015


class BaseNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_input = nn.Linear(input_size, layer_1)
        self.layer_hidden_one = nn.Linear(layer_1, layer_2)
        self.layer_hidden_two = nn.Linear(layer_2, layer_3)
        self.layer_output = nn.Linear(layer_3, num_classes)

    @abstractmethod
    def forward(self, x):
        pass


class NetLinear(BaseNet):
    def forward(self, x):
        out = self.layer_input(x)
        out = self.layer_hidden_one(out)
        out = self.layer_hidden_two(out)
        out = self.layer_output(out)
        return out


class NetTanh(BaseNet):
    def __init__(self):
        super().__init__()
        self.tanh = nn.Tanh()

    def forward(self, x):
        out = self.tanh(self.layer_input(x))
        out = self.tanh(self.layer_hidden_one(out))
        out = self.tanh(self.layer_hidden_two(out))
        out = self.layer_output(out)
        return out

class NetSigmoid(BaseNet):
    def __init__(self):
        super().__init__()
        self.sigmoid = nn.Sigmoid()
    def forward (self, x):
        out = self.sigmoid(self.layer_input(x))
        out = self.sigmoid(self.layer_hidden_one(out))
        out = self.sigmoid(self.layer_hidden_two(out))
        out = self.layer_output(out)
        return out

class NetReLu(BaseNet):
    def __init__(self):
        super().__init__()
        self.relu = nn.ReLU()
    def forward (self, x):
        out = self.relu(self.layer_input(x))
        out = self.relu(self.layer_hidden_one(out))
        out = self.relu(self.layer_hidden_two(out))
        out = self.layer_output(out)
        return out


if __name__ == '__main__':
    # load train data
    train_path = get_klassifikation_train_path();
    train_filename = Path.joinpath(train_path, 'x1train.csv')
    train = pd.read_csv(train_filename)
    train_data = train.drop(train.columns[-1], axis=1)
    train_label = train.iloc[:, -1]
    train_data_tensor = torch.tensor(train_data.values)
    train_label_tensor = torch.tensor(train_label.values)

    # load test data
    test_path = get_klassifikation_test_path();
    test_filename = Path.joinpath(test_path, 'x1test.csv')
    test = pd.read_csv(test_filename)
    test_data = test.drop(test.columns[-1], axis=1)
    test_label = test.iloc[:, -1]
    test_data_tensor = torch.tensor(test_data.values)
    test_label_tensor = torch.tensor(test_label.values)

    batch_size = 16





