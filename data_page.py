import streamlit as st
from st_clickable_images import clickable_images
from streamlit_image_select import image_select
from PIL import Image
from utils import get_orderedList, get_imageNames, load_HEImages, load_coreImages, show_plotly_image, get_core_feature, get_coreStatistic, load_clickable_coreImages
from style import define_layout
import os
import requests
import re

def disable_other_checkboxes(*other_checkboxes_keys):
	# if current one is trun to false, reset it to true
	if st.session_state[other_checkboxes_keys[-1]] == False:
		st.session_state[other_checkboxes_keys[-1]] = True
		
	for checkbox_key in other_checkboxes_keys[:-1]:
		st.session_state[checkbox_key] = False
		
def get_current_checkedBox(options):
	key = list(options.keys())[list(options.values()).index(True)]
	return (key)	 
		
def data_page():
	
	
	REPO_HE = 'https://raw.githubusercontent.com/xim2016/MesotheliomaSpatialAtlas_data/main/H%26E_level1'
	REPO_TMA = 'https://raw.githubusercontent.com/xim2016/MesotheliomaSpatialAtlas_data/main'
 

	max_width = '100%'
	padding_top = '0rem'
	padding_right = '0rem'
	padding_left = '0rem'
	padding_bottom = '0rem'
	define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
	
	st.markdown("""
	<style>
		[data-testid=stSidebar] {
			background-color: white;
		}

	#	 [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
	#	 width: 300px;
	# }
	# [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
	#	 width: 300px;
	#	 margin-left: -100px;
	# }
	</style>
	""", unsafe_allow_html=True)

	PATH_IMG_TMA = "./data/core_image"
	PATH_IMG_HE = "./data/core_image/H&E_level1"  
	path_img_logo = "./data/core_image/H&E_logo" 
	
	with st.expander("Core selection", expanded=True):
		col1, col2, col3 = st.columns([2,1,1])
	
		#Filters
		with col2:
			st.subheader("Filters")
			
			# Filter Column 1
			c2_IDs = ["Institute", "Classification","CaseType","subtype", "Grade"]
			c2_names = ["Institute", "Classification","Case type","Subtype", "Tumor grade"]
			#c2 = st.columns([3,3,3,3,3])
			cs2 = dict()
			for i in range(5):
				cs2[i] = st.selectbox(
							c2_names[i],
							get_orderedList(c2_IDs[i]),
							key = c2_IDs[i]
						)
		with col3:
			st.subheader("") #used for spacing
			
			# Filter Column 2
			c3_IDs = ["Gender", "DiagnosisAge","AsbestosExposure","Race", "smoking"]
			c3_names = ["Gender", "Diagnosis age","Asbestos exposure","Race", "Smoking"]
			cs3 = dict()
			for i in range(5):
				cs3[i] = st.selectbox(
							c3_names[i],
							get_orderedList(c3_IDs[i]),
							key = c3_IDs[i]
						)
		
		with col1:
							
			#H&E use image_names , others use core_ids as image names
	
			image_names, core_ids, core_ids2 = get_imageNames(cs2, cs3, c2_IDs,c3_IDs)
			images, showedImage_names, showedCore_ids, showedCore_ids2 = load_HEImages(path_img_logo , list(image_names), list(core_ids), list(core_ids2))
			
			
			if len(images) > 0 :
				st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Please select a core:</p>',  unsafe_allow_html=True)
				with st.container(height=350):
					clicked = image_select(
						label="",
						images=images,
						captions=showedImage_names,#[f"{i+1:04}" for i in range(len(images))],
						use_container_width=False,
						return_value="index"
					)

			else:
				st.write("No core for current selection.")


					
	if len(images) == 0:
		for i in range(20):
			st.markdown("#")
			
	if len(images) > 0 :

		st.divider()

		if clicked == -1: clicked = 0

		vargs0 = ["H&E"] # 0
		vargs1 = ["mIF (Marker Panel)", "CD4 (Marker Panel)", "CD8 (Marker Panel)", "CD20 (Marker Panel)", "CD68 (Marker Panel)", "FOXP3 (Marker Panel)", "panCK (Marker Panel)"] # 1-7
		vargs2 = ["mIF (Protein Panel)", "CD56 (Protein Panel)", "CD11c (Protein Panel)", "BAP1 (Protein Panel)","NF2 (Protein Panel)", "MTAP (Protein Panel)","LAG3 (Protein Panel)"] # 8-14
		vargs = vargs0 + vargs1 + vargs2   

		chanel_images = load_coreImages(showedImage_names[clicked],showedCore_ids[clicked],showedCore_ids2[clicked] )
	
		cimg = st.columns(15)

		c1, c2,_,c3 = st.columns([4, 6.75,0.25,2.5])
		with c1:
			st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Image type</p>',  unsafe_allow_html=True) #sans-serif   Soin Sans Pro

			
			with st.container(height=650):
				clicked_img = image_select(
					label="",
					images=chanel_images,
					captions=vargs,
					use_container_width=False,
					return_value="index"
				)
		option2dir = [f"{REPO_HE}",
					f"{REPO_TMA}/panel1/multi",
					f"{REPO_TMA}/panel1/CD4",
					f"{REPO_TMA}/panel1/CD8",
					f"{REPO_TMA}/panel1/CD20",
					f"{REPO_TMA}/panel1/CD68",
					f"{REPO_TMA}/panel1/FOXP3",
					f"{REPO_TMA}/panel1/panCK",
					f"{REPO_TMA}/panel2/multi2",
					f"{REPO_TMA}/panel2/CD56",
					f"{REPO_TMA}/panel2/CD11c",
					f"{REPO_TMA}/panel2/BAP1",
					f"{REPO_TMA}/panel2/NF2",
					f"{REPO_TMA}/panel2/MTAP",
					f"{REPO_TMA}/panel2/LAG3"
		]
		
		clicked_img2name = [
			"H&E",
			"mIF",
			"CD4",
			"CD8",
			"CD20",
			"CD68",
			"FOXP3",
			"panCK",
			"mIF ",
			"CD56",
			"CD11c",
			"BAP1",
			"NF2",
			"MTAP",
			"LAG3"
		]


		options = dict()

		# Image Column
		with c2:

			dir = option2dir[clicked_img]
			option = clicked_img2name[clicked_img]

			if clicked_img == 0: #H&E
				filename = f"{showedImage_names[clicked]}.jpg"
			elif 1 <= clicked_img <=7 : # in vargs1 :   
				filename = f"{showedCore_ids[clicked]}_composite_image.jpg"
			else:
				filename = f"{showedCore_ids2[clicked]}_composite_image.jpg"

			imgurl = f"{dir}/{filename}"
			imgurl = imgurl.replace(" ", "%20") # replace space
			imgurl = imgurl.replace("#", "%23") # replace # 

			def exists(path): #not used
				r = requests.head(path)
				return r.status_code == requests.codes.ok
			
			def is_url_image(image_url):
				image_formats = ("image/png", "image/jpeg")
				r = requests.head(image_url)
				# st.write(r.headers["content-type"])
				if r.headers["content-type"] in image_formats:
					return True
				return False

			if is_url_image(imgurl):
