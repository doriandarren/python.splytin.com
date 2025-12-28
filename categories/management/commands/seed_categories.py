from django.core.management.base import BaseCommand
from categories.models import Category

## ------------------------
## Se ejecuta con: python3 manage.py seed_categories
## ------------------------

class Command(BaseCommand):
    help = "Seed initial categories"
    
    def handle(self, *args, **options):
        
        categories = [
            "Tecnology",
            "Entertainment",
            "Gaming",
            "Music",
            "Movies",
            "Books",
            "Food",
        ]
        
        for title in categories:
            Category.objects.get_or_create(title=title)
            
        self.stdout.write(self.style.SUCCESS("Categories created"))