from __future__ import annotations

from enum import Enum

g_image_type_extension = {
    'BMP':  [ 'bmp' ],
    'GIF':  [ 'gif' ],
    'HEIC': [ 'heic' ],
    'ICO':  [ 'ico' ],
    'JPG':  [ 'jpg', 'jpeg' ],
    'PNG':  [ 'png' ],
    'TIFF': [ 'tiff', 'tif' ],
    'WEBP': [ 'webp' ],
    'RAW':  [ 'cr2', 'crw', 'nef', 'pef' ]
}

g_image_extension_type = {
    'bmp':  'BMP',
    'gif':  'GIF',
    'heic': 'HEIC',
    'ico':  'ICO',
    'jpg':  'JPG',
    'jpeg': 'JPG',
    'png':  'PNG',
    'tiff': 'TIFF',
    'tif':  'TIFF',
    'webp': 'WEBP',
    'cr2':  'RAW',
    'crw':  'RAW',
    'nef':  'RAW',
    'pef':  'RAW'
}

class ImageFileType(Enum):
    BMP  = 1
    GIF  = 2
    HEIC = 3
    ICO  = 4
    JPG  = 5
    PNG  = 6
    TIFF = 7
    WEBP = 8
    RAW  = 9

    @staticmethod
    def assert_is_image_extension(ext: str) -> None:
        if not ext in g_image_extension_type:
            raise RuntimeError

    @staticmethod
    def from_extension(ext: str) -> ImageFileType:
        return ImageFileType[g_image_extension_type[ext]]

    @staticmethod
    def file_name_add_extension(file_name: str, type: ImageFileType) -> str:
        return file_name + '.' + g_image_type_extension[type.name][0]