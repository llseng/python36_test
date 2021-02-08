from bpmappers import RawField
from bpmappers.djangomodel import ModelMapper
from polls.models import Subject

class SubjectMapper( ModelMapper ):
    isHot = RawField( 'is_hot' )
    
    class Meta:
        model = Subject
        exclude = ( 'is_hot',)

