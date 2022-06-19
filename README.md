# ForHeart: Live a long life with Good Heart!
***
## Website Link
website link
## Demo Link
link
***
### ✨ Inspiration
We are observing a recent trend of increase in heart attack fatalities with every passing generation. With the consultation of medical experts, we have figured out, that with the increasing workload, stress, and unhealthy lifestyle, their an increase in the upwardness of the curve of heart attack victims. Due to the lack of awareness of the general masses, this trend is not going to reduce in the coming future. We, as a group, did a brainstorming session to figure out what we can do, and have tried our best to come to a solution.

### 🚀 What it does
We have made a tool for the prediction of Heart Attacks using the Machine Learning Model. We have also made a website for the same. The website will take input parameters related to their health like blood pressure, the occurrence of chest pain, etc. from the user, and based on it, will provide the output (chances of getting heart attack) from our model on the website.

### 👨‍💻 How we built it
* We shall train and validate models and develop a machine learning pipeline for deployment.
* We shall build an HTML front end with an input form for independent variables(age, sex, chest pain type, resting blood pressure, etc.)
* Build a back-end of the web application using Flask Framework
***
## Run the Program from your local computer
### <u>Dependencies and Installation</u>

- Python >= 3.7 (Recommend to use [Anaconda](https://www.anaconda.com/download/#linux))

- Optional: NVIDIA GPU + [CUDA](https://developer.nvidia.com/cuda-downloads)


### Installation

1. Clone repo

    ```bash
    (base) git clone https://github.com/AniruddhA-Omni/ForHeart.git
    (base) cd ForHeart
    ```
2. Install dependent packages
    ```bash
    (base)     conda create -name "forheart" python=3.8
    (base)     conda activate forheart 
    (forheart) pip install -r requirements.txt
   ```
3. Download files from Auth0
   * SignUp in Auth0
   * Create application from dashboard
   * Select Python
   * Read the instructions in Python app in Auth0
   * Download the .env file from Auth0
   * Move the .env file in ForHeart directory
### Run the program
   ```
   (forheart) python app.py
   ```
