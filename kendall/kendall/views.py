from django.views.generic import TemplateView

CARDS = [
    {
        'icon': 'room',
        'title': 'Simplicité',
        'content': 'Trouvez tous les produits locaux que vous aimez en un seul endroit'
    },
    {
        'icon': 'store',
        'title': 'Rapidité',
        'content': 'Livraison rapide dans toute la métropole lilloise'
    },
    {
        'icon': 'airplanemode_active',
        'title': 'Economie',
        'content': 'Gagnez du temps et achetez à moindre coût sur notre plateforme'
    }
]

class Home(TemplateView):
    template_name = 'home/hero.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cards'] = CARDS
        return context