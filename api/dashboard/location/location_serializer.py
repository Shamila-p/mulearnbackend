import uuid

from rest_framework import serializers

from db.organization import Country, District, State, Zone
from utils.utils import DateTimeUtils


class CountryRetrievalSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    value = serializers.CharField(source="id")

    class Meta:
        model = Country
        fields = ["label", "value"]


class CountryCreateEditSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    # value = serializers.CharField(source="id")

    class Meta:
        model = Country
        fields = ["label"]

    def update(self, instance, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = self.context.get("user_id")

        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = validated_data["created_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = validated_data["created_by_id"] = self.context.get("user_id")

        return super().create(validated_data)


class StateRetrievalSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    value = serializers.CharField(source="id")

    class Meta:
        model = Country
        fields = ["label", "value"]


class StateCreateEditSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    # value = serializers.CharField(source="id")

    class Meta:
        model = State
        fields = ["label", "country"]

    def update(self, instance, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = self.context.get("user_id")

        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = validated_data["created_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = validated_data["created_by_id"] = self.context.get("user_id")

        return super().create(validated_data)


class ZoneRetrievalSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    value = serializers.CharField(source="id")

    class Meta:
        model = Country
        fields = ["label", "value"]


class ZoneCreateEditSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    # value = serializers.CharField(source="id")

    class Meta:
        model = Zone
        fields = ["label", "state"]

    def update(self, instance, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = self.context.get("user_id")

        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = validated_data["created_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = validated_data["created_by_id"] = self.context.get("user_id")

        return super().create(validated_data)


class DistrictRetrievalSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    value = serializers.CharField(source="id")

    class Meta:
        model = Country
        fields = ["label", "value"]


class DistrictCreateEditSerializer(serializers.ModelSerializer):
    label = serializers.CharField(source="name")
    # value = serializers.CharField(source="id")

    class Meta:
        model = District
        fields = ["label", "zone"]

    def update(self, instance, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = self.context.get("user_id")

        return super().update(instance, validated_data)

    def create(self, validated_data):
        validated_data['id'] = uuid.uuid4()
        validated_data["updated_at"] = validated_data["created_at"] = DateTimeUtils.get_current_utc_time()
        validated_data["updated_by_id"] = validated_data["created_by_id"] = self.context.get("user_id")

        return super().create(validated_data)
