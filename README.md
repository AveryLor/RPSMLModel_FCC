# RPSMLModel_FCC
Created a machine learning model with TensorFlow through the FreeCodeCamp course. 


Key Features of This Strategy:
Pattern Length: This function tracks patterns of length 3 (you can adjust pattern_length for different lengths).

Frequency Dictionary: Maintains a frequency dictionary to track which move the opponent is likely to make after specific patterns.

Adaptive Response: Predicts the opponent's next move based on the most frequent response to the detected pattern and counters it.

Testing and Adjustment:

Test the updated player function against the bots using main.py to check if it meets the 60% win rate requirement.

Adjust Pattern Length if needed to improve performance based on observed results.

This strategy leverages pattern recognition and adaptive responses to improve the win rate. Place this code in RPS.py and test it against the bots to see if it achieves the desired win rate.