from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import models
import numpy as np
import matplotlib.pyplot as plt
from os import walk
from sklearn.metrics import confusion_matrix
import tensorflow as tf
#to test an image, you must have a the  model already trained and stored in a file

model = models.load_model("tomatoe.keras")  #model to be loaded

validation_dir = 'Tomato_Test'

validation_datagen = ImageDataGenerator(
    rescale = 1./255,
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size = (224,224),
    batch_size = 64,
    class_mode = 'categorical',
    subset = 'training',
    shuffle = True,
)

#
test_img = '/Ripe/healthy (24).jpg'
#test_img = '/Reject/reject (611).jpg'
#test_img = '/Unripe/unripe (608).jpg'


img_path = 'Tomato_Test'+ test_img   #image to be tested

#image preprocessing to be used
img = image.load_img(img_path,  target_size=(224,224))
img_tensor = image.img_to_array(img)
print(img_tensor.shape)
img_tensor = np.expand_dims(img_tensor, axis = 0)
img_tensor /= 255.

confidence = model.predict(img_tensor)
predict_class = (confidence > 0.5).astype("int32")
print (confidence)
print(predict_class)
print ("class ", predict_class[0][0], "confindence", )

if predict_class[0][1] == 1:
  print("Ripe")
elif predict_class[0][0] == 1:
  print("Reject")
else:
  print("Unripe")

plt.imshow(img_tensor[0])
plt.show()

img_path = 'WhatsApp Image 2024-04-29 at 12.08.09 AM 2.jpeg'   #image to be tested
#image preprocessing to be used
img = image.load_img(img_path,  target_size=(224,224))
img_tensor = image.img_to_array(img)
print(img_tensor.shape)
img_tensor = np.expand_dims(img_tensor, axis = 0)
img_tensor /= 255.

confidence = model.predict(img_tensor)
predict_class = (confidence > 0.5).astype("int32")
print (confidence)
print(predict_class)
print ("class ", predict_class[0][0], "confindence", )

if predict_class[0][1] == 1:
  print("Ripe")
elif predict_class[0][0] == 1:
  print("Reject")
else:
  print("Unripe")

plt.imshow(img_tensor[0])
plt.show()

images = ['/Unripe/augmented__0_6335.jpg','/Ripe/healthy (49).jpg','/Ripe/healthy (72).jpg','/Reject/reject (100).jpg']
labels = ["reject", "ripe", "unripe"]
size = len(images)

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1, size, figsize=(size*3, 4))

i = 0

for test_img in images:
  L_index = 0
  img_path = 'Tomato_Test'+ test_img
  img = image.load_img(img_path,  target_size=(224,224))
  img_tensor = image.img_to_array(img)
  img_tensor = np.expand_dims(img_tensor, axis = 0)
  img_tensor /= 255.
  confidence = model.predict(img_tensor)
  predict_class = (confidence > 0.5).astype("int32")

  if predict_class[0][1] == 1:
    L_index = 1
  elif predict_class[0][0] == 1:
    L_index = 0
  else:
    L_index = 2

  axarr[i].set_title("pred:" + labels[L_index])
  axarr[i].imshow(img)
  axarr[i].axis("off")
  i = i + 1

labels = ["reject", "ripe", "unripe"]

files = next(walk('Tomato_Test/Unripe'), (None, None, []))[2]
size = len(files)

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots((size//4)+1, 4, figsize=(20, 20))

i = 0
true = []
test = []

for test_img in files:
  L_index = 0
  img_path = 'Tomato_Test/Unripe/' + test_img
  if(img_path != "Tomato_Test/Unripe/.DS_Store"):
    img = image.load_img(img_path,  target_size=(224,224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis = 0)
    img_tensor /= 255.
    confidence = model.predict(img_tensor, verbose = 0)
    predict_class = (confidence > 0.5).astype("int32")
  
    if predict_class[0][1] == 1:
      L_index = 1
    elif predict_class[0][0] == 1:
      L_index = 0
    else:
      L_index = 2
  
    axarr[i//4,i%4].set_title("pred: "+ str(i) + labels[L_index])
    axarr[i//4,i%4].axis("off")
    axarr[i//4,i%4].imshow(img)
  
    test.append(L_index)
    true.append(2)
  
    i = i + 1

labels = ["reject", "ripe", "unripe"]

files = next(walk('Tomato_Test/Ripe'), (None, None, []))[2]
size = len(files)

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots((size//4)+1, 4, figsize=(20, 20))

i = 0

for test_img in files:
  L_index = 0
  img_path = 'Tomato_Test/Ripe/' + test_img
  if(img_path != "Tomato_Test/Ripe/.DS_Store"):
    img = image.load_img(img_path,  target_size=(224,224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis = 0)
    img_tensor /= 255.
    confidence = model.predict(img_tensor, verbose = 0)
    predict_class = (confidence > 0.5).astype("int32")
  
    if predict_class[0][1] == 1:
      L_index = 1
    elif predict_class[0][0] == 1:
      L_index = 0
    else:
      L_index = 2
  
    axarr[i//4,i%4].set_title("pred: "+ str(i) + labels[L_index])
    axarr[i//4,i%4].axis("off")
    axarr[i//4,i%4].imshow(img)
  
    test.append(L_index)
    true.append(1)
  
    i = i + 1

labels = ["reject", "ripe", "unripe"]

files = next(walk('Tomato_Test/Reject'), (None, None, []))[2]
size = len(files)

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots((size//4), 4, figsize=(20, 20))

i = 0

for test_img in files:
  L_index = 0
  img_path = 'Tomato_Test/Reject/' + test_img
  if(img_path != "Tomato_Test/Reject/.DS_Store"):
    img = image.load_img(img_path,  target_size=(224,224))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis = 0)
    img_tensor /= 255.
    confidence = model.predict(img_tensor, verbose = 0)
    predict_class = (confidence > 0.5).astype("int32")
  
    if predict_class[0][1] == 1:
      L_index = 1
    elif predict_class[0][0] == 1:
      L_index = 0
    else:
      L_index = 2
  
    axarr[i//4,i%4].set_title("pred: "+ str(i) + labels[L_index])
    axarr[i//4,i%4].axis("off")
    axarr[i//4,i%4].imshow(img)
  
    test.append(L_index)
    true.append(0)
  
    i = i + 1

matrix = confusion_matrix(true, test)

print("Reject: ", matrix[0])
print("Ripe:   ", matrix[1])
print("Unripe: ",matrix[2])

class_names = ['reject', 'ripe', 'unripe']
test_labels = [0,1,2]

def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  true_label = true_label[i]
  plt.grid(False)
  plt.xticks(range(3))
  plt.yticks([])
  thisplot = plt.bar(range(3), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

predictions = model.predict(validation_generator[0][0])
test_labels = validation_generator[0][1]
test_nV = np.argmax(test_labels, axis = 1)

print(tf.__version__)

# Plot the first X test images, their predicted labels, and the true labels.
# Color correct predictions in blue and incorrect predictions in red.
num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_nV, validation_generator[0][0])
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_nV)
plt.tight_layout()
plt.show()