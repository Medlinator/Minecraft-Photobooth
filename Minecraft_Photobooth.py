from mcpi.minecraft import Minecraft
from mcpi import block
from picamera import PiCamera
from time import sleep

mc = Minecraft.create()
camera = PiCamera()

# message to instruct player
mc.postToChat("Enter the photobooth and proceed to gold block.")

# create photobooth
pos = mc.player.getTilePos()

mc.setBlocks(pos.x-1, pos.y, pos.z+5,
             pos.x-1, pos.y+1, pos.z+7, 5)
mc.setBlocks(pos.x+1, pos.y, pos.z+5,
             pos.x+1, pos.y+1, pos.z+7, 5)
mc.setBlocks(pos.x, pos.y, pos.z+7,
             pos.x, pos.y+1, pos.z+7, 5)
mc.setBlocks(pos.x-1, pos.y+2, pos.z+5,
             pos.x+1, pos.y+2, pos.z+7, 5)
mc.setBlocks(pos.x, pos.y-1, pos.z+3,
             pos.x, pos.y-1, pos.z+5, 35, 14)
mc.setBlocks(pos.x, pos.y-1, pos.z+6,
             pos.x, pos.y-1, pos.z+6, 41)
mc.setBlock(pos.x-2, pos.y, pos.z+4,
            block.SAPLING.id)
mc.setBlock(pos.x+2, pos.y, pos.z+4,
            block.SAPLING.id)

# take picture
while True:
        x, y, z = mc.player.getPos()
        block_beneath = mc.getBlock(x, y-1, z)

        if block_beneath == 41:
            mc.postToChat("You are in the Photobooth!")
            sleep(1)
            mc.postToChat("Smile!")
            sleep(1)
            ## enable below code if camera is upside down
            ## camera.vflip = True
            camera.start_preview()
            sleep(2)
            camera.capture('/home/pi/selfie.jpg')            
            camera.stop_preview()
            sleep(5)
