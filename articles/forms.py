from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data   #data dictionary
    #     #print(cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("This title is taken")
    #     #print(title)
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        # if title.lower().strip() == "the office":
        #     raise forms.ValidationError("This title is taken")
        
        if "office" in content or "office" in title:
            self.add_error("content", "Office can't be in content")
            raise forms.ValidationError("Office is not allowed")

        return cleaned_data


