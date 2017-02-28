from django.shortcuts import render
from django.http import HttpResponse
from wandr.forms import UserForm, UserProfile

# Create your views here.
def index(request):
	return render(request,'wandr/index.html')


def register(request):
	registered = False
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

				registered = True

			else:
				print(user_form.errors, profile_forms.errors)
		else:
			user_form = UserForm()
			profile_form = UserProfileForm()
	return render( request, 'wandr/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})