from django import forms


class Subscribe(forms.Form):
    Email = forms.EmailField()

    def __str__(self) -> str:
        return super().__str__() + self.Email
