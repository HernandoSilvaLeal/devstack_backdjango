from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.activities.api.models import ActivitiesModel, ControlsModel, RisksModel, ThreatsModel, ResultsModel
from apps.activities.api.serializers import ActivitiesSerializer, ControlsSerializer, RisksSerializer, ThreatsSerializer, ResultsSerializer

class ActivitiesViewSet(viewsets.GenericViewSet):
    """
    Endpoint de Acctividades de Implementacion
    """
    model = ActivitiesModel                 
    serializer_class = ActivitiesSerializer

    # Consulta queryset para el GET list
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    # Consulta object para GET{Iid}, PUT{Iid}, DELETE{Iid}
    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    # Method GET list
    def list(self, request):
        """
        Metodo GET list --> Se utilizar para listar todas las actividades creadas de implementacion

        Sin parametros
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": data.data
        }
        return Response(data)

    # Method POST
    def create(self, request):
        """
        Metodo GET create --> Se utilizar para crear las actividades creadas de implementacion

        Sin parametros
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Unidad registrada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # Method GET {Iid}
    def retrieve(self, request, pk=None):
        """
        Metodo GET retrieve --> Se utilizar para obtener la actividad de implementacion seleccionada por id

        Sin parametros
        """
        if self.get_object().exists():
            data = self.get_object().get()
            data = self.get_serializer(data)
            return Response(data.data)
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

    # Method PUT {Iid}
    def update(self, request, pk=None):
        """
        Metodo UPDATE update --> Se utilizar para actualizar la actividad de implementacion seleccionada por id

        Sin parametros
        """
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)       
            if serializer.is_valid():       
                serializer.save()       
                return Response({'message':'Unidad actualizada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

    # Method DELETE {Iid}
    def destroy(self, request, pk=None):  
        """
        Metodo DELETE destroy --> Se utilizar para borrar la actividad de implementacion seleccionada por id

        Sin parametros
        """     
        if self.get_object().exists():       
            self.get_object().get().delete()       
            return Response({'message':'Unidad eliminada correctamente!'}, status=status.HTTP_200_OK)       
        return Response({'message':'', 'error':'Unidad no encontrada!'}, status=status.HTTP_400_BAD_REQUEST)

class ControlsViewSet(viewsets.GenericViewSet):
    model = ControlsModel
    serializer_class = ControlsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = ControlsModel.objects.filter(state=True)
        data = ControlsSerializer(data, many=True)
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

class RisksViewSet(viewsets.GenericViewSet):
    model = RisksModel
    serializer_class = RisksSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = RisksModel.objects.filter(state=True)
        data = RisksSerializer(data, many=True)
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

class ThreatsViewSet(viewsets.GenericViewSet):
    model = ThreatsModel
    serializer_class = ThreatsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = ThreatsModel.objects.filter(state=True)
        data = ThreatsSerializer(data, many=True)
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

class ResultsViewSet(viewsets.GenericViewSet):
    model = ResultsModel
    serializer_class = ResultsSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    @action(detail=False, methods=['get'])
    def get_measure_units(self, request):
        data = ResultsModel.objects.filter(state=True)
        data = ResultsSerializer(data, many=True)
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


