from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from .forms import ContactForm
from wandr.forms import UserForm, UserProfileForm, PictureForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from registration.backends.simple.views import RegistrationView
from .models import User, HaveBeenList, Picture

# needed for the contact form email setup
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def index(request):
    picture_list = Picture.objects.order_by('likes')
    context_dict = {'pictures': picture_list}
    return render(request, 'wandr/index.html', context=context_dict)


# register view added by Cristina 28.02.
def register(request):
    registered = False

    # If it's a HTTP POST, process form data
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

                profile.save()


        else:
            print(user_form.errors, profile_form.errors)

        registered = True

    # Not a HTTP POST request so input is blank
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'wandr/register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


# Created 01.03
def user_login(request):
    # If POST
    if request.method == 'POST':
        # Get username and password
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            # If account is valid and active
            if user.is_active:
                login(request, user)
                # return user to homepage
                return HttpResponseRedirect(reverse('index'))
            else:
                # Account is inactive
                return HttpResponse("Your Wandr account is disabled.")
        else:
            # Wrong details used
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # If not POST
    else:
        return render(request, 'wandr/login.html', {})


# Created 01.03
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Created 02.03. Cristina
def about(request):
    return render(request, 'wandr/about.html')

# created 08.03. Cynthia; email does not get sent
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('wandr/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Wandr" +'',
                ['2275765L@student.gla.ac.uk'],
                headers = {'Reply-To': contact_email }
            )
            email.send(fail_silently=False)
            return redirect('contact')

    return render(request, 'wandr/contact.html', {
        'form': form_class,
    })

# created 02.03. Cynthia
def add_picture(request):
	# form = PictureForm()

	# if request.method == 'POST':
	# 	form = PictureForm(request.POST)

	# 	if form.is_valid():
	# 		form.save(commit = True)
	# 		return index(request)
	# 	else:
	# 		print(form.errors)
	# return render(request, 'wandr/add_picture.html', {'form' : form})

    if request.method == 'POST':
        picture_form = PictureForm(request.POST, request.FILES)
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            picture.save()
        else:
            print(picture_form.errors)

    picture_form = PictureForm()

    return render(request, 'wandr/add_picture.html', {'picture_form':picture_form})

# Redirect after successful login - Cristina 04.03.
#class MyRegistrationView(RegistrationView):
#    def get_success_url(self, user):
#        return '/wandr/'

# Registration - redirect user to index after registration 04.03 Cristina
class WandrRegistrationView(RegistrationView):
   def get_success_url(self, user):
        return reverse('index')


def user_profile_view(request, user_id):
    try:
        u = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User Does Not Exist")

    have_been_list = HaveBeenList.objects.get(belongs_to=user_id)
    context_dict = {
        'hbl': have_been_list,
        'user': u,
    }
    return render(request, 'wandr/user_profile.html', context_dict)