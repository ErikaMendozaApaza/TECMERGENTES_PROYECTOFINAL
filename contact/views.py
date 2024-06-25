from django.shortcuts import render, redirect, get_object_or_404
from contact.models import *
from contact.forms import *
from django.utils import timezone
from datetime import datetime
from django.http import JsonResponse

# # # # # # # # # # # # # # # # # #
#Portada de la página de contacto #
# # # # # # # # # # # # # # # # # #
def contactPageFront(request):
    seo = contactPageSEO.objects.first()

    context = {
        'seo' : seo,
    }
    return render(request, 'front/main/contact.html', context)

# # # # # # # # # # # # # # # # # #
#       Contacto Enviar           #
# # # # # # # # # # # # # # # # # #
def ContactSubmit(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Compruebe si hay una variable de sesión para la hora del último envío
        last_submission_time_str = request.session.get('last_contact_submission_time')

        if last_submission_time_str:
            # Volver a convertir la cadena de tiempo almacenada en un objeto de fecha y hora
            last_submission_time = datetime.fromisoformat(last_submission_time_str)

            # Calcular la diferencia de tiempo entre el último envío y la hora actual
            time_difference = timezone.now() - last_submission_time

            # Compruebe si han pasado menos de cinco minutos desde el último envío
            if time_difference.total_seconds() < 300:  # 300 seconds = 5 minutes
                # Calculate the time left for the next submission
                time_left_seconds = 300 - time_difference.total_seconds()
                minutes_left = int(time_left_seconds / 60)
                seconds_left = int(time_left_seconds % 60)

                return JsonResponse({'status': 'error', 'message': f'You can submit again in {minutes_left} minutes and {seconds_left} seconds.'})

        # Guarde la hora actual en la sesión como una cadena en formato ISO 8601
        request.session['last_contact_submission_time'] = timezone.now().isoformat()

        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': '¡Formulario de contacto enviado con éxito! Nos pondremos en contacto con usted pronto.'})
        else:
            return JsonResponse({'status': 'error', 'message': '¡Envío no válido! Vuelve a intentarlo.'})

    return JsonResponse({'status': 'error', 'message': '¡Método no válido o no es una solicitud AJAX!'})

# # # # # # # # # # # # # # # # # #
#   Envío de suscriptor           #
# # # # # # # # # # # # # # # # # #        
def SubscriberSubmit(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        email = request.POST.get('email') 
        
        # Compruebe si el correo electrónico ya existe en la base de datos
        if Subscriber.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'Email already exists!'})
        
        # Compruebe si hay una variable de sesión para la hora del último envío
        last_submission_time_str = request.session.get('last_submission_time')
        
        if last_submission_time_str:
            # Volver a convertir la cadena de tiempo almacenada en un objeto de fecha y hora
            last_submission_time = datetime.fromisoformat(last_submission_time_str)
            
            # Calcular la diferencia de tiempo entre el último envío y la hora actual
            time_difference = timezone.now() - last_submission_time
            
            # Compruebe si han pasado menos de cinco minutos desde el último envío
            if time_difference.total_seconds() < 300:  # 300 seconds = 5 minutes
                # Calculate the time left for the next submission
                time_left_seconds = 300 - time_difference.total_seconds()
                minutes_left = int(time_left_seconds / 60)
                seconds_left = int(time_left_seconds % 60)
                
                return JsonResponse({'status': 'error', 'message': f'You can submit again in {minutes_left} minutes and {seconds_left} seconds.'})
        
        # Guarde la hora actual en la sesión como una cadena en formato ISO 8601
        request.session['last_submission_time'] = timezone.now().isoformat()
        
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Subscribed successfully!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid email!'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid method or not an AJAX request!'})

def error_404(request, exception):
    return render(request, 'error/404.html', status=404)