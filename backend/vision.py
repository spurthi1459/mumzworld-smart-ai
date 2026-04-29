from PIL import Image
import io
import torch
import clip

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Predefined product categories
CATEGORIES = [
    "baby stroller",
    "baby carrier",
    "baby toy",
    "baby bottle",
    "baby skincare",
    "baby bouncer",
    "baby monitor",
    "baby play mat"
]


def describe_image(image_bytes):
    try:
        # Convert bytes to image
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        # Preprocess image
        image_input = preprocess(image).unsqueeze(0).to(device)

        # Encode image
        with torch.no_grad():
            image_features = model.encode_image(image_input)

        # Encode text labels
        text_inputs = torch.cat([clip.tokenize(c) for c in CATEGORIES]).to(device)

        with torch.no_grad():
            text_features = model.encode_text(text_inputs)

        # Compute similarity
        similarity = (image_features @ text_features.T).softmax(dim=-1)

        # Get best match
        index = similarity.argmax().item()

        return CATEGORIES[index]

    except Exception as e:
        print("Vision error:", e)

        # Safe fallback
        return "baby product"