# mturk-lean-external-question
A lean, mean, very quickly deployable ExternalQuestion for Amazon Mechanical Turk. MTurk HITs simplified to a hosted static file. 

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
