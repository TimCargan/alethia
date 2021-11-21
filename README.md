# Read Me
This is a very basic experiment tracker that uses firestore to track things.
its still very much a work in progress and is tailored to my current workflow

### TODOs:
- Add dynamic loading of run experiments
- hook in the data connectors and chache so we can download datasets etc and track them 
- Add some spark conneectors so I can add it to my data / results pipelines wit ease

## Installation
use pip to install the repo:

`pip install git+https://github.com/TimCargan/aletheia.git`

Make sure to have your auth key in the environment:

`export GOOGLE_APPLICATION_CREDENTIALS = "/path/to/token.json"`
## Usage

Example usage of package in experiments

```python
ms = Metastore("alethea-fcf82")
ms.set_downloader(local_cache_dir)
exper = ms.exper("exper Name", debug=False, auto_inc_ids=True)
exper.desc = "Description / notes etc"
with expr.start_run(fold=1) as run:
    run.set_fold()

    ds = run.get_dataset("ds_name", download=True) #this will register use of dataset
    #for now lets keep fold splitting etc external i.e just download the file to the cache
    path_to_data = ds.local_path

    #Make hyper parmas etc
    run.set_model()
    run.set_hyper_params(hp.to_dict())
    ex.add_artifact("name", "path/to/artifact", is_local=True, is_dir=True, upload_file=True)
    ex.add_metric("name", value)
```

## Some other notes
### Workflow

The plan for the workflow is:
- Maka a data source
- Define a model
- Git commit
- run expr
- will check to see if you are running on an uptodate commit
- write results to db etc


MetaStore - hold info about expers etc
BlobStore - holds raw data
LocalCache - uses metaData to find data, downloads it to the local system
Repo - Code Tracking / Tagging

### Database layout
```
Root
    Projects - col
        Project (e.g zephyous)
            Experiments - col
                expr - doc
                    Runs - Col
                    Artifcats - Col
                        name - doc
                            files - col
                    Results - Col
            Datasets - col
                name - doc
                    files - col
            Metadtata - col
                name - doc
    Files - col
 ```   
### Data Structs

Data: Type
    Des
    Location
    Source
    Partitons
    Par
    Date Created

Model:
    Project
    Description
    Version

Fold:
    fold
    Model
    Run
    Data

Run:
    GitHash
    Date
    fold
    Model
    Data
    LogDir
    SavedModel
    Res
    Discritoion

Data Source
