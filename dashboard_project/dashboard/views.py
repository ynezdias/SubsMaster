from django.shortcuts import render
from django.utils import timezone
from .models import Usermaster,Subscription
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timedelta
from django.db.models import Count
from django.utils import timezone
from django.db.models import Q
from django.shortcuts import get_object_or_404
from datetime import date

'''def dashboard(request):
    return render(request, 'dashboard/dashboard.html')'''
#expiring_soon_users=0


def dashboard(request):
    today = timezone.now().date()
    #n=expiry_date__lt=timezone.now() + timezone.timedelta(days=30)
    active_users_count = Usermaster.objects.filter(status='active').count()
    expiring_users_count = Usermaster.objects.filter(Q(status='active') | Q(status='inactive'), expiry_date__gte=timezone.now()).count()
    inactive_users_count = Usermaster.objects.filter(status='inactive').count()
    expired_users_count = Usermaster.objects.filter(status='inactive',expiry_date__lte=timezone.now()).count()

    context = {
        'active_users_count': active_users_count,
       'expiring_users_count': expiring_users_count,
        'inactive_users_count': inactive_users_count,
        'expired_users_count': expired_users_count,
    }

    return render(request, 'dashboard/dashboard.html' ,context)


def active_users(request):
    thirty_days_ago = timezone.now() - timedelta(days=30)
    active_users = Usermaster.objects.filter(status='active', activation_date__lt=thirty_days_ago)
    users = []
    for user in active_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user_id': user.user_id,
            'username': user.username,
            'activation_date': user.activation_date,
            'expiry_date': user.expiry_date,
            'status': user.status,
        })
    context = {
        'users': users,
    }
    return render(request, 'dashboard/active_users.html', context)


# active_users = User.objects.filter(is_active=True)
#active_users = User.objects.filter(date_joined__gte=thirty_days_ago)

def inactive_users(request):
    # Retrieve users with expiry date in the past
    today = timezone.now().date()
    
    inactive_users = Usermaster.objects.filter(status='inactive')
    
    context = {
        'users': inactive_users,
        'menu': 'Inactive Users'
    }
    return render(request, 'dashboard/inactive_users.html', context)


def expiring_soon(request):
    today = timezone.now().date()
    next_month = today.replace(day=30) + timedelta(days=15)
    
    expiring_users = Usermaster.objects.all()
    users = []
    for user in expiring_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        if today <= expiry_date <= next_month:
            users.append({
                'user': user,
                'username': user.username,
                'f_name': user.f_name,
                'l_name': user.l_name,
                'user_id': user.user_id,
                'expiry_date': user.expiry_date,
                'last_login': user.last_login,
            })

    context = {
        'users': users,
        'menu': 'Expiring Soon'
    }
    return render(request, 'dashboard/expiring_soon.html', context)
 

def extend_subscription(request, user_id):
    if request.method == 'POST':
        # Get the form data from the POST request
        months = int(request.POST.get('months'))
        years = int(request.POST.get('years'))
        
        user = get_object_or_404(Usermaster, user_id=user_id)
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        
        # Calculate the new expiry date based on the selected months and years
        total_days = 30 * months + 365 * years
        new_expiry_date = expiry_date + timedelta(days=total_days)
        
        # Update the user's expiry date and save the changes
        user.expiry_date = new_expiry_date.strftime('%d/%m/%y')
        user.save()
        
        return redirect('expiring_soon')  # Redirect to the appropriate page after extension

    # Render the extend_subscription.html template
    context = {'user_id': user_id}
    return render(request, 'dashboard/extend_subscription.html', context)



def expired_users(request):
    today = timezone.now().date()
    expired_users = Usermaster.objects.filter(expiry_date__lte=today)
    users = []
    for user in expired_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        if expiry_date.year < today.year or (expiry_date.year == today.year and expiry_date < today):
            users.append({
                'user_id': user.user_id,
                'username': user.username,
                'expiry_date': user.expiry_date,
                'is_active': user.is_active,
            })
    context = {
        'users': users,
        'menu': 'Expired Users',
    }
    return render(request, 'dashboard/expired_users.html', context)



def activate_deactivate_user(request, user_id):
    user = get_object_or_404(Usermaster, user_id=user_id)
    user.is_active = not user.is_active
    if user.is_active:
        user.activation_date = date.today()  # Set activation date to today's date
    else:
        user.activation_date = None  # Reset activation date if deactivated
    user.save()

    # Convert the is_active field to 'Yes' or 'No' before creating the JSON response
    is_active_display = 'Yes' if user.is_active else 'No'
    print(is_active_display)

    activation_date_formatted = user.activation_date.strftime('%d/%m/%Y') if user.activation_date else None

    return JsonResponse({
        'status': 'success',
        'activation_date': activation_date_formatted,
        'is_active': is_active_display  # Display 'Yes' or 'No' in the JSON response
    })


