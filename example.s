# execute the script 6 times
# loops always have to be delimited by an 'end;'
loop 5;
	# move the cursor from current position to new position.
	# `move (min_x, max_x), (min_y, max_y), duration;`
	# here, it will take 0.5 seconds (duration) time to
	# perform the movement
	mov (333, 1015),    
		(241, 460),
		0.5;
	click right; # simulates right click
	loop 10;
		click double; # simulates double click
		rtxt 10; # write 10 words of random english text
		# `rstr <count>` randomly writes 'count' 
		# characters present on the keyboard
	end;
	# move the cursor from current position to new position.
	mov (333, 1015),
		(241, 460),
		1;
	click left;
	# simulates a human typing the string
	type "hello world";
end;