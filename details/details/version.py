# import os
# import subprocess
#
# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
#
#
# def get_version_from_git():
#     try:
#         return subprocess.check_output(['git', 'describe', '--tags'],
#                                        cwd=FILE_DIR).decode('utf-8').strip()
#     except:
#         return '?'
#
#
# VERSION = get_version_from_git()
# from django import template
# import time
# import os
#
# register = template.Library()
#
# @register.simple_tag
# def version_date():
#     return time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime('../.git')))

# in base.html : <!--<footer> {% load version %}-->
# <!--<span class='version'>Last Updated: {% version_date %}</span> </footer>-->