def temp_view(request):
    
    pass


''' 


def expired_users(request):
    today = timezone.now().date()
    expired_users = Usermaster.objects.filter(expiry_date__lte=today)
    users = []
    for user in expired_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        if expiry_date.year < today.year or (expiry_date.year == today.year and expiry_date < today):
            users.append({
                
                'user_id': user.user_id,
                'username': user.username,
                'expiry_date': expiry_date,
            })
    context = {
        'users': users,
        'menu': 'Expired Users',
    }
    return render(request, 'dashboard/expired_users.html', context)


def activate_deactivate_user(request, user_id):
    user = get_object_or_404(Usermaster, user_id=user_id)
    user.is_active = not user.is_active
    if user.is_active:
        user.activation_date = date.today()  # Set activation date to today's date
    user.save()
    return JsonResponse({'status': 'success'})'''



    # Redirect or render a success message
    
'''def activate_deactivate_user(request, user_id):
    user = get_object_or_404(Usermaster, id=user_id)
    user.is_active = not user.is_active
    user.save()'''
    
    # Redirect or render a success message

    #expired_users_count = Usermaster.objects.filter(Q(status='active') | Q(status='inactive'), expiry_date__lte=timezone.now()).count()
    # expiring_users_count = Usermaster.objects.filter(status='active',expiry_date__gt=timezone.now()).count()
'''from django.shortcuts import render
from django.views import View
from django.db.models import Count
from datetime import date, timedelta
from .models import Usermaster, Subscription
from django.utils import timezone
from datetime import timedelta


    if request.method == 'POST':
        username = request.POST.get('username')
        activation_date = request.POST.get('activation_date')
        expiry_date = request.POST.get('expiry_date')
        today = timezone.now()
from django.http import HttpResponse

def active_users(request):
    users = [
        {'username': 'User1', 'date_joined': '2022-01-01', 'subscription_expiry_date': '2022-12-31'},
        {'username': 'User2', 'date_joined': '2022-02-01', 'subscription_expiry_date': '2022-11-30'},
    ]
    table_data = '\n'.join([f"<tr><td>{user['username']}</td><td>{user['date_joined']}</td><td>{user['subscription_expiry_date']}</td></tr>" for user in users])
    html = f"<table>{table_data}</table>"
    return HttpResponse(html)

def expired_users(request):
    today = timezone.now().date()
    expired_users = Usermaster.objects.filter(expiry_date__lte=today)
    users = []
    for user in expired_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user': user,
            'username': user.username,
            'user_id': user.user_id,
            'expiry_date': expiry_date,
        })
    context = {
        'users': users,
        'menu': 'Expired Users'
    }
    return render(request, 'dashboard/expired_users.html', context)
class DashboardView(View):
    def get(self, request):
        # Calculate the date range for the last 30 days
        today = date.today()
        start_date = today - timedelta(days=30)
        end_date = today

        # Get the counts of active users, expiring soon, inactive users, and expired users
        active_users_count = Usermaster.objects.filter(status='active', activation_date__gte=timezone.now() - timedelta(days=30)).count()
        expiring_soon_count = Usermaster.objects.filter(expiry_date__gte=timezone.now(), expiry_date__lte=timezone.now() + timedelta(days=30)).count()
        inactive_users_count = Usermaster.objects.filter(status='inactive', last_login__lt=timezone.now() - timedelta(days=30)).count()
        expired_users_count = Usermaster.objects.filter(expiry_date__lt=timezone.now()).count()

        context = {
            'active_users_count': active_users_count,
            'expiring_soon_count': expiring_soon_count,
            'inactive_users_count': inactive_users_count,
            'expired_users_count': expired_users_count
        }

        return render(request, 'dashboard/dashboard.html', context)
def active_users(request):
    active_users  = Usermaster.objects.all()
    active_users_count = Usermaster.objects.filter(status='active', activation_date__gte=timezone.now())
    context = {
        'users': active_users,
        #'menu': 'Active Users'
        'active_users_count': active_users_count,
    }
    return render(request, 'dashboard/active_users.html', context)

def active_users(request):
    month_param = request.GET.get('month', 1)
    current_month = timezone.now().date()
    start_date = current_month - timedelta(days=30 * int(month_param))
    
    active_users = Usermaster.objects.filter(is_active=True, activation_date__gte=start_date)
    context = {
        'active_users': active_users
    }
    return render(request, 'dashboard/active_users.html', context)'''




