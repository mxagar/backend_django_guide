from rest_framework.permissions import BasePermission


def is_manager(user) -> bool:
    # The admin/superuser counts as a manager too (grading criteria: "the
    # admin can add menu items"/"...categories"), without needing to also
    # be added to the Manager group.
    return user.is_superuser or user.groups.filter(name='Manager').exists()


def is_delivery_crew(user) -> bool:
    return user.groups.filter(name='Delivery crew').exists()


class IsManager(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated and is_manager(request.user)


class IsDeliveryCrew(BasePermission):
    def has_permission(self, request, view) -> bool:
        return request.user.is_authenticated and is_delivery_crew(request.user)
