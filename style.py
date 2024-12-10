import streamlit as st

footer="""
<style>
	h1 {
		color: #003594;
	}
	
	.image 
	{ 
		padding: 10px;
		transition: transform .2s;
	}


	.image:hover {  
		transform: scale(1.5);
		transition: 0.2s;
	}
	
	.footer {
		position: relative;
		width: 100%;
		left: 0;
		bottom: 0;
		background-color: #003594;
		margin-top: auto;
		color: black;
		padding: 24px;
		text-align: center;
	}
</style>

<div class="footer">
<p style="font-size:  14px; color:#FFB81C;">© 2023 Osmanbeyoglulab.com. All rights reserved.</p>
<a href="https://hillman.upmc.com/"><img class="image" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS7c7pXIkFgMPVM2csVE6MenUFLEsgF5beCeMJzogkPkXPC4xEo9OTHf6nVpqsb3PvisRk&usqp=CAU" alt="Hillman.UPMC.com Link" height="45"></a>
<a href="https://www.pitt.edu/"><img class="image" src="https://upload.wikimedia.org/wikipedia/en/thumb/f/fb/University_of_Pittsburgh_seal.svg/300px-University_of_Pittsburgh_seal.svg.png"alt="Pitt.edu Link" width="45" height="45"></a>
<a href="https://github.com/osmanbeyoglulab"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Github_logo_svg.svg/1200px-Github_logo_svg.svg.png?20230420150203" alt="GitHub Link" width="45" height="45"></a>
<a href="https://twitter.com/hosmanbeyoglu?lang=en"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/X_logo_2023_%28white%29.svg/600px-X_logo_2023_%28white%29.svg.png?20241003144821"alt="X Link" width="45" height="40"></a>
<a href="https://scholar.google.com/citations?user=YzCsmdgAAAAJ&hl=en&inst=7044483460239389945"><img class="image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Google_Scholar_logo.svg/512px-Google_Scholar_logo.svg.png"alt="Google Scholar Link" width="45" height="45"></a>
</div>

"""


page_style = """
	<style>
		#MainMenu {visibility: hidden;} 
		footer {visibility: hidden;} 
	</style>
"""


def define_layout(max_width, padding_top='0rem', padding_right='0rem', padding_left='0rem', padding_bottom='0rem'):

	# # add page to relative width
# max_width_str = f"max-width: {63.5}%;"
# st.markdown(f"""
#	 <style>
#	 .appview-container .main .block-container{{{max_width_str}}}
#	 </style>
#	 """,
#	 unsafe_allow_html=True,
# )   

	st.markdown(
		f"""
		<style>
			.appview-container .main .block-container{{
				max-width: {max_width};
				padding-top: {padding_top};
				padding-right: {padding_right};
				padding-left: {padding_left};
				padding-bottom: {padding_bottom};
			}}
		  
		</style>
		""",
		unsafe_allow_html=True,
	)
