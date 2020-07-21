# for getting the category dynamically from the super-user

class FriendsForm(forms.ModelForm):
    class Meta:
        model = Catagory
    def __init__(self, *args, **kwargs):
        group_input = kwargs.pop('group_input', None)
        super(FriendsForm, self).__init__(*args, **kwargs)
        **pseudo-code: use group to get color list**
        self.fields['color'].widget = forms.Select(choices=new_list)