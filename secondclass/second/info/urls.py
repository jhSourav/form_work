from django.urls import path
from info.views import division,district,allDis


urlpatterns = [
    path('', division, name='division'), #kivabe url chara default page e show korabo
    path('dist/<name>',district, name='district'),
    path('all/<name>',allDis,name='alldistrict')
    # path('guard/<name>',guardian_detail, name='guardian_detail'),
    # path('profile/<roll>',profile, name='profile'),
    # path('class/<clss>',check, name='check'),
]
