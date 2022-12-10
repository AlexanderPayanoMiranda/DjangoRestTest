from rest_framework import serializers
from todos.models import Todo, TestValidation
from todos.validators import starts_with_t
# from .models import Todo


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

    def validate_status(self, value):
        if value not in [0, 1, 2, 3]:
            raise serializers.ValidationError("El status solo puede tener de valores 0, 1, 2, 3")
        return value

    def validate(self, data):
        title = data.get('title')
        body = data.get('body')
        if "$" in title or "$" in body:
            raise serializers.ValidationError("El titulo y el body no pueden contener el simbolo $")
        return data

    class Meta:
        model = Todo
        fields = (
            "id", "title", "body", "created_at",
            "done_at", "updated_at", "deleted_at",
            "status",
        )

        read_only_fields = (
            "created_at", "done_at", "updated_at",
            "deleted_at",
        )


class TestTodoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    body = serializers.CharField(max_length=200)
    status = serializers.IntegerField()

    def create(self, validated_data):
        return Todo(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        return instance


class TestValidationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=True)
    email = serializers.EmailField(allow_blank=True)
    url = serializers.URLField(allow_blank=True)
    ip = serializers.IPAddressField(protocol="both")
    integer = serializers.IntegerField(min_value=0, max_value=15)
    float = serializers.FloatField(min_value=0, max_value=15)
    # decimal = serializers.DecimalField()
    # date = serializers.DateField()
    # time = serializers.TimeField()
    time_now = serializers.HiddenField(default="08:00:00")

    class Meta:
        model = TestValidation
        fields = (
            "name", "email", "url",
            "ip", "integer", "float", "decimal",
            "date", "time", "time_now"
        )