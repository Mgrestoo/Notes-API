#!/usr/bin/env bash
# Render runs this script automatically on every deploy

# Exit immediately if any command fails
# Without this → script keeps running even after errors
set -o errexit

# Install all packages from requirements.txt
pip install -r requirements.txt

# Collect all static files into STATIC_ROOT folder
python manage.py collectstatic --no-input
# --no-input → don't ask for confirmation, just do it

# Run database migrations automatically
python manage.py migrate
# Creates/updates all tables on the PostgreSQL database