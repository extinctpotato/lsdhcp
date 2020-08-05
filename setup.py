import setuptools

setuptools.setup(
        name="lsdhcp",
        version="0.1",
        author="Adam Olech",
        author_email="nddr89@gmail.com",
        description="List DHCP leases from an SSH-enabled OpenWRT device",
        packages=["lsdhcp"],
        python_requires='>=3.5',
        entry_points={
            "console_scripts": ["lsdhcp = lsdhcp.cli:main"]
            },
        install_requires=["paramiko", "prettytable", "mac-vendor-lookup"],
        )
