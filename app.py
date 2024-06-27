import os
import json
import streamlit as st
from src.utils_json import get_json
from src.utils_fileid import get_json_drive
from src.utils_dycrypt import decrypt_string
from src.utils_method import get_query_params
from readfromgoogledrive import getfilefromdrive

from dotenv import load_dotenv
load_dotenv()

key=os.getenv("encryptkey")

mystyle = '''
    <style>
        p {
            text-align: right;
        }
    </style>
    '''

#st.markdown(mystyle, unsafe_allow_html=True)

# Main function to run the app
def main() -> None:
    query_params = get_query_params()
    if query_params:
        if st.query_params["source"] is not None:
            sourceId = st.query_params["source"]
            st.title("Translation")
            response = get_json(sourceId)
            if response is not None:
                source = decrypt_string(response.get('source'),key)
                title = response.get('title'),key
                thumbnail_url = decrypt_string(response.get('thumbnail_url'),key)
                publish_date = response.get('publish_date')
                youtubelink = decrypt_string(response.get('youtubelink'),key)
                # Print the values
                st.write(f"Title: {title}")
                st.write(f"Thumbnail URL: {thumbnail_url}")
                st.write(f"Publish Date: {publish_date}")
                st.write(f"YouTube Link: {youtubelink}")

                with st.spinner("Please wait......"):
                    fileidobj = get_json_drive(source)
                    #print(fileidobj['id'])
                    if fileidobj:
                        translation = getfilefromdrive(fileidobj['id'])
                        translation = json.loads(translation)
                        st.title("English")
                        st.markdown(f"<div style='text-align: left;'>{translation['t_english']}</div>", unsafe_allow_html=True)
                        st.title("Urdu")
                        st.markdown(f"<div style='text-align: right;'>{translation['t_urdu']}</div>", unsafe_allow_html=True)
                        st.title("Spanish")
                        st.markdown(f"<div style='text-align: left;'>{translation['t_spanish']}</div>", unsafe_allow_html=True)
                        st.title("Arabic")
                        st.markdown(f"<div style='text-align: right;'>{translation['t_arabic']}</div>", unsafe_allow_html=True)
                        st.title("Italian")
                        st.markdown(f"<div style='text-align: left;'>{translation['t_italian']}</div>", unsafe_allow_html=True)
                    else:
                        st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
                    

            else:
                st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
        else:
            st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")
    else:
        st.write("No tranlation found please contact on this email leodeveloper@gmail.com or message on linkedin https://www.linkedin.com/in/sulemanmuhammad/")

if __name__ == "__main__":
    main()