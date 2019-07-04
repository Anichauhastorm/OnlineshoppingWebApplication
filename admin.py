from django.contrib import admin
from shop1.models import Phones,PhonesImage,Tv,TvsImage,Poster,Laptop,LaptopImage,HeadPhone,HeadPhoneImage,Cart,Product
from shop1.models import Review,Address,Itemcount ,Myorder
# Register your models here.
class PhonesImageInline(admin.TabularInline):
    model = PhonesImage
    extra = 5
class PhonesAdmin(admin.ModelAdmin):
    list_display = ('Price','BrandName')
    inlines = [ PhonesImageInline, ]

admin.site.register(Phones,PhonesAdmin)

class TvsImageInline(admin.TabularInline):
    model = TvsImage
    extra = 5
class TvAdmin(admin.ModelAdmin):
    list_display = ('Price','BrandName','Tvname')
    inlines = [TvsImageInline, ]
admin.site.register(Tv,TvAdmin)

class PosterAdmin(admin.ModelAdmin):
    list_display = ('postername','image')
admin.site.register(Poster)

class LaptopImageInline(admin.TabularInline):
    model = LaptopImage
    extra = 5
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('Price','BrandName')
    inlines = [LaptopImageInline, ]
admin.site.register(Laptop,LaptopAdmin)

class HeadPhoneImageInline(admin.TabularInline):
    model = HeadPhoneImage
    extra = 5

class HeadPhoneAdmin(admin.ModelAdmin):
    list_display = ('Price','BrandName')
    inlines = [HeadPhoneImageInline,]
admin.site.register(HeadPhone,HeadPhoneAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display=('user','Price')

class ReviewAdmin(admin.ModelAdmin):
    list_display=('user','modalno')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user')


admin.site.register(Address)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(Product)


class ItemcountAdmin(admin.ModelAdmin):
    list_display = ('user', 'itemmodelno')



admin.site.register(Itemcount)

class MyorderAdmin(admin.ModelAdmin):
    list_display = ('user', 'itemid')

admin.site.register(Myorder)    