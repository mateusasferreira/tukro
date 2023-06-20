from rest_framework import permissions

class CommunityPermission(permissions.BasePermission):
    safe_methods = ['POST','GET','HEAD','OPTIONS']

    def has_object_permission(self, request, view, obj):
        return request.method in self.safe_methods or request.user == obj.owner