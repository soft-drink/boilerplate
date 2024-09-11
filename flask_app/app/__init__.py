from flask import Flask

import os


APP_NAME = "site"


def create_app(test_config=None):
    site = Flask(APP_NAME, instance_relative_config=True, template_folder="template")
    site.config.from_mapping(
        SECRET_KEY="DeBuG",
        DATABASE=os.path.join(site.instance_path, "app.sqlite"),
    )

    if test_config is None:
        site.config.from_pyfile("config.py", silent=True)
    else:
        site.config.from_mapping(test_config)

    try:
        os.makedirs(site.instance_path)
    except OSError:
        pass

    from . import index
    site.register_blueprint(index.bp)

    return site
