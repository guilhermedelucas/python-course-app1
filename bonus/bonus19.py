import streamlit as st
from PIL import Image
import io

uploaded_image = st.file_uploader("Upload Image")

with st.expander('Start Camera'):
    # Start the camera
    camera_image = st.camera_input('Camera')

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Display the grayscale image on the webpage
    st.image(gray_img)

    # Convert the grayscale image to bytes
    img_bytes = io.BytesIO()
    gray_img.save(img_bytes, format='PNG')

    # Add a download button for the grayscale image
    st.download_button(
        label='Download Grayscale Image',
        data=img_bytes.getvalue(),
        file_name='grayscale_image.png',
    )


if uploaded_image:
    # Create a pillow image instance
    img = Image.open(uploaded_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert('L')

    # Display the grayscale image on the webpage
    st.image(gray_img)