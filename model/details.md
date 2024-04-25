## Data Processing
  - Creates arrays and stuff to be used in the RNN 

## Model 1
  - Basic model
  - Uses a set amount of 1s and 0s
  - Can change the structure of the RNN easily
  - Un-optimised things such as optimiser, structure, learning rate, etc.

## Model 2
  - GPU capability added
  - More complex model
    -  uses a bidirectional LSTM
    -  Dropout added
    -  Increased hidden layer size

## Hyperparameter Search
#### Search 1: 
  | Learning Rates | Hidden Sizes | Dropout Values | Num Layers |
|----------------|--------------|----------------|------------|
| 0.001          | 128          | 0.2            | 2          |
| 0.01           | 256          | 0.4            | 3          |
| 0.1            | 512          | 0.6            | 4          |

Best: 0.001, 256, 0.4, 3

## Model 3
  - Weight decay added
  - Hyperparameters changed from search
  - Added a learning rate scheduler

## Model 5
  - Runs 9 iterations of different years combos

## Model 6
  - Runs 10 iterations of 2 different years and 5 different ratios
    
