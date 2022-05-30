# -*- coding: utf-8 -*-
"""FINAL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nqTEraYKPQjAShaZjKmhwD7Z5rNWKg-F

# 인공지능 텀프로젝트 - 딥페이크 탐지 
팀원: 정찬영, 정선영, 김태헌

#1. Image Selector
"""

from glob import glob

fake_paths=glob('d:/AI_term_project/deepfake_1st/fake/*/*/*/*/*')
real_paths=glob('d:/AI_term_project/deepfake_1st/real/*/*/*/*')

print(len(fake_paths))
print(len(real_paths))
# 85177 
# 13500

import random
import shutil

path_for_fake = 'd:/AI_term_project/select/fake/'  # fake image 저장할 폴더경로

count = 0
names = []
for path in fake_paths:
    images = glob(path+'/*.jpg')
    names = []
    while(len(names) <len(images) and len(names)<2): # choose 2 images per folder
        random_choice = random.choice(images)
        if(random_choice not in names):
            shutil.copyfile(random_choice, path_for_fake+ str(count) +'.jpg')
            count+=1
            names.append(random_choice)

path_for_real = 'd:/AI_term_project/select/real/'  # real image 저장할 폴더경로

count = 0
names = []
for path in real_paths:
    images = glob(path+'/*.jpg')
    names = []
    while(len(names) <len(images) and len(names)<10): # choose 10 images per folder
        random_choice = random.choice(images)
        if(random_choice not in names):
            shutil.copyfile(random_choice, path_for_real+ str(count) +'.jpg')
            count+=1
            names.append(random_choice)

"""Total fake image selected: 169868

Total real image selected: 134967

# 2. Face Crop

using MTCNN
"""

!pip install mtcnn

from glob import glob

fake_image= glob('d:/AI_term_project/select/fake/*.jpg')
fake_image.sort()
print(len(fake_image))  # 169876
real_image= glob('d:/AI_term_project/select/real/*.jpg')
real_image.sort()
print(len(real_image))  # 134967

# MTCNN을 이용할 때 어쩌다 한번씩 매우 작은 영역을 얼굴로 인식하여 결과 리스트에 포함하기 때문에 
# 만약 여러 개의 얼굴을 찾았다고 했을 시에 가장 큰 영역을 가지는 결과를 채택하는 함수
def get_max_size_box(results):
    max_idx = 0
    max_size = 0
    i = 0

    for result in results:
        box = result['box']
        w = box[3]
        h = box[2]
        box_size = w * h
        if max_size < box_size:
            max_size = box_size
            max_idx = i
        i += 1
    return max_idx

import tensorflow as tf

tf.get_logger().setLevel('ERROR')

from mtcnn import MTCNN
import cv2
err_path = []
for i in range(, len(fake_image)): # face extract 할 path를 지정 (fake/real/test)
    path = fake_image[i]  # face extract 할 path를 지정 (fake/real/test)
    img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    detector = MTCNN()
    results = detector.detect_faces(img)

  # mtcnn은 뒤집어진 얼굴은 인식을 못함. 실제 우리 데이터에도 뒤집어놓은 사진이 존재함.
    if len(results)<1:
        img = cv2.rotate(img, cv2.ROTATE_180)
        results = detector.detect_faces(img)
  
  # 얼굴 못찾은경우
    if len(results)<1:
        print(path)
        continue
  
    bounding_box = []
    if len(results)==1:
        bounding_box = results[0]['box']   # mtcnn의 detect_faces가 detect한 얼굴의 네 좌표
    else:
        idx = get_max_size_box(results)
        bounding_box = results[idx]['box']
  
    margin_x = bounding_box[2] * 0.1  # 20% as margin
    margin_y = bounding_box[3] * 0.135  # 27% as margin

    x1 = int(bounding_box[0] - margin_x)
    if x1 < 0:
        x1 = 0
        
    x2 = int(bounding_box[0] + bounding_box[2] + margin_x)
    if x2 > img.shape[1]:
        x2 = img.shape[1]
          
    y1 = int(bounding_box[1] - margin_y)
    if y1 < 0:
        y1 = 0
          
    y2 = int(bounding_box[1] + bounding_box[3] + margin_y)
    if y2 > img.shape[0]:
        y2 = img.shape[0]

    face_image = img[y1:y2,x1:x2].copy()

    #face_image = cv2.resize(face_image, (380, 380)) 

    name = path.split('\\')[-1]
    new_filename= 'd:/AI_term_project/face_crop/fake/' + name  # 여기도 fake/real/test 선택
    cv2.imwrite(new_filename, cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR))

