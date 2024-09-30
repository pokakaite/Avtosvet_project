with open('brand_autos.txt', 'r+', encoding='utf-8') as f:
    with open('brand_autos_slug.txt', 'w+', encoding='utf-8') as f1:
        for s in map(str.strip, f.readlines()):
            f1.write(s.lower())
            f1.write('\n')
