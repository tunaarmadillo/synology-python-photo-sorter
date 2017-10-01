import datetime
import os
import shutil
from random import randint

def sort_photos_by_month(base_dir_array, dest_dir, file_type_array):
    for each_directory in base_dir_array:
        image_files = []

        # switch directory and parse to find .jpg files.
        os.chdir(each_directory)

        for each_file_type in file_type_array:
            print "Gathering list of all: " + each_file_type + " files"
            for each_file in os.listdir(os.getcwd()):
                if each_file.endswith(each_file_type):
                    image_files.append(each_file)
        print image_files

        # Create folders and move files
        for each_file in image_files:

            file_path = str(os.path.abspath(each_file))

            date_modified = os.path.getmtime(each_file)
            date_modified = datetime.datetime.fromtimestamp(date_modified)
            date_modified_string = date_modified.strftime('%c')

            print "Path: " + file_path \
                  + " Modified: " + date_modified_string

            # join file modified date (year and month) for directory check / create
            date_modified_year_month = str(date_modified.year) + "/" + str(date_modified.month)
            print date_modified_year_month

            # CREATE THE NEW MONTHLY ARCHIVE DIRECTORY IF IT DOES NOT ALREADY EXIST

            new_file_destination = dest_dir + "/" + date_modified_year_month

            if not os.path.exists(new_file_destination):
                os.makedirs(new_file_destination)

            new_file_full_path = new_file_destination + "/" + each_file

            # DUPPLICATE THE FILE FROM THE SOURCE DIR IF IT ALREADY EXISTS (ADD RANDOM INT TO FILENAME)
            if os.path.exists(new_file_full_path):
                print "File: " + new_file_full_path + \
                      " exists, delete from source DIR: " + file_path

                file_name = each_file.split(".")[0]
                file_ext = each_file.split(".")[1]

                new_file_full_path = new_file_destination + "/" + file_name + "_" + str(randint(0, 1000000)) + "." + file_ext
                shutil.move(each_file, new_file_full_path)

            # MOVE THE FILE TO THE NEW DIR IF IT DOES NOT ALREADY EXIST
            else:
                try:
                    shutil.move(each_file, new_file_full_path)
                    print "SUCCESS - FILE: " + each_file + " - FILE MOVED TO DIR: " + new_file_full_path
                except:
                    print "ERROR - FILE: " + each_file + " - FAILED TO MOVE DUE TO ERROR"


# Initialisation parameters

# base_directories = ["C:\\Users\\Josh\\Pictures\\test\\"]
base_directories = ["/volume1/photo/Home Pictures/Josh Phone",
                    "/volume1/photo/Home Pictures/Josh Phone/WhatsApp Images",
                    "/volume1/photo/Home Pictures/Josh Phone/WhatsApp Video",
                    "/volume1/photo/Home Pictures/Josh Phone/Snapseed",
                    "/volume1/photo/Home Pictures/Monika Phone",
                    "/volume1/photo/Home Pictures/Monika Phone/WhatsApp Images",
                    "/volume1/photo/Home Pictures/Monika Phone/WhatsApp Video",
                    "/volume1/photo/Home Pictures/Monika Phone/Snapseed"
                    ]

# destination_dir = "C:\\Users\\Josh\\Pictures"
destination_dir = "/volume1/photo/Home Pictures"

file_types = [".jpg", ".mp4", ".png", ".JPG", "jpeg"]

sort_photos_by_month(base_directories, destination_dir, file_types)
