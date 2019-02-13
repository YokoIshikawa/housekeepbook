from django.shortcuts import render


def money_list(request):
    return render(request, 'money/money_list.html', {})
