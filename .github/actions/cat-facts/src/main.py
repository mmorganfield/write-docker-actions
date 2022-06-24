import requests
import random
import sys


random_fact = "The catfact site no longer functions, for cats"

# Print the individual randomly returned cat-fact
print(random_fact)

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
