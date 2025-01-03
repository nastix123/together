from rest_framework import filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class CoreViewSet:
    filter_backends = (filters.SearchFilter,)
    search_fields = []
    action_serializers = {"retrieve": None, "list": None}

    def get_serializer_class(self):
        if (
            self.action in self.action_serializers
            and self.action_serializers.get(self.action) is not None
        ):
            return self.action_serializers[self.action]
        return super().get_serializer_class()

    def get_permissions(self):
        try:
            return [
                permission() for permission in self.permission_by_action[self.action]
            ]
        except (KeyError, AttributeError):
            return [permission() for permission in self.permission_classes]


class AbsReadOnlyModelViewSet(CoreViewSet, ReadOnlyModelViewSet):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)


class AbsCRUDView(CoreViewSet, ModelViewSet):
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
