
from setuptools import find_packages, setup

requirements = [
    "requests>=2.28.1"
]

setup(
    name = "kanashi",
    author = "Ari Setiawan",
    author_email = "ari160824@gmail.com",
    version = "1.1.3",
    license = "GNU General Public License v3",
    url = "https://github.com/hxAri/Kanashi",
    install_requires = requirements,
    keywords = [
        "instagram",
        "instagram-login", "instagram-image",
        "instagram-video", "instagram-feeds",
        "instagram-story", "instagram-private",
        "instagram-cookie", "instagram-session",
        "linux",
        "termux",
        "android",
    ],
    description = "Kanashi is an open source project that can be used to login to real Instagram accounts via Linux Terminal and Android Termux.",
    packages = find_packages(),
    python_requires = ">=3.10.4",
    include_package_data = True
)
