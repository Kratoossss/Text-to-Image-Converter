import streamlit as st
from llm_utils import expand_prompt, generate_image

# Set Streamlit page configuration
st.set_page_config(page_title="🎨 PromptToImage", layout="centered")
st.title("🖼️ PromptToImage Convertor")
st.markdown("✨ **Enter a prompt to generate an image!** ✨")

# --- Style Selection ---
# List of available art styles for the user to choose from
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
# Dropdown for selecting art style
style = st.selectbox("🎭 Choose an art style (optional):", styles)

# --- Prompt Input ---
# Text input for the user to describe the scene they want to generate
prompt = st.text_input("📝 Describe your scene:", "A futuristic city skyline at sunset")

# --- Style prompt append ---
# Remove emoji from style for prompt
style_clean = style.split(" ", 1)[-1] if style != "None" else "None"
final_prompt = prompt
if style and style_clean != "None":
    final_prompt = f"{prompt}, {style_clean} style"

# --- Generate Button ---
# When the user clicks the button, expand the prompt and generate the image
if st.button("✨ Generate Image!"):
    # Expand the prompt using the LLM
    with st.spinner("🧠 Expanding prompt..."):
        expanded = expand_prompt(final_prompt)
    st.write("**📝 Expanded Prompt:**", expanded)

    # Generate the image using the expanded prompt
    with st.spinner("🎨 Generating image..."):
        image_path = generate_image(expanded)
    st.image(image_path, caption="🖼️ Generated Image", use_container_width=True)
    st.success("✅ Image generated!")

    # --- Image Download ---
    # Allow the user to download the generated image
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        st.download_button(
            label="⬇️ Download Image",
            data=img_bytes,
            file_name="generated_image.png",
            mime="image/png"
        )