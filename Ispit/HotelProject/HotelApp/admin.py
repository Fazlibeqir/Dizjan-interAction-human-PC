from django.contrib import admin
from .models import Hotels, Room, Employee, EmployeeRoom


# Register your models here.

class EmployeeRoomInline(admin.StackedInline):
    model = EmployeeRoom
    extra = 1


class EmployeeAdmin(admin.ModelAdmin):
    inlines = [EmployeeRoomInline]


class HotelsAdmin(admin.ModelAdmin):
    list_filter = ['id', 'reserved', ]
    exclude = ['user', ]

    def save_model(self, request, obj, form, change):
        if not obj.room.status:
            return False;
        obj.user = request.user
        return super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user


class RoomAdmin(admin.ModelAdmin):
    list_filter = ['number', 'status', ]

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Hotels, HotelsAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeRoom)
