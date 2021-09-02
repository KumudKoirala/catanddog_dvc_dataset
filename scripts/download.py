import wget
import os
import zipfile
from pathlib import Path
import yaml
import hydra 
from omegaconf import OmegaConf,DictConfig

@hydra.main(config_path=("/home/kumud/CAT-DOG/config"),config_name="config")
def func_app(cfg:DictConfig):

    url=cfg.data.download.url
    zip_file=cfg.data.download.zip_file
    print(hydra.utils.get_original_cwd())
    wget.download(url,zip_file)  # run as hydra.run.dir="data"
    with zipfile.ZipFile(Path(hydra.utils.get_original_cwd())/Path(cfg.data.download.dir)/Path(cfg.data.download.zip_file),'r') as zip_ref:
        zip_ref.extractall(Path(hydra.utils.get_original_cwd())/Path(cfg.data.download.dir)/Path(cfg.data.download.sub_dir))
    os.remove(Path(hydra.utils.get_original_cwd())/Path(cfg.data.download.dir)/Path(cfg.data.download.zip_file))
        
    
        
    
    


if __name__=='__main__':
        func_app()
