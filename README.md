# Selfie Partículas 3D 🎥✨

Aplicação web interativa em **Processing (p5.js)** e **HTML5** que utiliza a câmera do dispositivo para exibir a imagem em tempo real transformada em uma representação artística de partículas tridimensionais flutuantes.

## 🚀 Recursos
- **Câmera em Tempo Real:** Captura o feed de vídeo da câmera (frontal ou traseira).
- **Efeito de Partículas 3D (WEBGL):** O brilho e a cor de cada pixel do vídeo determinam a profundidade (eixo Z) e a cor das partículas.
- **Estilos Dinâmicos:** Alternância entre grade estruturada em 3D e partículas esféricas flutuantes.
- **Gravação de Vídeo e Áudio:** Permite gravar a tela e o áudio do microfone simultaneamente e baixar o vídeo gerado (`.webm`) diretamente no dispositivo.
- **Design Responsivo:** Otimizado para dispositivos móveis e desktops.

## 🛠️ Tecnologias Utilizadas
- [p5.js](https://p5js.org/) (Biblioteca JavaScript para computação criativa / Processing)
- HTML5 / CSS3 (WEBGL, MediaRecorder API, getUserMedia)

## 📦 Como Usar Localmente
1. Clone o repositório ou baixe os arquivos.
2. Inicie um servidor HTTP local (por exemplo, via Python):
   ```bash
   python3 -m http.server 8000
   ```
3. Acesse no navegador: `http://localhost:8000/index.html`
4. Conceda permissão para a câmera e o microfone.
