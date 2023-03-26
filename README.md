# Google-Cloud-Compute-Engine-API-Django-connector
Google Compute Engine (GCE) API connector to django web site

I offer you a simple way to connect the Google Compute Engine (GCE) to your django project. Use the computing power of Google in your project. To connect your Django web application to Google Compute Engine API, you can use the `google-cloud-compute` Python client library.

First, you need to install the library using pip:
`pip install google-cloud-compute`

Next, you need to authenticate your application with the Google Compute Engine API by creating a service account and providing its credentials. You can do this by following these steps:

+ Go to the Google Cloud Console and select your project.
+ Click on the Navigation menu and select APIs & Services > Credentials.
+ Click on Create credentials and select Service account key.
+ Select a service account and a key type (JSON).
+ Click on Create to download the JSON key file.
+ Store the key file in a secure location, outside of your project directory.
+ Now that you have the authentication credentials, you can use the google-cloud-compute library to access your Google Compute Engine instances from your Django web application. Here in the `GCEAPI_connector.py` file is an example of how to do this.
