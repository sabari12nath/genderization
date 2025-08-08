<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />

# Genderization 🎯

## Basic Details
### Team Name: ByteBeards

### Team Members
- Team Lead: Sabarinath ps , SNMIMT

### Project Description
A hilariously over-engineered AI tool that takes your photo and predicts whether you look male or female — because nothing says “innovation” like reinventing the obvious. Powered by a PyTorch model (or pure randomness for extra spice).

### The Problem (that doesn't exist)
Sometimes you wake up, look in the mirror, and think, *"Hmm… am I me today?"*  
Or maybe you just want a computer to confirm what you already know.

### The Solution (that nobody asked for)
Upload your photo, hit **Analyze**, and let our AI deliver a confident verdict.  
Is it useful? Not at all. Is it entertaining? Absolutely.

---

## Technical Details
### Technologies/Components Used
For Software:
- **Languages:** TypeScript, Python
- **Frameworks:** Next.js (App Router), FastAPI
- **Libraries:** React, Tailwind CSS, PyTorch, TorchVision, Pillow
- **Tools:** npm, uvicorn, Postman

For Hardware:
- None — just your laptop and a webcam/smartphone for taking selfies.

---

### Implementation
For Software:
#### Installation
```bash
# Frontend setup
cd frontend
npm install

# Backend setup
cd ../backend
pip install fastapi uvicorn pillow python-multipart
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Start backend
cd backend
uvicorn api:app --reload --port 8000

# Start frontend
cd ../frontend
echo "NEXT_PUBLIC_API_URL=http://127.0.0.1:8000" > .env.local
npm run dev

Project Documentation
For Software:

Screenshots
![Screenshot1](<img width="1784" height="847" alt="image" src="https://github.com/user-attachments/assets/91869b75-b010-4b04-98e4-e4500c54a31c" />
)
Landing page with Upload & Analyze buttons.

![Screenshot2](<img width="1816" height="788" alt="image" src="https://github.com/user-attachments/assets/83dd9198-30ab-4e80-b9f7-bc6d563ba3c4" />
)
Image preview after uploading a photo.



Diagrams
![Workflow](Add workflow diagram here)
The process: User → Next.js → FastAPI → PyTorch/random → JSON → UI renders result.

For Hardware:
(No hardware used for this project.)

Project Demo
Video
[Add your demo video link here]
Shows how a user uploads a photo, clicks Analyze, and receives a prediction.

Additional Demos
Optional: [Link to hosted demo if available]

Team Contributions
sabarinath ps  ui/ux, frontend, backend, fastapi, AI-bot implementation

Made with ❤️ at TinkerHub Useless Projects


