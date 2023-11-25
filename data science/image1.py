# tensorflow and keras
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load the CSV file
csv_file_path = "path/to/your/csvfile.csv"  # Replace with the actual path
df = pd.read_csv(csv_file_path)

# Define image directory
image_dir = "path/to/your/image_directory"  # Replace with the actual path

# Split the data into training and testing sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Create an ImageDataGenerator for data augmentation
datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)

# Create data generators
train_generator = datagen.flow_from_dataframe(
    dataframe=train_df,
    directory=image_dir,
    x_col="Image Filename",
    y_col="Defect",
    target_size=(128, 128),  # Adjust the target size based on your images
    batch_size=32,
    class_mode="binary"  # Change to "categorical" if you have multiple classes
)

test_generator = datagen.flow_from_dataframe(
    dataframe=test_df,
    directory=image_dir,
    x_col="Image Filename",
    y_col="Defect",
    target_size=(128, 128),
    batch_size=32,
    class_mode="binary"
)

# Build a simple CNN model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(128, 128, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Binary classification, change for multiclass

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=10, validation_data=test_generator)

# Evaluate the model
accuracy = model.evaluate(test_generator)[1]
print(f"Test Accuracy: {accuracy}")
