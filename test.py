import requests

# L'URL de votre API Flask
url = 'https://api-render-146a.onrender.com/predict'

# Chemin vers l'image à tester
image_path = 'test_image_1.png'

# Charger l'image et l'envoyer avec le modèle choisi
with open(image_path, 'rb') as file:
    files = {'file': file}
    data = {'model': 'Logistic Regression'}  # Indiquez le modèle ici
    response = requests.post(url, files=files, data=data)

# Afficher la réponse
print(response.json())
