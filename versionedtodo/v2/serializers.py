from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=100, validators=[starts_with_t])
    # title = serializers.CharField(allow_blank=True)
    # title = serializers.CharField(trim_whitespace=True)
    # title = serializers.CharField(max_length=100, min_length=1)

    # def validate_title(self, value):
    #     if "$" in value:
    #         raise serializers.ValidationError("El titulo no puede contener el simbolo $")
    #     return value

    # def validate_body(self, value):
    #     if "$" in value:
    #         raise serializers.ValidationError("El body no puede contener el simbolo $")
    #     return value

    # def validate_status(self, value):
    #     if value not in [0, 1, 2, 3]:
    #         raise serializers.ValidationError("El status solo puede tener de valores 0, 1, 2, 3")
    #     return value
    #
    # def validate(self, data):
    #     title = data.get('title')
    #     body = data.get('body')
    #     if "$" in title or "$" in body:
    #         raise serializers.ValidationError("El titulo y el body no pueden contener el simbolo $")
    #     return data

    class Meta:
        model = Todo
        fields = (
            "id", "title", "body",
            "status",
        )
