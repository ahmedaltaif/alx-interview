def makeChange(coin_denominations, amount_due):
    """
    Returns the fewest number of coins needed to meet the amount_due.
    If it's not possible to make exact change, returns -1.
    
    coin_denominations: List of available coin denominations.
    amount_due: The total amount for which change is to be made.
    """
    if amount_due <= 0:
        # No change needed for non-positive amounts
        return 0
    
    # Sort the coin denominations in descending order to use the largest coin first
    coin_denominations.sort(reverse=True)
    
    coin_count = 0  # Total number of coins used

    for coin in coin_denominations:
        if amount_due <= 0:
            break
        
        # Find the maximum number of this coin that can be used
        num_coins = amount_due // coin  
        coin_count += num_coins  # Increment the total count of coins
        amount_due -= num_coins * coin  # Reduce the amount_due by the equivalent coin value

    # If the amount_due is not zero, it means exact change cannot be made
    if amount_due != 0:
        return -1
    
    return coin_count

