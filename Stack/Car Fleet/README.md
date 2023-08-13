# Car Fleet

Sort cars in reverse order of position. Put last car in stack and then for every car check if it finishes earlier than the one before it. If it does, it will get blocked by the one in front of it. Otherwise push it into the stack