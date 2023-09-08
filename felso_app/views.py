from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import *
from .forms import *


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class IndexView(TemplateView):
    template_name = 'index.html'



class ComponentsView(View):
    template_name = 'components.html'

    def get(self, request):
        form = ComponentsForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ComponentsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            data = {
                'project': instance.project,
                'item_name': instance.item_name,
                'base_quantity': instance.base_quantity,
                'new_unit_price': instance.new_unit_price,
                'type': instance.type
            }
            return JsonResponse(data)
        else:
            return render(request, self.template_name, {'form': form})

# class ComponentsView(CreateView):
#     model = Components
#     form_class = ComponentsForm  
#     template_name = 'components.html'  
#     # success_url = '/home'


#     def form_valid(self, form):
#         instance = form.save()
#         print(instance)
#         data = {'project': instance.project, 'item_name': instance.item_name, 
#                 'base_quantity': instance.base_quantity, 'new_unit_price': instance.new_unit_price,
#                 'type': instance.type}
#         return JsonResponse(data)
# class ComponentsView(View):
#     template_name = 'components.html'  # Your HTML template file

#     # def get(self, request):
#     #     form = ComponentsForm()
#     #     return render(request, self.template_name, {'form': form})

#     def post(self, request):
#         form = ComponentsForm(request.POST)
#         if form.is_valid():
#             instance = form.save()
#             print(instance)
#             print("hcgjvhxbljhjkx")
#             data = {
#                 'project': instance.project,
#                 'item_name': instance.item_name
#             }
#             return JsonResponse(data, status=200)  # Return JSON response with status code 200
#         else:
#             errors = form.errors
#             return JsonResponse({'errors': errors}, status=400)


class ComponentsListView(View):
    def get(self,request,*args,**kwargs):
        ab=Item.objects.all()
        return render(request,"components_list.html",{'components':ab})


class ComponentsEditView(UpdateView):
    form_class = ComponentsForm
    template_name = "components-edit.html"
    model = Item
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"

class GroupView(CreateView):
    model = Assembly
    form_class = GroupsForm  
    template_name = 'groups.html'  
    # success_url = '/components'

    def form_valid(self, form):
        instance = form.save()
        instance.status = True
        instance.save()
        print(instance)
        data = {'project': instance.project, 'item_name': instance.item_name, 
                'base_quantity': instance.base_quantity, 'group_cost': instance.group_cost,
                'type': instance.type}
        return JsonResponse(data)


