import json

def img(url):
    return url + "?w=400&h=400&fit=crop"

def get_images(name, category):
    name = name.lower()

    # -------- STROLLERS --------
    if "stroller" in name:
        return [
            img("https://images.unsplash.com/photo-1591088398332-8a7791972843"),
            img("https://images.unsplash.com/photo-1519689680058-324335c77eba")
        ]

    # -------- PLAY MAT / GYM --------
    if "play mat" in name or "gym" in name:
        return [
            img("https://images.unsplash.com/photo-1566140967404-b8b3932483f5"),
            img("https://images.unsplash.com/photo-1587654780291-39c9404d746b")
        ]

    # -------- COT / NURSERY --------
    if "cot" in name or "crib" in name or "playard" in name:
        return [
            img("https://images.unsplash.com/photo-1586105251261-72a756497a11"),
            img("https://images.unsplash.com/photo-1595526114035-0d45ed16cfbf")
        ]

    # -------- CAR SEAT --------
    if "car seat" in name:
        return [
            img("https://images.unsplash.com/photo-1558618666-fcd25c85cd64"),
            img("https://images.unsplash.com/photo-1519689680058-324335c77eba")
        ]

    # -------- BOTTLES / FEEDING --------
    if "bottle" in name or "feeding" in name or "pump" in name:
        return [
            img("https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4"),
            img("https://images.unsplash.com/photo-1584515933487-779824d29309")
        ]

    # -------- BOUNCER --------
    if "bouncer" in name:
        return [
            img("https://images.unsplash.com/photo-1585435557343-3b092031a831"),
            img("https://images.unsplash.com/photo-1519689680058-324335c77eba")
        ]

    # -------- TOYS --------
    if "toy" in name or "lego" in name:
        return [
            img("https://images.unsplash.com/photo-1558060370-d644479cb6f7"),
            img("https://images.unsplash.com/photo-1587654780291-39c9404d746b")
        ]

    # -------- SKINCARE --------
    if "lotion" in name or "cleansing" in name:
        return [
            img("https://images.unsplash.com/photo-1556228578-0d85b1a4d571"),
            img("https://images.unsplash.com/photo-1596462502278-27bfdc403348")
        ]

    # -------- CLOTHING --------
    if "onesie" in name:
        return [
            img("https://images.unsplash.com/photo-1522771930-78848d9293e8"),
            img("https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9")
        ]

    # -------- BABY MONITOR --------
    if "monitor" in name:
        return [
            img("https://images.unsplash.com/photo-1563302111-eab4b145e6c9"),
            img("https://images.unsplash.com/photo-1581578731548-c64695cc6952")
        ]

    # -------- CARRIER --------
    if "carrier" in name:
        return [
            img("https://images.unsplash.com/photo-1476703993599-0035a21b17a9"),
            img("https://images.unsplash.com/photo-1519689680058-324335c77eba")
        ]

    # -------- DEFAULT (fallback) --------
    return [
        img("https://images.unsplash.com/photo-1519689680058-324335c77eba"),
        img("https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c")
    ]


# -------- LOAD DATA --------
with open("data/products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# -------- UPDATE PRODUCTS --------
for p in products:
    p["images"] = get_images(p["name"], p["category"])

    # remove old field
    if "image_url" in p:
        del p["image_url"]

# -------- SAVE UPDATED DATA --------
with open("data/products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("✅ All products updated with 2 correct images each")