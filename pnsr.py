import cv2
import os
from skimage.metrics import structural_similarity


sr_dir = os.listdir('./SR')
hr_dir = os.listdir('./HR')

psnr = 0.0
ssim = 0.0
n = 0

def to_grey(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
for sr_image in sr_dir:
    for hr_image in hr_dir:
        if sr_image == hr_image:
            if (sr_image[-3:]) != 'png':
                continue
            compute_psnr = cv2.PSNR(cv2.imread('./SR/' + sr_image), cv2.imread('./HR/' + hr_image))
            compute_ssim = structural_similarity(to_grey(cv2.imread('./SR/' + sr_image)),
                                        to_grey(cv2.imread('./HR/' + hr_image)))
            psnr += compute_psnr
            ssim += compute_ssim
            n += 1
            if n%100 == 0:
                print("finish compute [%d/%d]" % (n, len(hr_dir)))

psnr = psnr / n
ssim = ssim / n
print("average psnr = ", psnr)
print("average ssim = ", ssim)
