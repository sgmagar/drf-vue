from django.contrib import admin

from django.contrib.auth.admin import UserAdmin, UserChangeForm as DjangoUserChangeForm, \
    UserCreationForm as DjangoUserCreationForm
from django import forms

from users.models import User


class UserCreationForm(DjangoUserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(DjangoUserChangeForm):
    class Meta(DjangoUserChangeForm.Meta):
        model = User

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class CustomUserAdmin(UserAdmin):
    ordering = ('email',)
    form = UserChangeForm
    add_form = UserCreationForm
    filter_horizontal = ()
    list_display_links = ('id', 'full_name', 'email')
    list_display = ('id', 'full_name', 'email')
    list_filter = ('is_superuser', 'is_active')
    fieldsets = ((None,
                  {'fields': ('full_name',
                              'email',
                              'password',
                              'is_active',
                              'is_superuser',)}),
                 )
    add_fieldsets = ((None,
                      {'fields': ('full_name',
                                  'email',
                                  'password1',
                                  'password2',
                                  'is_active',
                                  'is_superuser')}),
                     )
    search_fields = ('full_name', 'email')
    readonly_fields = ('is_superuser',)


admin.site.register(User, CustomUserAdmin)