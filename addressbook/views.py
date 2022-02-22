from .models import Addressbook
from .serializers import AddressbookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


FILTER_SEARCH_ORDERING_FIELDS = ["id", "country", "city", "postcode"]


class AddressbookView(ModelViewSet):
    queryset = Addressbook.objects.all()
    serializer_class = AddressbookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = FILTER_SEARCH_ORDERING_FIELDS
    search_fields = FILTER_SEARCH_ORDERING_FIELDS
    ordering_fields = FILTER_SEARCH_ORDERING_FIELDS

    def perform_create(self, serializer):
        # TODO: need to add unit test on this one
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # TODO: need to add unit test on this one
        # filter by owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset

    def delete(self, request, *args, **kwargs):
        # TODO: need to add unit test on this one
        # TODO: deletes all the items of the user, and all items of user for given filtering e.g. /?country=Netherlands
        #  but needs to be extended to work with search filtering (i.e. /?search=)
        owner_queryset = self.get_queryset()
        query = self.request.query_params
        filtered_queryset = owner_queryset.filter(**query.dict())
        filtered_queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
