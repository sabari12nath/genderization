# model.py
import torch
import torch.nn as nn
from torchvision import models, transforms


def build_model(num_classes: int = 2) -> nn.Module:
    m = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
    in_features = m.fc.in_features
    m.fc = nn.Linear(in_features, num_classes)
    return m
