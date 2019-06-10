import requests
from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image
from users.models import User
from django.db.models import Q

def get_avatar(request, backend, strategy, details, response, user=None, *args, **kwargs):
    url = None
    # if backend.name == 'facebook':
    #     url = "http://graph.facebook.com/%s/picture?type=large"%response['id']
    # if backend.name == 'twitter':
    #     url = response.get('profile_image_url', '').replace('_normal','')
    if backend.name == 'google-oauth2':
        try:
            url = response["picture"]
        except KeyError:
            url = response['image'].get('url')

        get_file = download(url)
        file_name = url.split('/')[-1]
        extension = 'jpeg'

        f = BytesIO(get_file)
        out = BytesIO()

        image = Image.open(f)
        image.save(out, extension)

        try:
            userData = User.objects.get(Q(email=details['email']))
            userData.photo.save(file_name, ContentFile(out.getvalue()), save=False)
            userData.save()
            request.session['photo'] = userData.photo.name
        except User.DoesNotExist:
            userData = User.objects.create(
                first_name=details['first_name'],
                last_name=details['last_name'],
                email=details['email'],
                password='',
                role_id=4,
                photo=''
            )
            userData.photo.save(file_name, ContentFile(out.getvalue()), save=False)
            userData.save()
            request.session['photo'] = userData.photo.name


def download(url):
    try:
        r = requests.get(url)
        if not r.status_code == 200:
            raise Exception('file request failed with status code: ' + str(r.status_code))
        return (r.content)
    except Exception as ex:
        return ('error')