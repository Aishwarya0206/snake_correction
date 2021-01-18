import string
import random
from captcha.image import ImageCaptcha

def generate_image_captcha(n = 5):
    image = ImageCaptcha()

    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
    data = image.generate(res)
    image.write(res,'one.png')
    return (res)