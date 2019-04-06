from django.http import HttpResponse


def clientes(request):
    return HttpResponse('<ul><li>Jáber</li><li>Sindy</li><li>Julio</li></ul>')


def cliente_detalhe(request, id):
    return HttpResponse(id)


def cliente_nome(request, nome):
    return HttpResponse('Ola %s' % nome)
