from setuptools import setup, find_packages

setup(
    name='QR_Code_Generator_and_Reader',
    version='1.0',
    author='Ruban Gino Singh',
    author_email='info@rubangino.in',
    description="Python Application to generate QR code with in one click.",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta", 
        "Intented Audience :: Social Media managers and Online program managers",
        "Licence :: OSI Approved :: MIT Licence"
    ],
    keywords="QRcode QRgenerator QRreader QRcodeGenerator",
    packages=find_packages(),
    install_requires=["requests>=2"],
    python_requires="~=3.5"
)