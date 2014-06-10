#!/usr/bin/env python
'''
Global data from hitslink.com

http://marketshare.hitslink.com/
http://marketshare.hitslink.com/report.aspx?qprid=4&qpmr=100&qpdt=1&qpct=3&qpcal=1&qptimeframe=Q&qpsp=24&qpnp=1

From Site Front Page:

<quote>
About Our Market Share Statistics

This data provides valuable insight into significant trends for internet usage.  These statistics include monthly information on key statistics such as browser trends (e.g. Internet Explorer vs. Firefox market share), search engine referral data (e.g. Yahoo vs. MSN vs. Google traffic market share) and operating system share (Windows vs. Mac vs. Linux market share or even the iPhone market share vs. Windows Mobile).

We use a unique methodology for collecting this data.  We collect data from the browsers of site visitors to our exclusive on-demand network of live stats customers.  The data is compiled from approximately 160 million visitors per month.  The information published is an aggregate of the data from this network of hosted website statistics.  The site unique visitor and referral information is summarized on a monthly basis.

In addition, we classify 430+ referral sources identified as search engines.  Aggregate traffic referrals from these engines are summarized and reported monthly.  The statistics for search engines include both organic and sponsored referrals.  The websites in our population represent dozens of countries in regions including North America, South America, Western Europe, Australia / Pacific Rim and Parts of Asia.

The data is made available free of charge on a monthly basis that includes monthly browser market share trends, top search engine referrals, screen resolutions, top ISPs and operating systems trends.  An upgraded version is available that provides reports by geolocation, preview weekly data and other features.

# Additional estimates about the website population: 76% participate in pay per click programs to drive traffic to their sites.
# 43% are commerce sites
# 18% are corporate sites
# 10% are content sites
# 29% classify themselves as other (includes gov, org, search engine marketers etc..) 
</quote>
'''
import urllib
import sys
import econ.data.tabular as t
import tidy

START_MONTH = 69
END_MONTH = 113

def download():
    baseurl = 'http://marketshare.hitslink.com/report.aspx?qprid=4&qpmr=100&qpdt=1&qpct=3&qpcal=1&qptimeframe=M&qpsp=%d'
    # beginning 2004 to 2008 apr
    for month in range(START_MONTH, END_MONTH):
        url = baseurl % month
        fn = 'netapplications-month-%d.html' % month
        print 'Downloading %s\n  to %s' % (url, fn)
        urllib.urlretrieve(url, fn)

DATA_FILE = 'netapplications.csv'
class DataExtractor(object):

    def process(self, file_name, table_index=19):
        reader = t.HtmlReader()
        tidied = tidy.parse(file_name)
        from StringIO import StringIO
        tidied = StringIO(tidied)

        out = reader.read(tidied, table_index).data
        # print len(reader.tables)
        # print reader.tables[22]
        out = out[4:]
        out[-1] = out[-1][:2]
        # strip out unnecessary stuff
        out = [ [ x[0].replace(' -\nGlobal', ''), float(x[1][:-1]) ] for x in out ]
        out = dict(out)
        # consolidate microsoft results into one value
        def consolidate_row(row):
            # always have MSN but not always Live
            mslive = 'Microsoft Live\nSearch'
            row['MSN'] = row['MSN'] + row.get(mslive, 0)
            if row.has_key(mslive):
                del row[mslive]
            return row
        out = consolidate_row(out)
        return out

    def all(self):
        results = []
        for ii in range(START_MONTH, END_MONTH):
            # start in October 2004
            year = 2004 + int((9 + ii - 69) / 12)
            month = 1 + (9 + ii - 69) % 12
            fn = 'netapplications-month-%s.html' % ii
            print 'Processing file: %s' % fn
            # table_index depends on download date
            # items from 112 onwards were downloaded later
            if ii < 112:
                out = self.process(fn, 19)
            else:
                out = self.process(fn, 22)
            out['Year'] = year
            out['Month'] = month
            results.append(out)
        return results

    def convert_to_tabular(self, dict_list):
        results = dict_list
        tdata = t.TabularData()
        headings = results[0].keys()
        headings.sort()
        headings.remove('Year')
        headings.remove('Month')
        headings = ['Year', 'Month'] + headings
        tdata.header = headings
        tdata.data = [ [ row[k] for k in headings ] for row in results ]
        return tdata

    def dump(self):
        results = self.all()
        tabdata = self.convert_to_tabular(results)
        writer = t.CsvWriter()
        out_fn = DATA_FILE
        print 'extracting and appending to %s' % out_fn
        # append to avoid losing old material
        outfo = file(out_fn, 'a')
        writer.write(outfo, tabdata)
        outfo.close()


import econ.data.misc as m
import datetime
def plot():
    reader = t.CsvReader()
    tdata = reader.read(file(DATA_FILE))
    data = tdata.data
    data = m.floatify_matrix(data)
    dates = []
    for row in data:
        date = datetime.date(row[0], row[1], 1)
        dates.append(date)
    # transpose
    market_shares = zip(*data)
    # delete first 2 to avoid using year and month
    market_shares = zip(tdata.header, market_shares)[2:]
    market_shares = dict(market_shares)
    print market_shares.keys()

    import pylab
    import matplotlib.dates
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    ax.plot_date(dates, market_shares['Google'], 'ko-', label='Google')
    ax.plot_date(dates, market_shares['Yahoo'], 'b+-', label='Yahoo')
    ax.plot_date(dates, market_shares['MSN'], 'rx-', label='MSN')

    def fancy_format():
        years    = matplotlib.dates.YearLocator()   # every year
        months   = matplotlib.dates.MonthLocator(bymonthday=1)  # every month
        monthsFmt = matplotlib.dates.DateFormatter("%b '%y")
        # yearsFmt = matplotlib.dates.DateFormatter('%Y')

        # format the ticks
        ax.xaxis.set_major_locator(months)
        ax.xaxis.set_major_formatter(monthsFmt)
        # ax.xaxis.set_minor_locator(months)
        # ax.fmt_xdata = matplotlib.dates.DateFormatter('%Y-%m')

        ax.autoscale_view()

    # puts date labels nicely at an angle
    fig.autofmt_xdate()

    pylab.ylabel('Market Share')
    pylab.xlabel('Date')
    pylab.ylim(ymax=100)
    ax.grid()
    ax.legend(loc='upper left')
    fig.savefig('netapplications_2004_to_2008.png')


if __name__ == '__main__':
    extractor = DataExtractor()
    fn = sys.argv[1]
    if fn == 'download':
        download()
    elif fn == 'all':
        out = extractor.all()
        print out
    elif fn == 'dump':
        out = extractor.dump()
    elif fn == 'plot':
        plot()
    else:
        print extractor.process(fn)

