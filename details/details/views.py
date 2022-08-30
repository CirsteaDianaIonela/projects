# from django.contrib.auth import views as auth_views
# from django.shortcuts import redirect
#
#
# def _validate_recaptcha(token, ip):
#     # implement server side validation according to google docs
#     pass
#
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
# class MyLogIn(auth_views.LoginView):
#     '''Edited per @avib answer
#     '''
#
#
#     def post(self, form):
#         request_body = self.request.POST
#         print("a")
#         if not request_body:
#             return None
#
#         recaptcha_token = request_body['g-recaptcha-response']
#         ip_addr, _ = get_client_ip(self.request)
#         print("a")
#         if not _validate_recaptcha(recaptcha_token, ip_addr):
#             # your logic
#             print("a")
#             return redirect('login')
#         print("a")
#
#         return super().post(form)

