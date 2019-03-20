from django.contrib import admin
from .models import Theme, Booking


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['name']

                                            #despositWay 추가 
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'time', 'numPeople','depositWay']


admin.site.register(Booking, BookingAdmin)
admin.site.register(Theme, ThemeAdmin)