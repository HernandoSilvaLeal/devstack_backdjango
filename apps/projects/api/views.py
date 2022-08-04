from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.projects.api.models import ProjectsModel, CompaniesModel, StagesModel, AreasModel
from apps.projects.api.serializers import ProjectsSerializer, CompaniesSerializer, StagesSerializer, AreasSerializer

class ProjectsViewSet(viewsets.GenericViewSet):
    model = ProjectsModel
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = ProjectsModel.objects.filter(state=True)
        data = ProjectsSerializer(data, many=True)
        return Response(data.data)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Unidad registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Unidad actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Unidad eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

class CompaniesViewSet(viewsets.GenericViewSet):
    model = CompaniesModel
    serializer_class = CompaniesSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = CompaniesModel.objects.filter(state=True)
        data = CompaniesSerializer(data, many=True)
        return Response(data.data)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Unidad registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Unidad actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Unidad eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

class StagesViewSet(viewsets.GenericViewSet):
    model = StagesModel
    serializer_class = StagesSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = StagesModel.objects.filter(state=True)
        data = StagesSerializer(data, many=True)
        return Response(data.data)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Unidad registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Unidad actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Unidad eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

class AreasViewSet(viewsets.GenericViewSet):
    model = AreasModel
    serializer_class = AreasSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = AreasModel.objects.filter(state=True)
        data = AreasSerializer(data, many=True)
        return Response(data.data)

    def list(self, request):
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Unidad registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Unidad actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, pk=None):       
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Unidad eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

