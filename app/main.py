import streamlit as st
from llm_utils import generate_image

# Set Streamlit page configuration
st.set_page_config(page_title="🎨 PromptToImage", layout="centered")
st.title("🖼️ PromptToImage Converter")
st.markdown("✨ **Enter a prompt to generate an image!** ✨")

# --- Style Selection ---
styles = [
    "None",
    "📸 Photorealistic",
    "🌸 Anime",
    "🎨 Watercolor",
    "🤖 Cyberpunk",
    "🦸 Cartoon",
    "🖌️ Oil Painting",
    "🟦 Pixel Art",
    "✏️ Sketch"
]
style = st.selectbox("🎭 Choose an art style (optional):", styles)

# --- Prompt Input ---
prompt = st.text_input("📝 Describe your scene:", "A futuristic city skyline at sunset")

# --- Style prompt append ---
style_clean = style.split(" ", 1)[-1] if style != "None" else "None"
final_prompt = prompt
if style and style_clean != "None":
    final_prompt = f"{prompt}, {style_clean} style"

# --- Generate Button ---
if st.button("✨ Generate Image!"):
    with st.spinner("🎨 Generating image..."):
        image_path = generate_image(final_prompt)
    st.image(image_path, caption="🖼️ Generated Image", use_container_width=True)
    st.success("✅ Image generated!")

    # --- Image Download ---
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        st.download_button(
            label="⬇️ Download Image",
            data=img_bytes,
            file_name="generated_image.png",
            mime="image/png"
        )
