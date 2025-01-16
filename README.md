![Smash hack image](https://indico.cern.ch/event/1489401/logo-3797433634.png)
# SMASH-hackathon
NSF HDR A3D3: Detecting Anomalous Gravitational Wave Signals (UCSD SMASH Hackathon)

## Important Links 
* NSF HDR and UCSD SMASH Hackathon: [Link](https://indico.cern.ch/event/1489401/)
* Competition and Dataset Information: [Link](https://www.codabench.org/competitions/2626/)
* More info on LIGO and gravitational waves: [Link](https://www.ligo.caltech.edu/page/ligo-gw-interferometer)

## Prompt description and background 
Gravitational waves are ripples in spacetime caused by massive cosmic events. We detect those by LIGO's two interferometers in Washington and Louisiana, which enable signal verification, noise reduction, and enhanced sensitivity.
Traditional methods like matched filtering are effective for known gravitational-wave sources, such as merging black holes and neutron stars, but struggle with other unmodeled phenomenas. The purpose of this project was 
 to develop machine learning models to identify transient gravitational-wave anomalies from unknown sources. 

### For more background information, please read the notes for a better understanding of gravitational waves and LIGO. Link here: [notes](notes.md) 

## Model description 
Our final submitted model is a transformer feeding into an auto encoder model that capture temporal aspects of the data. Four additional features have been engineered for the model to process, including power and dominant frequency. 

## Our tasks: 
**EJ**: I helped with the exploratory data analysis on the complete data segments so I could observe the general patterns, and after that tried to put together Autoencoder and Energy Models. With some difficulties in that direction, I then adjusted the VAE model into a higher ROC/accuracy.

**Calvin**: I helped with the exploratory data analysis by creating MFCCs and spectrograms of the wave data. I also created different visualization to determine good features to input into the models, such as power and dominant frequencies. I initially tried variational autoencoder. Pivoted to adjusting the transformer --> autoencoder model by feature engineering. 

**Rebecca**: I explored various models such as one class SVM, Isolation forest, CNN, RNN, autoencoder and a mix of those approaches for anomaly detection. I also helped organizing the project repo and write the notes page in this project for background information. 

## Challenges, reflections and future improvements; 
**Ej**: I learned a lot about types of ml models and encoders, and the main difficulty was trying to understand the challenge premise and putting the model into the correct format. 

**Calvin**: I learned about how different ML models worked like variational autoencoders and how to train a ML model on time-series data. Some challenges include figuring out appropriate features for the model and understanding the challenge itself. 

**Rebecca**: A challenge I faced constantly with my models is that they keep on overfitting. To conquer this problem, I utilized L2 regularization and changed metrics used to evaluate each model based on suitability. Many of the models jump from overfitting to underfitting in a landside, which is interesting to observe. I see this project as a way to improve and learn, and in the future, I will spend more time understanding how those models work to trouble shoot better. 


## Members
* Jiaying Chen [Linkedin](https://www.linkedin.com/in/jiaying-chen01/) | [Github](https://github.com/rcwoshimao) 
* Ernest Ibarolle Ernest Ibarolle: [Linkedin](https://www.linkedin.com/in/ernest-ibarolle) |  [github]("https://github.com/eibarolle) 
* Calvin Nguyen: [Linkedin](https://www.linkedin.com/in/calvin-nguyen-data/) | [Github](https://github.com/Neniflight)
* Siddharth Vyasabattu: [LinkedIn](https://www.linkedin.com/in/siddharth-vyasabattu) | [GitHub](https://github.com/eliteapex)
