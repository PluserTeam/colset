#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, ButtonHolder, Layout, Div


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'placeholder': 'Email', 'class': "form-control form-control-lg"})
    )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña', 'class': "form-control form-control-lg"})
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            'email',
            'password',
            Div(
                ButtonHolder(
                    Submit('submit', 'Ingresar', css_class='btn btn-success btn-block btn-lg')
                ),
                css_class="login-buttons"
            )
        )
