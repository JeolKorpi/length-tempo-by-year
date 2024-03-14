# Length & Tempo by Year & Decade
This project analyzes the length and tempo of songs by utilizing the [Million Song Dataset](http://millionsongdataset.com/ "Million song dataset") in a PySpark Environment. The project aims to assess if music during the past couple of decades has shifted in length and tempo since it's common speculation that music is constantly getting faster and shorter.

## The dataset
The 1.8 GB subset of the Million Song Dataset was selected, as it sizewise was suitable for a virtual environment with limited storage. The dataset was converted from `HDF5` to `CSV` format for readability, and all columns except "Year", "Tempo" & "Duration" have been dropped. Lastly, any rows with empty entries in one of the three remaining columns were dropped. The resulting dataset `MillionSongSubset_aggregated.csv` is available in the `/csv` directory, together with an inflation script `inflateDS.py`, which concatenates duplicate rows to the bottom of the dataset until a desired specified size is reached.

## The analysis
The notebook file, `Experiments_length_tempo.ipynb` is configured to be run in an Apache Spark cluster, built on top of a Hadoop cluster made for accessing and distributing the large working dataset. These frameworks are meant to provide efficient, robust, and error-prone operations when processing and querying the dataset. The purpose of the cluster is to provide the needed infrastructure for scaling with larger datasets and more processing nodes. The needed steps for running the analysis are:

- Specify the correct location of the CSV file within the HDFS directory, with the correct file size in mind.
- Configure the `spark_session` to specify the correct IP of the cluster's Master node, and appropriately change the number of worker nodes for the analysis.

The analysis is then performed by running all cells in the notebook. For scaling tests, the time required for the analysis should be noted.

___
*This repository belongs to the group 9 project in the Data Engineering 1 (1TD169) course at Uppsala University*.
*In the analysis for the project report, only a pseudo-distributed cluster was used and the number of spark executors was tweaked to simulate horizontal scaling*.
