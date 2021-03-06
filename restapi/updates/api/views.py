import json
from django.views.generic import View
from django.http import HttpResponse
from restapi.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm
from updates.models import Update as UpdateModel
from .mixins import CSRFExemptMixin
from .utils import is_json

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    '''
    Retrieve, Update, Delete --> Object
    '''
    is_json = True

    def get_object(self, id=None):
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, id, *args, **kwargs):
        json_data = json.dumps({'message': 'method not allowed'})
        return self.render_to_response(json_data, status=403)

    def put(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        new_data = json.loads(request.body)
        print(new_data['content'])
        json_data = json.dumps({'message': 'something'})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({"message": "Update not found"})
            return self.render_to_response(error_data, status=404)
        json_data = json.dumps({'message': 'something'})
        return self.render_to_response(json_data, status=403)

class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    """
    """
    is_json = True
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data,status=400)
        data = {'message':'Not allowed'}
        return self.render_to_response(obj_data, status=400)

