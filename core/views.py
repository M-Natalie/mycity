from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ProposalListSerializer
from .models import Proposal

class ProposalListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        proposals = Proposal.objects.all()
        proposals_json = ProposalListSerializer(proposals, many=True)
        return Response(data=proposals_json.data)

# Create your views here.
