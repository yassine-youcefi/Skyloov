from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status




class CustomPageNumber(PageNumberPagination):
    page_size = 20
    last_page_strings = ('last',)
    
    def paginate_queryset(self, queryset, request, view=None):
        """
        Paginate the queryset, but raise a 404 error if the queryset is empty.
        """
        page = super().paginate_queryset(queryset, request, view=view)
        if not page:
            raise NotFound('No results found for the requested page')
        return page