"""real와 test에서는 전부 얼굴을 제대로 찾아서 crop 성공, fake에서는 변형을 매우 심하게 하여 얼굴처럼 보이지 않는 사진들이 존재. 그것들은 어차피 학습을 하여도 매우 쉬운 문제이기 때문에 그냥 무시.

# 3. Data Preprocessing
"""

import os
import cv2
import random
import numpy as np
import pandas as pd
from glob import glob

fake_paths=glob('d:/AI_term_project/face_crop/fake/*.jpg')
real_paths=glob('d:/AI_term_project/face_crop/real/*.jpg')

print(len(fake_paths))  # 169868
print(len(real_paths))  # 134967

all_paths=fake_paths+real_paths

# Face Mask
# 얼굴 일부를 가려서 학습을 진행.
from imutils import face_utils
import dlib
detector = dlib.get_frontal_face_detector ()
predictor = dlib.shape_predictor('d:/AI_term_project/shape_predictor_68_face_landmarks.dat')

def blind_face(img):
    seed = random.random ()
    probability = 0.5

    if (seed < probability):
        seed = random.random ()
        case = int (seed * 3)
        gray = cv2.cvtColor (img, cv2.COLOR_RGB2GRAY)

        results = detector(gray, 0)
        if len(results) > 0 :
            shape = predictor (gray, results[0])
            shape = face_utils.shape_to_np (shape)
            pts_ = get_poly (shape, case, img.shape[1], img.shape[0])
            cv2.fillConvexPoly (img, pts_, (0, 0, 0))
            del shape, pts_

        
def get_poly(points, case_, x, y):
    input_shape = (x, y)

    pts = np.array ([points[36], points[20], points[23], points[45]], np.int32)

    if case_ == 0:  # both eye
        pts = np.array ([[points[36][0]-10, points[36][1]-20], [points[36][0]-10, points[36][1]+20], [points[45][0]+10, points[45][1]+20], [points[45][0]+10, points[45][1]-20]], np.int32)
    elif case_ == 1:  # nose
        pt1 = np.array ([points[31][0], points[28][1]])
        pt2 = np.array ([points[35][0], points[28][1]])
        pts = np.array ([points[27], pt1, points[31], points[51], points[35], pt2], np.int32)
    elif case_ == 2:  # forehead
        pt1 = np.array ([0, points[17][1]])
        pt2 = np.array ([input_shape[0] - 1, points[26][1]])
        pt3 = np.array ([input_shape[0] - 1, 0])
        pt4 = np.array ([0, 0])
        pts = np.array ([pt1, pt2, pt3, pt4], np.int32)
    
    return pts

from tensorflow.keras.utils import Sequence
import albumentations as A

labeling={'fake':1, 'real':0, 'test':2}

def load_img_label(path):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    label = labeling[path.split('/')[-1][:4]]
    return image, label

