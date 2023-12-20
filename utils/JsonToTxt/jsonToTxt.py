import json
import os
# open the file where there are jsons of the picture
#Author: Muhammad Sufiyan Sadiq

# add your path to your json files here
main_folder_path = "C:/Users/RA/Desktop/github clones/drone_comp/jsons"
main_target_path = "C:/Users/RA/Desktop/github clones/drone_comp/data/labels/train"


# user-defined class mapping
class_mapping = {
    'cross': 0
    # Add more classes as needed
}

# we also need to get the number of folders present in this directory
folders = os.listdir(main_folder_path)
print(folders)
for folder in folders:
    folder_path = os.path.join(main_folder_path, folder) 
    Json_list = os.listdir(folder_path)
    number_of_jsons = len(Json_list)
    for i in range(number_of_jsons):
        new_path  = os.path.join(folder_path, Json_list[i])
        with open(new_path, 'r') as json_file:
            data = json.load(json_file)
            
            # find the length and width of the image
            height = data["imageHeight"]
            width = data["imageWidth"]

            yolo_format_string = ""        
            number_of_boxes = len(data["shapes"])
            for i in range(number_of_boxes):
                box_data = data["shapes"][i]
                # getting the class id
                try:
                    Class = class_mapping[box_data["label"]]    
                
                except:
                    print("Unknown class label found please add this class in your python file and try again (Ps delete all the dummy files that are created!)")
                    break
                
                # get the points array
                points_array = box_data["points"]
                
                # get the points from the array
                x_coordinate1 = points_array[0][0]
                x_coordinate2 = points_array[1][0]
                y_coordinate1 = points_array[0][1]
                y_coordinate2 = points_array[1][1]
                
                # get the box width and height
                box_height = (y_coordinate2 -y_coordinate1) / height
                box_width = (x_coordinate2 - x_coordinate1) / width
                
                x_center = (x_coordinate1 + (x_coordinate2 - x_coordinate1) / 2) / width
                y_center = (y_coordinate1 + (y_coordinate2 - y_coordinate1) / 2) / height
                
                yolo_format_string  = yolo_format_string + f"{Class} {x_center} {y_center} {box_width} {box_height}\n"
                # end of for loop
            
            # this is the yolo format paragraph that can be written inside of our text file
            yolo_format_string = yolo_format_string.rstrip('\n')
            
            
            file_name = data["imagePath"]
            file_name= os.path.basename(file_name)
            file_name = os.path.splitext(file_name)[0] + '.txt'  # convert it to txt file
            
            
            target_file_path = os.path.join(main_target_path, file_name)
            print(main_target_path)
            with open(target_file_path, 'w') as writeFile:
                writeFile.write(yolo_format_string)
