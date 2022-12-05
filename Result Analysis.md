# **DL PROJECT FINAL SUBMISSION**
## **Facial Emotion Recognition on images**
<br>


 ### 1. **Visualization of validation accuracy and loss:**

The curves show the epoch-wise variation of the validation accuracy and validation loss calculated while training of the 4 models implemented in this project, more details about which can be seen in the notebook with the code.

![image](https://user-images.githubusercontent.com/85495621/205617861-f86bf586-91de-4804-893d-d5564995e379.png)
![image](https://user-images.githubusercontent.com/85495621/205618027-9f2bb76c-c073-4e58-8989-8d7059e1b3ea.png)
![image](https://user-images.githubusercontent.com/85495621/205618085-7e9f13a1-2b24-47a8-a1a1-2d74497a05a0.png)
![image](https://user-images.githubusercontent.com/85495621/205618137-724758bb-27ca-4a9b-bbc0-615381f96607.png)


### 2. **Tabulation of the results**

The performance of these 4 trained models was evaluated on the testing data, and the following metrics were calculated for each: Accuracy, Loss, Precision, Recall, f1 score, AUC
![image](https://user-images.githubusercontent.com/85495621/205618212-f8b8c243-5152-4678-ace5-fa69c5c322b8.png)


### 3. **Result analysis**

![image](https://user-images.githubusercontent.com/85495621/205618275-798d2772-a06c-4ebe-8d16-1d14fd9118c2.png)

### 4. **Comment on performance & hyperparameters**

Based on the results, and the comparison among the models as seen in the plot above, we can make the following observations:

- The CNN models were optimized after changing **hyperparameters** by trial and error over ADAM and AGD optimizers, ELU and ReLU activation functions and variation in number of dense and CONV2D layers.
- Among the 2 basic CNNs (i.e lightweight options) implemented, the CNN-2 model shows better performance in terms of Accuracy and CNN-1 based on Loss on test data.
- The Xception model was implemented using ADAM optimizer with a GAP layer after baseline architecture after going through research papers which indicated improvement with these parameters. The model is more complicated than the simple CNNs but shows better Accuracy and Loss than both the CNNs on test data.
- The VGG-Face transfer learning model has much heavier implementation than the other models and takes much longer to train (2+ hours). My model could not converge fully, as I do not have sufficient computing power, although training for more than 2 hours still gives better testing Accuracy and Loss values than the other models.

### 5. **Conclusion**

This project has successfully achieved the objective of classifying facial emojis into emotion categories using Deep Learning approaches, based on convolution neural networks and transfer learning strategies. The following inference can be made based on the evaluation of the models implemented:

- For simple easier computation, CNN-2 model can be chosen for satisfactory results.

- If computing power is not an issue, VGG-Face model will be chosen for best results.
