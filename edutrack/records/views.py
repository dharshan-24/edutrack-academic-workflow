from rest_framework import viewsets
from .models import AcademicRecord
from .serializers import AcademicRecordSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AcademicRecordViewSet(viewsets.ModelViewSet):
    queryset = AcademicRecord.objects.all()
    serializer_class = AcademicRecordSerializer
    permission_classes=[IsAuthenticated]



def update(self, request, *args, **kwargs):
        
        if request.user.role != "ADMIN":
            return Response({"error" : "Admin Access required"}, status=403)
        return super().update(request, *args, **kwargs)
    
def create(self, request, *args, **kwargs):
        
        if request.user.role != "FACULTY":
            return Response({"error" : "Faculty access required"}, status=403)
        return super().create(request, *args, **kwargs)

def list(self, request, *args, **kwargs):
        
        if request.user.role != "STUDENT" :
            return Response({"error" : "student access only"}, status=403)
        return super().list(request, *args, **kwargs)
