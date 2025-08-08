from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import torch
import random
from PIL import Image
from io import BytesIO
from torchvision import transforms
from model import build_model

app = FastAPI()

# Allow CORS so Next.js frontend can connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can replace "*" with ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy model (no training, random output)
model = build_model(num_classes=2)
model.eval()

# Just for resizing images before sending to model
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    try:
        # Read and preprocess image
        image_bytes = await file.read()
        image = Image.open(BytesIO(image_bytes)).convert("RGB")
        image_tensor = transform(image).unsqueeze(0)

        # Since we don’t have a trained model, return random output
        classes = ["male", "female"]
        prediction = random.choice(classes)

        return {"gender": prediction}

    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def root():
    return {"message": "Gender Detection API is running"}