# views.py
'''from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

def dashboard(request):
    # Calculate the counts
    active_users_count = User.objects.filter(status='active', last_login__gte=timezone.now() - timedelta(days=30)).count()
    expiring_soon_count = User.objects.filter(expiry_date__gte=timezone.now(), expiry_date__lte=timezone.now() + timedelta(days=30)).count()
    inactive_users_count = User.objects.filter(status='inactive', last_login__lt=timezone.now() - timedelta(days=30)).count()
    expired_users_count = User.objects.filter(expiry_date__lt=timezone.now()).count()

    context = {
        'active_users_count': active_users_count,
        'expiring_soon_count': expiring_soon_count,
        'inactive_users_count': inactive_users_count,
        'expired_users_count': expired_users_count,
    }
    return render(request, 'dashboard/dashboard.html', context)

def active_users(request):
    month_param = request.GET.get('month', 1)
    current_month = timezone.now().date()
    start_date = current_month - timedelta(days=30 * int(month_param))
    
    active_users = User.objects.filter(status='active', last_login__gte=start_date)
    context = {
        'active_users': active_users
    }
    return render(request, 'dashboard/active_users.html', context)'''

# Similar modifications for other views (expiring_soon, inactive_users, expired_users)
'''def expired_users(request):
    today = timezone.now().date()
    thirty_days_ago = today - timezone.timedelta(days=30)
    expired_users = Usermaster.objects.filter(expiry_date__range=[thirty_days_ago, today])
    users = []
    for user in expired_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user': user,
            'expiry_date': expiry_date,
        })
    context = {
        'users': users,
        'menu': 'Expired Users'
    }
    return render(request, 'dashboard/expired_users.html', context)'''
    #expiring_soon = Usermaster.objects.count()
    #next_month = today.replace(day=28) + timezone.timedelta(days=4)
    #expiring_users_count = Usermaster.objects.filter(status='active',expiry_date__range=[today, next_month]).count(

'''def expiring_soon(request):
    today = timezone.now().date()
    seven_days_from_now = today + timezone.timedelta(days=7)
    expiring_users = Usermaster.objects.filter(expiry_date__range=[today, seven_days_from_now])
    users = []
    for user in expiring_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user': user,
            'username': user.username,
            'f_name':user.f_name,
            'l_name':user.l_name,
            'user_id': user.user_id,
            'expiry_date': expiry_date,
            'last_login': user.last_login,
        })
    context = {
        'users': users,
        'menu': 'Expiring Soon'
    }
    return render(request, 'dashboard/expiring_soon.html', context)'''



'''def inactive_users(request):
    today = timezone.now().date()
    #thirty_days_ago = today - timezone.timedelta(days=30)
    inactive_users = Usermaster.objects.filter( activation_date__lt=today)
    #inactive_users = Usermaster.objects.filter(status='inactive', activation_date__range=[thirty_days_ago, today])
    users = []
    for user in inactive_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user': user,
            'user_id': user.user_id,
            'username': user.username,
            'activation_date': user.activation_date,
            'expiry_date': expiry_date,

        })
    context = {
        'users': users,
        'menu': 'Inactive Users'
    }
    return render(request, 'dashboard/inactive_users.html', context)'''

'''def expiring_soon(request):
    today = timezone.now().date()
    seven_days_from_now = today + timezone.timedelta(days=7)
    expiring_users = Usermaster.objects.filter(expiry_date__lte=seven_days_from_now)
    users = []
    for user in expiring_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user': user,
            'username': user.username,
            'f_name':user.f_name,
            'l_name':user.l_name,
            'user_id': user.user_id,
            'expiry_date': expiry_date,
            'last_login': user.last_login,
        })
    context = {
        'users': users,
        'menu': 'Expiring Soon'
    }
    return render(request, 'dashboard/expiring_soon.html', context) '''  

'''def active_users(request):
    active_users = Usermaster.objects.filter(status='active', activation_date__gte=timezone.now())
    users = []
    for user in active_users:
        expiry_date = datetime.strptime(user.expiry_date, '%d/%m/%y').date()
        users.append({
            'user': user,
            'expiry_date': expiry_date,
            'username': user.username,
            'user_id': user.user_id,
            'activation_date': user.activation_date,
            'status':user.status,
        })
    context = {
        'users': users,
    }
    return render(request, 'dashboard/active_users.html', context)'''