#				show_plotly_image(imgurl, 750)
				st.image(imgurl)
				
				img = requests.get(imgurl)
				image_data = img.content
				
				st.markdown(f"[Click here to view full size image. :material/open_in_new:]({imgurl})")
				
				# Button to open image in another window
				
				st.download_button(
					label="Download image",
					data=image_data,
					file_name=filename,
					mime="image/png",
					type="primary",
					icon=":material/download:"
				)
			else:
				st.markdown("#")
				info = '<p style="font-size: 16px; font-weight: bold;text-align: center">Image datas is not available for this core.</p>'  #sans-serif   Soin Sans Pro
				st.markdown(info, unsafe_allow_html=True)


		#Core Feature Column
		with c3:
			
			# st.markdown("#### Core feature", True)
			st.markdown( '<p style="font-family:sans-serif; color:#002e8c; font-size: 22px;  font-weight: bold">Core feature</p>',  unsafe_allow_html=True) 
			st.write("")
			st.write("")	


			core_id = showedCore_ids[clicked]

			fetu1, fetu2, fetu_plus = get_core_feature(c2_IDs, c3_IDs, core_id)
			for i in range(5):
				st.markdown(f"**{c2_names[i]}** : {fetu1[i]}", True)
			for i in range(5):
				st.markdown(f"**{c3_names[i]}** : {fetu2[i]}", True)
				# st.markdown(f"**:black[{c2_names[i]}]** : {fetu2[i]}", True) 
			for item in fetu_plus.keys():
				st.markdown(f"**{item}** : {fetu_plus[item]}", True)   

			percent, count1, count2 = get_coreStatistic(core_id, option)

			if option in vargs1:
				count = count1
			else:
				count = count2
			st.markdown(f"**Number of cells** : {count}", True) 
			# st.markdown(f"**{option} percentage** : {percent}", True)  

			if option != "H&E":
				st.divider()
				st.markdown("**DAPI in :blue[blue color]**")


	
