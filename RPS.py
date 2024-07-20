import random
from collections import defaultdict

# Initialize counters and histories
history = defaultdict(list)
pattern_length = 3

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    # Initialize random move if there's insufficient history
    if len(opponent_history) < 2:
        return random.choice(['R', 'P', 'S'])
    
    # Get the last pattern from the opponent's history
    if len(opponent_history) < pattern_length:
        last_pattern = ''.join(opponent_history)
    else:
        last_pattern = ''.join(opponent_history[-pattern_length:])
    
    # Use a frequency dictionary to track patterns and responses
    freq_dict = defaultdict(lambda: {'R': 0, 'P': 0, 'S': 0})
    
    for i in range(len(opponent_history) - pattern_length):
        pattern = ''.join(opponent_history[i:i+pattern_length])
        next_move = opponent_history[i+pattern_length]
        freq_dict[pattern][next_move] += 1

    # Determine the most likely next move based on the current pattern
    if last_pattern in freq_dict:
        next_move = max(freq_dict[last_pattern], key=freq_dict[last_pattern].get)
    else:
        next_move = random.choice(['R', 'P', 'S'])
    
    # Return the move that counters the most likely opponent move
    counter_moves = {'R': 'P', 'P': 'S', 'S': 'R'}
    return counter_moves[next_move]
