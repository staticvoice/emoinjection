# Low-level feature space

## Jitter and Shimmer features (11)
| Feature name     | Description         |
|------------------|---------------------|
| shimmer_local    | localShimmer        |
| shimmer_local_db | localdbShimmer      |
| shimmer_apq3     | apq3Shimmer         |
| shimmer_aqpq5    | aqpq5Shimmer        |
| shimmer_apq11    | apq11Shimmer        |
| shimmer_dda      | ddaShimmer          |
| jitter_local     | localJitter         |
| jitter_local_abs | localabsoluteJitter |
| jitter_rap       | rapJitter           |
| jitter_ppq5      | ppq5Jitter          |
| jitter_ddp       | ddpJitter           |

## Formants features (30)
| Feature name | Description               |
|--------------|---------------------------|
| f1_var       | variance of f1            |
| f1_mean      | mean of f1                |
| f1_max       | max of f1                 |
| f1_min       | min of f1                 |
| f1_range     | range of f1               |
| f2_var       | variance of f2            |
| f2_mean      | mean of f2                |
| f2_max       | max of f2                 |
| f2_min       | min of f2                 |
| f2_range     | range of f2               |
| f3_var       | variance of f3            |
| f3_mean      | mean of f3                |
| f3_max       | max of f3                 |
| f3_min       | min of f3                 |
| f3_range     | range of f3               |
| f1_d_var     | variance of derivative f1 |
| f1_d_mean    | mean of derivative f1     |
| f1_d_max     | max of derivative f1      |
| f1_d_min     | min of derivative f1      |
| f1_d_range   | range of derivative f1    |
| f2_d_var     | variance of derivative f2 |
| f2_d_mean    | mean of derivative f2     |
| f2_d_max     | max of derivative f2      |
| f2_d_min     | min of derivative f2      |
| f2_d_range   | range of derivative f2    |
| f3_d_var     | variance of derivative f2 |
| f3_d_mean    | mean of derivative f2     |
| f3_d_max     | max of derivative f2      |
| f3_d_min     | min of derivative f2      |
| f3_d_range   | range of derivative f2    |

## Fundamental frequency features (58)
| Feature name        | Description                                      |
|---------------------|--------------------------------------------------|
| f0\_v\_mean         | Median of the voiced F0 trajectory               |
| f0\_v\_std          | Std. of the voiced F0 trajectory                 |
| f0\_v\_min          | Min. of the voiced F0 trajectory                 |
| f0\_v\_max          | Max. of the voiced F0 trajectory                 |
| f0\_v\_range        | Range of the voiced F0 trajectory                |
| f0\_v\_q1           | Lower quartile of the voiced F0 trajectory       |
| f0\_v\_q3           | Upper quartile of the voiced F0 trajectory       |
| f0\_v\_qrange       | Q range of the voiced F0 trajectory              |
| f0\_v\_slope        | Slope of voiced F0 trajectory                    |
| f0\_v\_d\_mean      | Mean of the voiced F0' trajectory                |
| f0\_v\_d\_std       | Std. of the voiced F0' trajectory                |
| f0\_v\_d\_min       | Min. of the voiced F0' trajectory                |
| f0\_v\_d\_max       | Max. of the voiced F0' trajectory                |
| f0\_v\_d\_median    | Median of the voiced F0' trajectory              |
| f0\_v\_d\_range     | Q range of the voiced F0' trajectory             |
| f0\_v\_d\_q1        | Lower quartile of the voiced F0' trajectory      |
| f0\_v\_d\_q3        | Upper quartile of the voiced F0' trajectory      |
| f0\_mean\_v\_range  | Mean of the voiced segment ranges                |
| f0\_mean\_v\_max    | Mean of the voiced segment max                   |
| f0\_mean\_v\_min    | Mean of the voiced segment min                   |
| f0\_mean\_v\_q1     | Mean of the voiced segment lower quart           |
| f0\_mean\_v\_q3     | Mean of the voiced segment upper quart           |
| f0\_mean\_v\_qrange | Mean of the voiced segment q ranges              |
| f0\_mean\_v\_slope  | Mean of the voiced segment slopes                |
| f0\_max\_v\_slope   | Max. of the voiced segment slopes                |
| f0\_max\_v\_mean    | Max. of the voiced segment mean                  |
| f0\_std\_v\_mean    | Std. of the voiced segment means                 |
| f0\_std\_v\_slope   | Std. of the voiced segment slopes                |
| f0\_rps\_max        | Rising pitch slope maximum                       |
| f0\_rps\_mean       | Rising pitch slope mean                          |
| f0\_fps\_max        | Falling pitch slope maximum                      |
| f0\_fps\_mean       | Falling pitch slope mean                         |
| f0\_ops\_median     | Overall pitch slope median                       |
| f0\_mean\_pause     | Mean pause length                                |
| f0\_rps\_median     | Rising pitch slope median                        |
| f0\_fps\_median     | Falling pitch slope median                       |
| f0\_ops\_mean       | Overall pitch slope mean                         |
| f0\_ops\_max        | Overall pitch slope max                          |
| f0\_rps\_min        | Rising pitch slope min                           |
| f0\_fps\_min        | Falling pitch slope min                          |
| f0\_ops\_min        | Overall pitch slope min                          |
| f0\_v\_start        | F0 start                                         |
| f0\_v\_stop         | F0 stop                                          |
| f0\_rsd\_max        | Max of durations of the rising slopes of F0      |
| f0\_fsd\_max        | Max of durations of the falling slopes of F0     |
| f0\_rsd\_median     | Median of durations of the rising slopes of F0   |
| f0\_fsd\_median     | Median of durations of the falling slopes of F0  |
| f0\_rsd\_mean       | Mean of durations of the rising slopes of F0     |
| f0\_fld\_mean       | Mean of durations of the falling slopes of F0    |
| f0\_rsd\_qrange     | Q range of durations of the rising slopes of F0  |
| f0\_fsd\_qrange     | Q range of durations of the falling slopes of F0 |
| f0\_range\_st       | F0 range: values expressed in semitones          |
| f0\_grad\_max       | Pitch maximum gradient                           |
| f0\_grad\_mean      | Pitch mean value gradient                        |
| f0\_max\_relpos     | Pitch relative position of maximum               |
| f0\_min\_relpos     | Pitch relative position of minimum               |
| f0\_vd\_mean        | Duration mean value of voiced sounds             |
| f0\_vd\_std         | Duration std value of voiced sounds              |
