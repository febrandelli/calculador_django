from django.http import HttpResponse

def hello (request):
    return HttpResponse("Hello WORD!!!")

def oper (request,operador,n1,n2):
    if operador == 'soma':
        soma = n1+n2
        return HttpResponse (soma)
    elif operador == 'multiplicacao':
        multiplicacao = n1 * n2
        return HttpResponse (multiplicacao)
    elif operador == 'subtracao':
        subtracao = n1-n2
        return HttpResponse (subtracao)
    elif operador == 'divisao':
        divisao = n1/n2
        return HttpResponse (divisao)