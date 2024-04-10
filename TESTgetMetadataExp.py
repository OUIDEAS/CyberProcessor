# import packages
import sys, time, os
from importlib import import_module
import numpy as np
import cv2
from PIL import Image
import io
import google.protobuf as protobuf
import google.protobuf.descriptor_pb2 as descriptor_pb2
import apollopy.proto.record_pb2 as record_pb2
import apollopy.proto.proto_desc_pb2 as proto_desc_pb2
from google.protobuf.json_format import MessageToJson
import json
from tqdm import tqdm
from cybertools.cyberreaderlib import ProtobufFactory, RecordReader, RecordMessage
import base64
from datetime import datetime
import glob
import utm
import math
 
###########################################################
class VideoExporter:
    
    def __init__(self, camera_topic, fileset, export_dir):
        # Topics
        self.fileset = str(fileset)
        self.camera_topic = camera_topic
        self.export_folder = ""
        self.export_dimensions = (3840, 2160)
        self.image = None
        self.addMeta = True
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.videoWriter = cv2.VideoWriter(export_dir + self.fileset + '_metadataVidMatched.mp4', self.fourcc, 14.0, self.export_dimensions)
        if not self.videoWriter.isOpened():
            print("Error: Could not open VideoWriter")
 
    def stringToImage(self):
        self.image = base64.b64decode(self.image)
        self.image = Image.open(io.BytesIO(self.image))        
        self.image_ts = 0
        return self.image_ts
 
    def toRGB(self):
        self.image = cv2.cvtColor(np.array(self.image), cv2.COLOR_BGR2RGB)
 
    def add_frame(self):

        self.videoWriter.write(self.image)

 
    def export_video(self):
        self.videoWriter.release()
        print('')
        print('VIDEO RELEASED')
        print('')
 
###########################################################
 
 
def initReader(filename):
    unqiue_channel = []
    pbfactory = ProtobufFactory()
    reader = RecordReader(filename)
    
    for channel in reader.GetChannelList():
        desc = reader.GetProtoDesc(channel)
        pbfactory.RegisterMessage(desc)
        unqiue_channel.append(channel)
        
    message = RecordMessage()
    return message, reader, pbfactory


 
###########################################################
 
