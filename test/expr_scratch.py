import time

from aletheia.metastore import Metastore
from data import LocalCache


ms = Metastore("alethea-fcf82") # Get a projects metastore

# filestore = LocalCache()
# ms.set_downloader(filestore)



with ms.start_exper("exper id3", debug=True, auto_inc_ids=True) as run:
    # run.set_fold()

    ds = run.load_dataset("New Dataset2") #download=True #this will register use of dataset
    #for now lets keep fold splitting etc external i.e just download the file to the cache
    # path_to_data = ds.local_path
    time.sleep(5)
    # Make hyper parmas etc
    # run.set_model()
    hps = {"size": 1, "test": run._run_id()}
    run.hyper_params = hps
    run.add_artifact("name", "path/to/artifact", is_local=True, is_dir=True, upload_file=True)
    run.add_metric("name", 5)
    run.rando_prop = "this is  a test"