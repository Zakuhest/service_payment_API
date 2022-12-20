from django.shortcuts import get_object_or_404
from pagos.models import Payment_user
from rest_framework import (
    viewsets, 
    permissions, 
    status,
    filters)
from rest_framework.response import Response
from .serializers import PaymentUserSerializerV1
from .pagination import StandardResultsSetPagination

class PaymentUserViewSet(viewsets.ModelViewSet):

    queryset = Payment_user.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id','service_id','user_id']
    search_fields = ['user_id__username','service_id__name', 'payment_date']
    permission_classes = [permissions.IsAuthenticated]
    throttle_scope = 'payments'

    def get_serializer_class(self):

        return PaymentUserSerializerV1

    def retrieve(self, request, pk=None):
        queryset = Payment_user.objects.all()
        payment = get_object_or_404(queryset, pk=pk)
        serializer = PaymentUserSerializerV1(payment)

        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = PaymentUserSerializerV1(data=request.data, many = True)
        else:
            serializer = PaymentUserSerializerV1(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)