# import urllib
#
# from django.conf import settings
# from django.contrib import messages
# from django.http import request
# from django.shortcuts import redirect
# # from login.html import form
# import json
# with open('login.html', 'r') as f:
#     html_string = f.read()
#     if f.is_valid():
#         recaptcha_response = request.POST.get('g-recaptcha-response')
#         url = 'https://www.google.com/recaptcha/api/siteverify'
#         values = {
#             'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#             'response': recaptcha_response
#             }
#         data = urllib.parse.urlencode(values).encode()
#         req = urllib.request.Request(url, data=data)
#         response = urllib.request.urlopen(req)
#         result = json.loads(response.read().decode())
#
#         if result['success']:
#             f.save()
#             messages.success(request, 'Welcome!')
#         else:
#             messages.error(request, 'Invalid reCAPTCHA. Please try again.')

