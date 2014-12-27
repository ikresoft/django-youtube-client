from setuptools import setup, find_packages

setup(
    name='django-youtube-client',
    version='0.1',
    description='Django Youtube Client',
    url='http://github.com/ikresoft/django-youtube-client',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 0.1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['google-api-python-client'],
)