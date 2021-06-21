import io
from setuptools import find_packages, setup


with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()


setup(
    name="feedwerk",
    version="0.0.2",
    url="https://github.com/uniphil/feedwerk",
    project_urls={
        "Documentation": "https://github.com/uniphil/feedwerk",
        "Code": "https://github.com/uniphil/feedwerk",
        "Issue tracker": "https://github.com/uniphil/feedwerk/issues",
    },
    license='BSD-3-Clause',
    author="phil",
    author_email="phil@commit--blog.com",
    description="The atom feed generator from werkzeug.",
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=('tests*',)),
    include_package_data=True,
    install_requires=["werkzeug >= 1.0.0"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    extras_require={"dev": ["pytest"]},
)
