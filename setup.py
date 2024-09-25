from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rfsynth",
    version="0.0.1",
    author="Stephen Akinremi",
    author_email="s.akinremi@utwente.nl",
    description="Synthetic receiver functions calculation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/akinremisa/rfsynth",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    keywords="Seismology, Synthetic Data, Receiver Function, Earth Sciences",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6, <3.11",
    install_requires=[
        "obspy>=1.0.3",
        "rf>=1.0.3",
        "numpy<=1.24.0",
        "obspyh5",
        "matplotlib"],
    zip_safe=False,
    include_package_data=True,
    package_data={"": ["*.py", ".ipynb", ".md", "jpeg"]},
)
