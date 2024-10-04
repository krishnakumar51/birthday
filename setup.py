from setuptools import setup, find_packages

setup(
    name="birthday-wish-app",
    version="0.1",
    description="A simple Streamlit app for sending birthday wishes",
    author="Krishna-kumar",
    author_email="godkrishnasskal@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "birthday_wish=birthday_wish_app.main:main",
        ],
    },
)
