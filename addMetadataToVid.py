import cv2
import json
import utm
import subprocess
import os

def read_metadata_from_json(json_file):
    with open(json_file, 'r') as file:
        metadata = json.load(file)
    return metadata

def create_ffmpeg_metadata(metadata):
    chassis = metadata.get('chassis')
    loco = metadata.get('localization')

    lat, lon = utm.to_latlon(loco['pose']['position']['x'], loco['pose']['position']['y'], 17, 'S')
    lat = round(lat, 5)
    lon = round(lon, 5)

    driving_mode = chassis['drivingMode']
    speed = round(chassis['speedMps'] * 2.23694, 2)

    metadata_str = f";FFMETADATA\ntitle=Van Metadata\nlatitude={lat}\nlongitude={lon}\ndriving_mode={driving_mode}\nspeed_mph={speed}"
    return metadata_str

def main(video_path, json_file, output_file):
    metadata_list = read_metadata_from_json(json_file)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Couldn't open video file.")
        return

    # Get video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create a temporary directory for metadata files
    temp_dir = 'temp_metadata'
    os.makedirs(temp_dir, exist_ok=True)

    # Define VideoWriter object for output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

    for frame_number in range(frame_count):

        # Show specific metadata for frames 0 and 1
        if frame_number == 0:
            print("GOT COMMENTS", metadata_list[frame_number])
        elif frame_number == 1:
            print("GOT METADATA", metadata_list[frame_number])
        else:
            ret, frame = cap.read()

            if not ret:
                print("Error reading frame.")
                break

            # Get metadata for the current frame
            metadata = metadata_list[frame_number]
            ffmpeg_metadata = create_ffmpeg_metadata(metadata)

            # Write metadata to a temporary file
            temp_metadata_file = os.path.join(temp_dir, f'metadata_{frame_number}.txt')
            with open(temp_metadata_file, 'w') as metadata_file:
                metadata_file.write(ffmpeg_metadata)

            # Use FFmpeg to concatenate metadata files
            subprocess.run([
                'ffmpeg',
                '-y',
                '-i', video_path,
                '-i', temp_metadata_file,
                '-c:v', 'libx264',  # Change video codec to libx264 (H.264)
                '-crf', '18',       # Set Constant Rate Factor (CRF) for video quality (adjust as needed)
                '-c:a', 'aac',      # Set audio codec to AAC
                '-strict', 'experimental',
                '-b:a', '192k',     # Set audio bitrate (adjust as needed)
                '-map', '0',
                '-map_metadata', '1',
                '-metadata:s:v', 'title=Video Metadata',
                output_file
            ])

            cv2.imshow('Video with Metadata', frame)
            out.write(frame)

            # Break the loop if the user presses 'q'
            if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
                break

    # Release video capture object, VideoWriter, and close window
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Remove temporary directory and files
    for file_name in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, file_name)
        os.remove(file_path)
    os.rmdir(temp_dir)

if __name__ == "__main__":
    video_path = "/home/croback/CyberProcessor/CyberExport/CyberExport.avi"
    met_file = "/home/croback/CyberProcessor/CyberExport/CyberExport.json"
    output_video_file = "/home/croback/CyberProcessor/OutputVid.mp4"

    main(video_path, met_file, output_video_file)