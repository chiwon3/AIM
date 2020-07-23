crud 작업

지난 시간 복습

우선 유저들의 계정을 관리하는것은 새로운 기능임으로 새로운 앱을 만들어준다

python manage.py startapp account

views에는 추가를 해줘야 하지만 먼저 url에 

from account.views import signup
path('signup/',signup, name="signup")

을 추가해준다

html 에도 a tag 걸어서 signup을 만들어준다

views에 이제 signup을 만들어준다

def signup(request):
    return render(request, 'signup.html')
    
이제 함수는 만들었지만 signup 페이지를 만들어야한다

쟝고는 편리하게 회원가입 폼을 어느정도 제공한다.

from django.contrib.auth.forms import UserCreationForm

이게 쟝고에서 기본으로 제공하는 회원가입 폼
궁금하면 github 가서 django에 찾아보면 됨
이미 찾아봐서 밑에 복붙해둠

def signup(request):
    context-dict()
    signup_form = UserCreationForm
    contesxt['signup_form'] = signup_form
    
    return render(request, 'signup.html')

이렇게 views.py에 수정해두면 일단 기능구현은 하도록 되었다.

signup.html을 만들어 주고

```python
<form method="Post">

    {% csrf_token %}
    {{signup_form}}

    <button type="submit">signup</button>
    
</form>
```

이렇게 하면 영어로 설명이 나온다.

한글로 바꾸려면 settings.py에 가서 맨 밑쪽에
LANGUAGE_CODE = 'ko'
TIME_ZONE = 'Asia/Seoul'
이렇게 수정해준다

views.py를 수정해본다

def signup(request):
    context-dict()
    if request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        
        if signup_form.isvalid():
            signup_form.save()
        else :
            context['signup_form'] = signup_form
    
            return render(request, 'signup.html',context)
            
    else : 
        signup_form = UserCreationForm()
            
        context['signup_form'] = signup_form
        
        return render(request, 'signup.html',context)


정상적으로 작동하는지 볼려면 index.html에

<h1>현재사용자 : {{USER}} <h1>

추가하면 됨

이제 login,logout을 만들면 됨

url에 쟝고에서 만들어둔 로그인 로그아웃 기능을 불러옴

from django.contrib.auth.views import LoginView,LogoutView

path('login/',LoginView.as_view(),name="login")
path('logout/',LogoutView.as_view(),name="logout")

이렇게 추가해 줌

class는 재사용이 쉽지만 직관적이지 않고 어렵다
def 함수는 재사용이 어렵지만 직관적이고 알아보기 쉽다

하지만 login은 LoginView 라고 앞글자가 대문자라서 눈치챘겠지만 Class로 이루어져있다.

그래서 이 부분은 Class로 지켜주자

보통은 templates에 html을 저장해두지만 login은 지정된 약속이 있기 때문에 registration 폴더를 만들어서 그 안에 login.html을 만들어준다.

settings.py에 가서

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

이렇게 설정해준다.
이걸 안해주면 기본 세팅은 쟝고에서 만든 프로필 페이지로 가라고 하는데 그 부분을 사용하지 않게 하기 위해서 넣은 부분
이렇게 해줘야 index로 이동함

로그인 안한 사람들에게 권한을 안주고 싶다면 우선 urls.py에

from django.contrib.auth.decorators import login_required

이렇게 설정해준다

그 다음 views.py에 권한이 필요한 설정 한줄 위에

@login_required

를 설정해준다

그리고 나서 urls.py에

    path('accounts/login/',LoginView.as_view(),name="login"),

이렇게 수정해주면 권한이 없는 페이지에 접근시 로그인화면으로 이동하게 된다

이거는 약속이기때문에 외우지 않기!!












class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': _('The two password fields didn’t match.'),
    }
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs['autofocus'] = True

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def _post_clean(self):
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get('password2')
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error('password2', error)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




class LoginView(SuccessURLAllowedHostsMixin, FormView):
    """
    Display the login form and handle the login action.
    """
    form_class = AuthenticationForm
    authentication_form = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/login.html'
    redirect_authenticated_user = False
    extra_context = None

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            redirect_to = self.get_success_url()
            if redirect_to == self.request.path:
                raise ValueError(
                    "Redirection loop for authenticated user detected. Check that "
                    "your LOGIN_REDIRECT_URL doesn't point to a login page."
                )
            return HttpResponseRedirect(redirect_to)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_redirect_url(self):
        """Return the user-originating redirect URL if it's safe."""
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        url_is_safe = url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts=self.get_success_url_allowed_hosts(),
            require_https=self.request.is_secure(),
        )
        return redirect_to if url_is_safe else ''

    def get_form_class(self):
        return self.authentication_form or self.form_class

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            self.redirect_field_name: self.get_redirect_url(),
            'site': current_site,
            'site_name': current_site.name,
            **(self.extra_context or {})
        })
        return context


class LogoutView(SuccessURLAllowedHostsMixin, TemplateView):
    """
    Log out the user and display the 'You are logged out' message.
    """
    next_page = None
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'registration/logged_out.html'
    extra_context = None

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        next_page = self.get_next_page()
        if next_page:
            # Redirect to this page until the session has been cleared.
            return HttpResponseRedirect(next_page)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        return self.get(request, *args, **kwargs)

    def get_next_page(self):
        if self.next_page is not None:
            next_page = resolve_url(self.next_page)
        elif settings.LOGOUT_REDIRECT_URL:
            next_page = resolve_url(settings.LOGOUT_REDIRECT_URL)
        else:
            next_page = self.next_page

        if (self.redirect_field_name in self.request.POST or
                self.redirect_field_name in self.request.GET):
            next_page = self.request.POST.get(
                self.redirect_field_name,
                self.request.GET.get(self.redirect_field_name)
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_page,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            # Security check -- Ensure the user-originating redirection URL is
            # safe.
            if not url_is_safe:
                next_page = self.request.path
        return next_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_site = get_current_site(self.request)
        context.update({
            'site': current_site,
            'site_name': current_site.name,
            'title': _('Logged out'),
            **(self.extra_context or {})
        })
        return context


def logout_then_login(request, login_url=None):
    """
    Log out the user if they are logged in. Then redirect to the login page.
    """
    login_url = resolve_url(login_url or settings.LOGIN_URL)
    return LogoutView.as_view(next_page=login_url)(request)


def redirect_to_login(next, login_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Redirect the user to the login page, passing the given 'next' page.
    """
    resolved_url = resolve_url(login_url or settings.LOGIN_URL)

    login_url_parts = list(urlparse(resolved_url))
    if redirect_field_name:
        querystring = QueryDict(login_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        login_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(login_url_parts))

