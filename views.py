from django.shortcuts import render
def home(request):
    context = {
        'page_title': 'Home',
        'message': 'ยินดีต้อนรับสู่หน้าแรก'
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        'page_title': 'About',
        'message': 'เกี่ยวกับฉัน'
    }
    return render(request, 'about.html', context)
def contact(request):
    context = {
        'page_title': 'Contact Us',
        'message': 'ติดต่อเรา'
    }
    return render(request, 'contact.html', context)

def forPage(request):
    context = {}
    context['title'] = 'รายชื่อนักศึกษา'
    
    students  render(requst, 'students.html', context)
    
    
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