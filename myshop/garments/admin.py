from django.contrib import admin
from .models import Formalshirt,Casualshirt,Tshirt,IndianWear,WesternWear,FootWear,BoysClothing,GirlsClothing,Brand




# Register your models here.
class FormalshirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(Formalshirt,FormalshirtAdmin)

class CasualshirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(Casualshirt,CasualshirtAdmin)

class TshirtAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(Tshirt,TshirtAdmin)

class IndianWearAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(IndianWear,IndianWearAdmin)

class WesternWearAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(WesternWear,WesternWearAdmin)

class FootWearAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(FootWear,FootWearAdmin)

class BoysClothingAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(BoysClothing,BoysClothingAdmin)

class GirlsClothingAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(GirlsClothing,GirlsClothingAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display=('name','price','stock','available','created','updated')

admin.site.register(Brand,BrandAdmin)

