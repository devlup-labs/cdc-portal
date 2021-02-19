from rest_framework import serializers
from .models import CompanyProfile, JobAdvertisement, JobOffer, InternshipAdvertisement, InternshipOffer, CompanyPerson
from student.serializers import UserSerializer


class InternshipAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternshipAdvertisement
        fields = '__all__'


class JobAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobAdvertisement
        fields = '__all__'


class JobOfferSerializer(serializers.ModelSerializer):
    profile = JobAdvertisementSerializer(read_only=True)

    class Meta:
        model = JobOffer
        fields = '__all__'


class InternshipOfferSerializer(serializers.ModelSerializer):
    profile = InternshipAdvertisementSerializer(read_only=True)

    class Meta:
        model = InternshipOffer
        fields = '__all__'


class CompanyProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    job_offers = JobOfferSerializer(read_only=True)
    intership_offers = InternshipOfferSerializer(read_only=True)

    class Meta:
        model = CompanyProfile
        fields = '__all__'


class CompanyPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyPerson
        fields = '__all__'