if __name__ == "__main__":
    
    file_set = sys.argv[1]


    ### OPTIONS ###
    main_dir = "/home/croback_linux/s3bucket/Deployment_2_SEOhio/Blue Route/OU Pacifica/"
 
    for root, dirnames, filenames in os.walk(main_dir):
        break
 
    print("Dirnames:", dirnames)
    print("Fileset:", file_set)
 
    # file_set = 1695931464



    direct = "/home/croback_linux/s3bucket/Deployment_2_SEOhio/Blue Route/OU Pacifica/" + str(file_set) + "/"
    # vid_export_dir = "/home/croback_linux/s3bucket/Deployment_2_SEOhio/Blue Route/OU Pacifica/" + str(file_set) + "/"
    vid_export_dir = "/home/croback_linux/metadataOverlayData/" + str(file_set) + "in4K/"

    files_total = sorted(os.listdir(direct))

                
    # ARRAYS
    loc_data_to_metadata = {
        'metadata': None,
        'comments': None,
        'frames': []
        }

    ### MAIN CODE ###
    for file in files_total:
        filename = os.path.join(direct,file)
        if file == 'comments.json':
            print("FOUND COMMENTS IN: ", filename)
            comment_file = open(filename)
            loc_data_to_metadata['comments'] = json.load(comment_file)['comments']

        elif file.endswith('.json') and 'comments.json' not in file  and 'VanDrive' not in file:
            name, extension = os.path.splitext(filename)
            print("FOUND METADATA IN: ", filename)
            j_file = open(filename)
            loc_data_to_metadata['metadata'] = json.load(j_file)['metadata']

    record_set = set(glob.glob(direct+"/*.record.*"))

    file_num = []
    for val in record_set:
        end = val.split('/')[-1]
        file_num.append(end.split('.')[0])

    unique_file_nums = sorted(list(set(file_num)))
    print(unique_file_nums)

    for f in unique_file_nums:

        # f = '20240202155226'

        files = sorted(glob.glob(direct+"/" + f + ".record.*"))

        # print(files)
        print(f)

        if not os.path.exists(vid_export_dir):
            os.makedirs(vid_export_dir)
            print(f"Directory '{vid_export_dir}' created successfully.")
        else:
            print(f"Directory '{vid_export_dir}' already exists.")

        # TOPICS
        image_handler = VideoExporter(camera_topic="/apollo/sensor/camera/front_6mm/image/compressed", export_dir=vid_export_dir, fileset=f)

        localization_topic = "/apollo/localization/pose"
        chassis_topic = "/apollo/canbus/chassis"
        
        # FILE LOCATION
        # direct = "/mnt/h/cyber_bags/1698251665/"
        # direct = "/media/travis/moleski1/cyber_bags/1698251665"
        # direct = "/media/autobuntu/chonk/chonk/git_repos/apollo/10252023_blue_route/"
        
        # FILE CUTOFF
        max_files_to_process = 2
        early_break = False
        
        ### VAR INIT ###

        # IMPORT FILE CHECK
        if direct.endswith("/"):
            pass
        else:
            direct = direct + "/"
            

        # COUNTERS
        file_count = 0
        frame_count = 0
        frame_interval = 500

        for file in tqdm(files):

            filename = os.path.join(direct,file)
            # print(filename)

            if '.record' in filename:
                message, reader, pbfactory = initReader(filename)
                while reader.ReadMessage(message):
                    
                    message_type = reader.GetMessageType(message.channel_name)
                    msg = pbfactory.GenerateMessageByType(message_type)
                    msg.ParseFromString(message.content)
                    
                    if(message.channel_name == localization_topic):

                        locdata = MessageToJson(msg)
                        locdata = json.loads(locdata)
                        loc_timestamp = (locdata['header']['timestampSec'])

                        
                    if(message.channel_name == chassis_topic):
                        
                        chasdata = MessageToJson(msg)
                        chasdata = json.loads(chasdata)
                        chas_timestamp = (chasdata['header']['timestampSec'])
                        
                    if(message.channel_name == image_handler.camera_topic):

                        
                        imgdata = MessageToJson(msg)
                        imgdata = json.loads(imgdata)
                        
                        # Get the timestamp of the frame
                        img_timestamp = (imgdata['header']['timestampSec'])

                        image_meta = {
                            'header': imgdata['header'],
                            'format': imgdata['format'],
                            'measurementTime':imgdata['measurementTime']
                        }


                        try:

                            loc_chas_separation = abs(locdata['header']['timestampSec'] - chasdata['header']['timestampSec'])
                            loc_img_separation = abs(locdata['header']['timestampSec'] - imgdata['header']['timestampSec'])

                            if loc_img_separation <= 1.0 and loc_chas_separation <= 1.0:

                                # print(f"Timestamp seperation between loc and chas is : {loc_chas_seperation}")
                                # print(f"Timestamp seperation between loc and img is : {loc_img_seperation}")
                                # print(f"Frame count: {frame_count}")

                                # Append data to a frame
                                frame = {
                                    'localization': locdata,
                                    'chassis': chasdata,
                                    'image_data': image_meta
                                }
                                # Append to the json variable
                                loc_data_to_metadata['frames'].append(frame)

                                image_handler.image = imgdata['data']
                                image_ts = image_handler.stringToImage()
                                image_handler.toRGB()
                                image_handler.image = cv2.resize(image_handler.image, image_handler.export_dimensions)

                                # print("Resized image dimensions:", image_handler.image.shape)


                                van_time = f'{round(locdata["header"]["timestampSec"], 3):.1f}'

                                lat, lon = utm.to_latlon(locdata['pose']['position']['x'], locdata['pose']['position']['y'], 17, 'S')
                                lat = f'{lat:.4f}'
                                lon = f'{lon:.4f}'
                                alt = f'{locdata["pose"]["position"]["z"]:.3f}'

                                # print("Lat:",lat)
                                # print("Lon",lon)
                                # print("Alt",alt)

                                driving_mode = chasdata['drivingMode']
                                speed = f'{chasdata["speedMps"] * 2.23694:.2f}'
                                
                                heading = f'{locdata["pose"]["heading"] * (180/math.pi):.3f}'

                                # Display values on the screen
                                text_line1 = 'OHIO UNIVERSITY IDEAS LAB'
                                text_line2 = f'Frame: {frame_count},Timestamp: {van_time}, Lat: {lat}, Lon: {lon}, Alt (m): {alt}'    # NEED TO CHECK THE UNITS FOR HEADING AND ALTITUDE
                                text_line3 = f'Speed (mph): {speed}, Heading(deg): {heading}, Driving Mode: {driving_mode}'


                                position_line1 = (10, 40)
                                font_scale = 1.25  

                                cv2.putText(image_handler.image, text_line1, position_line1, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 0), 7)  # Black outline
                                cv2.putText(image_handler.image, text_line1, position_line1, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 255, 255), 2)  # Yellow text

                                text_size_line1 = cv2.getTextSize(text_line1, cv2.FONT_HERSHEY_COMPLEX, font_scale, 7)[0]
                                text_height_line1 = text_size_line1[1]

                                position_line2 = (10, position_line1[1] + text_height_line1 + 10)

                                cv2.putText(image_handler.image, text_line2, position_line2, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 0), 7)  # Black outline
                                cv2.putText(image_handler.image, text_line2, position_line2, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 255, 255), 2)  # Yellow text

                                text_size_line2 = cv2.getTextSize(text_line2, cv2.FONT_HERSHEY_COMPLEX, font_scale, 7)[0]
                                text_height_line2 = text_size_line2[1]

                                position_line3 = (10, position_line2[1] + text_height_line2 + 10)

                                cv2.putText(image_handler.image, text_line3, position_line3, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 0, 0), 7)  # Black outline
                                cv2.putText(image_handler.image, text_line3, position_line3, cv2.FONT_HERSHEY_COMPLEX, font_scale, (0, 255, 255), 2)  # Yellow text
                                    
                                image_handler.add_frame()
                                

                                frame_count += 1

                                if frame_count % frame_interval == 0:
                                    cv2.imwrite('/home/croback_linux/metadataOverlayData/' + str(file_set) + f'in4K/frame_{frame_count}.png', image_handler.image)  # Save frame as image
                                    print('Frame image has been saved')
                                
                            else:
                                if loc_img_separation > 1.0:
                                    print(f"Timestamp separation between image and loclization data too large in file : {file}")
                                    print('Separation:', loc_img_separation)
                                    print('Localization timestamp:', locdata['header']['timestampSec'])
                                    raise ValueError("Exiting program...")
                                elif loc_chas_separation > 1.0:
                                    print(f"Timestamp seperation between chassis data and localization data too large in file : {file}")
                                    print('Separation:', loc_chas_separation)
                                    print('Localization timestamp:', locdata['header']['timestampSec'])
                                    raise ValueError("Exiting program...")

                        except ValueError as e:
                            print(e)
                            sys.exit(1)

                        except:
                            continue
                            
                            

                # Break Condition
                file_count += 1
                
                if early_break:
                    
                    if file_count == max_files_to_process:
                        break
                
        image_handler.export_video()
                    
        # print(loc_data_to_metadata)

        json_export_dir = "/home/croback_linux/metadataOverlayData/BlueRoute/" + str(file_set) + "/"

        if not os.path.exists(json_export_dir):
            os.makedirs(json_export_dir)
            print(f"Directory '{json_export_dir}' created successfully.")
        else:
            print(f"Directory '{json_export_dir}' already exists.")

        with open (json_export_dir + str(f) + ".json", 'w') as f:
            json.dump(loc_data_to_metadata,f,indent=4)

        loc_data_to_metadata['frames'] = []
        sys.exit(1)
