from django.contrib import admin
from home.models import *

# Registro de administrador de controles deslizantes
admin.site.register(sliderSection)

# Registro de administrador de servicios
admin.site.register(serviceSection)

# Acerca del registro de administrador
admin.site.register(aboutSection)

# Registro de administrador de Funfact
admin.site.register(funFactSection)

# Registro de administrador de sección y categoría de proyecto
admin.site.register(projectCategory)
admin.site.register(projectSection)

# Registro de administrador de clientes
admin.site.register(clientSection)

# Registro de administrador de testimonios
admin.site.register(testimonialsSection)

# Página de inicio Administrador SEO Registrarse
admin.site.register(homePageSEO)