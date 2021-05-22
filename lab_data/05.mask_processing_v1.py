import face_recognition
from PIL import Image, ImageDraw

image_path = '../data/without_mask/galleryImgView.jpg'
face_image_path = '../data/without_mask/galleryImgView.jpg'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)

face_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_image)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    #draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=6)
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0), width=1)

    #print(face_location)
    mask_image = Image.open(mask_image_path)
    mask_width = int((right-left)*1.2)
    mask_height = int((bottom-top)*0.75)
    #mask_image = mask_image.resize((right-left, bottom-top))
    #face_image.paste(mask_image, (left, top), mask_image)
    mask_image = mask_image.resize((mask_width, mask_height))
    #face_image.paste(mask_image, (int(left-(mask_width-(right-left))/2), int(top*1.3)), mask_image)
    face_image.paste(mask_image, (int(left-(mask_width-(right-left))/2), int((top+bottom)/2.5)), mask_image)
    print(top,int(top*1.3))
face_image.show()

'''
print(face_location)
mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((int((right-left)*1.25), int((bottom-top)*0.75)))
face_image.paste(mask_image, (int(left-((right-left)*1.25-(right-left))/2.1), int((top+bottom)/2.5)), mask_image)
face_image.show()
'''