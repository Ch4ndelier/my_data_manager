## Data_manager

This repository collects the method to process data.

## Scripts

* `BM3D`: contains the BM3D process

* `HRtoLR`: contains the method to turn an image to LR state.

* `del_time.py`: Delete the time stamp in raw data.

* `filter.py`: For the press_label data, turn it into 0/1 style, and using plt to show.

* `gather_path.py`: To gather all the label path we need.

* `label_generator.py`: using filter, process the press_label raw data for later use.

* `data_preprocess.py`: before step prediction, transform y to float between 0 and 1.