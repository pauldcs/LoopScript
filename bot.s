loop (10, 15); 
	move
		(540, 240)
		(540, 550)
		1.0,
		1.5;
	click right;
	loop (3, 4);
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