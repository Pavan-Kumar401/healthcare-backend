from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    RegisterSerializer, PatientSerializer,
    DoctorSerializer, MappingSerializer
)

# Auth
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# Patients
from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the logged-in user automatically
        serializer.save(user=self.request.user)



# Doctors
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# Mappings
class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(patient__user=self.request.user)
