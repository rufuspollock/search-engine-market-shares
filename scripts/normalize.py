import csv
outfp = 'market-share.normalized.csv'
writer = csv.writer(open(outfp, 'w'))
headings = ['Date', 'Country', 'Provider', 'Share', 'Source', 'Notes']
writer.writerow(headings)
for row in csv.DictReader(open('market-share.initial.csv')):
    outrowtmpl = [ row['Date'], row['Country'] ]
    for provider in ['AOL', 'All the Web', 'AltaVista', 'Ask', 'Excite',
            'Google', 'Lycos', 'MSN', 'Yahoo', 'Others']:
        value = row.get(provider)
        if not value:
            continue
        outrow = list(outrowtmpl)
        outrow.extend([provider, value, row['Source'], ''])
        writer.writerow(outrow)


