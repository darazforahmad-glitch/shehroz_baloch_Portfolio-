from django.urls import path

from portfolio import views

handler404 = "portfolio.views.page_not_found"
handler500 = "portfolio.views.server_error"

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    path("resume/", views.resume, name="resume"),
    path("robots.txt", views.robots_txt, name="robots"),
    path("sitemap.xml", views.sitemap_xml, name="sitemap"),
    path("healthz", views.healthz, name="healthz"),
]
