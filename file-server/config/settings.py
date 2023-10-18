import os

SAVE_DIRECTORY = f"{os.environ['RAILWAY_VOLUME_MOUNT_PATH']}/"
ARCHIVE_DIRECTORY = f"{os.environ['RAILWAY_VOLUME_MOUNT_PATH']}/archive/"
FILENAME = 'railway_graphql_collection.json'

CURRENT_FILE = SAVE_DIRECTORY + FILENAME

DIRECTORY_TEMPLATE = """
<!doctype html>
<html>
    <head>
        <title>Directory Listing</title>
    </head>
    <body>
    <h1>File Explorer</h1>
    <hr>
        <ul>
            {% for file_obj in files %}
            <li>
                <a href="{{ req_path + file_obj.name + ('/' if file_obj.is_directory else '') }}">
                    {{ file_obj.name }}{{ '/' if file_obj.is_directory else '' }}
                </a>
            </li>
            {% endfor %}
        </ul>
    </body>
</html>
"""

if not os.path.exists(ARCHIVE_DIRECTORY):
    os.makedirs(ARCHIVE_DIRECTORY)