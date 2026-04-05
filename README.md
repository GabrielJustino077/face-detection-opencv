# Detector de Rostos em Tempo Real

Projeto desenvolvido com Python e OpenCV para detecção de rostos em tempo real via webcam,
como parte do meu aprendizado prático em visão computacional.

## Como funciona

O sistema utiliza o classificador *Haar Cascade* — um algoritmo de machine learning treinado
com milhares de imagens de rostos que aprende a identificar padrões faciais (olhos, nariz,
contorno do rosto). A cada frame capturado pela webcam, o algoritmo varre a imagem em busca
desses padrões e marca os rostos detectados com um retângulo.

Pipeline de processamento:
1. Captura do frame da webcam
2. Conversão para escala de cinza (reduz complexidade e melhora desempenho)
3. Detecção de rostos com Haar Cascade
4. Desenho de bounding boxes sobre os rostos encontrados
5. Exibição do frame anotado em tempo real

## Tecnologias

- Python
- OpenCV

## Como executar

1. Instale as dependências:
      pip install opencv-python
2. Execute:
     python detector.py
3. Pressione **ESC** para encerrar.

## Aprendizados

O maior desafio foi entender como o OpenCV organiza e processa imagens — especialmente
por que a conversão para escala de cinza é necessária antes da detecção, e como os
parâmetros do `detectMultiScale` (escala e vizinhos mínimos) afetam a precisão.
