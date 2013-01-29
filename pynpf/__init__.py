import os
import shutil

def install(target_dir):
    source_dir = os.path.abspath(os.path.dirname(__file__))
    source_dir = os.path.join(source_dir, 'npf/source')
    shutil.rmtree(target_dir, ignore_errors=True)
    shutil.copytree(source_dir, target_dir)
