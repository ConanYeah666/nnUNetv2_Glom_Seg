import numpy as np
import tifffile as tif
from batchgenerators.utilities.file_and_folder_operations import *
if __name__ == '__main__':

    path = '/Users/17914/phd/nnUNet-master/nnunetv2/media/fabian/nnUNet_raw/label/'
    t_path = '/Users/17914/phd/nnUNet-master/nnunetv2/media/fabian/nnUNet_raw/label_new/'
    threshold = 250
    images = subfiles(path, suffix='.tif', sort=True, join=False)
    for i, im in enumerate(images):
        cur_tif = tif.imread(path + im)
        num_channels = cur_tif.shape[1]
        im_new = np.zeros_like(cur_tif[:, 0, :, :])
        single_channel_tif = cur_tif[:, 3, :, :]
        im_new[single_channel_tif > threshold] = 5
        single_channel_tif = cur_tif[:, 0, :, :]
        im_new[single_channel_tif > threshold] = 4
        single_channel_tif = cur_tif[:, 2, :, :]
        im_new[single_channel_tif > threshold] = 3
        single_channel_tif = cur_tif[:, 1, :, :]
        im_new[single_channel_tif > threshold] = 2
        single_channel_tif = cur_tif[:, 4, :, :]
        im_new[single_channel_tif > threshold] = 1
        output_path = os.path.join(t_path, im)
        tif.imwrite(output_path, im_new)
