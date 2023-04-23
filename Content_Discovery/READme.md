Content refers to files, video, backup or even a website feature.
It doesnt have to refer to the files/pages that we can see exactly.

There are 3 ways of discovering content:
- Manually
- Automated
- OSINT

### Manual Content Discovery

- Checking the robots.txt file.(This file is a document that tells search engines pages that are allowed and not allowed to be crawled for search engine results.)
-  Favicon - This is an icon on the web-server that shows the websites logo.(In this case, it can help us to identify the type of framework being used)
- sitemap - The sitemap gives out a list of every file in the webserver that a user wishes to be listed on a search engine.(sitemap.txt)
- HTTPS headers - Headers may have some good information such as the web-server software and probably the backend language

### OSINT

- Google dorking - This refers to utilizing google's advanced search engine features, which allow you to pick out custom content.
- Wappalyzer - This is a browser extension/online tool that helps to identify the technologies running on a server.
- Wayback machine - This is a historical archive of websites that date back to the late 90's. It usually works like a library as you can view a sites data from a specific time period.
- Github - Git is a **version control system** that tracks changes to files in a project. You can use github to search for companies names /websites to try and find the source code.
- S3 Buckets - S3 Buckets are a storage service provided by Amazon AWS, allowing people to save files and even static website content in the cloud accessible over HTTP and HTTPS. The owner of the files can set access permissions to either make files public, private and even writable. Sometimes these access permissions are incorrectly set and inadvertently allow access to files that shouldn't be available to the public.

### Automated Content Discovery
This involves using tools to discover content rather than doing it manually.
