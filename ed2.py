import streamlit as st
import time

# Set background color to light blue
st.markdown("""
<style>
.stApp {
    background-color: lightblue;
}
</style>
""", unsafe_allow_html=True)

if "photo" not in st.session_state:
    st.session_state["photo"] = "not done"

st.title("Hello, I am Edward Hillenaar")
st.header("This is a first website made with python and Streamlit!")
st.subheader("This is a simple app to demonstrate some of the features of Streamlit.")
st.text("This is a simple text element.")

col1, col2, col3 = st.columns([1, 2, 1])
col1.markdown("Welcome to my website!")
col1.markdown("Here is some info on the app.")

def change_photo_state():
    st.session_state["photo"] = "done"

uploaded_photo = col2.file_uploader("Upload a photo", type=["png", "jpg", "jpeg"], on_change=change_photo_state)
camera_photo = col2.camera_input("Take a picture", on_change=change_photo_state)

if st.session_state["photo"] == "done":
    # Ensure progress bar runs only once
    if not hasattr(st.session_state, "progress_done"):
        st.session_state.progress_done = False

    if not st.session_state.progress_done:
        progress_bar = col2.progress(0)
        for percent_complete in range(100): 
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        st.session_state.progress_done = True
        col2.success("Photo Loading complete!")

    # Display metric in column 3
    col3.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    with st.expander("See explanation"):
        st.write("""
            This is an example of an expander. 
            You can put any content you want inside it, 
            including text, images, and other Streamlit components.
        """)
        # Display the correct image based on user input
        if uploaded_photo is not None:
            st.image(uploaded_photo)
        elif camera_photo is not None:
            st.image(camera_photo)
        else:
            st.warning("No photo available.")



