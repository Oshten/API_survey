from rest_framework import permissions


class SurveyPermission(permissions.IsAuthenticatedOrReadOnly):
    '''Добавление прав для просмотра и создания/изменения опросов'''

    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS or
            request.user and request.user.is_staff
        )



