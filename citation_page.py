from style import define_layout
import streamlit as st
# from descriptions import Desc

def citation_page():
	 
	max_width = '90%'
	padding_top = '0rem'
	padding_right = '0rem'
	padding_left = '13rem'
	padding_bottom = '0rem'
	define_layout(max_width, padding_top, padding_right, padding_left, padding_bottom)
		 
	# st.markdown(f"<p style='color: black; font-weight: bold'>Citation guidelines for the Mesothelioma Spatial Atlas</h2>", unsafe_allow_html=True)
	st.markdown("**Citation guidelines for the Mesothelioma Spatial Atlas**")
	st.markdown("While we encourage you to use these resources for your research and commercial purposes, we want to ensure that our content is given proper citation in all cases where it is used.") 
	 
	st.markdown("###")
	# st.markdown(f"<p style='color: black; font-weight: bold'>General citation for the Mesothelioma Spatial Atlas</h3>", unsafe_allow_html=True)
	# st.markdown(f"<p style='text-align: justify; color: black;'>{Citation_general}</h4>", unsafe_allow_html=True) 
	st.markdown("**General citation for the Mesothelioma Spatial Atlas**") 
	st.markdown("If you cite or display any content, or reference this website, in any format, written or otherwise, including print or web publications, presentations, grant applications, websites, other online applications such as blogs, or other works, you must include a reference to our website: https://mesotheliomaspatialatlas.streamlit.app.")

	st.markdown("###")
	# st.markdown(f"<p style='color: black; font-weight: bold'>Specific citation for image, chanel or data</h3>", unsafe_allow_html=True)
	st.markdown("**Specific citation for image, chanel or data**")
	st.markdown("If you use images, or reference a specific image type, or other data downloaded from the site, in addition to citing the Mesothelioma Spatial Atlas, please also cite the specific image,  or data used and the URL that links directly to that information in a manner that will allow a third party to navigate to that image or data on the site.") 
	 
	st.markdown("###")
	# st.markdown(f"<p style='color: black; font-weight: bold'>Citation</h3>", unsafe_allow_html=True)
	st.markdown("**Citation**")
	st.markdown("If you find the images or data from this website helpful, please cite the paper: https://www.biorxiv.org/content/10.1101/2023.09.06.556559v1")

	st.markdown("#")
	st.markdown("Click below for a downloable citation")


#citation in APA format and MLA format

	apa_citation= "Ma, X., Lembersky, D., Kim, E. S., Becich, M. J., Testa, J. R., Bruno, T. C., & Osmanbeyoglu, H. U. (2024). Spatial Landscape of Malignant Pleural and Peritoneal Mesothelioma Tumor Immune Microenvironments. Cancer research communications, 4(8), 2133–2146. https://doi.org/10.1158/2767-9764.CRC-23-0524"

	mla_citation="Ma, Xiaojun et al. “Spatial Landscape of Malignant Pleural and Peritoneal Mesothelioma Tumor Immune Microenvironments.” Cancer research communications vol. 4,8 (2024): 2133-2146. doi:10.1158/2767-9764.CRC-23-0524"


	#button for APA citation- clicking on the button downlaods a textedit file with the citation

	#label is text on button, data is the varible apa_citation that was created on line 42.

	# file name is the name on the user computer, mime indicates the type of file being downloaded.

	st.download_button(
		label="APA",
		data=apa_citation,
		file_name="citations_apa.txt",
		mime="text/plain"
	)

	#button for MLA citation- clicking on the button downlaods a textedit file with the citation

	#label is text on button, data is the varible mla_citation that was created on line 43.

	# file name is the name on the user computer, mime indicates the type of file being downloaded.

	st.download_button(

		label="MLA",
		data=mla_citation,
		file_name="citations_mla.txt",
		mime="text/plain"
	)
