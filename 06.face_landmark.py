import face_recognition
from PIL import Image, ImageDraw

face_image_path = 'data/without_mask/0.jpg'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmarks_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmarks_image)

for face_landmark in face_landmarks:
    for feature_name, points in face_landmark.items():
        for point in points:
            draw.point(point)
#draw.point((10, 10))

face_landmarks_image.show()