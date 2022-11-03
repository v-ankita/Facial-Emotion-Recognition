import streamlit as st
from PIL import Image, ImageOps
from classifier import teachable_machine_classification

st.title("Facial Emotion Recognition using Deep Learning models")
st.header("Classifiying facial images based on emotion")
st.write("""""")
st.write("""
##### Upload the image of a face for recognizing it as belonging to one of the 7 emotion categroies -
""")
st.write("""##### Happy, Sad, Neutral, Angry, Fear, Surprise, Disgust""")

uploaded_file = st.file_uploader("Choose an image of a face ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width='auto')
    st.write("")
    st.write("##### Classifying...")
    label = teachable_machine_classification(image, 'cnn_2.h5')
    if label == 0:
        st.write("### Emotion: ANGRY")
    elif label == 1:
        st.write("### Emotion: DISGUST")
    elif label == 2:
        st.write("### Emotion: FEAR")
    elif label == 3:
        st.write("### Emotion: HAPPY")
    elif label == 4:
        st.write("### Emotion: NEUTRAL")
    elif label == 5:
        st.write("### Emotion: SAD")
    elif label == 6:
        st.write("### Emotion: SURPRISE")
    else:
        st.write("Invalid Label")
