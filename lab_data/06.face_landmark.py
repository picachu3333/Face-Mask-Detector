#얼굴 랜드마크 추출
import face_recognition, math
from PIL import Image, ImageDraw

face_image_path = '../data/without_mask/1.jpg'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmarks_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmarks_image)

for face_landmark in face_landmarks:
    print(face_landmark)
    left_chin_x = face_landmark['chin'][0][0]
    left_chin_y = face_landmark['chin'][0][1]
    right_chin_x = face_landmark['chin'][16][0]
    right_chin_y = face_landmark['chin'][16][1]
    nose_top_x = face_landmark['nose_bridge'][0][0]
    nose_top_y = face_landmark['nose_bridge'][0][1]
    chin_bottom_x = face_landmark['chin'][8][0]
    chin_bottom_y = face_landmark['chin'][8][1]

    angle = (math.atan((left_chin_y - right_chin_y)/(right_chin_x - left_chin_x)))*(180/math.pi)
    print(angle)

    mask_image = Image.open(mask_image_path)
    mask_width = math.sqrt(math.pow(right_chin_x - left_chin_x,2) + math.pow(right_chin_y - left_chin_y,2))
    mask_height = math.sqrt(math.pow(chin_bottom_x - nose_top_x,2) + math.pow(chin_bottom_y - nose_top_y,2))
    mask_image = mask_image.resize((int(mask_width), int(mask_height)))
    mask_image = mask_image.rotate(angle,expand=True)
    face_landmarks_image.paste(mask_image, (left_chin_x, nose_top_y), mask_image)
    #face_landmarks_image.paste(mask_image, (0,0), mask_image)



    print(left_chin_x, left_chin_y)
    for feature_name, points in face_landmark.items():
        #print(feature_name, points)
        for point in points:
            draw.point(point)



face_landmarks_image.show()