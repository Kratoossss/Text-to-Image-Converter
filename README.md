# PromptToImage Converter

PromptToImage Converter is a Streamlit web application that allows users to generate images from text prompts using a large language model (Llama) and the Stability AI image generation API. Users can select different art styles, expand their prompt for more vivid descriptions, and download the generated images.

---

## Features

- **Text-to-Image Generation:** Enter a prompt and generate a unique image.
- **Art Style Selection:** Choose from styles like Photorealistic, Anime, Watercolor, Cyberpunk, Cartoon, Oil Painting, Pixel Art, and Sketch.
- **Image Download:** Download the generated image directly from the app.

---

## Project Structure

```
ai-test/
│
├── app/
│   ├── main.py            # Streamlit app code
│   └── llm_utils.py       # Llama image generation utilities
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation


```

---

## Setup Instructions

### 1. **Clone the Repository**

```bash
git clone <your-repo-url>
cd ai-test
```

### 2. **Install Python**

- Python 3.8–3.11 is recommended.

### 3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Set Your Stability API Key**

- Get your API key from [Stability AI](https://platform.stability.ai/).
- Set it as an environment variable:
  - **Windows (CMD):**
    ```cmd
    set STABILITY_API_KEY=your_api_key_here
    ```
  - **Windows (PowerShell):**
    ```powershell
    $env:STABILITY_API_KEY="your_api_key_here"
    ```
  - **Linux/Mac:**
    ```bash
    export STABILITY_API_KEY=your_api_key_here
    ```

### 5. **Run the App**

```bash
streamlit run app/main.py
```

- Open your browser and go to [http://localhost:8501](http://localhost:8501)

---

## Usage

1. Enter a description of the scene you want to generate.
2. Select an art style (optional).
3. Click the "✨ Generate" button.
4. View the generated image.
5. Download the image using the provided button.

---

## Requirements

See `requirements.txt` for all Python dependencies.

- Python >=3.8, <3.12
- streamlit
- llama-cpp-python
- requests
- certifi

---

## Notes

- The Stability API key is required for image generation.
- For best results, use a machine with sufficient RAM and CPU resources.

---

## License

This project is for educational and research purposes. Check the licenses Stability AI before commercial use.

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [Stability AI](https://stability.ai/)
