import pandas as pd
import tensorflow as tf
from glob import glob
from tensorflow import keras


model = tf.keras.models.load_model('D:/enB4_model')
dir = 'D:/test/submission.csv'
sc = open(dir, 'w')
sc.write('path,y')
sc.write('\n')

test_path = 'D:/test/leaderboard/*.jpg'

def read_image(image_path):
  image = tf.io.read_file(image_path)
  image = tf.image.decode_jpeg(image, channels=3)
  image = (tf.cast(image, tf.float32) / 127.5 ) - 1
  return image

# collect all images
images = glob(test_path)
images.sort()

test_set=tf.data.Dataset.from_tensor_slices(images)
test_set=test_set.map(read_image)
test_set = test_set.batch(1)

predictions = model.predict(test_set)

predictions[:100]

for i in range(len(images)):
    images[i][-27:].replace("\\", "/", 2)
    print(images[i][-27:])

    if predictions[i] < 0.5:
        saveline = images[i][-27:] + ',1'
        sc.write(saveline)
        sc.write('\n')
    else:
        saveline = images[i][-27:] + ',0'
        sc.write(saveline)
        sc.write('\n')

sc.close()

submission = pd.read_csv(dir, index_col = False)

submission["y"].value_counts()