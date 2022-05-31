
from setuptools import find_packages, setup

requirements = [
    "certifi==2022.5.18.1",
    "charset-normalizer==2.0.12",
    "httpagentparser==1.9.2",
    "idna==3.3",
    "requests==2.27.1",
    "urllib3==1.26.9"
]

setup(
    name = "kanashi",
    author = "Ari Setiawan",
    author_email = "ari160824@gmail.com",
    version = "1.1.2",
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
