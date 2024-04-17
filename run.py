#%cd /content/I2TV_BahaaMahmoudTUT
!cd I2TV_BahaaMahmoudTUT && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "../video/input_vid.mp4" --audio "../audio/input_audio.wav" --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor

#!cd I2TV_BahaaMahmoudTUT && python inference.py --checkpoint_path checkpoints/wav2lip_gan.pth --face "../video/input_vid.mp4" --audio "../audio/input_audio.wav" --pads $pad_top $pad_bottom $pad_left $pad_right --resize_factor $rescaleFactor --nosmooth
