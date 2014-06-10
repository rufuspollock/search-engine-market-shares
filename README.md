Search engine market shares around the world over time. Data sourced from NetApplications, WebSideStory, Nielsen's NetRatings, comScore's MediaMetrix and other sources. Some figures and data come from *Is Google the next Microsoft? Competition, Welfare and Regulation in Online Search, Review of Network Economics, Rufus Pollock, December 2010.* Please cite that as well as this dataset when using.

## Data

Obtaining good (comparable) market share data over a reasonable period is difficult. In particular, in the late 90s and early 2000s the only information recorded was the number of visits to a particular website. Since many providers of search also ran `portals' it can be difficult to distinguish pure search from simple visits.

In addition, early data frequently only records the number of unique visitors a month rather than giving a breakdown of the number of hits and this can severely distort results since pure-search providers (such as Google) are much more likely to have multiple visits from the same user than more portal-like sites.

Matters are further complicated by the fact that in the late 1990s and early 2000s many search \emph{sites} had their search powered by a third-party provider. For example, up until 2004, Yahoo! did not have their own search engine but `bought-in' results, first from Inktomi (up until 2000) and then Google.

Figure shows combined data from NetApplications and WebSideStory (now part of Omniture). Both firms source their data from web analytic applications installed on customers' sites and NetApplications appears to be more global in its customer-base than WebSideStory (which may partially explain the non-exact match between the two datasets apparent in the 2004 values).

Note these sources of data differs from that found in the likes of Nielsen's NetRatings, comScore's MediaMetrix. Those products get their data from the users themselves (directly or indirectly via ISPs) rather than from websites they visit. In this sense they may be more reliable sources of data. However, it has proved difficult to obtain continuous time-series data for these providers for more than a couple of years -- and for that period the trend they show is very similar to that found in the data shown.

The graph shows a simple story: a single firm (Google) emerges to dominate the market. In terms of general concentration, it is noteworthy that even in 2002, when Google was not yet as dominant as it is today, the top two firms (Google and Yahoo!) accounted for over 70% of the market while adding in Microsoft pushes this up to close to 90% (and of course at that point Yahoo!'s search was being powered by Google and MSN's by LookSmart and Inktomi).

### Sources

#### SEW / WebSideStory

http://searchenginewatch.com/showPage.html?page=3334881

Gives graph with USA (World?) data from WebSideStory from which we can infer data. Data not used:

<pre>
Outside US:

Country   Google      Yahoo
Germany   80.5%   5.6%
UK        65.6%   10.8%
China     72.6%   12.7%
</pre>

#### NetApplications

See netapplications.py file in code files.

Global data from hitslink.com

* http://marketshare.hitslink.com/
* http://marketshare.hitslink.com/report.aspx?qprid=4&qpmr=100&qpdt=1&qpct=3&qpcal=1&qptimeframe=Q&qpsp=24&qpnp=1

From Site Front Page:

> About Our Market Share Statistics
>
> This data provides valuable insight into significant trends for internet usage.  These statistics include monthly information on key statistics such as browser trends (e.g. Internet Explorer vs. Firefox market share), search engine referral data (e.g. Yahoo vs. MSN vs. Google traffic market share) and operating system share (Windows vs. Mac vs. Linux market share or even the iPhone market share vs. Windows Mobile).
>
> We use a unique methodology for collecting this data.  We collect data from the browsers of site visitors to our exclusive on-demand network of live stats customers.  The data is compiled from approximately 160 million visitors per month.  The information published is an aggregate of the data from this network of hosted website statistics.  The site unique visitor and referral information is summarized on a monthly basis.
>
> In addition, we classify 430+ referral sources identified as search engines.  Aggregate traffic referrals from these engines are summarized and reported monthly.  The statistics for search engines include both organic and sponsored referrals.  The websites in our population represent dozens of countries in regions including North America, South America, Western Europe, Australia / Pacific Rim and Parts of Asia.
>
> The data is made available free of charge on a monthly basis that includes monthly browser market share trends, top search engine referrals, screen resolutions, top ISPs and operating systems trends.  An upgraded version is available that provides reports by geolocation, preview weekly data and other features.

