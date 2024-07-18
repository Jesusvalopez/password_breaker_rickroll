import cv2
import os
import numpy as np
import time
import random

ASCII_CHARS = "@#S%?*+;:,."

def delay():
    time.sleep(random.uniform(0.5, 1.5))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def resize_image(image, new_width=100):
    (old_width, old_height) = image.shape[1], image.shape[0]
    aspect_ratio = old_height / float(old_width)
    new_height = int(aspect_ratio * new_width)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image

def grayify(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def pixels_to_ascii(image):
    pixels = image.flatten()
    ascii_str = "".join([ASCII_CHARS[pixel // (256 // len(ASCII_CHARS))] for pixel in pixels])
    return ascii_str

def video_to_ascii(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        gray_image = grayify(frame)
        resized_image = resize_image(gray_image)
        ascii_str = pixels_to_ascii(resized_image)
        ascii_image = "\n".join([ascii_str[i:i+resized_image.shape[1]] for i in range(0, len(ascii_str), resized_image.shape[1])])
        
        clear()

        print(ascii_image)
        
        time.sleep(1/60)

    cap.release()


clear()

print("Por favor, selecciona la red social de tu objetivo:")
print("1. Facebook")
print("2. Instagram")
print("3. Twitter/X")
print("4. TikTok")

option = input("Ingresa el número de tu elección: ")
clear()

email = input("Ingresa el correo eléctronico del objetivo: ")
clear()

if option == "1":
    server = "https://facebook.com/auth?user="+email

elif option == "2":
    server = "https://instagram.com/auth?user="+email

elif option == "3":
    server = "https://x.com/auth?user="+email

elif option == "4":
    server = "https://tiktok.com/auth?user="+email

else:
    print("Opción no válida. Por favor, intenta de nuevo.")


print("Intentando conexión a "+server+".")
delay()
clear()
print("Intentando conexión a "+server+"..")
delay()
clear()
print("Intentando conexión a "+server+"...")
clear()
delay()
print("Buscando usuario "+email+".")
delay()
clear()
print("Buscando usuario "+email+"..")
delay()
clear()
print("Usuario encontrado.")
delay()
clear()

for i in range(0, 101, random.randint(21, 29)):
    print("Desencriptando contraseña")
    print(f"Progreso: {i}%")
    delay()
    clear()


# Ruta del video que deseas convertir
video_path = 'C:\\video.mp4'
video_to_ascii(video_path)