# infer.py
import io, torch
from PIL import Image
from torchvision import transforms
from model import build_model

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

tf = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=(0.485,0.456,0.406), std=(0.229,0.224,0.225)),
])

class GenderPredictor:
    def __init__(self, ckpt_path="gender_resnet18.pth"):
        ckpt = torch.load(ckpt_path, map_location="cpu")
        self.classes = ckpt.get("classes", ["male","female"])  # fallback
        self.model = build_model(num_classes=len(self.classes))
        self.model.load_state_dict(ckpt["state_dict"])
        self.model.eval().to(DEVICE)

    @torch.inference_mode()
    def predict_pil(self, img: Image.Image):
        x = tf(img).unsqueeze(0).to(DEVICE)
        logits = self.model(x)
        prob = torch.softmax(logits, dim=1)[0]
        conf, idx = torch.max(prob, dim=0)
        return self.classes[idx.item()], float(conf)

    def predict_bytes(self, b: bytes):
        img = Image.open(io.BytesIO(b)).convert("RGB")
        return self.predict_pil(img)

    def predict_path(self, path: str):
        img = Image.open(path).convert("RGB")
        return self.predict_pil(img)

if __name__ == "__main__":
    gp = GenderPredictor("gender_resnet18.pth")
    label, conf = gp.predict_path("sample.jpg")
    print(label, f"{conf*100:.1f}%")
