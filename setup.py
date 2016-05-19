#   Copyright 2012-2013 Rackspace
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import setuptools


novaclient_extensions = [
    'rackspace-auth-openstack',                         # RAX-KSKEY
    'os_diskconfig_python_novaclient_ext',              # Disk_config
    'rax_scheduled_images_python_novaclient_ext',       # RAX-SI (replaces
                                                        #   backup_schedule)
    'os_networksv2_python_novaclient_ext',              # Rax_Networks
    'os_virtual_interfacesv2_python_novaclient_ext',    # Virtual interfaces
    'rax_default_network_flags_python_novaclient_ext',  # default network flags
    'ip_associations_python_novaclient_ext',            # ip associations
]


setuptools.setup(
    name='rackspace-novaclient',
    version='1.6',
    author='Rackspace',
    author_email='johannes.erdfelt@rackspace.com',
    description='Metapackage to install python-novaclient and Rackspace '
                'extensions',
    license='Apache License, Version 2.0',
    url='https://github.com/rackerlabs/rackspace-novaclient',
    install_requires=[
        'python-novaclient>=2.35.0,<3'
    ] + novaclient_extensions,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
