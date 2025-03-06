import streamlit as st
from PIL import Image

camera_image=st.camera_input("Capture Image")
if camera_image:
    img=Image.open(camera_image)
    grey_img=img.convert('L') 
    st.image(grey_img,caption="Grey Image")  

