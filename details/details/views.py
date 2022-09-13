# from django.contrib.auth import views as auth_views
# from django.shortcuts import redirect
#
#
# def _validate_recaptcha(token, ip):
#     # implement server side validation according to google docs
#     pass
# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip
#
#
# class MyLoginView(auth_views.LoginView):
#     '''Edited per @avib answer
#     '''
#
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         request_body = self.request.POST
#         if not request_body:
#             return None
#
#         recaptcha_token = request_body['g-recaptcha-response']
#         ip_addr, _ = get_client_ip(self.request)
#         if not _validate_recaptcha(recaptcha_token, ip_addr):
#             # your logic
#             return redirect('login')
#
#
#         return super().post(form)
#
#
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
#
# from .forms import UserRegistrationForm, UserLoginForm
#
#
# # Create your views here.
#
# # def register(request):
# #     if request.method == "POST":
# #         form = UserRegistrationForm(request.POST)
# #         if form.is_valid():
# #             user = form.save()
# #             login(request, user)
# #             messages.success(request, f"New account created: {user.username}")
# #             return redirect('/')
# #
# #         else:
# #             for error in list(form.errors.values()):
# #                 messages.error(request, error)
# #
# #     else:
# #         form = UserRegistrationForm()
# #
# #     return render(
# #         request=request,
# #         template_name="users/register.html",
# #         context={"form": form}
# #     )
# #
#
# @login_required
# def custom_logout(request):
#     logout(request)
#     messages.info(request, "Logged out successfully!")
#     return redirect("homepage")
#
#
#
# def custom_login(request):
#     if request.method == "POST":
#         form = UserLoginForm(request=request, data=request.POST)
#         if form.is_valid():
#             user = authenticate(
#                 username=form.cleaned_data["username"],
#                 password=form.cleaned_data["password"],
#             )
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
#                 return redirect("homepage")
#
#         else:
#             for key, error in list(form.errors.items()):
#                 if key == 'captcha' and error[0] == 'This field is required.':
#                     messages.error(request, "You must pass the reCAPTCHA test")
#                     continue
#
#                 messages.error(request, error)
#
#     form = UserLoginForm()
#     print(form)
#     return render(
#         request=request,
#         template_name="registration/login.html",
#         context={"form": form}
#     )
#
