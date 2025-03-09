import requests

# L'URL de votre API Flask
url = 'https://api-render-146a.onrender.com/predict'

# Chemin vers l'image à tester
#image_path = 'test_image_11.png'
image_path="test_images/test_image_11.png"
# Charger l'image et l'envoyer avec le modèle choisi
with open(image_path, 'rb') as file:
    files = {'file': file}
    data = {'model': 'Logistic Regression'}  # Indiquez le modèle ici
    response = requests.post(url, files=files, data=data)
fmnist_classes = [
    "T-shirt/top",  # Classe 0
    "Trouser",      # Classe 1
    "Pullover",     # Classe 2
    "Dress",        # Classe 3
    "Coat",         # Classe 4
    "Sandal",       # Classe 5
    "Shirt",        # Classe 6
    "Sneaker",      # Classe 7
    "Bag",          # Classe 8
    "Ankle boot"    # Classe 9
]

# Afficher la réponse
print(fmnist_classes[response.json()['prediction']])
