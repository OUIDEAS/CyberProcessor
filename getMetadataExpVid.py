import cv2
import json
import utm
import math
import os
import glob

def read_metadata_from_json(json_file):
    with open(json_file, 'r') as file:
        metadata = json.load(file)
    return metadata

def main(main_dir):

    for root, dirnames, filenames in os.walk(main_dir):
        break

    print(dirnames)

    for file_set in dirnames:

        print(file_set)
    
        direct = main_dir + str(file_set) + "/out_data/"
        export_dir = main_dir + str(file_set) + "/out_data_video/"

        total_set = set(glob.glob(direct + '*.*', recursive = True))
        print(total_set)
        file_num = []
        for val in total_set:
            end = val.split('/')[-1]
            file_num.append(end.split('.')[0])

        unique_file_nums = list(set(file_num))
        print(unique_file_nums)

        for f in unique_file_nums:

            files = sorted(glob.glob(direct + f + '.*', recursive = True))

            if not os.path.exists(export_dir):
                os.makedirs(export_dir)
                print(f"Directory '{export_dir}' created successfully.")
            else:
                print(f"Directory '{export_dir}' already exists.")

            for file in files:
                if file.endswith('.avi'):
                    video_file = file
                else:
                    json_file = file

            # Read metadata from JSON file
            metadata = read_metadata_from_json(json_file)

            # Open video file
            cap = cv2.VideoCapture(video_file)

            if not cap.isOpened():
                print("Error: Couldn't open video file.")
                return

            # Get video properties
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            fourcc = cv2.VideoWriter_fourcc(*'XVID')  

            # Initialize VideoWriter object
            out = cv2.VideoWriter(export_dir + f + '.avi', fourcc, fps, (frame_width, frame_height))

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
                frame_metadata = metadata['frames'][frame_number]
                print(frame_count)
                print(frame_number)

                # Extract values from metadata
                chassis = frame_metadata.get('chassis')
                loco = frame_metadata.get('localization')

                van_time = f'{round(loco["header"]["timestampSec"], 3):.1f}'

                lat, lon = utm.to_latlon(loco['pose']['position']['x'], loco['pose']['position']['y'], 17, 'S')
                lat = f'{lat:.4f}'
                lon = f'{lon:.4f}'
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


            # Release video capture object and close window
            cap.release()
            out.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # Specify the path to the video file and the JSON file
    main_dir = "/mnt/d/VanExperiment/"

    # Run the main function
    main(main_dir)

