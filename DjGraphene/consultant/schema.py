import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType
from .models import Patient, Consultant,Appointment
# first define all types
class PatientType(DjangoObjectType):
    class Meta:
        model = Patient
        fields = ("id", "name", "gender")

class ConsultantType(DjangoObjectType):
    class Meta:
        model = Consultant
        fields = ("id", "name", "specialization")

class AppointmentType(DjangoObjectType):
    class Meta:
        model = Appointment
        fields = ("date_appointment", "consultant", "patient","comment")
        
#Write queries
class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_appointments=graphene.List(AppointmentType, search=graphene.String())
    def resolve_all_appointments(parent, info, search=None, **kwargs):
        if search:
            filter = (
                Q(consultant__name__icontains=search)|
                Q(patient__name__icontains=search)
            )
            return Appointment.objects.filter(filter)
        return Appointment.objects.all()

schema = graphene.Schema(query=Query)
