# Script Name:      PSD Extractor
# Author:           Luigi Del Vecchio
# Version:          0.1.0
# Last Updated:     21/04/2019
#
#                 **************
# Description:    Tool to extract layers data from psd/psb, display
#                 file information and save each layers FileName_LayerName.png
#                 **************

import os
import sys
from PIL import Image
from psd_tools import PSDImage


def get_save_layers():
    print('*** PSD Extractor v1.0 ***')
    user_target = input('Enter the path of the psd/psb file: ')
    file_path = os.path.basename(user_target)
    file_name = os.path.splitext(file_path)[0]
    folder_name = 'Sprites'

    # Check if the file extension is .psd or .psb
    if user_target.endswith('.psd') or user_target.endswith('.psb'):
        image_file = PSDImage.open(user_target)

        # Print selected file details
        print('Selected File: ' + file_name)
        print('File Mode: {0} Bits'.format(image_file.depth))

        # Ask user where to save the file
        target_path = input('Target Path: ')
        output_path = os.path.join(target_path, folder_name, '')

        # if the path doesn't not exist, create the "Sprite" folder
        if not os.path.exists(output_path):
            os.mkdir(output_path)
            print('Sprite folder created')

        else:
            print('Sprite folder detected')

        i = 0
        # Save each layer in the "Sprite" folder as (File_name_LayerName.png)
        for layer in image_file.descendants():
            if layer.has_pixels():
                layer_ref = image_file[i]
                layer_ref.compose().save(output_path + (file_name + '_' + layer.name + '.png'))
                print(layer.name + ' Saved! ')
                i += 1

        print('Operation Completed!')

    else:
        print('Error: Invalid file!')
        sys.exit()


# Call function
get_save_layers()
