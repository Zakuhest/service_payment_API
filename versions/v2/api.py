from django.shortcuts import get_object_or_404
from pagos.models import (
    Payment_user, 
    Services, 
    Expired_payments,)
from rest_framework import (
    viewsets, 
    permissions, 
    status,
    filters)
from rest_framework.response import Response
from .serializers import (
    PaymentUserSerializerV2,
    ServicesSerializerV2,
    ExpiredPaymentsSerializerV2,
    )
from .pagination import StandardResultsSetPagination

class PaymentUserViewSet(viewsets.ModelViewSet):

    queryset = Payment_user.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id','service_id','user_id']
    search_fields = ['payment_date', 'expiration_date']
    throttle_scope = 'payments'

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create' or self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]

        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy' or self.action == 'retrieve':
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):

        return PaymentUserSerializerV2

    def retrieve(self, request, pk=None):
        payment = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializerV2(payment)

        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = PaymentUserSerializerV2(data=request.data, many = True)
        else:
            serializer = PaymentUserSerializerV2(data=request.data)

        if serializer.is_valid():
            serializer.save()

            if isinstance(request.data, list):
                lista = []
                for i in range(len(request.data)):
                    if request.data[i]["expiration_date"] < serializer.data[i]["payment_date"]:
                        lista.append({
                            "pay_user_id": serializer.data[i]["id"],
                            "penalty_fee_amount": 15.00
                            })
                expired_serial=ExpiredPaymentsSerializerV2(data=lista, many=True)

                if expired_serial.is_valid():
                    ExpiredPaymentsViewSet.create(ExpiredPaymentsViewSet,request=expired_serial)
            else:
                if request.data["expiration_date"] < serializer.data["payment_date"]:
                    expired_serial=ExpiredPaymentsSerializerV2(data={
                        "pay_user_id": serializer.data["id"],
                        "penalty_fee_amount": 15.00
                        })
                        
                    if expired_serial.is_valid():
                        ExpiredPaymentsViewSet.create(ExpiredPaymentsViewSet,request=expired_serial)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        payment = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializerV2(payment, data=request.data)

        if serializer.is_valid():
            serializer.save()

            if request.data["expiration_date"] < serializer.data["payment_date"]:
                expired_serial=ExpiredPaymentsSerializerV2(data={
                    "pay_user_id": serializer.data["id"],
                    "penalty_fee_amount": 15.00
                    })
                    
                if expired_serial.is_valid():
                    ExpiredPaymentsViewSet.create(ExpiredPaymentsViewSet,request=expired_serial)

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        payment = get_object_or_404(self.queryset, pk=pk)
        serializer = PaymentUserSerializerV2(payment, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            if request.data["expiration_date"] < serializer.data["payment_date"]:
                expired_serial=ExpiredPaymentsSerializerV2(data={
                    "pay_user_id": serializer.data["id"],
                    "penalty_fee_amount": 15.00
                    })
                    
                if expired_serial.is_valid():
                    ExpiredPaymentsViewSet.create(ExpiredPaymentsViewSet,request=expired_serial)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        payment = get_object_or_404(self.queryset, pk=pk)
        payment.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ServicesViewSet(viewsets.ModelViewSet):

    queryset = Services.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id','name']
    search_fields = ['name']
    throttle_scope = 'others'

    def get_permissions(self):
        permission_classes = []

        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]

        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy' or self.action == 'retrieve' or self.action == 'create':
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):

        return ServicesSerializerV2

    def retrieve(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        serializer = ServicesSerializerV2(service)

        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = ServicesSerializerV2(data=request.data, many = True)
        else:
            serializer = ServicesSerializerV2(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        serializer = ServicesSerializerV2(service, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        serializer = ServicesSerializerV2(service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        service = get_object_or_404(self.queryset, pk=pk)
        service.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class ExpiredPaymentsViewSet(viewsets.ModelViewSet):

    queryset = Expired_payments.objects.all()
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['id','pay_user_id','penalty_fee_amount']
    search_fields = ['pay_user_id__user_id__username','penalty_fee_amount']
    throttle_scope = 'others'

    def get_permissions(self):
        permission_classes = []

        if self.action == 'create' or self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]

        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy' or self.action == 'retrieve':
            permission_classes = [permissions.IsAdminUser]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):

        return ExpiredPaymentsSerializerV2

    def retrieve(self, request, pk=None):
        expired = get_object_or_404(self.queryset, pk=pk)
        serializer = ExpiredPaymentsSerializerV2(expired)

        return Response(serializer.data)

    def create(self, request):

        if isinstance(request.data, list):
            serializer = ExpiredPaymentsSerializerV2(data=request.data, many = True)
        else:
            serializer = ExpiredPaymentsSerializerV2(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        expired = get_object_or_404(self.queryset, pk=pk)
        serializer = ExpiredPaymentsSerializerV2(expired, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        expired = get_object_or_404(self.queryset, pk=pk)
        serializer = ExpiredPaymentsSerializerV2(expired, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        expired = get_object_or_404(self.queryset, pk=pk)
        expired.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)