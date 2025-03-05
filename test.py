import requests

# URL de l'API Flask
API_URL = "https://api-render-146a.onrender.com/predict"

# Chemin de l'image à tester
image_path = "C:/Users/abdal/OneDrive/Bureau/master-master/labs/Project/test_images/test_image_1.png"

# Nom du modèle sélectionné
model_name = "Logistic Regression"  # Remplacez par le modèle que vous voulez tester

# Lire l'image en mode binaire
with open(image_path, "rb") as img_file:
    img_bytes = img_file.read()

# Préparer les données de la requête
files = {"file": ("test_image_1.png", img_bytes, "image/png")}
data = {"model": model_name}

# Envoyer la requête POST à l'API
response = requests.post(API_URL, files=files, data=data)

# Afficher le résultat de la prédiction
if response.status_code == 200:
    result = response.json()
    prediction = result.get("prediction")
    
    if prediction is not None:
        # Liste des classes Fashion MNIST
        fmnist_classes = [
            "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal",
            "Shirt", "Sneaker", "Bag", "Ankle boot"
        ]
        
        # Afficher la classe prédite
        class_name = fmnist_classes[prediction]
        print(f"**Prédiction :** {class_name} (Classe {prediction})")
    else:
        print("Aucune prédiction reçue de l'API.")
else:
    print(f"Erreur lors de la prédiction : {response.text}")
