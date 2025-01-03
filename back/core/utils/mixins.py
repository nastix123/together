class PermissionActionMixin:
    def get_permissions(self):
        try:
            return [
                permission() for permission in self.permission_by_action[self.action]
            ]
        except (KeyError, AttributeError):
            return [permission() for permission in self.permission_classes]


class SerializerActionMixin:
    def get_serializer_class(self):
        try:
            return self.serializer_by_action[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
