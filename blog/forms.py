# coding: utf-8
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label='Ваше имя')
    message = forms.CharField(label='Сообщение',widget=forms.Textarea(attrs={'rows':'5','cols':'80'}))

class LoginForm(forms.Form):
    username = forms.CharField(label=u'', widget=forms.TextInput(attrs={'placeholder':'Логин'}))
    password = forms.CharField(label=u'', widget=forms.PasswordInput(attrs={'placeholder':'Пароль'}))

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None

