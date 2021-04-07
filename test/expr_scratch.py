import time
import aletheia
import aletheia.data.local_cache
from aletheia import Metastore


ms = Metastore("zephyrus")
plants_folds = {'far dane%27s': 0, 'asfordby b': 0, 'asfordby a': 0, 'kirton': 0,         'nailstone':    5,
          'kelly green': 1, 'bake solar farm': 1, 'newnham': 1, 'caegarw': 1,       'rosedew':      5,
          'moss electrical': 2, 'caldecote': 2, 'clapham': 2, 'lains farm': 2,      'magazine':     5,
          'roberts wall solar farm': 3, 'crumlin': 3, 'moor': 3, 'soho farm': 3,    'box road':     5,
          'grange farm': 4, 'ashby': 4, 'somersal solar farm': 4, 'combermere farm': 4}

ms.add_metadata("plant_folds", plants_folds)


ms = aletheia.Metastore("alethea-fcf82") # Get a projects metastore

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