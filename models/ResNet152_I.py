from torch import nn
import torch
from torchvision import models


class ResNet152_I(nn.Module):
    def __init__(self, n_classes, mlp_size=256, device='cpu'):
        super(ResNet152_I, self, ).__init__()

        self.pre_model = models.resnet152(weights=None)

        self.device = device

        self.injection_features = 99
        self.nn_features = mlp_size - self.injection_features

        self.part = nn.Sequential(
            self.pre_model.conv1,
            self.pre_model.bn1,
            self.pre_model.relu,
            self.pre_model.maxpool,
            self.pre_model.layer1,
            self.pre_model.layer2,
            self.pre_model.layer3,
            self.pre_model.layer4,
            self.pre_model.avgpool,
        )

        self.injection_layer1 = nn.Linear(2048, self.nn_features)
        self.injection_layer2 = nn.Linear(mlp_size, n_classes)
        self.logSoftmax = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x1 = x['x1'].to(self.device)

        b, c, h, w = x1.shape
        x1 = x1.expand(b, 3, h, w)

        x1 = self.part(x1)
        x1 = x1.reshape(x1.size(0), -1)

        out = self.injection_layer1(x1)

        x2 = x['x2'].to(self.device)
        x2 = torch.nn.functional.normalize(x2)
        out = torch.hstack([out, x2])

        out = self.injection_layer2(out)

        return self.logSoftmax(out)

