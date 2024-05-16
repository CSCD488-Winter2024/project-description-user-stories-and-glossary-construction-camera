#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <video_clip_file> <email_address> <sender_email>"
    exit 1
fi

# Assigning input arguments to variables
video_clip_file="$1"
email_address="$2"
sender_email="$3"

# Zip the video clip file
zip_file="${video_clip_file%.mp4}.zip"
zip -j "$zip_file" "$video_clip_file"

# Send the zipped file via email
(echo -e "Subject: Video Clip\nFrom: $sender_email\nTo: $email_address\nMIME-Version: 1.0\nContent-Type: multipart/mixed; boundary=\"boundary\"\n\n--boundary\nContent-Type: text/plain\n\nPlease find the attached video clip.\n\n--boundary\nContent-Type: application/zip\nContent-Disposition: attachment; filename=\"$zip_file\"\n\n"; cat "$zip_file"; echo -e "\n\n--boundary--") | sendmail -t

# Cleanup: Remove the zipped file
rm "$zip_file"

echo "Email sent successfully with the video clip attached."

