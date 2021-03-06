import subprocess

from django.contrib.auth.views import login_required
from django.contrib.messages import success, error
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.template.loader import render_to_string

# from ...utils.thread_mail import send_html_mail
from imalatlar.settings import ALLOWED_HOSTS
from .forms import MR30Form
from .models import MR30


@login_required
def detail_view(request, id):
    work_order = get_object_or_404(MR30, id=id)
    return render(request, 'mr30/detail.html', {'work_order': work_order})


@login_required
def create_view(request):
    if request.method == 'POST':
        form = MR30Form(request.POST)  # request.post un icinden gelen veriler ile bana bir form hazirla, onuda form a atadik

        if form.is_valid():  # kayit valid ise asagidaki islemlere gecilir degilse, else blogu calisir
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            success(request, f'{instance.crm} başarıyla oluşturuldu.')
            return redirect('mr30:list')
        else:
            error(request, 'Lütfen formu eksiksiz doldurduğunuza emin olun!')
    elif request.method == 'GET':
        form = MR30Form()
    context = {
        'form': form
    }
    return render(request, 'mr30/create.html', context)


@login_required
def list_view(request):
    return render(request, 'mr30/list.html', {'list': MR30.objects.all()})


@login_required
def send_mail(request, id):
    # tmp dizininin Windowsta olmamasından dolayı windowsta çalışmayabilir
    # wkhtmktopdf'i sunucuya kurmayı unutmayın!
    # Localde çalışırken default 8000 portunda çalıştırın!
    door = get_object_or_404(MR30, id=id)

    curr_url = ALLOWED_HOSTS[0].replace('http://', '').replace('https://', '') if ALLOWED_HOSTS else '127.0.0.1:8000'
    html = render_to_string('sld/detail.html', {'work_order': door, 'print': True}).replace('/static/',
                                                                                            f'http://{curr_url}/static/')

    with open(f'/tmp/{door.crm}.html', 'w') as f:
        f.write(html)

    pdf_file = f'/tmp/sld_{door.door_type}_{door.id}.pdf'
    subprocess.run([
        'wkhtmltopdf',
        '--javascript-delay', '2000',
        '--viewport-size', '1024x768',
        '--load-error-handling', 'ignore',
        f'/tmp/{door.crm}.html',
        pdf_file
    ])
    send_html_mail(
        f'{door.crm} - {door.get_door_type_display()}',
        '<p>Kapının teknik detayları ekteki pdftedir.</p>',
        file=pdf_file
    )
    return HttpResponse('Mail Başarıyla gönderildi.')
