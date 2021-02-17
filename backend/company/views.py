from rest_framework.response import Response
from .serializers import CompanyProfileSerializer, InternshipOfferSerializer, JobOfferSerializer
from .models import CompanyProfile, InternshipOffer, JobOffer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


class AddCompanyDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = {}
        for key in request.data.keys():
            data[key] = request.data.get(key)
        user = request.user
        user.first_name = data.pop('first_name')
        user.last_name = data.pop('last_name')
        user.save()
        job_offers = data.pop('job_offers')
        internship_offers = data.pop('internship_offers')
        profile = CompanyProfile.objects.create(user=user, **data, job_offers=JobOffer.objects.get(name=job_offers['profile']),
                                                internship_offers=InternshipOffer.objects.get(internship_offers['profile']))
        profile.save()
        return Response(CompanyProfileSerializer(profile).data, status=status.HTTP_200_OK)


class GetCompanyDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = CompanyProfile.objects.filter(user=user)
        serializer = CompanyProfileSerializer(profile, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateCompanyDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        serializer = CompanyProfileSerializer(instance=request.user, data=request.data)
        data = {}
        for key in request.data.keys():
            data[key] = request.data.get(key)
        user = request.user
        user.first_name = data.pop('first_name')
        user.last_name = data.pop('last_name')
        user.save()
        job_offers = data.pop('job_offers')
        internship_offers = data.pop('internship_offers')
        _ = CompanyProfile.objects.filter(user=user).update(**data, job_offers=JobOffer.objects.get(name=job_offers['profile']),
                                                            internship_offers=InternshipOffer.objects.get(name=internship_offers['profile']))
        profile = CompanyProfile.objects.filter(user=user)[0]
        profile.save()

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteCompanyDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        user = request.user
        profile = CompanyProfile.objects.get(user=user)
        fucntion = profile.delete()
        data = {}
        if fucntion:
            data["status"] = "Successfully deleted profile"
        else:
            data["status"] = "Failed to delete profile"
        return Response(data=data)


class AddJoboffer(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company=CompanyProfile.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetJoboffers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        job_offers = JobOffer.objects.filter(company__user=request.user)
        serializer = JobOfferSerializer(job_offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddInternshipoffer(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, format=None):
        serializer = InternshipOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company=CompanyProfile.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetInternshipoffers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        internship_offers = InternshipOffer.objects.filter(company__user=request.user)
        serializer = InternshipOfferSerializer(internship_offers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
