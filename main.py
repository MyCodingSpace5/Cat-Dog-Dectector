
# Cat and Dog Detector using opencv
import tensorflowjs as tfjs
import cv2
tfjs.converters.save_keras_model(model, "PATH TO TRAINED MODEL HERE")

def generateCv2(camera, active):
    cap = cv2.VideoCapture(camera)
    while active:
        ret, frame = cap.read()
        cv2.imshow("Webcam", frame)
        preprocessed_frame = cv2.resize(frame, (224, 224))
        preprocessed_frame = preprocessed_frame.astype('float32') / 255.0
        if cv2.waitKey(1) == ord("q"):
            break
        return preprocessed_frame

def generateTensorflowModelData(preprocessed_frame, model):
    input_tensor = tf.expand_dims(preprocessed_frame, 0)
    prediction = model.predict(input_tensor)
    return prediction

class Cat():
    def __init__(self,detected):
        if(detected == True):
            #Put something here
            pass
class Dog():
    def __init__(self,detected):
        if(detected == True):
            #Put something here
            pass

def checkClass(prediction):
    if prediction == "Cat":
        Cat(detected=True)
    else:
        # Put something here
        Dog(detected=True)


