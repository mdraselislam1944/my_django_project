from django import forms
from .models import Employee


class CreateEmployeeForm(forms.ModelForm):
    emp_id = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class':  'form-control'}))
    emp_name = forms.CharField(widget=forms.TextInput(
        attrs={'class':  'form-control'}))
    dept = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class':  'form-control'}))
    

    class Meta:
        model = Employee
        fields = ('emp_id', 'emp_name', 'dept')
        
        

# class EditForm(forms.ModelForm):
# 	class Meta:
# 		model = Employee
# 		fields = ('emp_id','emp_name','dept')

# 		widgets = {

# 			'emp_id': forms.TextInput(attrs={'class': 'form-control'}),
# 			'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
# 			'dept': forms.Textarea(attrs={'class': 'form-control'}),


# 		}
