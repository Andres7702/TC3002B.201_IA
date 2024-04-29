import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import optimizers
from tensorflow.keras import models
from tensorflow.keras import layers


"""input_dir = '/Users/andresacevedo/Downloads/tomatos/Tomato/Unripe'
output_dir = '/Users/andresacevedo/Downloads/tomatos/Tomato/Unripe/Augmented'
prefix = 'augmented_'
save_format = 'jpg'
num_augmented = 2

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

augment_params = {
    'rotation_range': 40,
    'zoom_range': 0.2,
    'horizontal_flip': True,
}
datagen = ImageDataGenerator(**augment_params)

for img_file in os.listdir(input_dir):
    img_path = os.path.join(input_dir, img_file)
    if(img_path != "/Users/andresacevedo/Downloads/tomatos/Tomato/Unripe/.DS_Store" and img_path != output_dir):
        img = load_img(img_path)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape) 
        i = 0
        for batch in datagen.flow(x, batch_size=1, save_to_dir=output_dir, save_prefix=prefix, save_format=save_format):
            i += 1
            if i >= num_augmented:
                break"""

train_dir = 'Tomato'

train_datagen = ImageDataGenerator(
    rescale = 1./255,
    zoom_range = 0.6,
    rotation_range = 10
    
)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size = (224,224),
    batch_size = 64,
    class_mode = 'categorical',
    shuffle = True
)

val_dir = 'Tomato_Validation'

validation_datagen = ImageDataGenerator(
    rescale = 1./255,
)

validation_generator = train_datagen.flow_from_directory(
    val_dir,
    target_size = (224,224),
    batch_size = 64,
    class_mode = 'categorical',
    shuffle = True
)


test_dir = 'Tomato_Test'

test_datagen = ImageDataGenerator(
    rescale = 1./255,
)

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size = (224,224),
    batch_size = 64,
    class_mode = 'categorical',
    shuffle = True,
)

label_categories = {
    0: "reject",
    1: "ripe",
    2: "unripe"
}

images , labels = train_generator[0]

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1, 10, figsize=(30, 4))

for i in range(10) :
    axarr[i].imshow(images[i])
    label_index = labels[i].argmax()
    axarr[i].axis("off")
    axarr[i].title.set_text(f"Label: {label_categories[label_index]}")

model = models.Sequential()

model.add(layers.Conv2D(64, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(256, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(3, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
						optimizer='adam',
						metrics=['acc'])

history = model.fit(
						train_generator,
						epochs = 30,
                        validation_data = validation_generator)

acc = history.history['acc']
loss = history.history['loss']

epochs = range(1, len(acc)+1)

plt.figure()
#subplot(r,c) provide the no. of rows and columns
f, axarr = plt.subplots(1, 2, figsize=(10, 3))
axarr[0].plot(epochs,acc,label='train accuracy')
axarr[0].legend()
axarr[0].plot(epochs,history.history['val_acc'],label=' val accuracy')
axarr[0].legend()
axarr[1].plot(epochs,loss,label='train loss')
axarr[1].legend()
axarr[1].plot(epochs,history.history['val_loss'],label=' val loss')
axarr[1].legend()


print(acc)
print(loss)

test_loss, test_acc = model.evaluate(test_generator)
print('\ntest acc :\n', test_acc)
print('\ntest loss :\n', test_loss)

predictions = model.predict(test_generator)
predict_class = (predictions > 0.5).astype("int32")
predict_class.shape

model.save("tomatoe.keras")