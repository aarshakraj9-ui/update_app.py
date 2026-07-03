import streamlit as st
import os
import glob
try:
  from moviepy.editor import ImageClip,concatenate_videoclips, AudiofileClip
except ImportError:
  from moviepy import IMageClip, concatenate_videoclips, AudioFileClip
import yt_dlp

if 'audio_path' not in st.session_state:
  st.session_state['audio_path'] = None 
if 'yt_error' in st.session_state:
  pass 
def cleanup_temp_files():
  """Remove temporary files and reset memory."""
  files = glob.glob("temp_*") + ["output_video.mp4"]
  for f in files:
    try:
      os.remove(f)
    except:
      pass
 st.session_state['audio_path'] = None
if'yt_error' in st.session_state:
  del st.session_state['yt_error']
  
