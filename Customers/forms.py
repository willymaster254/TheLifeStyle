from django.forms import ModelForm
from .models import Customer


class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		labels = {
            'phone':'Telephone',
            'service':'Services',
			'Service_me_at': 'Time For Service',
			'discription': 'Any More Details',
			'reach_me_via': 'How To Communicate'
        }
		def __init__(self, *args, **kwargs):
			super (CustomerForm,self).__init__(*args, **kwargs)
			self.fields['service'].empty_label = "Select"
        
        

	
       