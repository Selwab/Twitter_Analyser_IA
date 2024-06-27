# Tweet_Analyzer_IA

## Project Overview

This project aims to develop a website where users can compose tweets and have them analyzed by an AI model to determine their sentiment. By leveraging natural language processing techniques, the AI provides insights into the emotional tone of the tweets, classifying them as positive, negative, or neutral.

## Table of Contents
- [Technologies](#technologies)
- [Installation](#installation)
- [Running](#running)
  - [Twitter App](#twitter-app)
  - [Server](#server)
- [Usage](#usage)
- [Contributors](#contributors)

## Technologies

This project was developed using Angular, Flask, and TensorFlow.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/Tweet_Analyzer_IA.git
    cd Tweet_Analyzer_IA
    ```
2. Ensure you have `pip` installed on your system.
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running

### Twitter App

Ensure you have Angular installed. Run the following command in the `twitter_app` folder to execute the client application:

```bash
ng serve
```
Go to http://localhost:4200/.

### Server

Run `python ./app.py` in the backend-folder level to execute the server application.

## Usage

Write a tweet and post it! Check the sentiment identified by the AI.
![Post a tweet](![image](https://github.com/Selwab/Twitter_Analyser_IA/assets/129232511/72144a7b-7325-4cb3-82b8-3a24f6afe903))
![Check the sentiment](![image](https://github.com/Selwab/Twitter_Analyser_IA/assets/129232511/68f2ae4d-064c-44f6-abe0-5be1a5dd398b))

Go to the filter tab to search tweets by sentiment.
![Filter tweets](![image](https://github.com/Selwab/Twitter_Analyser_IA/assets/129232511/3b0c1db9-1600-4d73-ba9f-62bd8f1ba157))
