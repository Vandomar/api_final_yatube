from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Проверям что только автор имеет доступ к POST, PUT и т.д.
    Остальные имеют доступ только к GET."""

    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
