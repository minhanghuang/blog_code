from rest_framework.permissions import BasePermission




class IsMyAdminUser(BasePermission):

    def has_permission(self, request, view):
        """
        只允许自定义的管理员通过
        :param request:
        :param view:
        :return: bool
        """

        return True if request.user.role == 0 else False

