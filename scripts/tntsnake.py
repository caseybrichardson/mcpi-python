#!/usr/bin/env python

# Posted to mcpipy.com, created by brooksc and fleap3 aka mrfleap :)

# This script will:
# 1. Create a snake that will pick a random direction.
# if max_direction is set to 3, it will go backward/forward/left/right.  Set to 5 and it goes up/down.
# 2. Head in that direction for a random # of blocks from min_distance and max_distance
# leave a 5 block "plus" of TNT in it's path
# 3. Pick a new direction and go in that direction
# It should not double back on itself or go the same direction...


#import minecraft block module
import mcpi.block as block
#import time, so delays can be used
import time
import random
import math

def new_direction(old_direction):
    max_direction = 5
#    max_direction = 3

    directions = ["Forward", "Left", "Right", "Backward", "Up", "Down"]
    direction_opposite = [3,2,1,0,5,4]
    direction = old_direction
    while direction == old_direction and direction != direction_opposite[direction]:
        direction = random.randint(0, max_direction)
    print "changing direction from %s to %s" % (directions[old_direction], directions[direction])
    return direction

def tntsnake(mc):
    #mc.setBlocks(-10,-10,-10,10,100,10,block.AIR)
    p = mc.player.getPos()
    x = p.x
    y = p.y
    z = p.z
    max_x = 50
    max_y = 10
    max_z = 50
    min_distance = 10
    max_distance = 100
    direction = -1
    directions = ["Forward", "Left", "Right", "Backward", "Up", "Down"]
    count = 0
    while count < 500:
        count = count + 1
        mc.setBlock(x, y, z, block.DIAMOND_BLOCK)
        time.sleep(2)

        direction = new_direction(direction)
        duration = random.randint(min_distance, max_distance)
        print "New Roll: %s direction (%d) for %s more cycles!" % (directions[direction], direction,  duration)
#        time.sleep(3)
        while duration > 0:
            mc.setBlock(x, y, z, block.TNT)
            if direction == 0 or direction == 3:
                # Going forward or back Adjust Z
                mc.setBlock(x, y, z-1, block.TNT)
                mc.setBlock(x, y, z+1, block.TNT)
                mc.setBlock(x, y-1, z, block.TNT)
                mc.setBlock(x, y+1, z, block.TNT)
            elif direction == 1 or direction == 2:
                # Going left or right Adjust X
                mc.setBlock(x-1, y, z, block.TNT)
                mc.setBlock(x+1, y, z, block.TNT)
                mc.setBlock(x, y-1, z, block.TNT)
                mc.setBlock(x, y+1, z, block.TNT)
            else:
                # Going up or down, Adjust Y
                mc.setBlock(x-1, y, z, block.TNT)
                mc.setBlock(x+1, y, z, block.TNT)
                mc.setBlock(x, y, z-1, block.TNT)
                mc.setBlock(x, y, z+1, block.TNT)
            time.sleep(.25)
            if direction == 0:
                # forward
                x += 1
                if math.fabs(x) > max_x:
                    direction = new_direction(direction)
                    x -= 2
            elif direction == 1:
                # left
                z -= 1
                if math.fabs(z) > max_z:
                    direction = new_direction(direction)
                    z += 2
            elif direction == 2:
                # right
                z += 1
                if math.fabs(z) > max_z:
                    direction = new_direction(direction)
                    z -= 2
            elif direction == 3:
                # backward
                x -= 1
                if math.fabs(x) > max_x:
                    direction = new_direction(direction)
                    x += 2
            elif direction == 4:
                # up
                y += 1
                if math.fabs(y) > max_y:
                    # if it's going further than max_y allows, turn it around
                    direction = new_direction(direction)
                    y -= 2
            elif direction == 5:
                # down
                y -= 1
                if math.fabs(y) > max_y:
                    # if it's going further than max_y allows, turn it around
                    direction = new_direction(direction)
                    y += 2
            else:
                print "Error! %s" % (direction)

            duration -= 1
            print "Going %s for %s more cycles" % (directions[direction],duration)


if __name__ == "__main__":
    import server
    tntsnake(server.mc)
