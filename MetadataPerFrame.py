import cv2
import json
import utm
import subprocess
import os
import time

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

def embed_metadata_in_frame(frame_path, metadata_file_path, output_frame_path):
    # Use FFmpeg to embed metadata
    subprocess.run([
        'ffmpeg',
        '-i', frame_path,
        '-i', metadata_file_path,
        '-c', 'copy',
        '-map_metadata', '1',
        '-y',
        output_frame_path
    ])

def main(video_path, json_file, output_file):
    metadata_list = read_metadata_from_json(json_file)

    # Get video properties
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Create temporary directories for frames and metadata
    temp_frame_dir = 'temp_frames'
    os.makedirs(temp_frame_dir, exist_ok=True)

    temp_data_dir = 'temp_metadata'
    os.makedirs(temp_data_dir, exist_ok=True)

    temp_embedded_dir = 'temp_embedded'
    os.makedirs(temp_embedded_dir, exist_ok=True)

    for frame_number in range(frame_count):
        # Read only the current frame
        ret, frame = cap.read()

        if not ret:
            print(f"Error reading frame {frame_number}.")
            break

        metadata = metadata_list[frame_number+2]
        ffmpeg_metadata = create_ffmpeg_metadata(metadata)

        # Save the metadata to a temp text file
        metadata_file_path = os.path.join(temp_data_dir, f'metadata_{frame_number}.txt')
        with open(metadata_file_path, 'w') as metadata_file:
            metadata_file.write(ffmpeg_metadata)

        # Save the frame to a temp file
        frame_path = os.path.join(temp_frame_dir, f'frame_{frame_number}.png')
        cv2.imwrite(frame_path, frame)

        # Embed metadata in the frame
        output_frame_path = os.path.join(os.path.abspath(temp_embedded_dir), f'frame_with_metadata_{frame_number}.png')
        embed_metadata_in_frame(frame_path, metadata_file_path, output_frame_path)
        print(f'Saving frame: {output_frame_path}')
        time.sleep(0.1)
        print(os.path.exists(output_frame_path))

    # Release video capture object
    cap.release()

    # Use FFmpeg to combine frames with metadata into a video
    subprocess.run([
        'ffmpeg',
        '-y',
        '-framerate', str(fps),
        '-i', os.path.join(temp_embedded_dir, f'frame_with_metadata_%d.png'),
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        output_file
    ])

    # Remove temporary directories and files
    for file_name in os.listdir(temp_frame_dir):
        file_path = os.path.join(temp_frame_dir, file_name)
        os.remove(file_path)
    os.rmdir(temp_frame_dir)

    for file_name in os.listdir(temp_data_dir):
        file_path = os.path.join(temp_data_dir, file_name)
        os.remove(file_path)
    os.rmdir(temp_data_dir)

    for file_name in os.listdir(temp_embedded_dir):
        file_path = os.path.join(temp_embedded_dir, file_name)
        os.remove(file_path)
    os.rmdir(temp_embedded_dir)



if __name__ == "__main__":
    video_path = "/home/croback/CyberProcessor/CyberExport/CyberExport.avi"
    met_file = "/home/croback/CyberProcessor/CyberExport/CyberExport.json"
    output_video_file = "/home/croback/CyberProcessor/OutputVid.mp4"

    main(video_path, met_file, output_video_file)
