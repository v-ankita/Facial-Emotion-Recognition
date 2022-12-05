# **DL PROJECT FINAL SUBMISSION**
## **Facial Emotion Recognition on images**
<br>


 ### 1. **Visualization of validation accuracy and loss:**

The curves show the epoch-wise variation of the validation accuracy and validation loss calculated while training of the 4 models implemented in this project, more details about which can be seen in the notebook with the code.



2. CNN-2

3. Xception model

4. VGG-Face model

### 2. **Tabulation of the results**

The performance of these 4 trained models was evaluated on the testing data, and the following metrics were calculated for each: Accuracy, Loss, Precision, Recall, f1 score, AUC

### 3. **Result analysis**


### 4. **Comment on performance & hyperparameters**

Based on the results, and the comparison among the models as seen in the plot above,

we can make the following observations:

·

The CNN models were optimized after changing **hyperparameters** by trial and error

over ADAM and AGD optimizers, ELU and ReLU activation functions and variation in

number of dense and CONV2D layers.

·

·

Among the 2 basic CNNs (i.e lightweight options) implemented, the CNN-2 model

shows better performance in terms of Accuracy and CNN-1 based on Loss on test data.

The Xception model was implemented using ADAM optimizer with a GAP layer after

baseline architecture after going through research papers which indicated

improvement with these parameters. The model is more complicated than the simple

CNNs but shows better Accuracy and Loss than both the CNNs on test data.

The VGG-Face transfer learning model has much heavier implementation than the

other models and takes much longer to train (2+ hours).

·

·

My model could not converge fully, as I do not have sufficient computing power,

although training for more than 2 hours still gives better testing Accuracy and Loss

values than the other models.

### 5. **Conclusion**

This project has successfully achieved the objective of classifying facial emojis into

emotion categories using Deep Learning approaches, based on convolution neural

networks and transfer learning strategies.

The following inference can be made based on the evaluation of the models

implemented:

- For simple easier computation, CNN-2 model can be chosen for satisfactory results.

- If computing power is not an issue, VGG-Face model will be chosen for best results.
