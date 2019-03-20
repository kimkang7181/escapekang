from django.shortcuts import render
import datetime
import sys
sys.path.append('..')
from information.models import Information
from theme.models import Theme
from .models import Popup


#팝업 뷰 바뀐부분
def main(request):
    theme = Theme.objects.all()
    info = Information.objects.all()
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')

    qs = Popup.objects.all()

    print(nowDate)
    return render(request, 'main.html', {
        'popuo': qs,
        'today': nowDate,
        'info': info,
        'theme': theme,
    })
