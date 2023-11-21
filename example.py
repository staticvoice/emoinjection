from pathlib import Path
import numpy as np

from torch.utils.data import DataLoader
from torch.utils.data import Dataset
import torch

from models.ResNet152_I import ResNet152_I


class TorchDataset(Dataset):
    """ Interface for creating an instance of torch Dataset. """

    def __init__(self, dataset: dict):
        self.dataset = dataset

    def __len__(self) -> int:
        return self.dataset['len']

    def __getitem__(self, idx: int) -> dict:
        return {"x1": self.dataset['x1'][idx], "x2": self.dataset['x2'][idx],
                "y": self.dataset['y'][idx].double()}


def predict(x: dict, model: torch.nn.Module, device: str = 'cpu') -> int:
    
    model.eval()
    with torch.no_grad():
        y_pred = model(x)

    y_true = x['y'].long().to(device)
    
    return (y_pred.argmax(1) == y_true).type(torch.float).sum().item()


if __name__ == "__main__":

    device = 'cpu'

    data = torch.load("dataset/emodb-test-data.pth")
    data = DataLoader(TorchDataset(data), batch_size=8, shuffle=True)

    model = ResNet152_I(n_classes=7, mlp_size=2048, device=device)
    model.load_state_dict(torch.load("models/ResNet152_I.pth",
                          map_location=torch.device(device)))

    ACCURACY = 0.0

    for x in data:
        ACCURACY += predict(x, model)

    ACCURACY /= len(data.sampler)

    print(f"Weighted Accuracy (WA): {ACCURACY*100:.2f}")



