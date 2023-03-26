import imageio
from PIL import Image
import numpy as np

if __name__ == '__main__':

    path = '/Users/17914/phd/nnUNet-master/nnunetv2/media/fabian/nnUNet_raw/label/'
    t_path = '/Users/17914/phd/nnUNet-master/nnunetv2/media/fabian/nnUNet_raw/label_new/'
    i = 2
    for i in range(2,5):
        F0 = 'Glom ' + str(i) + ' Nuc.tif'
        F1 = 'Glom ' + str(i) + ' GBM.tif'
        F2 = 'Glom ' + str(i) + ' Capsule.tif'
    # Load a TIFF file
        threshold = 250
        F0_image = imageio.v3.imread(path + F0)
        F1_image = imageio.v3.imread(path + F1)
        F2_image = imageio.v3.imread(path + F2)
        new_im = np.zeros_like(F0_image)
        new_im[F0_image > threshold] = 1
        new_im[F1_image > threshold] = 2
        new_im[F2_image > threshold] = 3
        print(new_im.shape)
        zero_im = new_im[:, :, :]
        print(zero_im[zero_im > 0])
        imageio.v3.imwrite(t_path + 'Glom ' + str(i) + ' label.tif', new_im, format_hint='.tif')
