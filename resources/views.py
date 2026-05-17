from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm, ResourceUploadForm, SignupForm, CommentForm
from .models import Resource, UserProfile, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def home(request):
    return render(request, 'home.html')



def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            UserProfile.objects.create(
                user=user,
                registration_number=form.cleaned_data['registration_number']
            )

            return redirect('home')

    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    error = None

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            reg_no = form.cleaned_data['registration_number']
            password = form.cleaned_data['password']

            try:
                profile = UserProfile.objects.get(
                    registration_number=reg_no
                )

                user = authenticate(
                    request,
                    username=profile.user.username,
                    password=password
                )

                if user is not None:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    error = "Invalid password"

            except UserProfile.DoesNotExist:
                error = "Registration number not found"

    else:
        form = LoginForm()

    return render(request, 'login.html', {
        'form': form,
        'error': error
    })

def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def upload_resource(request):
    if request.method == "POST":
        form = ResourceUploadForm(
            request.POST,
            request.FILES
        ) 
        if form.is_valid():
            resource = form.save(commit=False)
            resource.uploaded_by = request.user
            resource.is_approved = False
            resource.save()
            return redirect('dashboard')
    else:
        form = ResourceUploadForm()

    return render(request, 'upload.html', {
        'form': form
    })


@staff_member_required
def pending_resources(request):
    resources = Resource.objects.filter(
        is_approved=False
    )

    return render(request,
        'pending_resources.html',
        {'resources': resources}
    )

@staff_member_required
def approve_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    resource.is_approved = True
    resource.save()

    return redirect('pending_resources')

@staff_member_required
def delete_resource(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    resource.delete()

    return redirect('pending_resources')


def browse_resources(request):
    resources = Resource.objects.filter(
        is_approved=True
    )

    subject = request.GET.get('subject')
    resource_type = request.GET.get('resource_type')
    semester = request.GET.get('semester')

    if subject:
        resources = resources.filter(
            subject__icontains=subject
        )

    if resource_type:
        resources = resources.filter(
            resource_type=resource_type
        )

    if semester:
        resources = resources.filter(
            semester=semester
        )

    return render(request, 'browse.html', {
        'resources': resources
    })

@login_required
def resource_detail(request, resource_id):
    resource = Resource.objects.get(
        id=resource_id,
        is_approved=True
    )

    comments = Comment.objects.filter(
        resource=resource
    ).order_by('-created_at')

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.resource = resource
            comment.user = request.user
            comment.save()

            return redirect(
                'resource_detail',
                resource_id=resource.id
            )

    else:
        form = CommentForm()

    return render(
        request,
        'resource_detail.html',
        {
            'resource': resource,
            'comments': comments,
            'form': form
        }
    )


@login_required
def my_uploads(request):
    resources = Resource.objects.filter(
        uploaded_by=request.user
    ).order_by('-upload_date')

    return render(
        request,
        'my_uploads.html',
        {'resources': resources}
    )

@login_required
def profile_view(request):
    user = request.user

    profile = UserProfile.objects.get(
        user=user
    )

    total_uploads = Resource.objects.filter(
        uploaded_by=user
    ).count()

    approved_uploads = Resource.objects.filter(
        uploaded_by=user,
        is_approved=True
    ).count()

    pending_uploads = Resource.objects.filter(
        uploaded_by=user,
        is_approved=False
    ).count()

    return render(
        request,
        'profile.html',
        {
            'profile': profile,
            'total_uploads': total_uploads,
            'approved_uploads': approved_uploads,
            'pending_uploads': pending_uploads,
        }
    )