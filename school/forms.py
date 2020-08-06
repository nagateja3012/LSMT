# from django import forms
# from school.models import Document

# class DocumentForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(DocumentForm, self).__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs = {"class": "form_control"}

#     class Meta:
#         model = Document
#         fields = ('description', 'document')