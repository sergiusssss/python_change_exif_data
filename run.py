import piexif
from PIL import Image

img = Image.open("test.jpg")
exif_dict = piexif.load(img.info['exif'])

# for ifd_name in exif_dict:
#     print("\n{0} IFD:".format(ifd_name))
#     for key in exif_dict[ifd_name]:
#         pass
#         # try:
#         #     print(key, exif_dict[ifd_name][key][:10])
#         # except:
#         #     print(key, exif_dict[ifd_name][key])

print(exif_dict['GPS'][7])

exif_dict['0th'][306] = b'2010:10:20 10:10:10'
exif_dict['Exif'][36867] = b'2010:10:20 10:10:10'
exif_dict['Exif'][36868] = b'2010:10:20 10:10:10'
exif_dict['GPS'][7] = ((10, 10), (10, 10), (10, 10))
exif_dict['GPS'][29] = b'2010:10:10'
exif_bytes = piexif.dump(exif_dict)

img.save("test3_result.jpg", "jpeg", exif=exif_bytes)
