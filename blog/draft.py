# with open('brand_autos.txt', 'r+', encoding='utf-8') as f:
#     with open('brand_autos_slug.txt', 'w+', encoding='utf-8') as f1:
#         for s in map(str.strip, f.readlines()):
#             f1.write(s.lower())
#             f1.write('\n')

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