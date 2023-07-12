import torch
import torch.nn as nn
import numpy as np
from abc import ABC, abstractmethod
import pandas as pd
from utils.paths import *
import matplotlib.pyplot as plt
import json


# define hyperparameters of NN
input_size = 25
layer_1 = 64
layer_2 = 32
layer_3 = 16
num_classes = 30
num_epochs = 50
learning_rate = 0.00015

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
        out = self.layer_input(x.to(self.layer_input.weight.dtype))
        out = self.layer_hidden_one(out)
        out = self.layer_hidden_two(out)
        out = self.layer_output(out)
        return out


class NetTanh(BaseNet):
    def __init__(self):
        super().__init__()
        self.tanh = nn.Tanh()

    def forward(self, x):
        out = self.tanh(self.layer_input(x.to(self.layer_input.weight.dtype)))
        out = self.tanh(self.layer_hidden_one(out))
        out = self.tanh(self.layer_hidden_two(out))
        out = self.layer_output(out)
        return out

class NetSigmoid(BaseNet):
    def __init__(self):
        super().__init__()
        self.sigmoid = nn.Sigmoid()
    def forward (self, x):
        out = self.sigmoid(self.layer_input(x.to(self.layer_input.weight.dtype)))
        out = self.sigmoid(self.layer_hidden_one(out))
        out = self.sigmoid(self.layer_hidden_two(out))
        out = self.layer_output(out)
        return out

class NetReLu(BaseNet):
    def __init__(self):
        super().__init__()
        self.relu = nn.ReLU()
    def forward (self, x):
        out = self.relu(self.layer_input(x.to(self.layer_input.weight.dtype)))
        out = self.relu(self.layer_hidden_one(out))
        out = self.relu(self.layer_hidden_two(out))
        out = self.layer_output(out)
        return out

class Plot:
    def __init__(self, initial_test):
        self.loss_train = [initial_test]
        self.loss_test = [initial_test]
        self.x_axis = [0]

    def append_loss_train(self, loss):
        self.loss_train.append(loss)

    def append_loss_test(self, loss):
        self.loss_test.append(loss)

    def append_x_axis(self, x_axis):
        self.x_axis.append(x_axis)

    def plot(self):
        limit = max(max(self.loss_train), max(self.loss_test))
        fig, ax1 = plt.subplots()
        color = 'tab:red'
        ax1.set_xlabel('epochs')
        ax1.set_ylabel('Loss train', color=color)
        ax1.set_ylim([0, limit])
        ax1.plot(self.x_axis, self.loss_train, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()

        color = 'tab:blue'
        ax2.set_ylabel('Loss test', color=color)
        ax2.plot(self.x_axis, self.loss_test, color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        ax2.set_ylim([0, limit])

        fig.tight_layout()
        plt.show()

def test_function(net, test_loader):
    loss_test = 0
    correct = 0
    total = 0

    for i, (data, labels) in enumerate(test_loader):
        outputs = net(data)
        loss = criterion(outputs, labels)

        loss_test += loss.item()
        _, predicted = torch.max(outputs.data, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    loss = loss_test / len(test_loader)
    accuracy = 100 * correct / total

    return loss, accuracy

def train_net(net, train_loader, test_loader):
    optimizer = torch.optim.Adam(net.parameters(), lr=learning_rate)
    plot = Plot(test_function(net, test_loader)[0])

    loss_epoch = []
    accuracy_epoch = []


    for epoch in range(num_epochs):
        loss_train = 0
        correct = 0
        total = 0

        for i, (datas, labels) in enumerate(train_loader):
            outputs = net(datas)
            loss = criterion(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            loss_train += loss.item()
            _, predicted = torch.max(outputs.data, 1)

            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        loss_test, accuracy = test_function(net, test_loader)
        loss_train1, accuracy_train = test_function(net, train_loader)
        loss_train = loss_train / len(train_loader)

        # plot for loss
        #plot.append_loss_test(loss_test)
        #plot.append_loss_train(loss_train)
        #plot.append_x_axis(epoch + (i + 1) / len(train_dataset) // batch_size)

        loss = loss_train / len(train_loader)
        accuracy = 100 * correct / total

        loss_epoch.append(loss)
        accuracy_epoch.append(accuracy)

        # plot for accuracy
        plot.append_loss_test(accuracy)
        plot.append_loss_train(accuracy_train)
        plot.append_x_axis(epoch + (i + 1) / len(train_dataset) // batch_size)

        if (epoch + 1) % 5 == 0:
            print('Epoch [%d/%d], loss train: %.8f, loss test: %.8f, accuracy test: %.2f, accuracy train: %.2f' % (epoch + 1, num_epochs, loss_train, loss_test, accuracy, accuracy_train))

    plot.plot()

    return loss_epoch, accuracy_epoch


if __name__ == '__main__':
    # load train data
    train_path = get_klassifikation_train_path()
    train_filename = Path.joinpath(train_path, 'x0train.csv')
    train = pd.read_csv(train_filename)
    train_data = train.drop(train.columns[-1], axis=1)
    train_label = train.iloc[:, -1]
    train_data_tensor = torch.tensor(train_data.values)
    train_label_tensor = torch.tensor(train_label.values)

    # load test data
    test_path = get_klassifikation_test_path()
    test_filename = Path.joinpath(test_path, 'x0test.csv')
    test = pd.read_csv(test_filename)
    test_data = test.drop(test.columns[-1], axis=1)
    test_label = test.iloc[:, -1]
    test_data_tensor = torch.tensor(test_data.values)
    test_label_tensor = torch.tensor(test_label.values)

    # 创建数据集对象
    train_dataset = torch.utils.data.TensorDataset(train_data_tensor, train_label_tensor)
    test_dataset = torch.utils.data.TensorDataset(train_data_tensor, train_label_tensor)

    # 创建数据加载器
    batch_size = 16 # 定义你的小批量大小
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

    criterion = nn.CrossEntropyLoss()

    net = NetLinear();
    train_net(net, train_loader, test_loader)




