loop 10; # this script will execute 10 times
	move
		# moves the mouse from the current position
	    # to the specified coordinates range
		(540, 240)  # min_x, max_x
		(540, 550)  # min_y, max_y
		(1.0, 1.5); # movement_speed, wait_after_moving
	click right;    # click the right button at the current position
	loop 3;         # nested loop, executes 3 time
		click right;
		move
			(100, 200)
			(300, 400)
			(0.5, 1.0);
		click left;
		type "hello world"; # types the string on the keyboard
	end; # marks the end of the first loop
end; # marks the end of the second loop