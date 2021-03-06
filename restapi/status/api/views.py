import json
from rest_framework.authentication import SessionAuthentication
from rest_framework import generics
from rest_framework import mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from status.models import Status
from .serializers import StatusSerializer 

def is_json(json_data):
    """
    """
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView):
    """
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()
    lookup_field                = "id"

    def put(self, request, *args, **kwargs):
        """
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        """
        return self.destroy(request, *args, **kwargs)

class StatusAPIView(mixins.CreateModelMixin,
        mixins.UpdateModelMixin,
        mixins.DestroyModelMixin,        
        generics.ListAPIView ):
    """
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    search_fields =  ('user__username', 'content')
    passed_id = None
    ordering_fields = ('user__username', 'timestamp')
    queryset = Status.objects.all()

    def get_queryset(self):
        request = self.request
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get("id", None) or self.passed_id 
#         queryset = self.get_queryset()
#         if passed_id is not None :
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)
#         return obj

    
#     def get(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or  None

#         self.passed_id = passed_id        
#         if passed_id is not None: #or passed_id is not "":
#             return self.retrieve(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)


    
#     def put(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or  None
#         self.passed_id = passed_id        
        
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or  None
#         self.passed_id = passed_id        
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get("id", None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get("id", None)
#         passed_id = url_passed_id or new_passed_id or  None
#         self.passed_id = passed_id        
#         return self.destroy(request, *args, **kwargs)


# # class StatusListSearchAPIView(APIView):
# #     '''
# #     Api views
# #     '''
# #     permission_classes = []
# #     authentication_classes = []

# #     def get(self, request):
# #         qs = Status.objects.all()
# #         serializer = StatusSerializer(qs, many=True)
# #         return Response(serializer.data)

# #     def post(self, request, format=None):
# #         qs = Status.objects.all()
# #         serializer = StatusSerializer(qs, many=True)
# #         return Response(serializer.data)



# # # class StatusCreateAPIView(generics.CreateAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer


# # class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
# #     permission_classes = []
# #     authentication_classes = []
# #     queryset = Status.objects.all()
# #     serializer_class = StatusSerializer
# #     lookup_field = "id"

# #     def put(self, request, *args, **kwargs):
# #         return self.update(request, *args, **kwargs)

# #     def delete(self, request, *args, **kwargs):
# #         return self.destroy(request, *args, **kwargs)

# # # class StatusUpdateAPIView(generics.UpdateAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer

# # # class StatusDeleteAPIView(generics.DestroyAPIView):
# # #     permission_classes = []
# # #     authentication_classes = []
# # #     queryset = Status.objects.all()
# # #     serializer_class = StatusSerializer
