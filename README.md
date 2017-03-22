# mturk-lean-external-question
A lean, mean, very quickly deployable ExternalQuestion template for Amazon Mechanical Turk. Specifically useful as it requires nothing beyond static files. 

# Overview
Using an ExternalQuestion is the easiest way to get MTurk workers to work on an arbitrary microtask and gives a requester the freedom to define their interface as they wish.

# Hosting
Host everything in the HOSTME folder on your choice of hosting platform. Mine is Amazon S3, so I would recommend just throwing the two files into an S3 bucket and making them public.

# Posting 
1. Download python
2. Use pip to install boto (pip install boto)
3. Add AWS access and secret keys to config.py.
4. Edit post_hits.py (especially base_url) and execute when ready. I suggest posting once with sandbox = True and running through the HIT on the sandbox to make sure everything is working properly first.
5. Login to your requester account on the prod or sandbox site and check that everything posted correctly.

# Screenshots
Checking from the requester UI that everything was sucessfully posted.
![posted](https://cloud.githubusercontent.com/assets/3171564/24210547/7a3a677c-0ef7-11e7-8d24-819115c3bf2f.png)
Finding our HIT as a worker
![workerfind](https://cloud.githubusercontent.com/assets/3171564/24210622/ae7138fe-0ef7-11e7-8727-ee425b2ef989.png)
Performing our HIT as a worker
![ourhit](https://cloud.githubusercontent.com/assets/3171564/24210543/779ad182-0ef7-11e7-9e67-fd2ee3672803.png)
Logging back in as a requester, and we see our HIT has been complete!
![results](https://cloud.githubusercontent.com/assets/3171564/24210540/7660ef4a-0ef7-11e7-8bac-9603fea6f86c.png)
Reviewing the HIT as a requester
![done](https://cloud.githubusercontent.com/assets/3171564/24210536/72fda334-0ef7-11e7-9329-32cd71d6d1ee.png)

