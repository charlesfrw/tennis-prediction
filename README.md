# tennis-prediction project

I am working on a machine learning program to predict accurately the outcome of tennis single matches. 

This repository contains a collection of Python programs for exploring tennis data and ultimatly performing some machine learning tasks. These programs are designed to help tennis enthusiasts analyze and preprocess tennis data, extract useful information, and make predictions using machine learning techniques.

The data used in my programs is from the tennis database provided by Jeff Sackmann : https://github.com/JeffSackmann

# Programs

1. Data Finder: This program allows you to search and locate specific ATP tennis data. It provides a user-friendly interface for finding and accessing specific datasets, you can preview or download the whole dataset in a .csv <img width="1229" alt="Data Finder" src="https://github.com/charlesfrw/tennis-prediction/assets/105107604/32f8e956-b44f-432f-b437-88cfbd775723">

2. ATP Rankings: This program give you access to the latest ATP ranking.<img width="438" alt="Tennis ATP rankings" src="https://github.com/charlesfrw/tennis-prediction/assets/105107604/452a06c1-52e4-4f09-87b3-c6139953c226">

3. ATP Players Statistics: This program provides comprehensive statistics for ATP players. You can obtain specific statistics by providing some filter (year, round, opponent, surface, tounament...)<img width="990" alt="Tennis ATP Player Statisteic" src="https://github.com/charlesfrw/tennis-prediction/assets/105107604/51495594-c864-492d-856d-311e89557ae5">
Programs 4-5-6 are working together for Machine Learning :
4. Data Extractor for Machine Learning: This program helps in extracting relevant features and data for machine learning tasks. It find it all the specifc data corresponding to the player and his opponent and merge it in single .csv file. The data extracted correspond to all the matches between the two players, but also matches of each player on a specific surface and season.
5.  Data Preprocessing for Machine Learning: This program focuses on data preprocessing techniques for machine learning. It cleans the data, handles missing values, performs feature engineering, and prepares the dataset for training machine learning models.
6. Prediction by Machine Learning: (Not avaible yet) This program is intended to make predictions using machine learning algorithms. It aims to train a random forest classifier on tennis data and predict the outcomes of tennis matches based on the input provided. Please note that this program is still a work in progress and is not functional at the moment.

All the programs can be easily launched by the Tennis_Menu.py program.<img width="503" alt="Tennis_Menu" src="https://github.com/charlesfrw/tennis-prediction/assets/105107604/015957c2-d4f3-469b-8e4f-1f2ab23ed3c5">


# Usage
To use these programs, follow these steps:

1. Clone the repository to your local machine.
2. Also clone the Jeff Sackmann ATP repository.
3. Install the required dependencies mentioned in the documentation.
4. Run the desired Python program by executing the corresponding file.
5. Follow the program prompts or instructions to interact with the data and perform the desired task.
Feel free to explore and modify the code to suit your specific needs. Contributions and suggestions are welcome.

# Note: 

The programs assume that the necessary data files are located in the specified directory (/Users/charles/Desktop/TENNIS/tennis_atp-master). Adjust the file paths in each .py accordingly to your files location...

The Data Extractor Program (5) will create a .csv in a specified directory (/Users/charles/Desktop/TENNIS/Data). Adjust it as you wish. The same file will be used by the Preprocessing Program so make sure to update the file path there as well.

+ I learned coding by myself, and also used some AI tools to improve my codes, please report me any error or issues if you find some, and feel free to complete/upgrade my work.

# Credits
The programs in this repository utilize the tennis database (tennis_atp-master) provided by Jeff Sackmann. I would like to express my gratitude to Jeff Sackmann for his valuable contribution to the tennis community by offering an high quality database.

# License
This project is licensed under the MIT License.

If you wanna run my code with the data from Jeff Sackmann repository you must respect his work, here is his license :

# Attention (If you use the data from Jeff Sackmann Repositery)

Please read, understand, and abide by the license below. It seems like a reasonable thing to ask, given the hundreds of hours I've put into amassing and maintaining this dataset. Unfortunately, a few bad apples have violated the license, and when people do that, it makes me considerably less motivated to continue updating.

Also, if you're using this for academic/research purposes (great!), take a minute and cite it properly. It's not that hard, it helps others find a useful resource, and let's face it, you should be doing it anyway.

# License (If you use the data from Jeff Sackmann Repositery)

Creative Commons License
Tennis databases, files, and algorithms by Jeff Sackmann / Tennis Abstract is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
Based on a work at https://github.com/JeffSackmann.

In other words: Attribution is required. Non-commercial use only.
