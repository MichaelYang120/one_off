import os
import shutil
import datetime
# we are not deleting any files here, we are just copying them to tmp directory and zipping them
# we start by orgainzing the data, then we zip the files and move them to tmp_zip zip_tmp_directory
# when finish running we should have three sets of files: organize data within the tmp directory, the original files, the sorted zipped files in the tmp_zip files
# we are only checking for _ in the file name, if we have more than one _ in the file name we are not checking for that

def organize_data():
    list_file = os.listdir(os.getcwd())
    if 'tmp' not in list_file:
        os.makedirs('tmp')
    for file in list_file:
        new_list = os.listdir('tmp')
        if 'tmp' in file:
            continue
        # if file contains
        if 't.py' in file:
            continue
        if 'finished' in file:
            continue
        tmp_file_name = file.split('.')
        # check if directory exist
        # create tmp directory
        # if tmp_file_name[0] is an empty string
        if tmp_file_name[0] == '':
            continue
        if tmp_file_name[0] not in new_list and '_' not in tmp_file_name[0]:
            os.makedirs('tmp/' + tmp_file_name[0])
        # check if file exist in tmp directory
        if file not in new_list:
            if '_' not in file:
                #copy file to tmp directory
                shutil.copy(file, 'tmp/' + tmp_file_name[0])
            else :
                check_tmp_file_name = file.split('_')
                if check_tmp_file_name[0] in new_list:
                    shutil.copy(file, 'tmp/' + check_tmp_file_name[0])
                else :
                    os.makedirs('tmp/' + check_tmp_file_name[0])
                    shutil.copy(file, 'tmp/' + check_tmp_file_name[0])


def zip_tmp_directory():
    #for each file in tmp directory we are ziping them
    for file in os.listdir('tmp'):
        if 'finished' in file:
            continue
        shutil.make_archive('tmp/' + file, 'zip', 'tmp/' + file)

def move_zip_files():
    #for each file in tmp directory we are moving items that are zip files into tmp_zip directory
    list_file = os.listdir('tmp')
    # if tmp_zip does not exist
    if 'tmp_zip' not in list_file:
        os.makedirs('tmp_zip')
    for file in list_file:
        if 'finished' in file:
            continue
        if '.zip' in file:
            shutil.move('tmp/' + file, 'tmp_zip/' + file)
        else:
            continue

def create_finished_directory():
    #create finished directory with timestamp
    #create timestamp
    # create finished with timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tmp_directory_str = 'finished' + timestamp
    os.makedirs(tmp_directory_str)
    #move tmp_zip to finished directory
    shutil.move('tmp_zip', tmp_directory_str)
    #move tmp to finished directory
    shutil.move('tmp', tmp_directory_str)

def execute():
    organize_data()
    zip_tmp_directory()
    move_zip_files()
    create_finished_directory()

execute()
