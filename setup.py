from setuptools import find_packages, setup

package_name = 'tdmpc2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[],
    install_requires=[
        'torch',
        'torchvision',
        'torchrl',
        'ffmpeg',
        'hydra-core',
        'hydra-submitit-launcher',
        'moviepy',
        'numpy<2',
        'omegaconf',
        'open3d',
        'opencv-contrib-python',
        'opencv-python',
        'pandas',
        'sapien',
        'submitit',
        'termcolor',
        'transforms3d',
        'trimesh',
        'tqdm',
        'wandb',
        ],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
