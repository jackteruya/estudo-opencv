from engine import DetecterMale, DetecterFemale


img = "img.png"

# Iniciando detector de faces masculino
print("Iniciando detector de faces masculino")
detector_masculino = DetecterMale()

# lendo a imagem
print("lendo a imagem")
detector_masculino.read_image(img)

# detectando faces em geral
print("detectando faces em geral")
detector_masculino.faces_detection()

# detectando faces masculina
print("detectando faces masculina")
detector_masculino.faces_gender_detection()

print("\n", "#" * 10)
# Iniciando detector de faces feminina
print("Iniciando detector de faces femininas")
detector_feminina = DetecterFemale()

# lendo a imagem
print("lendo a imagem")
detector_feminina.read_image(img)

# detectando faces em geral
print("detectando faces em geral")
detector_feminina.faces_detection()

# detectando faces masculina
print("detectando faces femininas")
detector_feminina.faces_gender_detection()
