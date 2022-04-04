# IQT
The environmental settings are described below.
- Pytorch=1.7.1 (with cuda 11.0)
- einops=0.3.0
- numpy=1.18.3
- cv2=4.2.0
- scipy=1.4.1
- json=2.0.9
- tqdm=4.45.0

# Train & Validation
First, you need to download weights of InceptionResNetV2 pretrained on ImageNet database.
- Download the weights from this website (http://data.lip6.fr/cadene/pretrainedmodels/inceptionresnetv2-520b38e4.pth)

Second, you need to download the PIPAL database.
- Download the PIPAL database (train/valid) from this website (https://github.com/HaomingCai/PIPAL-dataset)
- set the database path in "train.py" (It is represented as "db_path" in "train.py")
- Please check "PIPAL.txt" is in "IQA_list" folder

After those settings, you can run the train & validation code by running "train.py"
- python3 train.py (execution code)
- This code works on single GPU. If you want to train this code in muti-gpu, you need to change this code
- Options are all included in "train.py". So you should change the variable "config" in "train.py"

After those settings, you can run the inference code by running "test.py"
- python3 test.py (execution code)
- From here you will get four different output files outputScale0.5.txt, outputScale1.txt, outputScale2.txt, outputScale3.txt then you have to run averaging.py file to get final output file.


## Changes required at config part of train.py(for training) and test.py(for testing):

**Change the value of scale to :**

* 1 for training on actual image
* 0.5 for training on upscaled image by factor two
* 2 for training on downscaled image by factor two
* 3 for training on downscaled image by factor three

**Methodology**:

* Four instances are trained separately with respective scale value, and results are calculated separately.
* Final result is being computed by averaging the results from four different scaled images, i.e. for scale value 1,0.5,2 and 3.

**Link for trained weights**:
https://drive.google.com/drive/folders/1QbfB-_k90xqgQR2w8eVIi3G0FOUM4RKr
* Create a new directory of name weights and upload .pth file in this directory.
