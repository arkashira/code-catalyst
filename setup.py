import setuptools

setuptools.setup(
    name="axentx-product",
    version="0.1.0",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    tests_require=["pytest"],
    python_requires=">=3.8",
)
