from django.shortcuts import render
from .models import Pizza, Topping
from pizzas.forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
 
 
def index(request):
    """
    The home page for pizzas
    """
    return render(request, "pizzas/index.html")

def pizzas(request):
    """
    """
    pizza = Pizza.objects.all()
    context = {"Pizza" : pizza}
    return render(request, 'pizzas/pizzas.html', context)
    #return context
    

def topping(request):
    '''
    Show all topping.
    '''
    topping = Topping.objects.all()
    context = {"Topping" : topping}
    return render(request,"pizzas/topping.html", context)

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

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)
            
            email = EmailMessage(
                "New contact form submission",
                "Your website" +'',
                content,
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
            
    context = {'form': form_class}
    return render(request, 'pizzas/contact.html', context)


                        
@login_required
def order(request):
    context = { }
    return render(request, 'pizzas/order.html', context)
