def handle_uploaded_file(f):
    with open('details/media/store/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
