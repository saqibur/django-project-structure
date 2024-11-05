from typing import List

from rest_framework.request import Request
from rest_framework.serializers import ModelSerializer, Serializer


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


def create_validated_instance(serializer: Serializer, request: Request):
    serializer = serializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    return serializer.save(), serializer.validated_data


def get_validated_data(
    serializer: Serializer, request: Request, fields: List[str] = None
):
    if fields and issubclass(serializer, DynamicFieldsModelSerializer):
        serializer = serializer(fields=fields, data=request.data)
    else:
        serializer = serializer(data=request.data)

    serializer.is_valid(raise_exception=True)
    return serializer.validated_data
