#CodeFights Intro Gates
#Seats in Theater
#return the number of people who sit strictly behind you and in your column or to the left, assuming all seats are occupied.

def seatsInTheater(nCols, nRows, col, row):
    return (nCols - (col - 1)) * (nRows - row)
