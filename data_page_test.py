import streamlit as st
from st_clickable_images import clickable_images
from PIL import Image
from utils import get_orderedList, get_imageNames, load_HEImages, load_coreImages, show_plotly_image, get_core_feature, get_coreStatistic
from style import define_layout
import requests

# Set page layout
st.set_page_config(layout="wide")

# Utility Functions
def disable_other_checkboxes(*other_checkboxes_keys):
    if st.session_state[other_checkboxes_keys[-1]] == False:
        st.session_state[other_checkboxes_keys[-1]] = True
    for checkbox_key in other_checkboxes_keys[:-1]:
        st.session_state[checkbox_key] = False

def get_current_checkedBox(options):
    key = list(options.keys())[list(options.values()).index(True)]
    return key

# Define Layout
max_width = '100%'
define_layout(max_width, '0rem', '0rem', '0rem', '0rem')

# Style
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: white;
    }
    .core-image {
        border-radius: 10px;
        border: 2px solid #f0f0f0;
        margin: 5px;
    }
    .core-image.selected {
        border-color: #ff8000;
    }
    footer {
        font-size: 12px;
        color: #777;
        text-align: center;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align: center;'>The Human Spatial Atlas of Malignant Mesothelioma</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: #002e8c;'>Data Set</h2>", unsafe_allow_html=True)

# Filters Section
st.sidebar.header("Filters")
c1_IDs = ["Institute", "Classification", "CaseType", "subtype", "Grade"]
c1_names = ["Institute", "Classification", "Case type", "Subtype", "Tumor grade"]
cs1 = dict()
c1 = st.columns([3,3,3,3,3])
for i in range(5):
    cs1[i] = c1[i].selectbox(
        c1_names[i],
        get_orderedList(c1_IDs[i]),
        key = c1_IDs[i]
    )

c2_IDs = ["Gender", "DiagnosisAge", "AsbestosExposure", "Race", "smoking"]
c2_names = ["Gender", "Diagnosis age", "Asbestos exposure", "Race", "Smoking"]
cs2 = dict()
c2 = st.columns([3,3,3,3,3])
for i in range(5):
    cs2[i] = c2[i].selectbox(
        c2_names[i],
        get_orderedList(c2_IDs[i]),
        key = c2_IDs[i]
    )

#filters = {}
#for label, ids in zip(c1_names, c1_IDs):
#    filters[ids] = st.sidebar.selectbox(label, get_orderedList(ids))
#for label, ids in zip(c2_names, c2_IDs):
#    filters[ids] = st.sidebar.selectbox(label, get_orderedList(ids))

# Core Images Selection
st.markdown("### Please select a core:")
image_names, core_ids, core_ids2 = get_imageNames(cs1, cs2, c1_IDs, c2_IDs)
images, showedImage_names, showedCore_ids, showedCore_ids2 = load_HEImages('./data/core_image/H&E_logo', image_names, core_ids, core_ids2)

if len(images) > 0:
    clicked = clickable_images(
        images,
        div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
        img_style={"margin": "10px", "height": "70px"}
    )
else:
    st.write("No core available for the current selection.")
    clicked = -1

if len(images) > 0:
    st.divider()
    if clicked == -1: clicked = 0

    # Display Panels for Image Selection
    vargs0 = ["H&E"]
    vargs1 = ["mIF", "CD4", "CD8", "CD20", "CD68", "FOXP3", "panCK"]
    vargs2 = ["mIF ", "CD56", "CD11c", "BAP1", "NF2", "MTAP", "LAG3"]
    vargs = vargs0 + vargs1 + vargs2

    channel_images = load_coreImages(showedImage_names[clicked], showedCore_ids[clicked], showedCore_ids2[clicked])
    ls_images = list(channel_images.values())

    # Panel-Marker and Panel-Protein Headers
    st.markdown('<p style="font-size: 14px; font-weight: bold">Panel-Marker</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 14px; font-weight: bold">Panel-Protein</p>', unsafe_allow_html=True)

    # Image Panel
    cimg = st.columns(len(ls_images))
    for i, img in enumerate(ls_images):
        with cimg[i]:
            st.markdown(img, unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; font-weight: normal; text-align: center'>{vargs[i]}</p>", unsafe_allow_html=True)

    st.divider()

    # Core Features and Selected Image Display
    col1, col2, col3 = st.columns([1.5, 7, 2.5])
    with col1:
        st.markdown("<p style='font-family:sans-serif; color:#002e8c; font-size: 22px; font-weight: bold'>Image Type</p>", unsafe_allow_html=True)
        options = {}
        for key in vargs:
            options[key] = st.checkbox(
                key, value=(key == "H&E"),
                key=key,
                on_change=disable_other_checkboxes,
                args=(list(set(vargs) - {key}) + [key])
            )

        selected_option = get_current_checkedBox(options)

    with col2:
        imgurl = f"https://raw.githubusercontent.com/xim2016/MesotheliomaSpatialAtlas_data/main/{selected_option}/{showedImage_names[clicked]}.jpg"
        if requests.head(imgurl).headers["content-type"] in ("image/jpeg", "image/png"):
            show_plotly_image(imgurl, 750)
        else:
            st.markdown("<p style='font-size: 16px; text-align: center;'>Image data is not available for this core.</p>", unsafe_allow_html=True)

    with col3:
        st.markdown("<p style='font-family:sans-serif; color:#002e8c; font-size: 22px; font-weight: bold'>Core Feature</p>", unsafe_allow_html=True)
        features = get_core_feature(c1_IDs, c2_IDs, showedCore_ids[clicked])
        for feature in features:
            st.markdown(f"**{feature['label']}**: {feature['value']}")

# Footer Section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
<footer>
    <p>© 2024 OsmanbeyogluLab.com. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)
