from dotenv import load_dotenv
load_dotenv()

import os
import random
import time

from user import User
from helpers import did_user_register

import ldclient
from ldclient.config import Config

MIN_GROUP_SIZE = 3
MAX_GROUP_SIZE = 20
ITERATIONS = 400

# Setup client
ld_sdk_key = os.environ.get('LD_SDK_KEY')
ldclient.set_config(Config(ld_sdk_key))
ld_client = ldclient.get()

def send_data_for_user():
    # Instantiate a new User
    user = User()

    # Identify event
    ld_client.identify(user.get_context())

    # Flag events
    flag_variations = {
        "new_registration_flow": ld_client.variation("show-new-registration-flow", user.get_context(), False),
        "trial_duration": ld_client.variation("experiment-trial-duration", user.get_context(), 14),
        "cta_button_color": ld_client.variation("experiment-cta-button-color", user.get_context(), "blue")
    }

    # Custom event if the user registered
    if did_user_register(flag_variations):
        ld_client.track('user-registered', user.get_context())

# Send events for a group of users
def send_data_for_group():
    for i in range(random.randint(MIN_GROUP_SIZE, MAX_GROUP_SIZE)):
        send_data_for_user()

# Send groups of data over variable time for simulation purposes
for i in range(ITERATIONS):
    send_data_for_group()
    ld_client.flush()
    
    print(f'Finished iteration {i}')
    time.sleep(random.randint(15, 30))

# Exit safely
ld_client.flush()
ld_client.close()