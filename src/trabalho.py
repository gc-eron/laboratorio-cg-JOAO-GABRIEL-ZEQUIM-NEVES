import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("1. Saturação")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)
fator = col1.slider("Fator de saturação", 0.0, 2.0, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(img, caption="original")
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="saturação")

st.header("4. Tons de cinza")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
media = ((r + g + b) / 3).astype(np.uint8)
col1.image(media, caption="média")
peso_r = col2.slider("Peso do R", 0.0, 1.0, 0.30)
peso_g = col2.slider("Peso do G", 0.0, 1.0, 0.59)
peso_b = col2.slider("Peso do B", 0.0, 1.0, 0.11)
ponderada = peso_r * r + peso_g * g + peso_b * b
ponderada = np.clip(ponderada, 0, 255).astype(np.uint8)
col2.image(ponderada, caption="média ponderada")

st.header("10. Negativo numa região")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)
altura, largura = img.shape[0], img.shape[1]
y = col1.slider("Linha inicial (y)", 0, altura - 1, altura // 4)
x = col1.slider("Coluna inicial (x)", 0, largura - 1, largura // 4)
t = col1.slider("Lado do quadrado", 10, largura, largura // 3)
col1.image(img, caption="original")
nova = img.copy()
regiao = nova[y:y + t, x:x + t]
negativo = 255 - regiao
nova[y:y + t, x:x + t] = negativo
col2.image(nova, caption="negativo na região")

st.header("12. Simetria")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)
largura = img.shape[1]
meio = largura // 2
nova = img.copy()
esquerda = img[:, :meio]
espelho = esquerda[:, ::-1]
nova[:, largura - meio:] = espelho
col1.image(img, caption="original")
col2.image(nova, caption="simétrica")

st.header("14. Só uma cor")
foto = Image.open("imagens/foto.jpg")
img = np.array(foto)
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h_min, h_max = col1.slider("Faixa de H da cor", 0, 179, (100, 130))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
col1.image(img, caption="original")
so_cor = img.copy()
fora = mascara == 0
so_cor[fora] = 0
col2.image(so_cor, caption="só a cor escolhida")
