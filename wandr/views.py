from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from .forms import ContactForm
from wandr.forms import UserForm, ProfilePictureForm, PictureForm, CoverPhotoForm, BioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from registration.backends.simple.views import RegistrationView
from .models import User, HaveBeenList, Picture, UserProfile, ToGoList

# needed for the contact form email setup
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def index(request):
    picture_list = Picture.objects.order_by('likes')
    user_id = request.user.pk
    context_dict = {'pictures': picture_list, 'user_id': user_id}

    return render(request, 'wandr/index.html', context=context_dict)


# register view added by Cristina 28.02.
def register(request):
    registered = False

    # If it's a HTTP POST, process form data
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            registered = True
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
            # If account is valid and active
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)

    # Not a HTTP POST request so input is blank
    else:
        user_form = UserForm()

    return render(request, 'wandr/register.html',
                  {'user_form': user_form, 'registered': registered})


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


@login_required
def add_to_tgl(request, user_id, picture_id):
    this_user = request.user
    tgl = ToGoList.objects.get(belongs_to=this_user)
    hbl_user = User.objects.get(pk=user_id)
    hbl = HaveBeenList.objects.get(belongs_to=hbl_user)

    print 'tgl id is ' + str(tgl.pk)
    picture = Picture.objects.get(pk=picture_id)
    picture.to_go_list.add(tgl)
    picture.save()
    tgl.save()

    print 'picture id is ' + str(picture_id)

    return HttpResponseRedirect(reverse('user_profile', args=[user_id]))


@login_required
def remove_from_tgl(request, user_id, picture_id):
    this_user = request.user
    tgl = ToGoList.objects.get(belongs_to=this_user)
    hbl_user = User.objects.get(pk=user_id)
    hbl = HaveBeenList.objects.get(belongs_to=hbl_user)

    print 'tgl id is ' + str(tgl.pk)
    picture = Picture.objects.get(pk=picture_id)
    picture.to_go_list.remove(tgl)
    picture.save()
    tgl.save()

    print 'picture id is ' + str(picture_id)

    return HttpResponseRedirect(reverse('user_profile', args=[user_id]))


@login_required
def remove_from_hbl(request, user_id, picture_id):
    this_user = request.user
    # tgl = ToGoList.objects.get(belongs_to=this_user)
    hbl_user = User.objects.get(pk=user_id)
    hbl = HaveBeenList.objects.get(belongs_to=hbl_user)

    picture = Picture.objects.get(pk=picture_id)
    picture.delete()

    print 'picture id is ' + str(picture_id)

    return HttpResponseRedirect(reverse('user_profile', args=[user_id]))


@login_required
# def upload_profile_picture(request, user_id):
def upload_profile_picture(request, user_id):
    # user_profile = UserProfile.objects.get(user=request.user)
    # uploaded = False
    # form = ProfilePictureForm(initial={'picture':user_profile.picture})

    if request.method == 'POST':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        form = ProfilePictureForm(data=request.POST, instance=profile)

        # def get_object(self, queryset=None):
        #     return UserProfile.objects.get(user=self.request.user)

        if form.is_valid():
            page = form.save(commit=False)
            if 'picture' in request.FILES:
                page.picture = request.FILES['picture']
            # user = request.user
            # profile = UserProfile.objects.get(user=user)
            # profile.picture = page.picture
            # profile.picture = page.cleaned_data['picture']
            # picture = form.cleaned_data['picture']
            # profile.picture = picture
            profile.save()

            return HttpResponseRedirect(reverse('user_profile', args=[user_id]))

        else:
            print(form.errors)

        uploaded = True

    else:
        user = request.user
        profile = UserProfile.objects.get(user=user)
        form = ProfilePictureForm(instance=profile)

    return render(request, 'wandr/upload_profile_picture.html',
                  {'profile_picture_form': form, 'user_id': user_id})


@login_required
def like_picture(request, user_id, picture_id):
    if request.method == 'GET':
        if picture_id:
            pic = Picture.objects.get(picture_id=int(picture_id))
            if pic:
                likes = pic.likes + 1
                pic.likes = likes
                pic.save()
    return HttpResponseRedirect(reverse('user_profile', args=[user_id]))


@login_required
def upload_cover_photo(request, user_id):
    if request.method == 'POST':
        user = request.user
        profile = UserProfile.objects.get(user=user)
        form = CoverPhotoForm(data=request.POST, instance=profile)

        if form.is_valid():
            page = form.save(commit=False)
            if 'cover_photo' in request.FILES:
                page.cover_photo = request.FILES['cover_photo']

            profile.save()

            return HttpResponseRedirect(reverse('user_profile', args=[user_id]))

        else:
            print(form.errors)

    else:
        user = request.user
        profile = UserProfile.objects.get(user=user)
        form = CoverPhotoForm(instance=profile)

    return render(request, 'wandr/upload_cover_photo.html',
                  {'cover_photo_form': form, 'user_id': user_id})


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

def add_picture_success(request):
	return render(request, 'wandr/add_picture_success.html')

@login_required
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
        user_id = request.user.pk
        if picture_form.is_valid():
            picture = picture_form.save(commit=False)
            picture.have_been_list = HaveBeenList.objects.get(belongs_to=user_id)
            picture.save()

            #return HttpResponseRedirect(reverse('user_profile', args=[user_id]))
            return HttpResponseRedirect(reverse('add_picture_success'))
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


@login_required
def user_profile_view(request, user_id):
    try:
        u = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User Does Not Exist")

    if u == request.user:
        this_user = True
    else:
        this_user = False

    to_go_list = ToGoList.objects.get(belongs_to=user_id)
    have_been_list = HaveBeenList.objects.get(belongs_to=user_id)
    context_dict = {
        'hbl': have_been_list,
        'user': u,
        'this_user': this_user,
        'tgl': to_go_list,
    }
    return render(request, 'wandr/user_profile.html', context_dict)


@login_required
def update_profile(request, user_id):
    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():
            userProfile = UserProfile.objects.get(user=request.user)
            bio = form.cleaned_data['bio']
            userProfile.bio = bio
            userProfile.save()
            return HttpResponseRedirect(reverse('user_profile', args=[user_id]))

    else:

        userProfile = UserProfile.objects.get ( pk=user_id )
        form = BioForm ( initial={'bio': userProfile.bio} )
        return render ( request, 'wandr/update_profile.html', {'form': form, 'user_id': user_id})