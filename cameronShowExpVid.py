import cv2
import json
import utm
import math

def read_metadata_from_json(json_file):
    with open(json_file, 'r') as file:
        metadata = json.load(file)
    return metadata

def main(video_path, json_file):
    # Read metadata from JSON file
    metadata = read_metadata_from_json(json_file)

    # Open video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Couldn't open video file.")
        return

    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can also use 'XVID' or other codecs depending on your preference

    # Initialize VideoWriter object
    out = cv2.VideoWriter(output_video_file, fourcc, fps, (frame_width, frame_height))

    # Get video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Loop through frames
    for frame_number in range(frame_count):

        ret, frame = cap.read() 

        if not ret:
            print("Error reading frame.")
            break

        # Get metadata for the current frame
        frame_metadata = metadata[frame_number+1]
        print(frame_count)
        print(frame_number)

        # Extract values from metadata
        chassis = frame_metadata.get('chassis')
        loco = frame_metadata.get('localization')

        van_time = f'{round(loco["header"]["timestampSec"], 3):.3f}'

        lat, lon = utm.to_latlon(loco['pose']['position']['x'], loco['pose']['position']['y'], 17, 'S')
        lat = f'{lat:.3f}'
        lon = f'{lon:.3f}'
        alt = f'{loco["pose"]["position"]["z"]:.3f}'

        driving_mode = chassis['drivingMode']
        speed = f'{chassis["speedMps"] * 2.23694:.2f}'
        
        heading = f'{loco["pose"]["heading"] * (180/math.pi):.3f}'

        # Display values on the screen
        text_line1 = 'OHIO UNIVERSITY IDEAS LAB'
        text_line2 = f'Frame: {frame_number},Timestamp: {van_time}, Lat: {lat}, Lon: {lon}, Alt (m): {alt}'    # NEED TO CHECK THE UNITS FOR HEADING AND ALTITUDE
        text_line3 = f'Speed (mph): {speed}, Heading(deg): {heading}, Driving Mode: {driving_mode}'

        # Set the position for the first line above the existing two lines
        position_line1 = (10, 30)

        # Increase the font size
        font_scale = 1.25  # Adjust the scale as needed

        cv2.putText(frame, text_line1, position_line1, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 0), 7)  # Black outline
        cv2.putText(frame, text_line1, position_line1, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 255, 255), 2)  # Yellow text

        # Calculate the height of the text to adjust the position for the second line
        text_size_line1 = cv2.getTextSize(text_line1, cv2.FONT_HERSHEY_COMPLEX, font_scale, 7)[0]
        text_height_line1 = text_size_line1[1]

        # Set the position for the second line below the first line
        position_line2 = (10, position_line1[1] + text_height_line1 + 10)

        # Increase the font size for the second line
        cv2.putText(frame, text_line2, position_line2, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 0), 7)  # Black outline
        cv2.putText(frame, text_line2, position_line2, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 255, 255), 2)  # Yellow text

        # Calculate the height of the text to adjust the position for the third line
        text_size_line2 = cv2.getTextSize(text_line2, cv2.FONT_HERSHEY_COMPLEX, font_scale, 7)[0]
        text_height_line2 = text_size_line2[1]

        # Set the position for the third line below the second line
        position_line3 = (10, position_line2[1] + text_height_line2 + 10)

        # Increase the font size for the third line
        cv2.putText(frame, text_line3, position_line3, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 0), 7)  # Black outline
        cv2.putText(frame, text_line3, position_line3, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 255, 255), 2)  # Yellow text

        out.write(frame)
        # Show the frame
        cv2.imshow('Video with Metadata', frame)

        # Break the loop if the user presses 'q'
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    # Release video capture object and close window
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Specify the path to the video file and the JSON file
    video_path = "/mnt/d/VanExperiment/VideoTest/ExportedInfo.avi"
    met_file =   "/mnt/d/VanExperiment/VideoTest/ExportedInfo.json"
    output_video_file = "/mnt/d/VanExperiment/VideoTest/OutputVid.mp4"

      # Run the main function
    main(video_path, met_file)

