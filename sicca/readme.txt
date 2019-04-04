Requirements:
numpy, pillow, tensorflow, keras

How to use:
1. Import the prediction script
2. Make Predictor object
	eg: p = Predictor()
3. Call predict() methodd
	eg. res = p.predict('<filepath here, for ex: "heads.jpg">')  # Just the filename if the file is in the same directory as the script.
								     # Also, specify the file extension too
4. The method returns the prediction string, i.e. 'Heads" or 'Tails'

P.S. The images need to be clear and cropped, the model is kinda shitty, so it may not work if the images are not
ideal, or if there is some lighting issue and the edges are not clearly visible.
*sigh*
feelsbadman.jpg	