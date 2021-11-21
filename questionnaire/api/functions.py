def get_attachment(request):
    print(request.query_params)
    x_forwarded_for = request.get('HTTP')
    attachment = str(x_forwarded_for).split(',')[0]
    print('__________________________________________________________')
    print(attachment)
    print('__________________________________________________________')
    return attachment