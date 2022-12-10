from rest_framework import serializers


def starts_with_t(value):
    if value[0].lower() != "t":
        raise serializers.ValidationError("El titulo del ToDo debe empezar con T")
    return value
