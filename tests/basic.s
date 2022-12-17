loop (1, 1); 
	move
		(540, 240) # range x 
		(540, 550) # range y
		1.0,  # duration
		1.5;  # wait
	click right;
	loop (3, 3); 
		click right;
		move
			(100, 200)
			(300, 400)
			0.5,
			1.0;
		click left;
		type "Hello world";
		rtext (10, 20); 
	end;
	rstr (5, 10);
end;