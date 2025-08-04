def contact(request):
    context = {
        'page_title': 'Contact Us',
        'message': 'ติดต่อเรา'
    }
    return render(request, 'contact.html', context)

def forPage(request):
    context = {}
    context['count'] = list(range(1, 11))
    context['message'] = 'วนซ้ำข้อมูลใน Django'
    
    if request.method == 'POST':
        number = request.POST.get('count')
        try:
            number = int(number)
            context['count'] = list(range(1, number + 1))
        except:
            context['count'] = list(range(1, 2))
    else:
        context['count'] = list(range(1, 11))
    
    return render(request, 'for.html', context)