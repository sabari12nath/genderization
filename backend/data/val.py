# train.py
import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from model import build_model

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH = 32
EPOCHS = 5
LR = 3e-4
NUM_CLASSES = 2

train_tf = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
])
val_tf = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
])

train_ds = datasets.ImageFolder("data/train", transform=train_tf)
val_ds   = datasets.ImageFolder("data/val",   transform=val_tf)
train_ld = DataLoader(train_ds, batch_size=BATCH, shuffle=True, num_workers=2)
val_ld   = DataLoader(val_ds,   batch_size=BATCH, shuffle=False, num_workers=2)

model = build_model(NUM_CLASSES).to(DEVICE)
opt = optim.AdamW(model.parameters(), lr=LR)
crit = nn.CrossEntropyLoss()

best_acc = 0.0
for epoch in range(1, EPOCHS+1):
    model.train()
    loss_sum = 0
    for x, y in train_ld:
        x, y = x.to(DEVICE), y.to(DEVICE)
        opt.zero_grad()
        logits = model(x)
        loss = crit(logits, y)
        loss.backward()
        opt.step()
        loss_sum += loss.item() * x.size(0)
    train_loss = loss_sum / len(train_ds)

    model.eval()
    correct = 0
    with torch.no_grad():
        for x, y in val_ld:
            x, y = x.to(DEVICE), y.to(DEVICE)
            pred = model(x).argmax(1)
            correct += (pred == y).sum().item()
    val_acc = correct / len(val_ds)
    print(f"epoch {epoch}: train_loss={train_loss:.4f} val_acc={val_acc:.3f}")

    if val_acc > best_acc:
        best_acc = val_acc
        torch.save({"state_dict": model.state_dict(),
                    "classes": train_ds.classes}, "gender_resnet18.pth")
        print("saved: gender_resnet18.pth")
