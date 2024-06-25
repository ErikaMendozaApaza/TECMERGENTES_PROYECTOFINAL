from django.urls import path
from adminapp.views import *

urlpatterns = [
    path('admin/dashboard', adminHome, name='adminHome'),

    # URL del blog de administración
    path('admin/blogs', adminBlogList, name='adminBlogList'),
    path('admin/blog/create', adminBlogCreate, name='adminBlogCreate'),
    path('admin/blog/edit/<slug:slug>', adminBlogEdit, name='adminBlogEdit'),
    path('admin/blog/delete/<int:id>', adminBlogDelete, name='adminBlogDelete'),

    # URL de categoría del blog de administración
    path('admin/blog-category', adminBlogCategoryList, name='adminBlogCategoryList'),
    path('admin/blog-category/create', adminBlogCategoryCreate, name='adminBlogCategoryCreate'),
    path('admin/blog-category/edit/<slug:slug>', adminBlogCategoryEdit, name='adminBlogCategoryEdit'),
    path('admin/blog-category/delete/<int:id>', adminBlogCategoryDelete, name='adminBlogCategoryDelete'),

    # URL del proyecto de administración
    path('admin/projects', adminProjectList, name='adminProjectList'),
    path('admin/project/create', adminProjectCreate, name='adminProjectCreate'),
    path('admin/project/edit/<slug:slug>', adminProjectEdit, name='adminProjectEdit'),
    path('admin/project/delete/<int:id>', adminProjectDelete, name='adminProjectDelete'),

    # URL de categoría de proyecto de administración
    path('admin/project-category', adminProjectCategoryList, name='adminProjectCategoryList'),
    path('admin/project-category/create', adminProjectCategoryCreate, name='adminProjectCategoryCreate'),
    path('admin/project-category/edit/<slug:slug>', adminProjectCategoryEdit, name='adminProjectCategoryEdit'),
    path('admin/project-category/delete/<int:id>', adminProjectCategoryDelete, name='adminProjectCategoryDelete'),

    # URL del servicio de administración
    path('admin/services', adminServiceList, name='adminServiceList'),
    path('admin/service/create', adminServiceCreate, name='adminServiceCreate'),
    path('admin/service/edit/<slug:slug>', adminServiceEdit, name='adminServiceEdit'),
    path('admin/service/delete/<int:id>', adminServiceDelete, name='adminServiceDelete'),

    # URL del elemento deslizante de administración
    path('admin/element/sliders', adminSliderElementList, name='adminSliderElementList'),
    path('admin/element/slider/create', adminSliderElementCreate, name='adminSliderElementCreate'),
    path('admin/element/slider/edit/<int:id>', adminSliderElementEdit, name='adminSliderElementEdit'),
    path('admin/element/slider/delete/<int:id>', adminSliderElementDelete, name='adminSliderElementDelete'),

    # URL de elementos curiosos del administrador
    path('admin/element/fun-facts', adminFunFactElementList, name='adminFunFactElementList'),
    path('admin/element/fun-fact/create', adminFunFactElementCreate, name='adminFunFactElementCreate'),
    path('admin/element/fun-fact/edit/<int:id>', adminFunFactElementEdit, name='adminFunFactElementEdit'),
    path('admin/element/fun-fact/delete/<int:id>', adminFunFactElementDelete, name='adminFunFactElementDelete'),

    # URL del elemento de testimonio del administrador
    path('admin/element/testimonials', adminTestimonialsElementList, name='adminTestimonialsElementList'),
    path('admin/element/testimonial/create', adminTestimonialsElementCreate, name='adminTestimonialsElementCreate'),
    path('admin/element/testimonial/edit/<int:id>', adminTestimonialsElementEdit, name='adminTestimonialsElementEdit'),
    path('admin/element/testimonial/delete/<int:id>', adminTestimonialsElementDelete, name='adminTestimonialsElementDelete'),

    # URL de elementos del equipo de administración
    path('admin/element/teams', adminTeamElementList, name='adminTeamElementList'),
    path('admin/element/team/create', adminTeamElementCreate, name='adminTeamElementCreate'),
    path('admin/element/team/edit/<int:id>', adminTeamElementEdit, name='adminTeamElementEdit'),
    path('admin/element/team/delete/<int:id>', adminTeamElementDelete, name='adminTeamElementDelete'),

    # URL de elementos de cliente de administración
    path('admin/element/clients', adminClientElementList, name='adminClientElementList'),
    path('admin/element/client/create', adminClientElementCreate, name='adminClientElementCreate'),
    path('admin/element/client/edit/<int:id>', adminClientElementEdit, name='adminClientElementEdit'),
    path('admin/element/client/delete/<int:id>', adminClientElementDelete, name='adminClientElementDelete'),

    # URL de elementos de precios de administrador
    path('admin/element/pricings', adminPricingElementList, name='adminPricingElementList'),
    path('admin/element/pricing/create', adminPricingElementCreate, name='adminPricingElementCreate'),
    path('admin/element/pricing/edit/<int:id>', adminPricingElementEdit, name='adminPricingElementEdit'),
    path('admin/element/pricing/delete/<int:id>', adminPricingElementDelete, name='adminPricingElementDelete'),

    # URL de contacto del administrador
    path('admin/contacts', AdminContactList, name='AdminContactList'),
    path('admin/contact/delete/<int:id>', AdminContactDelete, name='AdminContactDelete'),

    # URL del suscriptor administrador
    path('admin/subscribers', AdminSubscriberList, name='AdminSubscriberList'),
    path('admin/subscriber/delete/<int:id>', AdminSubscriberDelete, name='AdminSubscriberDelete'),

    # URL de configuración de administrador
    path('admin/settings/website-settings', AdminWebsiteSettings, name='AdminWebsiteSettings'),
    path('admin/settings/header-footer', AdminHeaderFooterSettings, name='AdminHeaderFooterSettings'),
    path('admin/settings/seo', AdminSEOSettings, name='AdminSEOSettings'),

    # URL del menú principal de administrador
    path('admin/menus/primary-menu', AdminPrimaryMenuList, name='AdminPrimaryMenuList'),
    path('admin/primary-menu/create', AdminPrimaryMenuCreate, name='AdminPrimaryMenuCreate'),
    path('admin/primary-menu/edit/<int:id>', AdminPrimaryMenuEdit, name='AdminPrimaryMenuEdit'),
    path('admin/primary-menu/delete/<int:id>', AdminPrimaryMenuDelete, name='AdminPrimaryMenuDelete'),

    # URL del submenú de administración
    path('admin/menus/sub-menu', AdminSubMenuList, name='AdminSubMenuList'),
    path('admin/sub-menu/create', AdminSubMenuCreate, name='AdminSubMenuCreate'),
    path('admin/sub-menu/edit/<int:id>', AdminSubMenuEdit, name='AdminSubMenuEdit'),
    path('admin/sub-menu/delete/<int:id>', AdminSubMenuDelete, name='AdminSubMenuDelete'),

    # URL de páginas de administración
    path('admin/pages/home-page', AdminHomePage, name='AdminHomePage'),
    path('admin/pages/about-page', AdminAboutPage, name='AdminAboutPage'),
    path('admin/pages/service-page', AdminServicePage, name='AdminServicePage'),
    path('admin/pages/project-page', AdminProjectPage, name='AdminProjectPage'),
    path('admin/pages/pricing-page', AdminPricingPage, name='AdminPricingPage'),
    path('admin/pages/contact-page', AdminContactPage, name='AdminContactPage'),
    path('admin/pages/terms-page', AdminTermsPage, name='AdminTermsPage'),
    path('admin/pages/policy-page', AdminPolicyPage, name='AdminPolicyPage'),
]