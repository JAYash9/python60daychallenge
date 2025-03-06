import streamlit as st
# Pilloe is used to convert image to grey scale
from PIL import Image
# Title of the app
with st.expander("Start camera"):
    #  Capture Image
    camera_image=st.camera_input("Capture Image")
upload_image=st.file_uploader("Upload Image")
# If image is uploaded
if upload_image:
    img=Image.open(upload_image)
    grey_img=img.convert('L') 
    st.image(grey_img,caption="Grey Image")  

# If image is captured
if camera_image:
    img=Image.open(camera_image)
    grey_img=img.convert('L') 
    st.image(grey_img,caption="Grey Image")  
