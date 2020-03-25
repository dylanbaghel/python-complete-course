# Exercise

"""
Spotify Dictionary Data Modelling Example
"""

playlist = {
    'title': 'dope',
    'createdAt': 'some_date',
    'author': 'Abhishek Baghel',
    'songs': [
        {'title': 'Aelaan', 'artist': ['Muhfaad'], 'duration': 5.5},
        {'title': 'Maharaani', 'artist': ['Kr$na'], 'duration': 4.5},
        {'title': 'Untitled', 'artist': ['Kr$na'], 'duration': 3.0}
    ]
}

print(playlist)
sum = 0
for song in playlist['songs']:
    sum += song['duration']

print(sum)
