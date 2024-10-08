#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    # from brand_autos.models import BrandAuto

    # with open('brand_autos.txt', encoding='utf-8') as f:
    #     brands = list(map(str.strip, f.readlines()))
    # with open('brand_autos_slug.txt', encoding='utf-8') as f:
    #     brands_slug = list(map(str.strip, f.readlines()))
    # assert len(brands) == len(brands_slug), 'Длины не совпадают'
    # for s, s_slug in zip(brands, brands_slug):
    #     try:
    #         obj = BrandAuto.objects.create(name=s, slug=s_slug)
    #         obj.save()
    #     except BaseException as e:
    #         print(e)


if __name__ == '__main__':
    main()
