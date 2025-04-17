import streamlit as st
from PIL import Image

st.set_page_config(page_title="HVF Diagnosis Assistant", layout="centered")

st.title("👁️ HVF Diagnosis Assistant")
st.write("Upload a **Humphrey Visual Field (HVF)** grayscale image to get a diagnosis.")

# Upload image
uploaded_file = st.file_uploader("Choose an HVF image", type=["jpg", "jpeg", "png", "bmp"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded HVF", use_column_width=True)

    # Simulated diagnosis
    diagnosis = "🧠 Neurological Visual Field Defect"
    reasoning = (
        "The visual field shows a dense right-sided homonymous hemianopia that respects the vertical midline, "
        "suggesting a post-chiasmal lesion — likely a left occipital infarct. "
        "This is a classic neurological pattern and is not consistent with glaucoma."
    )

    st.subheader("📋 Diagnosis")
    st.success(diagnosis)

    st.subheader("🔍 Reasoning")
    st.write(reasoning)

