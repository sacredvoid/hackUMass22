import sda
va = sda.VideoAnimator(gpu=-1, model_path="crema")# Instantiate the animator
vid, aud = va(r"C:\Users\rajat\Downloads\c.jpg", "example/audio.wav")
va.save_video(vid, aud, "generated.mp4")