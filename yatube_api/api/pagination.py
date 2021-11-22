from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class CustomPagination(LimitOffsetPagination):
    def get_paginated_response(self, data):
        limit = self.request.query_params.get('limit')
        if limit is None:
            return Response(data)
        return super().get_paginated_response(data)
