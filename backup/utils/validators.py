from PIL import Image
from django.core.exceptions import ValidationError

def validate_image(file):
    try:
        with Image.open(file) as img:
            pass
    except IOError:
        raise ValidationError('File is not an image.')
    
    with Image.open(file) as img:
        if img.width != img.height:
            raise ValidationError('Image must be square.')
        
    if file.size > 3 * 1024 * 1024:
        raise ValidationError('Image must be less than 3MB.')
    
    return file