class DataGenerator(Sequence):

    def __init__(self, X, y, batch_size, step_per_epoch, input_shape, shuffle=True, augment = True):
        self.X = X
        self.y = y if y is not None else None
        self.batch_size = batch_size
        self.step_per_epoch = step_per_epoch
        self.input_shape = input_shape
        self.shuffle = shuffle
        self.augment = augment
        self.augment_size = int(self.batch_size*0.3)
        self.init_generator()
        self.on_epoch_end()

    def _shuffle_sample(self):
        if (self.shuffle == True):
            np.random.shuffle(self.indexes)

    # init_generator(): batch 생성 준비 및 잔여 데이터에 대한 batch 생성
    def init_generator(self):
        self.sample_size = len(self.X)
        self.indexes = np.zeros(self.sample_size, dtype=np.int)

        # 훈련 데이터에 쉬운 접근을 위한 인덱스 배열 생성
        for i in range(self.sample_size):
            self.indexes[i] = int(i)

        self._shuffle_sample()
        
        # 전체 데이터를 batch_size로 나누었을 때 남는 나머지 데이터들에 대한 작은 batch를 추가적으로 생성
        self.miniEpoch_size = self.batch_size * self.step_per_epoch
        self.cnt_mini_epoch = self.sample_size // self.miniEpoch_size
        self.iter_mini_epoch = 0


    # on_epoch_end(): 각 epoch의 처음과 끝에 실행되는 함수. shuffle 실행
    def on_epoch_end(self):
        if (self.iter_mini_epoch < self.cnt_mini_epoch):
            self.mini_indexes = self.indexes[self.iter_mini_epoch * self.miniEpoch_size: (self.iter_mini_epoch + 1) * self.miniEpoch_size]
            self.iter_mini_epoch = self.iter_mini_epoch + 1
        else:
            self.iter_mini_epoch = 0
            self._shuffle_sample()
            self.on_epoch_end()

    # len(): 한 배치에 있는 데이터의 크기 반환.
    def __len__(self):
        return int(self.step_per_epoch)

    # __data_generation(): 한 배치의 데이터에 전처리 기법 적용 후 반환
    def __data_generation(self, X_list, y_list):
        X = np.zeros ((self.batch_size, self.input_shape[0], self.input_shape[1], self.input_shape[2]), dtype=np.float32)
        y = np.zeros ((self.batch_size,), dtype=int)

        if y_list is not None:
            for i, (path, label) in enumerate(zip(X_list, y_list)):
                img, label = load_img_label(path)
                if self.augment and i < self.augment_size:
                    img = augmentor(img)
                X[i] = tf.image.resize(tf.cast(img, tf.float32), (224,224)) / 255.0  # resize the image to the same size
                y[i] = label

            return X, y
        else:
            for i, path in enumerate (X_list):
                img, _ = load_img_label(path)
                X[i] = tf.image.resize(tf.cast(img, tf.float32), (224,224)) / 255.0  # resize the image to the same size

            return X

    # __getitem__(): 한 배치의 데이터 반환
    def __getitem__(self, index):
        indexes = self.mini_indexes[index * self.batch_size: (index + 1) * self.batch_size]
        X_list = [self.X[k] for k in indexes]

        if self.y is not None:
            y_list = [self.y[k] for k in indexes]
            X, y = self.__data_generation (X_list, y_list)
            return X, y
        else:
            y_list = None
            X = self.__data_generation (X_list, y_list)
            return X

# Data Augmentation
# face mask,
# Horizontal flip,
# GaussianBlur, GaussianNoise, ImageCompression
def augmentor(img):
    image = np.array(img)
    blind_face(image)
    transform = A.Compose([
            A.augmentations.transforms.HorizontalFlip(p=0.5),
            A.augmentations.transforms.GaussianBlur(p=0.3),
            A.augmentations.transforms.GaussNoise(p=0.3),
            A.augmentations.transforms.ImageCompression(quality_lower=60, quality_upper=100, p=0.3),
    ])
    transformed = transform(image=image)
    image = transformed["image"]
    return image

# len(all_paths) = 304835, 
# 304835 / 6 = 50805
train_data = DataGenerator(all_paths, all_paths, 6, 50805, (224, 224, 3), True, True)

"""사용할 모델인 EfficientNetB4의 연산에 이미 엄청나게 많은 메모리를 사용하기 때문에 batch_size를 크게 만들 수 없어 6으로 설정하였습니다.

# 4. Model
EfficientNetB4 + RectifiedAdam
"""

import tensorflow as tf
from tensorflow import keras
import efficientnet.tfkeras as efficientnet  # !pip install efficientnet
import tensorflow_addons as tfa  # !pip install tensorflow-addons

