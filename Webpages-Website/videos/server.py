from flask import Flask, request, redirect, url_for
import os
from moviepy.editor import VideoFileClip

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def convert_avi_to_mp4(avi_filepath, output_folder):
    mp4_filename = os.path.splitext(os.path.basename(avi_filepath))[0] + '.mp4'
    mp4_filepath = os.path.join(output_folder, mp4_filename)
    
    # Convert the video
    clip = VideoFileClip(avi_filepath)
    clip.write_videofile(mp4_filepath, codec='libx264')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    if file.filename.lower().endswith('.avi'):
        convert_avi_to_mp4(filepath, CONVERTED_FOLDER)
    
    return f"File {file.filename} uploaded successfully and converted to MP4 if applicable.", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
