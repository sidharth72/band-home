from django.core.management.base import BaseCommand
from django.urls import get_resolver


class Command(BaseCommand):
    help = 'Display all URLs in the Django project.'

    def handle(self, *args, **options):
        url_patterns = get_resolver().url_patterns
        urls = []

        def traverse_patterns(patterns, prefix=''):
            for pattern in patterns:
                if hasattr(pattern, 'url_patterns'):  # If the pattern contains nested patterns
                    traverse_patterns(pattern.url_patterns, prefix + pattern.pattern.regex.pattern)
                else:
                    urls.append(prefix + pattern.pattern.regex.pattern)

        traverse_patterns(url_patterns)

        for url in urls:
            self.stdout.write(url)
