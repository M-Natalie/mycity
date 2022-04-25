from django.shortcuts import render
#from  import Serializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from .serializers import ProposalListSerializer, ProposalCreateSerializer, \
    ProposalSerializer
from .models import Proposal

class ProposalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerializer(proposals, many=True)
        return Response(data=proposals_json.data)

class ProposalCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        Serializer = ProposalCreateSerializer(data=data)
        if Serializer.is_valid():
            proposal = Serializer.save()
            json_data = ProposalSerializer(instance = proposal)
            return Response(json_data.data, 201)
        return Response(
            data={
                "message": "Data not valid",
                "errors": Serializer.errors

            }, 
                status=400
        )    

class ProposalRetrieveAPIView(RetrieveAPIView):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    
# Create your views here.