def model():
    pretrained_model = efficientnet.EfficientNetB4(
        include_top=False,
        weights='imagenet',
        input_shape=(224, 224, 3),
      )
    pretrained_model.trainable = True
  
    inputs = keras.layers.Input(shape=(224, 224, 3))
    x = pretrained_model(inputs)
    x = keras.layers.GlobalAveragePooling2D()(x)
    x = keras.layers.Dense(512, activation='relu', kernel_regularizer=keras.regularizers.l2(0.01))(x)
    x = keras.layers.Dropout(0.5)(x)
    output = keras.layers.Dense(1, activation='sigmoid')(x)
    model = keras.models.Model(inputs = inputs, outputs = output)

    model.compile(
        optimizer = tfa.optimizers.RectifiedAdam(lr=1e-3, weight_decay=0.0005),  # 5 epoch 까지는 lr = 1e-3, 6epoch에서는 1e-4 사용
        loss=keras.losses.BinaryCrossentropy(from_logits=False),
        metrics = ['accuracy']
    )

    return model

model = model()
model.summary()

#model.summary() 출력결과
Model: "model"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 input_14 (InputLayer)       [(None, 224, 224, 3)]     0         
                                                                 
 efficientnet-b4 (Functional  (None, 7, 7, 1792)       17673816  
 )                                                               
                                                                 
 global_average_pooling2d_6   (None, 1792)             0         
 (GlobalAveragePooling2D)                                        
                                                                 
 dense_12 (Dense)            (None, 512)               918016    
                                                                 
 dropout_5 (Dropout)         (None, 512)               0         
                                                                 
 dense_13 (Dense)            (None, 1)                 513       
                                                                 
=================================================================
Total params: 18,592,345
Trainable params: 18,467,145
Non-trainable params: 125,200
_________________________________________________________________

from keras import callbacks

filepath = 'd:/AI_term_project/model2.hdf5'

mcp = callbacks.ModelCheckpoint(filepath, monitor = 'loss', save_best_only=False, save_weights_only=True, mode='min', save_freq=50, verbose=0)

model.fit(train_data, epochs= 1, verbose=1, callbacks=[mcp])

"""처음에 5epoch 학습한 후, 해당 weights에 lr 감소시켜서 1epoch 추가 학습"""

test_path = 'd:/AI_term_project/test/test_crop/*.jpg'

# collect all images
images = glob(test_path)
images.sort()
print(len(images)) # 4100
test_data = DataGenerator(images, None, 1, 4100, (224, 224, 3), False, False)

model.load_weights('d:/AI_term_project/rectifiedAdam_90.5%.hdf5')  # 5epoch 훈련한 weights, 이것만 했을 때는 90.5% accuracy
p = model.predict(test_data)
model.load_weights('d:/AI_term_project/89%.hdf5')  # 추가로 1epoch 훈련한 weights,이것만 했을 때는 89% accuracy
p2 = model.predict(test_data)

dir = 'd:/AI_term_project/submission.csv'
sc = open(dir, 'w')
sc.write('path,y')
sc.write('\n')

for i in range(len(images)):
    if p[i]+p2[i] > 1.0:  # model ensemble
        saveline = 'leaderboard/'+images[i][-15:] + ',1'
        sc.write(saveline)
        sc.write('\n')
    else:
        saveline = 'leaderboard/'+images[i][-15:] + ',0'
        sc.write(saveline)
        sc.write('\n')

sc.close()

submission = pd.read_csv(dir, index_col = False)
print(submission["y"].value_counts())

# 출력결과
# 0    2117
# 1    1983
# Name: y, dtype: int64

"""최종 결과는 91.463%, public 리더보드 16위를 기록.

이외에 모델 weight 갯수를 조금씩 바꾸거나 augmentation 비율조정 등을 하였지만 90% 넘어가는 모델은 만들지 못했고, 그나마 가장 높게 나왔던 두 개를 합쳐서 91%가 나왔다.
"""