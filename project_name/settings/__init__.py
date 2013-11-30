import os

# APP_ENV environment variable determines environment
# (development, staging, production)
app_env = os.getenv("APP_ENV", "development")
# TODO, raise custom exception rather than having a default.

# Common settings always applied
from {{project_name}}.settings.common import *

# Apply environment specific settings
if app_env == "development":
	from {{project_name}}.settings.development import *
elif app_env == "staging":
	from {{project_name}}.settings.staging import *
elif app_env == "production":
	from {{project_name}}.settings.production import *
else:
	pass
	# TODO raise invalid environment variable value exception.
