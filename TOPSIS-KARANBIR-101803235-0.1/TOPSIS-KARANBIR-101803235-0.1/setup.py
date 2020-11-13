import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
  name = 'TOPSIS BY KARAN',
  author = 'KARANBIR SINGH',                    
  keywords = ['TOPSIS'],  
  install_requires=['pandas'],
  packages=setuptools.find_packages(),   
  version = '0.1',      
  license='MIT',        
  description = 'PACKAGE DESIGNED FOR RANKING THE DATASET BY THEIR TOPSIS SCORE',   
  long_description=long_description,
  long_description_content_type="text/markdown",
  
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: TIETCOE License',  
    'Programming Language :: Python :: 3',     
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
