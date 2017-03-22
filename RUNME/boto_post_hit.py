import config
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
from boto.mturk.qualification import (Qualifications, 
    PercentAssignmentsApprovedRequirement, 
    NumberHitsApprovedRequirement)
from boto.mturk.price import Price

# ============================HELPER METHODS=======================


# Quick method to encode url parameters
def encode_get_parameters(baseurl, arg_dict):
    queryString = baseurl + "?"
    for indx, key in enumerate(arg_dict):
        queryString += str(key) + "=" + str(arg_dict[key])
        if indx < len(arg_dict)-1:
            queryString += "&"
    return queryString


# ============================VARIABLES============================
# START AWS CONFIGURATION VARS
AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
# END MAIN CONFIGURATION VARS

# START IMPORTANT HIT VARIABLES
sandbox = True
base_url = ""
params_to_encode = {"ParameterToPass": "ValueToPass"}
assignments_per_hit = 1
payment_per_assignment = 0.05
# END IMPORTANT HIT VARIABLES

# START QUALIFICATION CONFIGURATION
qualifications = Qualifications()
qual_1 = PercentAssignmentsApprovedRequirement(
    comparator="GreaterThan",
    integer_value="0")
qual_2 = NumberHitsApprovedRequirement(
    comparator="GreaterThan",
    integer_value="0")
qualifications.add(qual_1)
qualifications.add(qual_2)
# END QUALIFICATION CONFIGURATION

# START DECORATIVE HIT VARIABLES
hit_title = "Insert the title of your HIT"
hit_description = "Insert your description here"
hit_keywords = ["add", "some", "keywords"]
duration_in_seconds = 60*60
frame_height = 800
# END DECORATIVE HIT VARIABLES
# =================================================================

# Initialize boto connection based on sandbox.
if sandbox:
    AMAZON_HOST = "mechanicalturk.sandbox.amazonaws.com"
else:
    AMAZON_HOST = "mechanicalturk.amazonaws.com"

connection = MTurkConnection(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    host=AMAZON_HOST)
# Selecting which endpoint to pass as parameter
if sandbox:
    external_submit_endpoint = "https://workersandbox.mturk.com/mturk/externalSubmit"
else:
    external_submit_endpoint = "https://www.mturk.com/mturk/externalSubmit"
params_to_encode['host'] = external_submit_endpoint

encoded_url = encode_get_parameters(base_url, params_to_encode)
create_hit_result = connection.create_hit(
    title=hit_title,
    description=hit_description,
    keywords=hit_keywords,
    duration=duration_in_seconds,
    max_assignments=assignments_per_hit,
    question=ExternalQuestion(encoded_url, frame_height),
    reward=Price(amount=payment_per_assignment),
    # Determines information returned by certain API methods.
    response_groups=('Minimal', 'HITDetail'),
    qualifications=qualifications)
